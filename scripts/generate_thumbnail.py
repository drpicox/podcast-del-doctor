#!/usr/bin/env python3
"""
Genera un thumbnail per a un episodi del podcast amb Qwen Image 2.1 (Draw Things).

Hi ha dos backends:

  draw-things-cli  (per defecte)  Escriu la imatge directament a --output.
  ollama           (llegat)       Escriu al cwd; cal executar-lo en un temporal
                                  i moure'n el resultat.

Ollama va retirar la generació d'imatges a la versió 0.32.6, així que el backend
d'ollama només funciona amb 0.32.5 o anterior.

Ús:
    python scripts/generate_thumbnail.py \\
        --episodi 013 \\
        --nom 013-youtuber-revista-pantalles \\
        --prompt-suffix "an old 1920s film projector, a wooden radio and a boxy CRT \\
television tumbling out one after another, followed by a huge muscular robot ..."

El sufix ha de ser DETALLAT (objectes, com són, personatges i què fan, text curt):
amb una frase curta el model hi posa quatre props genèrics i el tema no es llegeix.

Requisits (draw-things-cli):
    - brew install draw-things-cli  (26.1011.0 o posterior: les anteriors no
      coneixen Qwen Image 2.1)
    - El model al directori de models de Draw Things. Si falta:
        draw-things-cli models ensure --model qwen_image_2.1_turbo_q6p.ckpt

Requisits (ollama, llegat):
    - ollama <= 0.32.5 i el model: ollama pull x/z-image-turbo
"""

import os
import sys
import argparse
import json
import subprocess
import glob
import random
import shutil
import time
import tempfile

# Prompt base — la TARDIS caient pel vòrtex amb les portes obertes.
#
# Fins al 023 la composició era la cabina dreta i centrada amb el tema de
# l'episodi com a prop petit a sota, sobre fons clar. El problema: a mida de
# llistat (~110 px) la cabina ocupa el 70% del dibuix i és idèntica a tots els
# episodis, així que les portades eren indistingibles entre elles i el prop
# diferenciador no es veia. Ho vam mesurar amb un contact sheet a 110 px.
#
# La fórmula actual resol les dues coses alhora: el vòrtex omple el marc (silueta
# i color global diferents del catàleg antic), la cabina cau inclinada (dinamisme
# i angle nou cada episodi) i les portes obertes fan de contenidor — el que
# canvia entre episodis és el que en surt, no un prop arraconat.
#
# El fons és fosc a posta. Els thumbnails 001-022 tenen fons clar, així que el
# 023 obre una època visual nova; si algun dia es regenera el catàleg enrere,
# aquesta és la fórmula a aplicar-hi.
BASE_PROMPT = (
    "A TARDIS blue British police box wearing oversized futuristic headphones, tilted at a "
    "dramatic falling angle, tumbling down a swirling purple and gold time vortex tunnel that "
    "fills the entire frame edge to edge. One single sign board above the doors reads exactly "
    "'POLICE BOX' in clean white capital letters on black, no other text anywhere. Its double "
    "doors hang wide open as it falls, and you can see into the glowing golden interior. "
    "Streaming out of the open doorway and spiralling away down the vortex comes the subject of "
    "this episode. Everything is falling together down the same rabbit hole. Strong sense of "
    "motion, spiral and depth. Clean detailed illustration style with bold defined outlines and "
    "flat colors, high contrast, readable as a small thumbnail. Palette: TARDIS blue (#003B6F), "
    "gallifreyan gold (#D4AF37), vortex purple (#7B2FFE), cyan glow (#00E5FF)"
)

# 'white background' hi és perquè la fórmula anterior era de fons clar i el model
# hi recau tot sol; 'static'/'upright' perquè sense això deixa de caure.
NEGATIVE_PROMPT = (
    "white background, off-white background, pale background, static, upright, "
    "gibberish text, garbled lettering, misspelled words, duplicated text, watermark, "
    "signature, blurry, photorealistic photograph"
)


