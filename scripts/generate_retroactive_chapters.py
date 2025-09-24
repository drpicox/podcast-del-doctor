#!/usr/bin/env python3
"""
Genera capítols i soundbites per a tots els episodis del podcast.
Usa el text de les transcripcions i la durada coneguda per calcular timestamps proporcionals.
"""
import json
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).parent.parent

# Durades dels episodis en segons
DURATIONS = {
}

def load_transcript(num):
    sources = PROJECT / "sources"
    # Find file matching the episode number prefix
    for f in sorted(sources.glob(f"{num}-*transcripcio.txt")):
        return f.read_text(encoding="utf-8")
    return None

def word_to_time(word_index, total_words, duration_sec):
    """Convert word position to approximate time in seconds."""
    return round((word_index / total_words) * duration_sec, 1)

def split_words_after_header(text):
    """Strip header, return list of words."""
    lines = text.split("\n")
    # Skip header (everything before the ===== line)
    body_start = 0
    for i, line in enumerate(lines):
        if "======" in line:
            body_start = i + 1
            break
    body = " ".join(lines[body_start:])
    return body.split()

# ─────────────────────────────────────────────────────────────────────────────
# Per-episode chapter definitions
# Format: list of (fraction_of_text, chapter_title)
# Fraction 0.0 = start, 1.0 = end
# ─────────────────────────────────────────────────────────────────────────────
CHAPTERS_DEF = {
}

# ─────────────────────────────────────────────────────────────────────────────
# Per-episode soundbite definitions
# Format: (fraction_start, duration_sec, title)
# ─────────────────────────────────────────────────────────────────────────────
SOUNDBITES = {
}

def generate_chapters_json(num):
    duration = DURATIONS[num]
    chapters_def = CHAPTERS_DEF[num]
    chapters = []
    for frac, title in chapters_def:
        start = round(frac * duration, 1)
        chapters.append({"startTime": start, "title": title})
    return {
        "version": "1.2.0",
        "chapters": chapters
    }

def generate_soundbite(num):
    duration = DURATIONS[num]
    frac, sb_dur, title = SOUNDBITES[num]
    start = round(frac * duration, 1)
    return start, sb_dur, title

def main():
    episodes = sorted(DURATIONS.keys())
    
    for num in episodes:
        # Generate chapters JSON
        chapters = generate_chapters_json(num)
        
        # Find the episode md file to get the slug
        ep_files = sorted((PROJECT / "_episodes").glob(f"{num}-*.md"))
        if not ep_files:
            print(f"⚠️  No episode file found for {num}")
            continue
        ep_file = ep_files[0]
        slug = ep_file.stem  # e.g. "001-nom-episodi"
        
        # Write chapters JSON
        chapters_filename = f"{slug}-chapters.json"
        chapters_path = PROJECT / "sources" / chapters_filename
        with open(chapters_path, "w", encoding="utf-8") as f:
            json.dump(chapters, f, ensure_ascii=False, indent=2)
        print(f"✅ {chapters_filename} ({len(chapters['chapters'])} capítols)")
        
        # Update episode frontmatter
        sb_start, sb_dur, sb_title = generate_soundbite(num)
        
        ep_content = ep_file.read_text(encoding="utf-8")
        
        # Check if fields already exist
        if "chapters_file:" in ep_content:
            print(f"   ℹ️  {ep_file.name}: chapters_file ja existeix, ometent")
        else:
            # Add chapters_file, soundbite fields after 'layout:' or before closing ---
            # Find the second --- (end of frontmatter)
            parts = ep_content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                body = parts[2]
                new_fields = f"\nchapters_file: \"{chapters_filename}\"\nsoundbite_start: {sb_start}\nsoundbite_duration: {sb_dur}\nsoundbite_title: \"{sb_title}\""
                new_content = f"---{fm}{new_fields}\n---{body}"
                ep_file.write_text(new_content, encoding="utf-8")
                print(f"   ✅ Frontmatter actualitzat: {ep_file.name}")
    
    print("\n🎉 Tots els episodis processats!")

if __name__ == "__main__":
    main()
