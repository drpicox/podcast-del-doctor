#!/usr/bin/env python3
"""
Script per pujar automàticament tots els episodis del podcast a archive.org
Requereix: pip install internetarchive
Configuració: ia configure (només primera vegada)
"""

import os
import sys
import time
from pathlib import Path

import requests
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
    {
        "num": "002",
        "fitxer": "002-origen-caos-ortografic-angles.mp3",
        "identifier": "podcast-del-doctor-002-origen-caos-ortografic-angles",
        "title": "Episodi 2: L'Origen del Caos Ortogràfic Anglès",
        "description": "La gran rotació vocàlica anglesa: per què l'ortografia és un caos lingüístic. Analitzem els mecanismes interns (cadena d'arrossegament vs. d'empenta), el context històric (Pesta Negra, guerra de França), i com la impremta de Caxton va congelar la pronunciació del segle XV, creant fòssils ortogràfics com 'knight'.",
        "date": "2026-04-01",
        "duration": "15:02",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "lingüística", "idioma anglès", "ortografia", "gran rotació vocàlica", "història", "fonètica", "impremta", "caxton"]
    },
    {
        "num": "003",
        "fitxer": "003-spacex-ingenyeria-software-aprendre.mp3",
        "identifier": "podcast-del-doctor-003-spacex-ingenyeria-software-aprendre",
        "title": "Episodi 003: Test-Driven Development amb Dave Farley",
        "description": "Una anàlisi fonamental sobre Test-Driven Development (TDD). Amb Dave Farley, explorem com els tests no són només validació sinó una eina essencial de disseny que millora la qualitat del codi, la mantenibilitat i la col·laboració entre equips. Descobrim el cicle red-green-refactor, Behavior-Driven Development (BDD), i per què TDD accelera la desenvolupament en lloc de ralentir-la.",
        "date": "2026-04-01",
        "duration": "16:29",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "tdd", "test-driven development", "dave farley", "bdd", "testing", "refactoring", "software design", "software engineering"]
    },
    {
        "num": "004",
        "fitxer": "004-domar-ia-precisio.mp3",
        "identifier": "podcast-del-doctor-004-domar-ia-precisio",
        "title": "Episodi 004: Domar la IA per programar amb precisió",
        "description": "Com domesticar la intel·ligència artificial per aconseguir precisió en la programació? Explorem els descobriments reveladors de l'Ada Kessler sobre els veritables perills i potencials de treballar amb models de llenguatge extens. Descobrim per què els llocs comuns sobre la 'finestra de context' són insuficients, com gestionar la 'podridura del context', per què els 'superagents' generalistes són una trampa, la importància de la fricció intencionada, l'elasticitat del text (DOOM semàntic), i com els desenvolupadors passem de ser creadors de codi a directors d'orquestra de múltiples agents especialitzats.",
        "date": "2026-04-03",
        "duration": "32:43",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "ia", "llm", "ada kessler", "augmented coding", "context window", "agents", "prompt engineering", "software design", "nondeterminism", "git worktrees", "evaluation", "evals"]
    },
    {
        "num": "005",
        "fitxer": "005-ouro-ia-pensa-en-bucle.mp3",
        "identifier": "podcast-del-doctor-005-ouro-ia-pensa-en-bucle",
        "title": "Episodi 005: Ouro, la IA que pensa en bucle",
        "description": "Quin seria el proper gran salt en IA si en lloc de construir models cada vegada més grans i cars, ensenyéssim a un de petit a pensar en bucle? Explorem Ouro, un model de llenguatge en bucle (LoopLM) de només 2.6 bilions de paràmetres que supera models de 12 bilions en raonament matemàtic. Basat en l'article 'Scaling Latent Reasoning via Looped Language Models' (arxiv:2510.25741) de ByteDance, UC Santa Cruz i Princeton.",
        "date": "2026-04-11",
        "duration": "13:02",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "ia", "llm", "ouro", "looped language models", "latent reasoning", "chain-of-thought", "raonament", "arxiv", "bytedance", "princeton", "democratitzacio ia", "espai latent"]
    },
    {
        "num": "006",
        "fitxer": "006-raonament-autonom-claude-mythos.mp3",
        "identifier": "podcast-del-doctor-006-raonament-autonom-claude-mythos",
        "title": "Episodi 006: El raonament autònom de Claude Mythos",
        "description": "Una filtració massiva des de l'interior d'Anthropic ha exposat Claude Mythos, un model especulatiu de 10 bilions de paràmetres que combina Mixture of Experts ultradispers amb recurrència latent. Un sistema que rumia en silenci en el seu espai vectorial intern, aconsegueix un 97.6% al benchmark USAMO de matemàtiques i és capaç de trobar zero-days de 27 anys amagats en codi revisat 5 milions de vegades.",
        "date": "2026-04-11",
        "duration": "13:58",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "ia", "llm", "claude", "anthropic", "mixture of experts", "moe", "recurrència latent", "raonament autònom", "ciberseguretat", "zero-day", "espai latent", "claude mythos"]
    },
    {
        "num": "007",
        "fitxer": "007-com-domar-el-geni-trampos.mp3",
        "identifier": "podcast-del-doctor-007-com-domar-el-geni-trampos",
        "title": "Episodi 007: Com domar el geni trampós",
        "description": "La intel·ligència artificial és com un geni dels contes antics: immensament poderós, però trampós, descuidat i perillosament literal. Basant-nos en 'El geni trampós', una adaptació accessible dels patrons Augmented Coding de Lada Kessler, explorem per quin motiu la IA pateix amnèsia digital, per què una conversa es 'podreix', com evitar el biaix de complacència i les al·lucinacions, i com aplicar l'enginyeria de la conversa pas a pas.",
        "date": "2026-04-15",
        "duration": "37:21",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "ia", "intel·ligència artificial", "llm", "lada kessler", "augmented coding", "prompt engineering", "context window", "biaix de complacença", "amnèsia digital", "enginyeria de conversa", "productivitat"]
    },
    {
        "num": "008",
        "fitxer": "008-colmap-reconstrueix-mon-3d.mp3",
        "identifier": "podcast-del-doctor-008-colmap-reconstrueix-mon-3d",
        "title": "Episodi 008: Com COLMAP reconstrueix el món en 3D",
        "description": "Com pot un ordinador reconstruir un espai tridimensional a partir de simples fotografies planes? Analitzem a fons COLMAP, el programari de codi obert creat per Johannes Schönberger que s'ha convertit en l'estàndard de la indústria per a la reconstrucció 3D a partir d'imatges. Des de l'algorisme SIFT fins al bundle adjustment, passant pel drama CPU vs GPU i l'alternativa moderna GLOMAP.",
        "date": "2026-04-19",
        "duration": "16:03",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "colmap", "reconstrucció 3d", "fotogrametria", "sift", "bundle adjustment", "glomap", "gaussian splatting", "visió per computador", "estructura from motion", "sfm"]
    },
    {
        "num": "009",
        "fitxer": "009-construir-mons-3d-sense-drons.mp3",
        "identifier": "podcast-del-doctor-009-construir-mons-3d-sense-drons",
        "title": "Episodi 009: Construir mons 3D sense drons",
        "description": "Podem construir mons tridimensionals a partir de simples fotos fetes amb el mòbil, sense drons ni GPS? Aprofundim en el pipeline complet de COLMAP des de la perspectiva de la captura a peu: extracció SIFT, mascarament de soroll dinàmic, model de càmera amb distorsió radial, estratègies de matching, verificació geomètrica, reconstrucció incremental, bundle adjustment, el drama CPU vs GPU, i la revolució de GLOMAP amb les seves espectaculars fallades en forma de Borg cubes.",
        "date": "2026-04-20",
        "duration": "45:35",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "colmap", "reconstrucció 3d", "fotogrametria", "sift", "bundle adjustment", "glomap", "captura terrestre", "vocab tree", "matching", "verificació geomètrica", "cpu vs gpu", "loop closure"]
    },
    {
        "num": "010",
        "fitxer": "010-reconstruccio-3d-colmap-mobils.mp3",
        "identifier": "podcast-del-doctor-010-reconstruccio-3d-colmap-mobils",
        "title": "Episodi 010: Reconstrucció 3D amb COLMAP i mòbils",
        "description": "Com pot un simple telèfon mòbil capturar espais exteriors gegantins en 3D sense drons ni GPS? Tercer episodi de la sèrie sobre COLMAP — en català — repassant tot el pipeline: extracció SIFT, distorsió radial, estratègies d'emparellament, triangulació, bundle adjustment, CPU vs GPU, GLOMAP amb loop closures, i una reflexió sobre privacitat.",
        "date": "2026-04-20",
        "duration": "19:18",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "colmap", "reconstrucció 3d", "fotogrametria", "sift", "bundle adjustment", "glomap", "mòbil", "privacitat", "vocab tree", "cpu vs gpu", "loop closure", "català"]
    },
    {
        "num": "011",
        "fitxer": "011-parany-acomiadaments-ia.mp3",
        "identifier": "podcast-del-doctor-011-parany-acomiadaments-ia",
        "title": "Episodi 011: El parany dels acomiadaments per IA",
        "description": "Per què les empreses que acomiaden treballadors per estalviar costos amb IA podrien estar destruint els seus propis beneficis? Basat en el paper 'The AI Layoff Trap' de Falk i Tsoukalas (2026): l'externalitat de la demanda, el dilema del presoner de l'automatització, per què fallen els salaris flexibles, la renda bàsica i els pactes voluntaris — i com un impost pigouvià sobre l'automatització pot corregir la fallada de coordinació.",
        "date": "2026-06-11",
        "duration": "23:34",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "intel·ligència artificial", "acomiadaments", "automatització", "economia", "externalitat", "dilema del presoner", "impost pigouvià", "renda bàsica", "upskilling", "teoria de jocs", "català"]
    },
    {
        "num": "012",
        "fitxer": "012-especificacio-nou-codi.mp3",
        "identifier": "podcast-del-doctor-012-especificacio-nou-codi",
        "title": "Episodi 012: L'especificació és el nou codi",
        "description": "Per què una IA capaç d'escriure codi a la velocitat de la llum no ens estalvia la part difícil de programar? Basant-nos en un vídeo del canal Modern Software Engineering de Dave Farley, amb Stefan Ellisdorfer i Christian Gassel, explorem el desenvolupament dirigit per especificacions amb IA agèntica: la manca de determinisme com a verí, l'ATDD i el BDD que converteixen les proves en el contracte executable de la IA, l'efecte mirall, l'índex Farley i el pas de programadors a enginyers de comportaments.",
        "date": "2026-06-16",
        "duration": "14:03",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "intel·ligència artificial", "agentic ai", "dave farley", "spec-driven development", "atdd", "bdd", "tdd", "especificacions executables", "enginyeria de programari", "índex farley", "català"]
    },
    {
        "num": "013",
        "fitxer": "013-per-que-ningu-llegeix-el-que-escrius.mp3",
        "identifier": "podcast-del-doctor-013-per-que-ningu-llegeix-el-que-escrius",
        "title": "Episodi 013: Per què ningú llegeix el que escrius",
        "description": "I si tot allò que ens feia treure excel·lents en redacció a l'escola fos exactament la raó per la qual ningú llegeix els nostres informes a la feina? Basant-nos en dues conferències mítiques del Leadership Lab de la Universitat de Chicago, impartides per Larry McEnerney, explorem per què el valor d'un text no viu mai a les seves pàgines sinó dins del cervell de qui llegeix: la il·lusió del lector pagat, la metàfora de la paret de tenis, l'experiment dels 100 errors gramaticals que ningú va detectar, per què assenyalar un buit no serveix i cal assenyalar un error, i com el focus i l'estrès d'una frase decideixen si t'acaben llegint o et descarten.",
        "date": "2026-07-28",
        "duration": "35:22",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "escriptura", "comunicació", "larry mcenerney", "university of chicago", "leadership lab", "escriptura professional", "escriptura acadèmica", "retòrica", "comunicació efectiva", "català"]
    },
    {
        "num": "014",
        "fitxer": "014-impost-ocult-habilitats-ia.mp3",
        "identifier": "podcast-del-doctor-014-impost-ocult-habilitats-ia",
        "title": "Episodi 014: L'impost ocult de la IA (càpsula en anglès)",
        "description": "Càpsula curta —i excepcionalment en anglès— sobre l'estudi «How AI Impacts Skill Formation» de Judy Hanwen Shen i Alex Tamkin. Un assaig aleatoritzat amb desenvolupadors que aprenen una llibreria de programació asíncrona nova mostra que els qui la van aprendre amb ajuda de la IA van acabar entenent pitjor la feina que acabaven de lliurar, i van fallar especialment a l'hora de depurar codi trencat sense assistència. A la pantalla, el projecte està acabat; dins del cap, el mapa mental de com funciona aquell codi es queda buit. La versió llarga i en català d'aquest mateix estudi és l'episodi 015.",
        "date": "2026-07-31",
        "duration": "00:54",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "intel·ligència artificial", "aprenentatge", "habilitats", "desenvolupament de programari", "depuració", "arxiv", "skill formation", "anglès"]
    },
    {
        "num": "015",
        "fitxer": "015-ia-atrofia-les-habilitats.mp3",
        "identifier": "podcast-del-doctor-015-ia-atrofia-les-habilitats",
        "title": "Episodi 015: L'IA ens està atrofiant les habilitats",
        "description": "El GPS ens ha atrofiat el sentit de l'orientació —els taxistes de Londres tenien un hipocamp físicament més gran— i la pregunta d'aquest episodi és si la IA està fent exactament el mateix amb les nostres habilitats intel·lectuals. Analitzem a fons l'estudi «How AI Impacts Skill Formation» (arXiv:2601.20245), un assaig aleatoritzat amb 52 programadors que havien d'aprendre la llibreria asíncrona Trio: els que van tenir assistent d'IA van treure un 17% menys al test i no van guanyar temps, perquè el van gastar redactant prompts. Parlem de la fricció com a mecanisme d'aprenentatge, del problema de la verificació, dels sis perfils d'interacció (tres que fracassen i tres que funcionen), de la il·lusió de competència, de l'exosquelet cognitiu i del deute intel·lectual corporatiu.",
        "date": "2026-07-31",
        "duration": "19:19",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "intel·ligència artificial", "aprenentatge", "habilitats", "metacognició", "desenvolupament de programari", "depuració", "python", "trio", "programació asíncrona", "arxiv", "skill formation", "català"]
    },
    {
        "num": "016",
        "fitxer": "016-com-okf-ordena-la-ia.mp3",
        "identifier": "podcast-del-doctor-016-com-okf-ordena-la-ia",
        "title": "Episodi 016: OKF, la carpeta de text que ordena el caos de la IA",
        "description": "Imagina un agent d'IA que esborra les projeccions d'ingressos trimestrals no per un error de programari, sinó per un problema de lectura: ha trobat una nota oblidada de l'any passat que contradiu la base de dades. Aquest episodi analitza l'Open Knowledge Format (OKF), l'estàndard obert que Google Cloud va llançar el juny de 2026 per posar fi al caos del context. La sorpresa és com n'és, de senzill: un arbre de carpetes amb fitxers Markdown en UTF-8 i un bloc YAML al capdamunt on l'únic camp obligatori és «type». Parlem del patró LLM Wiki de Karpathy, de per què l'OKF passa d'una recuperació probabilística (el RAG i els seus vectors) a una de determinista amb enllaços explícits, dels cinc senyals de confiança de la v0.2 —provinença, generated/verified, estat, data de caducitat absoluta i atestació computacional—, de com encaixa amb MCP, Agent Skills i llms.txt (les canonades, el manual i l'aigua), del GEO i la capa de cervell de marca, de la sobirania de dades sota el GDPR, i d'una idea especulativa: els mercats de coneixement expert empaquetat.",
        "date": "2026-08-02",
        "duration": "20:54",
        "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", "intel·ligència artificial", "open knowledge format", "okf", "google cloud", "rag", "knowledge graph", "markdown", "yaml", "mcp", "model context protocol", "agent skills", "llms.txt", "geo", "gdpr", "agents", "català"]
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


