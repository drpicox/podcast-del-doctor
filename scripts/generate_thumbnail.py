#!/usr/bin/env python3
"""
Genera un thumbnail per a un episodi del podcast amb Qwen Image (Draw Things).

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
        --prompt-suffix "smartphones and magazine covers tumbling out, social media icons"

Requisits (draw-things-cli):
    - brew install draw-things-cli
    - El model qwen_image_2512_q8p.ckpt al directori de models de Draw Things.
      Si falta: draw-things-cli models ensure --model qwen_image_2512_q8p.ckpt

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


# Qwen segueix el prompt i escriu 'POLICE BOX' molt millor que Z-Image, a canvi
# d'anar unes 3x més lent (~4 min per imatge contra ~1,5).
DT_MODEL = "qwen_image_2512_q8p.ckpt"

# Paràmetres de generació explícits.
#
# Sense passar-los, draw-things-cli aplica els "recommended settings" del model
# base: desenes de passos amb guidance alta. Amb un model de 21 GB i la memòria
# justa això no arriba a acabar mai — generant el 025 va superar dos cops el
# límit de 900 s sense ni tan sols obrir el fitxer del model (4% de CPU, RSS
# clavat a 0,6 GB: thrashing contra el swap).
#
# Amb la LoRA turbo n'hi ha prou amb pocs passos i guidance 1: el mateix prompt
# surt en ~2,5 min. És la configuració que fa servir el David a l'app de Draw
# Things, aquí només se n'ha canviat la resolució a quadrada.
#
# DT_STEPS: 8, no 5. Amb 5 passos la imatge ja és neta, però la guidance 1 no
# arriba a resoldre les relacions espacials del prompt i els cascos surten
# surant separats de la cabina en comptes de seure-hi a sobre (es va veure
# generant el 025). Amb 8 la diadema torna a passar per sobre del sostre. Costa
# uns 45 s més per imatge.
DT_LORA = "wuli_qwen_image_2512_turbo_lora_2steps_v1.0_bf16_lora_f16.ckpt"
DT_STEPS = 8
DT_SAMPLER = 15
DT_SHIFT = 1
DT_GUIDANCE = 1
DT_SIZE = 1024  # tot el catàleg de thumbnails és 1024x1024
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


def _generate_draw_things(full_prompt, dest_image, seed):
    """draw-things-cli escriu directament a --output; no cal temporal."""
    config = {
        "model": DT_MODEL,
        "sampler": DT_SAMPLER,
        "steps": DT_STEPS,
        "guidanceScale": DT_GUIDANCE,
        "shift": DT_SHIFT,
        "width": DT_SIZE,
        "height": DT_SIZE,
        "batchCount": 1,
        "batchSize": 1,
        "strength": 1,
        "loras": [{"mode": "all", "file": DT_LORA, "weight": 1}],
    }

    cmd = [
        "draw-things-cli", "generate",
        "--model", DT_MODEL,
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
                       backend="auto", seed=None):
    """Genera un thumbnail amb Qwen Image i el desa a output_dir."""

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
    print(f"⚙️ Backend: {backend}")
    print(f"🎲 Seed: {seed}")
    print(f"⏳ Generant (Qwen triga uns 4 min; Z-Image, ~1,5)...")

    os.makedirs(output_dir, exist_ok=True)
    dest_image = os.path.join(output_dir, f"{nom}.png")

    start = time.perf_counter()
    if backend == "draw-things":
        _generate_draw_things(full_prompt, dest_image, seed)
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
        help="Què surt per la porta oberta i espireja vòrtex avall, en anglès "
             "(ex: 'glowing golden stock-market chart lines, tiny factories, gold coins')",
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
        "--seed", type=int, default=None,
        help="Llavor per a resultats reproduïbles (només backend draw-things)",
    )

    args = parser.parse_args()

    dest = generate_thumbnail(
        args.episodi, args.nom, args.prompt_suffix, args.output_dir,
        backend=args.backend, seed=args.seed,
    )
    ext = os.path.splitext(dest)[1]
    print(f"\n🔧 Afegeix al frontmatter de _episodes/{args.nom}.md:")
    print(f'thumbnail: "/{args.output_dir}/{args.nom}{ext}"')


if __name__ == "__main__":
    main()
