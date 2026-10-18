#!/usr/bin/env python3
"""
Genera els jingles d'entrada i sortida del podcast (assets/audio/jingle-*.wav).

Són notes compostes a mà i sintetitzades amb oscil·ladors, a l'estil del BBC
Radiophonic Workshop: baix galopant, glissando eteri, arpegi i un acord final
amb una nota aguda amb vibrato. Motius propis, res de la sintonia de Doctor Who
(té drets i archive.org/Spotify podrien retirar els episodis).

Per què no MusicGen: es va provar (2026-10) i té dos problemes. A MPS (torch
2.3) genera soroll en comptes de música, i a CPU fa música en bucle, sense
principi ni final, així que retallada a 2-3 s sona tallada.

Els fitxers de assets/audio/ són la referència. Es van triar d'una audició on
abans s'havien generat altres variants, així que el soroll del whoosh i de la
reverb va sortir d'un altre punt de la llavor: aquest script en dona una versió
gairebé idèntica (mateixes notes), no idèntica bit a bit. Escolta el resultat
abans de substituir-los.

Ús:
    python scripts/generate_jingles.py                 # escriu a assets/audio/
    python scripts/generate_jingles.py --output-dir /tmp/proves
"""

import argparse
import os

import numpy as np
import soundfile as sf
from scipy.signal import butter, fftconvolve, sosfilt

SR = 44100
rng = np.random.default_rng(7)


def hz(n):
    return 440.0 * 2 ** ((n - 69) / 12)  # MIDI -> Hz


def env(n, a=0.005, d=0.08, s=0.6, r=0.15):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    hold = max(n - a - d - r, 0)
    e = np.concatenate([np.linspace(0, 1, a), np.linspace(1, s, d), np.full(hold, s), np.linspace(s, 0, r)])
    return np.pad(e, (0, max(0, n - len(e))))[:n]


def osc(f, n, kind="saw", detune=0.0):
    t = np.arange(n) / SR
    out = 0
    for dt in ([0] if not detune else [-detune, detune]):
        if kind == "saw":
            out = out + 2 * ((f * (1 + dt) * t) % 1.0) - 1
        else:
            out = out + np.sign(np.sin(2 * np.pi * f * (1 + dt) * t))
    return out / (2 if detune else 1)


def lp(x, fc):
    return sosfilt(butter(2, min(fc, SR / 2 - 100) / (SR / 2), "low", output="sos"), x)


def sweep_lp(x, f0, f1):
    out = np.zeros_like(x)
    for i in range(0, len(x), 512):
        fc = f0 + (f1 - f0) * i / len(x)
        out[i:i + 512] = sosfilt(butter(2, fc / (SR / 2), "low", output="sos"), x[i:i + 512])
    return out


def place(buf, sig, t):
    i = int(t * SR)
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[:j - i]


def note(n, dur, kind="saw", vol=0.3, cutoff=3000, detune=0.004, **e):
    N = int(dur * SR)
    return lp(osc(hz(n), N, kind, detune), cutoff) * env(N, **e) * vol


def whoosh(dur, up=True, vol=0.15):
    N = int(dur * SR)
    x = rng.standard_normal(N)
    y = sweep_lp(x, 200, 6000) if up else sweep_lp(x, 6000, 200)
    return y * (np.linspace(0, 1, N) if up else np.linspace(1, 0, N)) ** 1.5 * vol


def gliss(n0, n1, dur, vol=0.25):
    N = int(dur * SR)
    ph = np.cumsum(np.geomspace(hz(n0), hz(n1), N)) / SR
    return np.sin(2 * np.pi * ph) * env(N, a=0.02, s=0.9, r=0.03) * vol


def ether(n, dur, vol=0.2):
    """Nota sinusoidal amb vibrato: el so 'eteri'."""
    N = int(dur * SR)
    t = np.arange(N) / SR
    vib = np.sin(2 * np.pi * hz(n) * t + 0.6 * np.sin(2 * np.pi * 6 * t))
    return lp(vib, 5000) * env(N, a=0.01, s=0.8, r=dur * 0.7) * vol


def chord(b, notes, t, dur, vol=0.12, cut=2500):
    for n in notes:
        place(b, note(n, dur, "saw", vol, cut, r=dur * 0.7), t)


def gallop(buf, root, t0, beats, bpm=150, vol=0.32):
    """Ritme galopant (ta-ta-TAM) al baix."""
    b = 60 / bpm
    for k in range(beats):
        t = t0 + k * b
        for off, d, v in ((0, b * 0.22, 0.7), (b * 0.25, b * 0.22, 0.7), (b * 0.5, b * 0.45, 1.0)):
            place(buf, note(root, d, "saw", vol * v, 900, 0.002, a=0.003, d=0.05, s=0.5, r=0.03), t + off)


def reverb(x, dur=1.6, decay=0.45, mix=0.35):
    t = np.arange(int(dur * SR)) / SR
    ir = rng.standard_normal(len(t)) * np.exp(-t / decay)
    ir /= np.sqrt(np.sum(ir ** 2))
    y = np.concatenate([x, np.zeros(len(ir))])
    return y + mix * fftconvolve(y, ir)[:len(y)]


def finish(buf, path):
    y = reverb(buf)
    y = y[:int(np.max(np.nonzero(np.abs(y) > 1e-3)) + 1)]
    f = int(0.05 * SR)
    y[-f:] *= np.linspace(1, 0, f)
    sf.write(path, y / np.max(np.abs(y)) * 0.9, SR)
    print(f"✅ {path} ({len(y) / SR:.1f}s)")


# Mi menor (E2 = 40).
def entrada(path):
    """Galop ràpid, glissando curt, arpegi que puja i acord amb nota eteria aguda."""
    b = np.zeros(int(4 * SR))
    gallop(b, 40, 0, 3, bpm=170, vol=0.27)
    place(b, gliss(52, 64, 0.35), 0.0)
    for i, n in enumerate([64, 67, 71, 76]):
        place(b, note(n, 0.12, "square", 0.15, 4500), 0.35 + i * 0.09)
    place(b, whoosh(0.7, True, 0.12), 0.1)
    chord(b, (64, 71, 76, 79), 0.75, 1.4, 0.1)
    place(b, ether(88, 1.4, 0.1), 0.75)
    place(b, note(40, 1.4, "saw", 0.3, 600, r=1.0), 0.75)
    finish(b, path)


def sortida(path):
    """El mateix recorregut a l'inrevés: arpegi i glissando baixant, resol en greu."""
    b = np.zeros(int(4 * SR))
    for i, n in enumerate([76, 71, 67, 64]):
        place(b, note(n, 0.12, "square", 0.15, 4500), i * 0.09)
    place(b, gliss(64, 52, 0.4), 0.36)
    gallop(b, 40, 0.2, 2, bpm=140, vol=0.22)
    chord(b, (40, 52, 59), 0.85, 1.8, 0.13, 1000)
    place(b, ether(64, 1.8, 0.1), 0.85)
    place(b, whoosh(0.9, False, 0.1), 0.2)
    finish(b, path)


def main():
    parser = argparse.ArgumentParser(description="Genera els jingles d'entrada i sortida")
    parser.add_argument("--output-dir", default="assets/audio")
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    entrada(os.path.join(args.output_dir, "jingle-entrada.wav"))
    sortida(os.path.join(args.output_dir, "jingle-sortida.wav"))


if __name__ == "__main__":
    main()