def cover_path(episodi, project_dir):
    """Retorna el path del thumbnail de l'episodi, o None si no existeix.

    La caràtula ha de dir-se com l'ítem perquè archive.org la trii com a imatge
    principal de l'ítem (genera __ia_thumb.jpg a partir seu en fer el derive).
    """
    nom = episodi['fitxer'].rsplit('.', 1)[0]
    path = project_dir / 'assets' / 'thumbnails' / f"{nom}.png"
    return path if path.exists() else None


def cover_arribada(identifier, nom_fitxer, mida_local=None):
    """Comprova que la NOSTRA caràtula és realment a l'ítem d'archive.org.

    Dues trampes que cal esquivar:

    1) Si l'ítem té un derive en curs, upload() retorna 200 i archive.org
       descarta el fitxer en silenci. El codi de resposta NO és garantia.
    2) archive.org genera un derivat de l'MP3 que es diu EXACTAMENT igual que
       el nostre thumbnail (<nom>.png) — la forma d'ona. Per això no n'hi ha
       prou de comprovar que el fitxer existeix: ha de ser 'source: original'
       (pujat per nosaltres) i no 'derivative'.
    """
    try:
        md = requests.get(f"https://archive.org/metadata/{identifier}",
                          timeout=30).json()
    except (requests.RequestException, ValueError):
        return False

    for f in md.get('files', []):
        if f.get('name') != nom_fitxer:
            continue
        if f.get('source') != 'original':
            return False  # és el derivat d'archive.org, no el nostre
        if mida_local is not None and int(f.get('size', 0)) != mida_local:
            return False  # hi ha un fitxer nostre però desactualitzat
        return True
    return False


