#!/usr/bin/env python3
"""
Verificador del workflow d'episodis del Podcast del Doctor.

Comprova que cada pas del workflow de generate-episode ha deixat els
fitxers i metadades en bon estat, i es queixa amb missatges concrets
de què cal corregir.

Ús:
    python scripts/check_episode.py 019              # tot (checks locals)
    python scripts/check_episode.py 019 --pas 5d     # només fins al PAS 5d
    python scripts/check_episode.py 019 --remot      # inclou archive.org i web publicada
    python scripts/check_episode.py --tots           # tots els episodis (checks locals)

Codi de sortida: 0 si no hi ha errors (els avisos no fallen), 1 si n'hi ha.
"""

import argparse
import glob
import json
import os
import re
import struct
import subprocess
import sys
import urllib.request

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASEURL = "/podcast-del-doctor"
WEB = "https://david-rodenas.com/podcast-del-doctor"

# Ordre dels passos del workflow (generate-episode.md)
PASSOS = ["1", "2", "3", "4", "5b", "5c", "5d", "6", "7", "8", "9"]

DESCRIPCIO_MAX_OK = 750       # per sobre: avís (la guia diu ~650)
DESCRIPCIO_MAX_ERROR = 1000   # per sobre: error (fa illegible el llistat)
CAPITOL_TITOL_MAX = 70


class Resultat:
    def __init__(self):
        self.ok = 0
        self.avisos = []
        self.errors = []

    def be(self, pas, msg):
        self.ok += 1
        print(f"  ✅ PAS {pas}: {msg}")

    def avis(self, pas, msg):
        self.avisos.append(msg)
        print(f"  ⚠️  PAS {pas}: {msg}")

    def error(self, pas, msg):
        self.errors.append(msg)
        print(f"  ❌ PAS {pas}: {msg}")


def troba_slug(episodi):
    """Accepta '019' o el slug sencer i retorna el slug (sense extensió)."""
    if re.fullmatch(r"\d{1,3}", episodi):
        num = episodi.zfill(3)
        candidats = sorted(glob.glob(os.path.join(ROOT, "_episodes", f"{num}-*.md")))
        if not candidats:
            candidats = sorted(glob.glob(os.path.join(ROOT, "episodes", f"{num}-*.mp3")))
        if not candidats:
            return None
        return re.sub(r"\.(md|mp3)$", "", os.path.basename(candidats[0]))
    return re.sub(r"\.(md|mp3)$", "", os.path.basename(episodi))


