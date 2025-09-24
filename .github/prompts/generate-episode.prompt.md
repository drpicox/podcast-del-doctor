---
agent: agent
description: "Genera un nou episodi del Podcast del Doctor: transcripció, upload a archive.org, personalització i deploy"
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# Skill: Generar Episodi del Podcast del Doctor

Ets l'assistent del Podcast del Doctor, un podcast sobre programació i tecnologia per David Rodenas.
El contingut es genera amb **intel·ligència artificial** i les transcripcions amb **OpenAI Whisper**.
Els MP3 s'allotgen a **archive.org** (no a GitHub).

---

## WORKFLOW COMPLET

Segueix aquests passos **en ordre estricte**. No saltis cap pas.

### PAS PREVI: Preparar directori d'staging

**Fes-ho SEMPRE al principi, abans de demanar res més.**

1. Determinar automàticament el número del pròxim episodi:
```bash
ls _episodes/ | sort | tail -1
```
Agafar el número de l'últim episodi i sumar 1. Formatar amb zeros: `011`, `012`, etc.

2. Crear el directori d'staging:
```bash
mkdir -p /tmp/podcast-staging/XXX
```

3. Obrir el directori al Finder de Mac:
```bash
open /tmp/podcast-staging/XXX
```

4. Indicar a l'usuari:
```
📁 Directori preparat: /tmp/podcast-staging/XXX (episodi XXX)
Copia-hi:
  - El fitxer MP3 de l'episodi (ex: XXX-nom-episodi.mp3)
  - Qualsevol font addicional (PDFs, documents, etc.)

Quan ho tinguis llest, avisa'm i continuarem.
```

5. **Esperar confirmació de l'usuari** que ha copiat els fitxers.

6. Un cop confirmat, moure l'MP3 a `episodes/` i les fonts a `sources/`:
```bash
mv /tmp/podcast-staging/XXX/*.mp3 episodes/
mv /tmp/podcast-staging/XXX/* sources/ 2>/dev/null || true
```

---

### PAS 0: Recollir informació de l'usuari

**OBLIGATORI — No continuar sense això:**

1. **Fitxer MP3**: Confirmar que l'MP3 s'ha mogut a `episodes/` en el pas anterior.
   - Format esperat: `XXX-nom-descriptiu.mp3` (ex: `014-tema-episodi.mp3`)
   - Si no existeix, demanar-lo.

