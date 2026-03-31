#!/usr/bin/env python3
"""
Script per pujar automàticament tots els episodis del podcast a archive.org
Requereix: pip install internetarchive
Configuració: ia configure (només primera vegada)
"""

import os
import sys
from pathlib import Path
from internetarchive import upload, get_item

# Configuració del podcast
CREATOR = "David Rodenas"
COLLECTION = None  # No especificar col·lecció - es crearà al compte personal
LICENSE = "http://creativecommons.org/licenses/by/4.0/"
LANGUAGE = "cat"
WEBSITE = "https://david-rodenas.com"
PODCAST_URL = "https://david-rodenas.com/podcast-del-doctor"

# Definició dels episodis amb les seves metadades
EPISODIS = [
    {
        "num": "001",
        "fitxer": "001-api-ollama-per-dins.mp3",
        "identifier": "podcast-del-doctor-001-api-ollama-per-dins",
        "title": "Episodi 1: Com funciona l'API d'Ollama per dins",
        "description": "Anàlisi a fons de l'API d'Ollama: gestió de recursos GPU/CPU, endpoints Generate i Chat, paràmetres de control, streaming NDJSON, Tool Calling, sortides estructurades i emulació d'OpenAI. Tot executant-se localment.",
        "date": "2026-03-31",
        "duration": "20:04",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "ollama", "api", "llm", "ia local", "gpu", "tool calling", "openai", "streaming"]
    },
]


def crear_metadata(episodi):
    """Crea el diccionari de metadades per archive.org"""
    
    description_completa = f"""{episodi['description']}

⚠️ Aquest contingut ha estat generat amb intel·ligència artificial. Pot contenir interpretacions que no encaixin completament amb la realitat. Consulta sempre les fonts originals.

Més informació: {WEBSITE}
Podcast: {PODCAST_URL}"""
    
    metadata = {
        'title': f"Podcast del Doctor - {episodi['title']}",
        'mediatype': 'audio',
        'creator': CREATOR,
        'description': description_completa,
        'date': episodi['date'],
        'language': LANGUAGE,
        'licenseurl': LICENSE,
        'subject': ';'.join(episodi['tags']),
        'duration': episodi['duration'],
        'external-identifier': f'urn:podcast:podcast-del-doctor:{episodi["num"]}',
    }
    
    # Afegir col·lecció només si està definida
    if COLLECTION:
        metadata['collection'] = COLLECTION
    
    return metadata


def pujar_episodi(episodi, episodes_dir, dry_run=False):
    """Puja un episodi a archive.org"""
    
    fitxer_path = episodes_dir / episodi['fitxer']
    
    if not fitxer_path.exists():
        print(f"❌ ERROR: No s'ha trobat el fitxer {fitxer_path}")
        return None
    
    identifier = episodi['identifier']
    metadata = crear_metadata(episodi)
    
    print(f"\n📦 Pujant episodi {episodi['num']}: {episodi['title']}")
    print(f"   Fitxer: {fitxer_path}")
    print(f"   Identifier: {identifier}")
    
    if dry_run:
        print("   🔍 MODE DRY-RUN: No es puja realment")
        print(f"   Metadades: {metadata}")
        url = f"https://archive.org/download/{identifier}/{episodi['fitxer']}"
        return url
    
    try:
        # Comprovar si ja existeix
        item = get_item(identifier)
        if item.exists:
            print(f"   ⚠️  L'ítem ja existeix a archive.org")
            resposta = input("   Vols sobreescriure'l? (s/N): ")
            if resposta.lower() != 's':
                print("   ⏭️  Saltat")
                url = f"https://archive.org/download/{identifier}/{episodi['fitxer']}"
                return url
        
        # Pujar el fitxer
        r = upload(
            identifier,
            files=[str(fitxer_path)],
            metadata=metadata,
            verify=True,
            verbose=True,
            queue_derive=True,
            retries=3
        )
        
        if r[0].status_code == 200:
            url = f"https://archive.org/download/{identifier}/{episodi['fitxer']}"
            print(f"   ✅ Pujat correctament!")
            print(f"   📍 URL: {url}")
            print(f"   🌐 Pàgina: https://archive.org/details/{identifier}")
            return url
        else:
            print(f"   ❌ Error en pujar: {r[0].status_code}")
            return None
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None


def actualitzar_markdown(episodi, url, episodes_md_dir):
    """Actualitza el camp audio_file del markdown de l'episodi"""
    
    md_file = episodes_md_dir / f"{episodi['fitxer'].replace('.mp3', '.md')}"
    
    if not md_file.exists():
        print(f"   ⚠️  No s'ha trobat el markdown: {md_file}")
        return False
    
    try:
        content = md_file.read_text()
        
        # Buscar la línia audio_file i reemplaçar-la
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('audio_file:'):
                old_value = line
                lines[i] = f'audio_file: "{url}"'
                print(f"   ✏️  Actualitzat markdown:")
                print(f"      Abans: {old_value}")
                print(f"      Ara:   {lines[i]}")
                break
        
        md_file.write_text('\n'.join(lines))
        return True
        
    except Exception as e:
        print(f"   ❌ Error actualitzant markdown: {e}")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Puja episodis a archive.org')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Mostra què es faria sense pujar res')
    parser.add_argument('--episodi', type=str,
                       help='Pujar només un episodi específic (ex: 001)')
    parser.add_argument('--no-update-md', action='store_true',
                       help='No actualitzar els fitxers markdown')
    
    args = parser.parse_args()
    
    # Directoris del projecte
    project_dir = Path(__file__).parent.parent
    episodes_dir = project_dir / 'episodes'
    episodes_md_dir = project_dir / '_episodes'
    
    print("🎙️  Script de pujada automàtica a archive.org")
    print("=" * 60)
    
    # Filtrar episodis si s'ha especificat un
    episodis_a_pujar = EPISODIS
    if args.episodi:
        episodis_a_pujar = [e for e in EPISODIS if e['num'] == args.episodi]
        if not episodis_a_pujar:
            print(f"❌ No s'ha trobat l'episodi {args.episodi}")
            sys.exit(1)
    
    print(f"\n📋 Episodis a processar: {len(episodis_a_pujar)}")
    
    if args.dry_run:
        print("\n🔍 MODE DRY-RUN ACTIVAT - No es pujarà res realment\n")
    
    # Processar cada episodi
    urls_generades = {}
    for episodi in episodis_a_pujar:
        url = pujar_episodi(episodi, episodes_dir, dry_run=args.dry_run)
        
        if url:
            urls_generades[episodi['num']] = url
            
            if not args.no_update_md and not args.dry_run:
                actualitzar_markdown(episodi, url, episodes_md_dir)
    
    # Resum final
    print("\n" + "=" * 60)
    print("📊 RESUM")
    print("=" * 60)
    print(f"✅ Episodis processats: {len(urls_generades)}/{len(episodis_a_pujar)}")
    
    if urls_generades:
        print("\n📍 URLs generades:")
        for num, url in sorted(urls_generades.items()):
            print(f"   {num}: {url}")
    
    if not args.dry_run and urls_generades and not args.no_update_md:
        print("\n💡 Recorda fer:")
        print("   git add _episodes/")
        print("   git commit -m 'Migrar URLs a archive.org'")
        print("   git push")


if __name__ == '__main__':
    main()