def durada_a_segons(text):
    parts = [int(p) for p in str(text).split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    raise ValueError(text)


def durada_mp3(camí):
    sortida = subprocess.run(
        ["ffprobe", "-i", camí, "-show_entries", "format=duration",
         "-v", "quiet", "-of", "csv=p=0"],
        capture_output=True, text=True, timeout=30)
    return float(sortida.stdout.strip())


def mida_png(camí):
    with open(camí, "rb") as f:
        cap = f.read(24)
    if cap[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    ample, alt = struct.unpack(">II", cap[16:24])
    return ample, alt


def llegeix_frontmatter(camí):
    with open(camí, encoding="utf-8") as f:
        text = f.read()
    linies = text.split("\n")
    if linies[0].strip() != "---":
        raise ValueError("el fitxer no comença amb '---'")
    fi = next(i for i in range(1, len(linies)) if linies[i].strip() == "---")
    fm = yaml.safe_load("\n".join(linies[1:fi]))
    body = "\n".join(linies[fi + 1:])
    return fm, body


def peticio(url, nomes_capcalera=True):
    peticio = urllib.request.Request(
        url, method="HEAD" if nomes_capcalera else "GET",
        headers={"User-Agent": "check-episode/1.0"})
    return urllib.request.urlopen(peticio, timeout=20)


def verifica(slug, fins_pas, remot, r, mp3_opcional=False):
    num = slug[:3]
    inclou = lambda pas: PASSOS.index(pas) <= PASSOS.index(fins_pas)

    mp3 = os.path.join(ROOT, "episodes", f"{slug}.mp3")
    md = os.path.join(ROOT, "_episodes", f"{slug}.md")
    txt = os.path.join(ROOT, "sources", f"{slug}-transcripcio.txt")
    srt = os.path.join(ROOT, "sources", f"{slug}-transcripcio.srt")
    capitols = os.path.join(ROOT, "sources", f"{slug}-chapters.json")
    thumbnail = os.path.join(ROOT, "assets", "thumbnails", f"{slug}.png")

    # ── PAS 1: MP3 ────────────────────────────────────────────────────
    te_mp3 = os.path.isfile(mp3)
    if inclou("1"):
        if te_mp3:
            r.be("1", f"MP3 present ({os.path.getsize(mp3):,} bytes)")
        elif mp3_opcional:
            r.avis("1", "MP3 no present en local (còpia de seguretat absent en aquesta màquina)")
        else:
            r.error("1", f"Falta l'MP3: episodes/{slug}.mp3. Copia'l a episodes/ abans de començar")

    # ── PAS 2: transcripció + markdown ────────────────────────────────
    fm, body = None, ""
    if inclou("2"):
        if os.path.isfile(txt) and os.path.getsize(txt) > 1000:
            r.be("2", "Transcripció .txt present")
        else:
            r.error("2", f"Falta o és massa curta sources/{slug}-transcripcio.txt. Torna a executar transcribe_episode.py")
        if os.path.isfile(srt):
            contingut_srt = open(srt, encoding="utf-8").read()
            blocs = len(re.findall(r"\d\d:\d\d:\d\d[,.]\d+\s*-->\s*\d\d:\d\d:\d\d", contingut_srt))
            if blocs >= 10:
                r.be("2", f"Subtítols .srt presents ({blocs} blocs)")
            else:
                r.error("2", f"L'SRT només té {blocs} blocs amb timestamps: sembla corrupte. Regenera'l amb transcribe_episode.py")
        else:
            r.error("2", f"Falta sources/{slug}-transcripcio.srt (el genera transcribe_episode.py)")
        if os.path.isfile(md):
            try:
                fm, body = llegeix_frontmatter(md)
                r.be("2", "Markdown present i YAML vàlid")
            except Exception as e:
                r.error("2", f"El YAML de _episodes/{slug}.md no es pot llegir: {e}")
        else:
            r.error("2", f"Falta _episodes/{slug}.md (el crea transcribe_episode.py)")

    if fm is None:
        return  # sense frontmatter no es pot verificar res més

    durada_fm = None
    if fm.get("duration"):
        try:
            durada_fm = durada_a_segons(fm["duration"])
        except ValueError:
            pass

    # ── PAS 3: durada ─────────────────────────────────────────────────
    if inclou("3"):
        if durada_fm is None:
            r.error("3", f"'duration' absent o amb mal format ({fm.get('duration')!r}). Format esperat: MM:SS (amb ffprobe)")
        elif te_mp3:
            try:
                real = durada_mp3(mp3)
                if abs(real - durada_fm) <= 3:
                    r.be("3", f"Durada {fm['duration']} coincideix amb l'MP3")
                else:
                    minuts, segons = int(real // 60), int(real % 60)
                    r.error("3", f"'duration' diu {fm['duration']} però l'MP3 fa {minuts:02d}:{segons:02d}. Corregeix el frontmatter")
            except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
                r.avis("3", "No s'ha pogut executar ffprobe; durada no contrastada")
        else:
            r.be("3", f"Durada {fm['duration']} amb format correcte (MP3 no present per contrastar)")

    # ── PAS 4: mida ───────────────────────────────────────────────────
    if inclou("4"):
        mida = fm.get("audio_size")
        if not isinstance(mida, int) or mida <= 0:
            r.error("4", f"'audio_size' absent o no numèric ({mida!r}). Obtén-lo amb: stat -f%z episodes/{slug}.mp3")
        elif te_mp3 and os.path.getsize(mp3) != mida:
            r.error("4", f"'audio_size' diu {mida:,} però l'MP3 local fa {os.path.getsize(mp3):,} bytes")
        else:
            r.be("4", f"audio_size = {mida:,} bytes")

    # ── PAS 5b: capítols ──────────────────────────────────────────────
    if inclou("5b"):
        if not os.path.isfile(capitols):
            r.error("5b", f"Falta sources/{slug}-chapters.json. Genera els capítols a partir de l'SRT")
        else:
            try:
                dades = json.load(open(capitols, encoding="utf-8"))
                llista = dades.get("chapters", [])
                temps = [c.get("startTime") for c in llista]
                titols = [c.get("title", "") for c in llista]
                if not dades.get("version"):
                    r.error("5b", "El JSON de capítols no té camp 'version'")
                elif len(llista) < 3:
                    r.error("5b", f"Només {len(llista)} capítols; en calen mínim 3")
                elif temps[0] != 0:
                    r.error("5b", f"El primer capítol ha de començar a startTime 0 (ara: {temps[0]})")
                elif any(b <= a for a, b in zip(temps, temps[1:])):
                    r.error("5b", "Els startTime dels capítols no són estrictament creixents")
                elif durada_fm and temps[-1] >= durada_fm:
                    r.error("5b", f"L'últim capítol comença a {temps[-1]}s però l'episodi fa {durada_fm}s")
                else:
                    r.be("5b", f"Capítols vàlids ({len(llista)})")
                    if len(llista) > 10:
                        r.avis("5b", f"{len(llista)} capítols; la guia en recomana màxim 10")
                llargs = [t for t in titols if len(t) > CAPITOL_TITOL_MAX]
                if llargs:
                    r.avis("5b", f"{len(llargs)} títols de capítol de més de {CAPITOL_TITOL_MAX} caràcters; escurça'ls perquè es llegeixin bé a les apps")
            except json.JSONDecodeError as e:
                r.error("5b", f"El JSON de capítols no es pot llegir: {e}")
            if fm.get("chapters_file") != f"{slug}-chapters.json":
                r.error("5b", f"'chapters_file' ({fm.get('chapters_file')!r}) no coincideix amb {slug}-chapters.json")

    # ── PAS 5c: soundbite ─────────────────────────────────────────────
    if inclou("5c"):
        inici = fm.get("soundbite_start")
        durada_sb = fm.get("soundbite_duration")
        titol_sb = fm.get("soundbite_title")
        if inici is None or durada_sb is None or not titol_sb:
            r.error("5c", "Falten soundbite_start, soundbite_duration o soundbite_title al frontmatter")
        else:
            problemes = []
            if not 15 <= durada_sb <= 120:
                problemes.append(f"durada {durada_sb}s fora del rang 15-120s")
            if durada_fm and inici + durada_sb > durada_fm + 2:
                problemes.append(f"acaba a {inici + durada_sb:.0f}s però l'episodi fa {durada_fm}s")
            if len(titol_sb) > 128:
                problemes.append(f"títol de {len(titol_sb)} caràcters (màxim 128)")
            if problemes:
                r.error("5c", "Soundbite invàlid: " + "; ".join(problemes))
            else:
                r.be("5c", f"Soundbite vàlid ({durada_sb}s)")
                if not 30 <= durada_sb <= 90:
                    r.avis("5c", f"Durada del soundbite {durada_sb}s; l'ideal és 30-90s")

    # ── PAS 5d: thumbnail ─────────────────────────────────────────────
    if inclou("5d"):
        if not os.path.isfile(thumbnail):
            r.error("5d", f"Falta assets/thumbnails/{slug}.png. Genera'l amb generate_thumbnail.py (sense caràtula NO es puja a archive.org)")
        else:
            dimensions = mida_png(thumbnail)
            if dimensions is None:
                r.error("5d", f"assets/thumbnails/{slug}.png no és un PNG vàlid")
            else:
                ample, alt = dimensions
                if ample != alt:
                    r.avis("5d", f"El thumbnail fa {ample}×{alt}; hauria de ser quadrat")
                else:
                    r.be("5d", f"Thumbnail present ({ample}×{alt})")
        if fm.get("thumbnail") != f"/assets/thumbnails/{slug}.png":
            r.error("5d", f"'thumbnail' al frontmatter ({fm.get('thumbnail')!r}) no coincideix amb /assets/thumbnails/{slug}.png")

    # ── PAS 6: contingut ──────────────────────────────────────────────
    if inclou("6"):
        titol = fm.get("title", "")
        if not re.match(rf"Episodi 0*{int(num)}: .+", titol):
            r.error("6", f"'title' ({titol!r}) no segueix el format \"Episodi {num}: ...\"")
        else:
            r.be("6", "Títol amb format correcte")

        if fm.get("episode_number") != int(num):
            r.error("6", f"'episode_number' ({fm.get('episode_number')!r}) no coincideix amb {int(num)}")

        descripcio = fm.get("description") or ""
        if not descripcio:
            r.error("6", "Falta 'description' al frontmatter")
        elif len(descripcio) > DESCRIPCIO_MAX_ERROR:
            r.error("6", f"'description' fa {len(descripcio)} caràcters (màxim {DESCRIPCIO_MAX_ERROR}). Surt sencera al llistat d'episodis i al RSS: retalla-la a ~650 (ganxo + temes principals)")
        elif len(descripcio) > DESCRIPCIO_MAX_OK:
            r.avis("6", f"'description' fa {len(descripcio)} caràcters; la guia recomana ~650 perquè el llistat es llegeixi bé")
        else:
            r.be("6", f"Descripció de {len(descripcio)} caràcters")

        fonts = fm.get("sources") or []
        entrada_transcripcio = [f for f in fonts if "transcripcio" in str(f.get("url", ""))]
        if len(fonts) < 2 or not entrada_transcripcio:
            r.error("6", "'sources' ha de tenir com a mínim una font real més l'entrada de la transcripció")
        else:
            url_esperada = f"{BASEURL}/sources/{slug}-transcripcio.txt"
            if entrada_transcripcio[0].get("url") != url_esperada:
                r.error("6", f"La URL de la transcripció ha de ser {url_esperada} (ara: {entrada_transcripcio[0].get('url')!r})")
            else:
                r.be("6", f"Fonts completes ({len(fonts)} entrades)")

        if body.count("**Important:**") != 1:
            r.error("6", f"El body té {body.count('**Important:**')} disclaimers '**Important:**'; n'hi ha d'haver exactament 1 (reescriu el fitxer sencer, no hi afegeixis al final)")
        if "## Fonts" not in body:
            r.error("6", "El body no té secció '## Fonts'")
        if len(body) > 25000:
            r.avis("6", f"El body fa {len(body):,} caràcters; comprova que no contingui la transcripció sencera")

        if re.search(r"/episodis/\d{3}-", body):
            r.error("6", "El body té enllaços amb /episodis/ (plural); el permalink és /episodi/ (singular)")
        enllacos_interns_malament = []
        for desti in re.findall(rf"{BASEURL}/episodi/(\d{{3}}-[a-z0-9-]+)", body):
            if not os.path.isfile(os.path.join(ROOT, "_episodes", f"{desti}.md")):
                enllacos_interns_malament.append(desti)
        for camí_intern in re.findall(rf"{BASEURL}(/(?:sources|assets)/[^)\s\"`]+)", body):
            if not os.path.isfile(os.path.join(ROOT, camí_intern.lstrip("/"))):
                enllacos_interns_malament.append(camí_intern)
        if enllacos_interns_malament:
            r.error("6", f"Enllaços interns que no existeixen: {', '.join(enllacos_interns_malament)}")
        elif not r.errors or all("enllaç" not in e for e in r.errors):
            r.be("6", "Enllaços interns correctes")

    # ── PAS 7: llista EPISODIS de l'script de pujada ──────────────────
    if inclou("7"):
        script_pujada = open(os.path.join(ROOT, "scripts", "upload_to_archive.py"), encoding="utf-8").read()
        if re.search(rf'"num":\s*"{num}"', script_pujada):
            r.be("7", "Episodi present a la llista EPISODIS d'upload_to_archive.py")
        else:
            r.error("7", f"Afegeix l'episodi {num} a la llista EPISODIS de scripts/upload_to_archive.py abans de pujar")

    # ── PAS 8: audio_file d'archive.org ───────────────────────────────
    identificador = f"podcast-del-doctor-{slug}"
    if inclou("8"):
        url_esperada = f"https://archive.org/download/{identificador}/{slug}.mp3"
        if fm.get("audio_file") == url_esperada:
            r.be("8", "audio_file apunta a archive.org amb el format correcte")
        else:
            r.error("8", f"'audio_file' hauria de ser {url_esperada} (ara: {fm.get('audio_file')!r}). El completa upload_to_archive.py al PAS 8")

    # ── Comprovacions remotes (--remot) ───────────────────────────────
    if remot:
        comprovacions = [
            ("MP3 a archive.org", fm.get("audio_file"), True),
            ("pàgina de l'episodi", f"{WEB}/episodi/{slug}/", True),
            ("transcripció .txt publicada", f"{WEB}/sources/{slug}-transcripcio.txt", True),
            ("subtítols .srt publicats", f"{WEB}/sources/{slug}-transcripcio.srt", True),
            ("capítols publicats", f"{WEB}/sources/{slug}-chapters.json", True),
        ]
        for nom, url, _ in comprovacions:
            if not url:
                continue
            try:
                resposta = peticio(url)
                if resposta.status == 200:
                    r.be("R", f"{nom}: 200 OK")
                else:
                    r.error("R", f"{nom}: codi {resposta.status} ({url})")
            except Exception as e:
                r.error("R", f"{nom}: no accessible ({url}): {e}")
        try:
            metadades = json.load(peticio(f"https://archive.org/metadata/{identificador}", nomes_capcalera=False))
            originals = {f["name"] for f in metadades.get("files", []) if f.get("source") == "original"}
            if f"{slug}.png" in originals:
                r.be("R", "Caràtula present a archive.org (source: original)")
            else:
                r.error("R", f"La caràtula {slug}.png no és a archive.org. Puja-la amb: python scripts/upload_to_archive.py --episodi {num} --nomes-cover")
        except Exception as e:
            r.error("R", f"No s'han pogut llegir les metadades d'archive.org: {e}")
        try:
            feed = peticio(f"{WEB}/feed.xml", nomes_capcalera=False).read().decode("utf-8")
            if identificador in feed:
                r.be("R", "Episodi present al feed RSS publicat")
            else:
                r.error("R", "L'episodi no surt al feed RSS publicat (falta el push, o GitHub Pages encara desplega)")
        except Exception as e:
            r.error("R", f"No s'ha pogut llegir el feed RSS: {e}")


def main():
    parser = argparse.ArgumentParser(description="Verifica que un episodi ha passat bé cada pas del workflow")
    parser.add_argument("episodi", nargs="?", help="Número (019) o slug de l'episodi")
    parser.add_argument("--pas", default="9", choices=PASSOS, help="Verificar només fins a aquest PAS del workflow (per defecte: tot)")
    parser.add_argument("--remot", action="store_true", help="Inclou comprovacions de xarxa (archive.org i web publicada)")
    parser.add_argument("--tots", action="store_true", help="Verifica tots els episodis (checks locals)")
    args = parser.parse_args()

    if not args.tots and not args.episodi:
        parser.error("cal un número d'episodi o --tots")

    if args.tots:
        slugs = sorted(re.sub(r"\.md$", "", os.path.basename(f))
                       for f in glob.glob(os.path.join(ROOT, "_episodes", "*.md")))
    else:
        slug = troba_slug(args.episodi)
        if not slug:
            print(f"❌ No s'ha trobat cap episodi que comenci per {args.episodi}")
            sys.exit(1)
        slugs = [slug]

    r = Resultat()
    for slug in slugs:
        etiqueta = f" — fins al PAS {args.pas}" if args.pas != "9" else ""
        print(f"\n🔍 {slug}{etiqueta}")
        verifica(slug, args.pas, args.remot, r, mp3_opcional=args.tots)

    print(f"\nResum: {r.ok} ✅  {len(r.avisos)} ⚠️  {len(r.errors)} ❌")
    if r.errors:
        print("\nCal corregir:")
        for e in r.errors:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