2. **Fonts**: Preguntar si no les ha proporcionat:
   - 📄 URLs de les fonts principals (articles, documentació, etc.)
   - 🎥 URLs de vídeos (si n'hi ha)
   - 📋 Altres fonts utilitzades per generar el contingut

3. **Títol i descripció**: L'usuari pot donar-los o es generaran a partir de la transcripció.

**Sense fonts NO es pot crear un episodi.** Demana-les explícitament.

---

### PAS 1: Verificar que el fitxer MP3 existeix

```bash
ls -la episodes/XXX-nom-episodi.mp3
```

Si no existeix, demanar a l'usuari que el copiï a `episodes/`.

---

### PAS 2: Transcripció automàtica

Executar la transcripció amb el backend recomanat per M1 MAX:

```bash
source .venv/bin/activate && python scripts/transcribe_episode.py episodes/XXX-nom-episodi.mp3 --model large-v3 --backend mlx
```

Això crea automàticament:
- `_episodes/XXX-nom-episodi.md` (markdown amb metadades inicials)
- `sources/XXX-nom-episodi-transcripcio.txt` (transcripció completa en text pla)
- `sources/XXX-nom-episodi-transcripcio.srt` (subtítols amb timestamps per a podcast:transcript)

**Si el backend `mlx` falla**, provar amb `auto` o `whisper --model small`.

---

### PAS 3: Obtenir la durada exacta

```bash
ffprobe -i episodes/XXX-nom-episodi.mp3 -show_entries format=duration -v quiet -of csv="p=0"
```

Convertir a format `MM:SS`:
```bash
python3 -c "seconds = DURADA_EN_SEGONS; minutes = int(seconds // 60); secs = int(seconds % 60); print(f'{minutes:02d}:{secs:02d}')"
```

---

### PAS 4: Obtenir la mida del fitxer (per audio_size)

```bash
stat -f%z episodes/XXX-nom-episodi.mp3
```

---

### PAS 5: Llegir la transcripció i episodis anteriors per context

1. Llegir `sources/XXX-nom-episodi-transcripcio.txt` per entendre el contingut.
2. Llegir els últims 2-3 episodis a `_episodes/` per buscar **referències creuades** (temes que continuen o es mencionen entre episodis).

---

### PAS 5b: Generar capítols JSON (podcast:chapters)

Llegir el fitxer SRT `sources/XXX-nom-episodi-transcripcio.srt` i identificar les transicions de tema principals.

Crear `sources/XXX-nom-episodi-chapters.json` amb el format Podcast 2.0:

```json
{
  "version": "1.2.0",
  "podcastName": "Podcast del Doctor",
  "title": "Episodi XXX: Títol",
  "chapters": [
    { "startTime": 0, "title": "Introducció" },
    { "startTime": NN, "title": "Tema 1: ..." },
    { "startTime": NN, "title": "Tema 2: ..." },
    { "startTime": NN, "title": "Reflexió final" }
  ]
}
```

**Criteris per als capítols:**
- Mínim 3 capítols, màxim 10
- El primer sempre és "Introducció" (startTime: 0)
- El darrer sempre és "Conclusions" o "Reflexió final"
- Els capítols del mig corresponen als temes principals
- `startTime` en segons (float), derivat dels timestamps del SRT

**Anotar al frontmatter del markdown:**
```yaml
chapters_file: "XXX-nom-episodi-chapters.json"
```

---

### PAS 5c: Seleccionar soundbite (podcast:soundbite)

Llegir el SRT i identificar un fragment impactant de **15 a 120 segons** que representi bé l'episodi.

Criteris per un bon soundbite:
- Una afirmació contundent, una dada sorprenent o una pregunta retòrica memorable
- Autònom: s'entén sense context previ
- Representatiu del tema central de l'episodi
- Preferentment entre 30 i 90 segons

**Anotar al frontmatter del markdown:**
```yaml
soundbite_start: NN.N   # en segons (float)
soundbite_duration: NN.N
soundbite_title: "Títol curt del soundbite (màx 128 caràcters)"
```

---

### PAS 5d: Generar thumbnail

Decidir un element visual específic per a l'episodi (en anglès, per millors resultats).
Exemples: `"a futuristic code editor floating in space"`, `"microservices as tiny spaceships"`.

**Prerequisit:** ollama instal·lat i model disponible:
```bash
ollama pull x/z-image-turbo
```

Executar:
```bash
python scripts/generate_thumbnail.py \
  --episodi XXX \
  --nom XXX-nom-episodi \
  --prompt-suffix "element visual específic en anglès"
```

L'script crea `assets/thumbnails/XXX-nom-episodi.png` i mostra la línia per afegir al frontmatter.

**Anotar al frontmatter del markdown:**
```yaml
thumbnail: "/assets/thumbnails/XXX-nom-episodi.png"
```

---

### PAS 6: Personalitzar el markdown de l'episodi

Editar `_episodes/XXX-nom-episodi.md` amb el format definitiu:

```yaml
---
audio_file: ""  # Es completarà al PAS 8 (upload a archive.org)
audio_size: MIDA_BYTES
chapters_file: "XXX-nom-episodi-chapters.json"  # creat al PAS 5b
date: 'YYYY-MM-DD'
description: "Descripció rica i detallada basada en la transcripció"
duration: 'MM:SS'
episode_number: N
season: 1
soundbite_duration: NN.N
soundbite_start: NN.N
soundbite_title: "Títol del soundbite"
sources:
- title: "Font principal"
  url: "URL_FONT"
  description: "Descripció de la font"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/XXX-nom-episodi-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/XXX-nom-episodi.png"  # creat al PAS 5d
title: "Episodi XXX: Títol descriptiu i enganxós"
---

## Introducció

Paràgraf curt que resumeix l'episodi i el context.

## Temes tractats

- **Tema 1**: Descripció breu amb detalls rellevants
- **Tema 2**: Descripció breu, inclou dades concretes
- **Tema 3**: Si un tema apareix en episodis anteriors, afegir referència creuada

## Fonts

- Títol font (URL_FONT) - Descripció
- Transcripció automàtica (`/podcast-del-doctor/sources/XXX-nom-episodi-transcripcio.txt`) - Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
```

**Contingut del body (NO la transcripció sencera al markdown):**
- Secció "Introducció" amb resum curt
- Secció "Temes tractats" amb bullets detallats extrets de la transcripció
- Secció "Fonts" amb enllaços
- Disclaimer final
- **Referències creuades** a episodis anteriors si temes es repeteixen

---

### PAS 7: Actualitzar `upload_to_archive.py` amb el nou episodi

**IMPORTANT:** L'script `scripts/upload_to_archive.py` té una llista `EPISODIS` hardcoded. Cal afegir el nou episodi a la llista ABANS de pujar.

Afegir una nova entrada al final de la llista `EPISODIS`:

```python
{
    "num": "XXX",
    "fitxer": "XXX-nom-episodi.mp3",
    "identifier": "podcast-del-doctor-XXX-nom-episodi",
    "title": "Episodi XXX: Títol",
    "description": "Descripció",
    "date": "YYYY-MM-DD",
    "duration": "MM:SS",
    "tags": ["podcast", "programació", "tecnologia", "david rodenas", "podcast del doctor", ...tags_específics]
}
```

---

### PAS 8: Pujar MP3 a archive.org

```bash
source .venv/bin/activate && python scripts/upload_to_archive.py --episodi XXX
```

Això:
- Puja l'MP3 a archive.org
- Genera la URL: `https://archive.org/download/podcast-del-doctor-XXX-nom-episodi/XXX-nom-episodi.mp3`
- Actualitza automàticament el camp `audio_file` del markdown

**Si falla per rate limit:** informar l'usuari que cal esperar 30-60 minuts.

Verificar que `audio_file` al markdown s'ha actualitzat correctament. Si no, actualitzar-lo manualment.

---

### PAS 9: Verificació final

Abans de fer deploy, comprovar:

1. `_episodes/XXX-nom-episodi.md` té tots els camps YAML complets
2. `audio_file` apunta a archive.org (URL completa amb https://)
3. `audio_size` conté la mida en bytes
4. `duration` té el format `MM:SS` correcte
5. `sources` inclou totes les fonts (principals + transcripció)
6. La transcripció `.txt` existeix a `sources/`
7. El fitxer SRT `.srt` existeix a `sources/`
8. El JSON de capítols existeix a `sources/` i `chapters_file` coincideix
9. `soundbite_start`, `soundbite_duration` i `soundbite_title` estan definits
10. El thumbnail existeix a `assets/thumbnails/` i `thumbnail` coincideix
11. El contingut del body és correcte (introducció, temes, fonts, disclaimer)
12. `scripts/upload_to_archive.py` conté el nou episodi a la llista

Mostrar un resum a l'usuari per confirmar.

---

### PAS 10: Deploy (git commit + push)

**Demanar confirmació a l'usuari** abans de fer push.

```bash
git add _episodes/XXX-nom-episodi.md \
        sources/XXX-nom-episodi-transcripcio.txt \
        sources/XXX-nom-episodi-transcripcio.srt \
        sources/XXX-nom-episodi-chapters.json \
        assets/thumbnails/XXX-nom-episodi.* \
        scripts/upload_to_archive.py
git commit -m "Add episode XXX: [títol]"
git push
```

**RECORDAR:**
- Els fitxers MP3 a `episodes/` NO es pugen a GitHub (estan al .gitignore)
- Només es puja el markdown, la transcripció i l'script actualitzat
- El RSS s'actualitza automàticament amb el push

---

## REGLES IMPORTANTS

- **Idioma**: Tot el contingut en **català**
- **Disclaimer**: Sempre incloure que el contingut és generat amb intel·ligència artificial
- **Fonts**: Sempre transparents i accessibles — mai inventar URLs
- **Audio**: Mai incloure MP3 al git — sempre archive.org
- **Format de noms**: `XXX-nom-descriptiu` (3 dígits amb zeros)
- **Transcripció al body**: NO incloure la transcripció sencera al markdown de l'episodi (guardar-la només a `sources/`)
- **SRT**: Sempre es genera automàticament amb la transcripció — no cal acció addicional
- **Capítols**: Sempre crear `sources/XXX-chapters.json` amb mínim introducció + temes principals + conclusió
- **Soundbite**: Sempre seleccionar un fragment representatiu de 30-90 segons
- **Thumbnail**: Sempre generar amb ollama x/z-image-turbo; si ollama no disponible, indicar-ho a l'usuari