def esperar_sense_tasques(identifier, timeout=900, interval=30):
    """Espera que l'ítem no tingui tasques en curs (derive, archive...)."""
    limit = time.time() + timeout
    while time.time() < limit:
        try:
            md = requests.get(f"https://archive.org/metadata/{identifier}",
                              timeout=30).json()
            if not md.get('pending_tasks'):
                return True
        except (requests.RequestException, ValueError):
            pass
        print(f"      ⏳ tasques en curs a l'ítem, esperant {interval}s…")
        time.sleep(interval)
    return False


def pujar_cover(episodi, project_dir, dry_run=False, intents=4, espera=90):
    """Puja la caràtula a un ítem existent i verifica que hi ha arribat."""

    identifier = episodi['identifier']
    cover = cover_path(episodi, project_dir)

    print(f"\n🖼️  Caràtula episodi {episodi['num']}: {episodi['title']}")

    if cover is None:
        print(f"   ⚠️  No s'ha trobat el thumbnail a assets/thumbnails/ — saltat")
        return False

    print(f"   Fitxer: {cover.name}")
    print(f"   Identifier: {identifier}")

    if dry_run:
        print("   🔍 MODE DRY-RUN: No es puja realment")
        return True

    try:
        item = get_item(identifier)
        if not item.exists:
            print(f"   ⚠️  L'ítem no existeix encara a archive.org — puja primer l'MP3")
            return False
    except Exception as e:
        print(f"   ❌ Error consultant l'ítem: {e}")
        return False

    mida = cover.stat().st_size
    if cover_arribada(identifier, cover.name, mida):
        print(f"   ⏭️  La caràtula ja hi és (nostra, {mida} bytes)")
        return True

    for intent in range(1, intents + 1):
        print(f"   🔄 Intent {intent}/{intents}")

        # Un derive en curs fa que la pujada es perdi silenciosament
        esperar_sense_tasques(identifier)

        try:
            r = upload(
                identifier,
                files=[str(cover)],
                verify=True,
                verbose=True,
                queue_derive=True,
                retries=3
            )
            codi = r[0].status_code if r else None
            print(f"      resposta: {codi if codi else 'cap (res a pujar)'}")
        except Exception as e:
            print(f"      ⚠️  Error en pujar: {e}")

        # Verificació real: el codi 200 no és garantia
        print(f"      🔎 verificant que el fitxer hi és…")
        time.sleep(espera)
        if cover_arribada(identifier, cover.name, mida):
            print(f"   ✅ Caràtula confirmada a archive.org!")
            print(f"   🌐 https://archive.org/details/{identifier}")
            return True

        print(f"      ❌ el fitxer encara no hi és")

    print(f"   ❌ No s'ha pogut confirmar la caràtula després de {intents} intents")
    return False