# Models de Draw Things, provats amb el 036 i un sufix detallat (2026-10):
#
#   qwen21    Qwen Image 2.1 Turbo. Per defecte: el més dinàmic i el que es llegeix
#             millor a 110 px. ~2 min. Ja ve destil·lat, no cal LoRA. Paràmetres
#             de l'app de Draw Things del David, amb la mida a 1024.
#             Sovint simplifica personatges (un "robot culturista" li surt home):
#             si el sufix depèn d'un detall així, insisteix-hi o prova llavors.
#   qwen2512  Qwen Image 2512 + LoRA turbo. El model fins al 038. ~3 min.
#   krea      Krea 2 Turbo. El més fidel als detalls, però la cabina cau poc i
#             les coses no sempre surten per la porta. ~4 min.
#
# Paràmetres sempre explícits: sense passar-los, draw-things-cli aplica els
# "recommended settings" del model base, i amb Qwen 2512 (21 GB) això feia
# thrashing contra el swap i superava els 900 s sense acabar (es va veure
# generant el 025).
#
# qwen2512 a 8 passos, no 5: amb 5 la guidance 1 no resolia les relacions
# espacials i els cascos surten surant separats de la cabina (025).
DT_SIZE = 1024  # tot el catàleg de thumbnails és 1024x1024
DT_MODELS = {
    "qwen21": {
        "model": "qwen_image_2.1_turbo_q6p.ckpt",
        "sampler": 16,
        "steps": 8,
        "guidanceScale": 1,
        "shift": 6.5,
        "resolutionDependentShift": False,
        "loras": [],
    },
    "qwen2512": {
        "model": "qwen_image_2512_q8p.ckpt",
        "sampler": 15,
        "steps": 8,
        "guidanceScale": 1,
        "shift": 1,
        "loras": [{"mode": "all", "file": "wuli_qwen_image_2512_turbo_lora_2steps_v1.0_bf16_lora_f16.ckpt", "weight": 1}],
    },
    "krea": {"model": "krea_2_turbo_q6p.ckpt"},
}
DT_DEFAULT_MODEL = "qwen21"
DT_TIMEOUT = 1800


def _resolve_backend(backend):
    """'auto' tria draw-things-cli si hi és; si no, ollama."""
    if backend != "auto":
        return backend
    if shutil.which("draw-things-cli"):
        return "draw-things"
    if shutil.which("ollama"):
        return "ollama"
    print("❌ No s'ha trobat ni 'draw-things-cli' ni 'ollama' al PATH.")
    print("   Instal·la: brew install draw-things-cli")
    sys.exit(1)


def _generate_draw_things(full_prompt, dest_image, seed, model):
    """draw-things-cli escriu directament a --output; no cal temporal."""
    config = dict(DT_MODELS[model])
    config.update({
        "width": DT_SIZE,
        "height": DT_SIZE,
        "batchCount": 1,
        "batchSize": 1,
        "strength": 1,
    })

    cmd = [
        "draw-things-cli", "generate",
        "--model", config["model"],
        "--config-json", json.dumps(config),
        "--prompt", full_prompt,
        "--negative-prompt", NEGATIVE_PROMPT,
        "--seed", str(seed),
        "--output", dest_image,
    ]

    try:
        subprocess.run(cmd, check=True, timeout=DT_TIMEOUT)
    except subprocess.TimeoutExpired:
        print(f"❌ Error: draw-things-cli ha superat el temps límit ({DT_TIMEOUT}s)")
        print("   Comprova la memòria lliure: un model de 21 GB fa thrashing si el swap va ple.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error de draw-things-cli (codi {e.returncode})")
        print(f"   Comprova que el model hi és: draw-things-cli models list --downloaded-only")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Error: 'draw-things-cli' no trobat al PATH.")
        print("   Instal·la'l amb: brew install draw-things-cli")
        sys.exit(1)

    if not os.path.exists(dest_image):
        print(f"❌ draw-things-cli ha acabat bé però no hi ha cap fitxer a {dest_image}")
        sys.exit(1)
    return dest_image


def _generate_ollama(full_prompt, dest_image, episodi):
    """Ollama escriu al cwd: l'executem en un temporal i en movem el resultat."""
    with tempfile.TemporaryDirectory(prefix=f"podcast_thumb_{episodi}_") as tmpdir:
        try:
            subprocess.run(
                ["ollama", "run", "x/z-image-turbo", full_prompt],
                cwd=tmpdir,
                check=True,
                timeout=900,
            )
        except subprocess.TimeoutExpired:
            print("❌ Error: ollama ha superat el temps límit (900s)")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error d'ollama (codi {e.returncode})")
            print("   Recorda que ollama va retirar la generació d'imatges a la 0.32.6.")
            sys.exit(1)
        except FileNotFoundError:
            print("❌ Error: 'ollama' no trobat al PATH.")
            print("   Instal·la'l des de: https://ollama.com")
            print("   I descarrega el model: ollama pull x/z-image-turbo")
            sys.exit(1)

        image_files = []
        for ext in ["*.png", "*.jpg", "*.jpeg", "*.webp"]:
            image_files.extend(glob.glob(os.path.join(tmpdir, ext)))

        if not image_files:
            print(f"❌ No s'ha trobat cap imatge a {tmpdir}")
            print(f"   Fitxers presents: {os.listdir(tmpdir)}")
            print("   Prova manualment: cd /tmp && ollama run x/z-image-turbo 'test'")
            sys.exit(1)

        image_files.sort(key=os.path.getmtime, reverse=True)
        shutil.copy2(image_files[0], dest_image)
    return dest_image


