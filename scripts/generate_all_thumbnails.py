#!/usr/bin/env python3
"""
Genera thumbnails per a tots els episodis del podcast usant ollama x/z-image-turbo.

Ús:
    python scripts/generate_all_thumbnails.py           # tots els episodis
    python scripts/generate_all_thumbnails.py 013       # un episodi concret
    python scripts/generate_all_thumbnails.py --force   # regenera fins i tot si ja existeix

Requisits:
    - ollama instal·lat: https://ollama.com
    - Model descarregat: ollama pull x/z-image-turbo
"""

import os
import sys
import subprocess

# Mapa episodi → (slug, prompt_suffix en anglès)
EPISODES = {
}


def main():
    args = sys.argv[1:]
    force = "--force" in args
    filter_ep = None
    for arg in args:
        if arg != "--force":
            filter_ep = arg.zfill(3)  # normalize: "13" → "013"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)

    episodes_to_process = sorted(EPISODES.keys()) if filter_ep is None else [filter_ep]

    if filter_ep and filter_ep not in EPISODES:
        print(f"❌ Episodi '{filter_ep}' no definit a EPISODES en aquest script.")
        print(f"   Episodis disponibles: {', '.join(sorted(EPISODES.keys()))}")
        sys.exit(1)

    total = 0
    success = 0
    skipped = 0
    failed = 0

    os.makedirs("assets/thumbnails", exist_ok=True)

    for num in episodes_to_process:
        slug, prompt_suffix = EPISODES[num]
        total += 1

        # Check if thumbnail already exists
        existing = [
            f for f in [
                f"assets/thumbnails/{slug}.png",
                f"assets/thumbnails/{slug}.jpg",
                f"assets/thumbnails/{slug}.jpeg",
                f"assets/thumbnails/{slug}.webp",
            ]
            if os.path.exists(f)
        ]

        if existing and not force:
            print(f"⏭️  Saltant episodi {num} (thumbnail ja existeix: {existing[0]})")
            skipped += 1
            continue

        print(f"\n{'═' * 52}")
        print(f"🎨 Generant thumbnail episodi {num}: {slug}")
        print(f"{'═' * 52}")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/generate_thumbnail.py",
                "--episodi", num,
                "--nom", slug,
                "--prompt-suffix", prompt_suffix,
            ]
        )

        if result.returncode == 0:
            success += 1
        else:
            print(f"❌ Error generant thumbnail per episodi {num}")
            failed += 1

    print(f"\n{'═' * 52}")
    print(f"📊 Resum: {total} episodis")
    print(f"   ✅ Nous thumbnails: {success}")
    print(f"   ⏭️  Saltats (ja existien): {skipped}")
    print(f"   ❌ Errors: {failed}")
    print(f"{'═' * 52}")

    if success > 0:
        print(f"\n🔧 Pròxim pas: afegir els thumbnails al repositori:")
        print(f"   git add assets/thumbnails/ && git commit -m 'Add episode thumbnails'")


if __name__ == "__main__":
    main()