def pujar_episodi(episodi, episodes_dir, dry_run=False, project_dir=None,
                  exigir_cover=True):
    """Puja un episodi a archive.org (MP3 + caràtula).

    Per defecte s'atura si no hi ha caràtula: val més no publicar que publicar
    un episodi sense imatge. Amb exigir_cover=False (--sense-cover) es força.
    """

    fitxer_path = episodes_dir / episodi['fitxer']

    if not fitxer_path.exists():
        print(f"❌ ERROR: No s'ha trobat el fitxer {fitxer_path}")
        return None

    identifier = episodi['identifier']
    metadata = crear_metadata(episodi)

    if project_dir is None:
        project_dir = episodes_dir.parent
    cover = cover_path(episodi, project_dir)

    fitxers = [str(fitxer_path)]
    if cover:
        fitxers.append(str(cover))

    print(f"\n📦 Pujant episodi {episodi['num']}: {episodi['title']}")
    print(f"   Fitxer: {fitxer_path}")
    print(f"   Identifier: {identifier}")

    if cover:
        print(f"   Caràtula: {cover.name}")
    else:
        nom = episodi['fitxer'].rsplit('.', 1)[0]
        esperat = project_dir / 'assets' / 'thumbnails' / f"{nom}.png"
        if exigir_cover:
            print(f"   ❌ ATURAT: no hi ha caràtula, no es puja res")
            print(f"      Esperava trobar-la a: {esperat}")
            print(f"      Genera-la amb:")
            print(f"      python scripts/generate_thumbnail.py --episodi {episodi['num']} \\")
            print(f"          --nom {nom} --prompt-suffix 'element visual en anglès'")
            print(f"      Si realment vols publicar sense imatge: afegeix --sense-cover")
            return None
        print(f"   ⚠️  ATENCIÓ: NO hi ha caràtula i s'ha demanat --sense-cover")
        print(f"      L'episodi es publicarà sense imatge. Per posar-la-hi més tard:")
        print(f"      python scripts/upload_to_archive.py --episodi {episodi['num']} --nomes-cover")

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

        # Pujar els fitxers
        r = upload(
            identifier,
            files=fitxers,
            metadata=metadata,
            verify=True,
            verbose=True,
            queue_derive=True,
            retries=3
        )

        if r[0].status_code != 200:
            print(f"   ❌ Error en pujar: {r[0].status_code}")
            return None

        url = f"https://archive.org/download/{identifier}/{episodi['fitxer']}"
        print(f"   ✅ MP3 pujat correctament!")
        print(f"   📍 URL: {url}")
        print(f"   🌐 Pàgina: https://archive.org/details/{identifier}")

        # El status_code de dalt és el de l'MP3: no diu res de la caràtula.
        # I un 200 tampoc garanteix que el fitxer hagi arribat (mira
        # cover_arribada). Cal verificar-ho i reintentar-ho a part.
        if cover:
            print(f"   🔎 verificant la caràtula…")
            time.sleep(30)
            if cover_arribada(identifier, cover.name, cover.stat().st_size):
                print(f"   ✅ Caràtula confirmada!")
            else:
                print(f"   ⚠️  La caràtula no ha arribat — reintentant a part")
                pujar_cover(episodi, project_dir)

        return url
            
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
    parser.add_argument('--nomes-cover', action='store_true',
                       help='Pujar només la caràtula a ítems que ja existeixen (no re-puja l\'MP3)')
    parser.add_argument('--sense-cover', action='store_true',
                       help='Permetre publicar un episodi sense caràtula (per defecte s\'atura)')

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
    
    # Mode caràtula: només pujar la imatge a ítems existents
    if args.nomes_cover:
        ok = 0
        for episodi in episodis_a_pujar:
            if pujar_cover(episodi, project_dir, dry_run=args.dry_run):
                ok += 1
        print("\n" + "=" * 60)
        print("📊 RESUM")
        print("=" * 60)
        print(f"✅ Caràtules processades: {ok}/{len(episodis_a_pujar)}")
        return

    # Processar cada episodi
    urls_generades = {}
    for episodi in episodis_a_pujar:
        url = pujar_episodi(episodi, episodes_dir, dry_run=args.dry_run,
                            project_dir=project_dir,
                            exigir_cover=not args.sense_cover)

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