def generate_thumbnail(episodi, nom, prompt_suffix, output_dir="assets/thumbnails",
                       backend="auto", seed=None, model=DT_DEFAULT_MODEL):
    """Genera un thumbnail amb Draw Things (o ollama) i el desa a output_dir."""

    full_prompt = BASE_PROMPT
    if prompt_suffix:
        full_prompt = f"{BASE_PROMPT}. Pouring out of the open doors and spiralling down the vortex: {prompt_suffix}"

    backend = _resolve_backend(backend)

    # Sempre una llavor explícita: draw-things-cli no la reporta, i sense això
    # no es pot reproduir ni ajustar un thumbnail que gairebé funciona.
    if seed is None:
        seed = random.randrange(2**31)

    print(f"🎨 Generant thumbnail per episodi {episodi} ({nom})")
    print(f"🖼️ Suffix: {prompt_suffix}")
    print(f"📝 Prompt (primeres 150 chars): {full_prompt[:150]}...")
    print(f"⚙️ Backend: {backend}" + (f" ({model})" if backend == "draw-things" else ""))
    print(f"🎲 Seed: {seed}")
    print(f"⏳ Generant (qwen21 ~2 min, qwen2512 ~3, krea ~4; Z-Image via ollama ~1,5)...")

    os.makedirs(output_dir, exist_ok=True)
    dest_image = os.path.join(output_dir, f"{nom}.png")

    start = time.perf_counter()
    if backend == "draw-things":
        _generate_draw_things(full_prompt, dest_image, seed, model)
    else:
        _generate_ollama(full_prompt, dest_image, episodi)
    elapsed = time.perf_counter() - start

    print(f"✅ Thumbnail guardat a: {dest_image}  ({elapsed:.1f}s, backend {backend}, seed {seed})")
    return dest_image


def main():
    parser = argparse.ArgumentParser(
        description="Genera thumbnail per episodi de podcast amb ollama x/z-image-turbo"
    )
    parser.add_argument(
        "--episodi", required=True, help="Número de l'episodi (ex: 013)"
    )
    parser.add_argument(
        "--nom",
        required=True,
        help="Nom complet del fitxer sense extensió (ex: 013-youtuber-revista-pantalles)",
    )
    parser.add_argument(
        "--prompt-suffix",
        default="",
        help="Què surt per la porta oberta i espireja vòrtex avall, en anglès i "
             "DETALLAT: quins objectes, com són, quins personatges i què fan, quin "
             "text curt hi surt (ex: 'an old 1920s film projector, a wooden radio and "
             "a boxy CRT television tumbling out, followed by a huge muscular robot "
             "lifting a golden barbell while a skinny student holds an exam marked 40%%')",
    )
    parser.add_argument(
        "--output-dir",
        default="assets/thumbnails",
        help="Directori de sortida (per defecte: assets/thumbnails)",
    )
    parser.add_argument(
        "--backend",
        choices=["auto", "draw-things", "ollama"],
        default="auto",
        help="Motor de generació (per defecte: auto — draw-things-cli si hi és)",
    )
    parser.add_argument(
        "--model",
        choices=sorted(DT_MODELS),
        default=DT_DEFAULT_MODEL,
        help="Model de Draw Things (per defecte: qwen21)",
    )
    parser.add_argument(
        "--seed", type=int, default=None,
        help="Llavor per a resultats reproduïbles (només backend draw-things)",
    )

    args = parser.parse_args()

    dest = generate_thumbnail(
        args.episodi, args.nom, args.prompt_suffix, args.output_dir,
        backend=args.backend, seed=args.seed, model=args.model,
    )
    ext = os.path.splitext(dest)[1]
    print(f"\n🔧 Afegeix al frontmatter de _episodes/{args.nom}.md:")
    print(f'thumbnail: "/{args.output_dir}/{args.nom}{ext}"')


if __name__ == "__main__":
    main()
