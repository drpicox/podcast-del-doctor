#!/usr/bin/env python3
"""
Afegeix els jingles a un episodi JA publicat i hi ajusta tots els temps.

Els episodis nous ja els porten des del PAS 1b (abans de transcriure). Per als
antics, en comptes de retranscriure (Whisper s'inventa text sobre la música),
es desplacen els temps existents:

  - sources/XXX-transcripcio.srt     tots els blocs + desplaçament
  - sources/XXX-chapters.json        startTime/endTime > 0 + desplaçament
                                     (el capítol 0, "Introducció", queda a 0
                                     i així inclou el jingle)
  - _episodes/XXX.md                 soundbite_start + desplaçament,
                                     duration i audio_size remesurats
  - sources/XXX-transcripcio.txt     sense temps: no es toca

El desplaçament es MESURA (correlació creuada entre l'àudio nou i l'original
desat a episodes/sense-jingles/) i s'atura sense tocar res si no coincideix amb
l'esperat (jingle d'entrada menys el solapament). No puja res: després cal
    python scripts/upload_to_archive.py --episodi XXX --nomes-mp3

Ús:
    python scripts/retrofit_jingles.py --episodi 038
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import add_jingles  # noqa: E402

SR_MESURA = 8000
TOLERANCIA = 0.05  # segons


def pcm(camí, inici, durada):
    """Tros d'àudio mono a 8 kHz com a array."""
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(inici), "-t", str(durada), "-i", camí,
         "-ac", "1", "-ar", str(SR_MESURA), "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, dtype=np.float32)


def mesura_desplaçament(nou, original):
    """On és, dins l'àudio nou, el tros 20-30 s de l'original."""
    ref = pcm(original, 20, 10)
    finestra = pcm(nou, 15, 25)  # cobreix desplaçaments de -5 a +15 s
    n = len(finestra) + len(ref)
    corr = np.fft.irfft(np.fft.rfft(finestra, n) * np.conj(np.fft.rfft(ref, n)), n)
    lag = int(np.argmax(corr[:len(finestra)]))
    return 15 + lag / SR_MESURA - 20


def esperat():
    return add_jingles.desplaçament()


def srt_temps(t):
    h, m, resta = t.split(":")
    s, ms = resta.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def temps_srt(x):
    ms = int(round(x * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def desplaça_srt(camí, d):
    text = open(camí, encoding="utf-8").read()
    patró = re.compile(r"(\d\d:\d\d:\d\d,\d\d\d)(\s*-->\s*)(\d\d:\d\d:\d\d,\d\d\d)")
    nou, n = patró.subn(lambda m: temps_srt(srt_temps(m[1]) + d) + m[2] + temps_srt(srt_temps(m[3]) + d), text)
    open(camí, "w", encoding="utf-8").write(nou)
    return n


def desplaça_capitols(camí, d):
    dades = json.load(open(camí, encoding="utf-8"))
    for c in dades["chapters"]:
        for k in ("startTime", "endTime"):
            if k in c and c[k] > 0:
                c[k] = round(c[k] + d, 1)
    # Respectar el format compacte (un capítol per línia) que fem servir
    linies = ",\n".join(
        "    { " + ", ".join(f"{json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}" for k, v in c.items()) + " }"
        for c in dades["chapters"])
    capçalera = {k: v for k, v in dades.items() if k != "chapters"}
    cos = json.dumps(capçalera, ensure_ascii=False, indent=2)[:-2]
    open(camí, "w", encoding="utf-8").write(cos + ',\n  "chapters": [\n' + linies + "\n  ]\n}\n")
    return len(dades["chapters"])


def actualitza_md(camí, d, mp3):
    text = open(camí, encoding="utf-8").read()
    durada = float(json.loads(subprocess.run(
        ["ffprobe", "-v", "quiet", "-of", "json", "-show_entries", "format=duration", mp3],
        capture_output=True, text=True, check=True).stdout)["format"]["duration"])

    def subst(camp, valor):
        nonlocal text
        text, n = re.subn(rf"^({camp}:\s*)(['\"]?)[^'\"\n]*\2\s*$", lambda m: f"{m[1]}{m[2]}{valor}{m[2]}", text, count=1, flags=re.M)
        if not n:
            print(f"   ⚠️  camp '{camp}' no trobat al frontmatter")

    m = re.search(r"^soundbite_start:\s*([\d.]+)", text, flags=re.M)
    if m:
        subst("soundbite_start", f"{float(m[1]) + d:.1f}")
    subst("duration", f"{int(durada // 60):02d}:{int(durada % 60):02d}")
    subst("audio_size", str(os.path.getsize(mp3)))
    open(camí, "w", encoding="utf-8").write(text)


def main():
    parser = argparse.ArgumentParser(description="Jingles retroactius + ajust de temps")
    parser.add_argument("--episodi", required=True)
    args = parser.parse_args()

    mp3 = add_jingles.troba_mp3(args.episodi)
    slug = os.path.basename(mp3)[:-4]
    md = os.path.join(ROOT, "_episodes", f"{slug}.md")
    srt = os.path.join(ROOT, "sources", f"{slug}-transcripcio.srt")
    capitols = os.path.join(ROOT, "sources", f"{slug}-chapters.json")
    original = os.path.join(os.path.dirname(mp3), "sense-jingles", os.path.basename(mp3))

    if add_jingles.ja_te_jingles(mp3):
        print(f"⏭️  {slug} ja té els jingles: no desplaço res (es desplaçaria dos cops)")
        return

    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "add_jingles.py"), mp3], check=True)

    d = mesura_desplaçament(mp3, original)
    e = esperat()
    print(f"📏 Desplaçament mesurat {d:.3f} s, esperat {e:.3f} s")
    if abs(d - e) > TOLERANCIA:
        os.replace(original, mp3)
        print(f"❌ No quadra: he restaurat l'MP3 original i no he tocat cap fitxer de text")
        sys.exit(1)
    d = round(d, 2)

    if os.path.isfile(srt):
        print(f"   SRT: {desplaça_srt(srt, d)} blocs desplaçats")
    if os.path.isfile(capitols):
        print(f"   Capítols: {desplaça_capitols(capitols, d)} revisats")
    actualitza_md(md, d, mp3)
    print(f"✅ {slug}: jingles afegits i temps ajustats (+{d:.2f} s). Ara cal pujar l'MP3:")
    print(f"   python scripts/upload_to_archive.py --episodi {args.episodi} --nomes-mp3")


if __name__ == "__main__":
    main()
