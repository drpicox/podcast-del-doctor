# Instruccions per a Claude Code - Podcast del Doctor

## Resum del Projecte

Podcast sobre programació i tecnologia per David Rodenas. El contingut es genera amb **intel·ligència artificial** basant-se en fonts públiques.

## Allotjament dels Fitxers MP3

Els fitxers MP3 dels episodis **NO s'allotgen a GitHub** (massa grans). En lloc d'això:

- 📦 **Archive.org**: Allotjament públic i permanent dels MP3
- 💾 **Local**: Còpia de seguretat a `episodes/` (ignorada per git)
- 🔗 **RSS Feed**: Apunta directament a les URLs d'archive.org

### Per què archive.org?
- Gratuït i sense límits de mida
- Preservació permanent de contingut
- URLs públiques estables
- Bandwidth il·limitat
- Missió d'arxiu cultural

## Estructura del Projecte

```
/
├── episodes/           # Fitxers MP3 dels episodis
├── _episodes/          # Fitxers markdown amb metadades dels episodis
├── sources/            # Fonts, transcripcions (.txt), subtítols (.srt) i capítols (.json)
├── scripts/            # Scripts d'automatització
├── assets/
│   ├── thumbnails/     # Thumbnails per episodi (generats amb ollama)
│   └── logo-podcast.jpg
├── _layouts/           # Plantilles Jekyll
└── feed.xml           # RSS feed del podcast (inclou Podcast 2.0 namespace)
```

## Workflow per Nous Episodis

### 0. **PRIMER PAS: Obtenir les fonts** ⚠️ OBLIGATORI

**SEMPRE demanar ABANS de començar:**
- 📄 **URLs de les fonts principals** (articles, documentació, etc.)
- 🎥 **URLs de vídeos** (si n'hi ha)
- 📋 **Altres fonts utilitzades** per generar el contingut

**Sense fonts NO es pot crear un episodi.**

### 1. **Preparar el nou episodi**
```bash
# Desar l'MP3 a episodes/ amb format: XXX-nom-episodi.mp3
# Exemple: 001-nom-episodi.mp3
# IMPORTANT: Aquest fitxer NO es pujarà a GitHub (està al .gitignore)
```

### 2. **Instal·lar dependències (primera vegada)**
```bash
pip install -r requirements.txt
```

### 3. **Transcripció automàtica**

**Backends disponibles:**
- `mlx` (per defecte en M1/M2/M3): GPU accelerat amb Apple MLX (~3-4x més ràpid)
- `lightning`: Ultra-ràpid, pot perdre precisió (~10x més ràpid)
- `whisper`: CPU/CUDA (fallback compatibilitat)
- `auto`: Detecció automàtica segons hardware

```bash
# RECOMANAT per M1 MAX (32GB RAM): model large-v3 amb MLX
python scripts/transcribe_episode.py episodes/001-nom-episodi.mp3 --model large-v3 --backend mlx

# Opció ràpida (detecta automàticament backend i model):
./scripts/quick_transcribe.sh episodes/001-nom-episodi.mp3

# Ultra-ràpid (experimental):
python scripts/transcribe_episode.py episodes/001-nom-episodi.mp3 --backend lightning

# CPU fallback:
python scripts/transcribe_episode.py episodes/001-nom-episodi.mp3 --backend whisper --model small
```

**Què fa automàticament:**
- Transcriu l'MP3 amb Whisper (backend seleccionat)
- Crea `_episodes/001-nom-episodi.md` amb metadades
- Guarda transcripció a `sources/001-nom-episodi-transcripcio.txt`
- **Genera `sources/001-nom-episodi-transcripcio.srt`** amb timestamps per a podcast:transcript
- Genera descripció automàtica

**Temps de transcripció (episodi 26 min, M1 MAX):**
- Backend `mlx` + model `large-v3`: ~2-3 min (màxima qualitat)
- Backend `mlx` + model `medium`: ~1-1.5 min
- Backend `lightning`: ~30-60 seg (experimental)
- Backend `whisper` (CPU): ~5-6 min

**El script de transcripció ja crea el markdown amb `audio_file` buit. Ara el completarem.**

### 4. **Pujar MP3 a archive.org** 🌐 (AUTOMÀTIC)

```bash
# Primera vegada només: configurar credencials d'archive.org
ia configure

# Pujar l'episodi automàticament (XXX = número episodi)
python scripts/upload_to_archive.py --episodi XXX
```

**Què fa l'script:**
- ✅ Puja l'MP3 a archive.org amb totes les metadades
- ✅ Puja `assets/thumbnails/XXX-nom-episodi.png` com a caràtula de l'ítem
- ✅ **Verifica** que la caràtula hi ha arribat i la reintenta si cal
- ✅ Genera la URL pública automàticament
- ✅ Actualitza el camp `audio_file` del markdown

⛔ **Sense caràtula NO puja res.** Si `assets/thumbnails/XXX-nom-episodi.png` no
existeix, l'script s'atura i no toca archive.org. Genera-la primer (PAS 5d). Per
publicar igualment sense imatge cal demanar-ho explícitament amb `--sense-cover`.

**IMPORTANT:** Si reps error de "rate limit", espera 30-60 minuts i torna a intentar.

**Caràtula a episodis ja publicats** (no re-puja l'MP3):
```bash
python scripts/upload_to_archive.py --nomes-cover              # tots
python scripts/upload_to_archive.py --episodi XXX --nomes-cover # un de sol
```

⚠️ **Dos paranys d'archive.org** (ja resolts a l'script, però convé saber-los):
1. `upload()` pot retornar **200 i descartar el fitxer en silenci** si l'ítem té
   un *derive* en curs. Per això l'script espera que no hi hagi tasques pendents
   i després **verifica** amb l'API de metadades.
2. archive.org genera un derivat de l'MP3 anomenat **exactament igual** que el
   nostre thumbnail (`XXX-nom-episodi.png`): la forma d'ona. Comprovar només que
   el fitxer existeix dona fals positiu — cal exigir `source: original` i que la
   mida coincideixi amb la del fitxer local.

Un cop pujada la caràtula, archive.org ha de refer el *derive* per regenerar
`__ia_thumb.jpg`, que és la imatge que surt als llistats. Pot trigar una estona.
Comprovació ràpida: `curl -sIL https://archive.org/services/img/<identifier>`
(la tira d'ona fa 180×45 en escala de grisos; una caràtula bona, 180×180 en color).

**Més detalls:** Consulta [ARCHIVE_ORG.md](ARCHIVE_ORG.md) o [scripts/README_UPLOAD.md](scripts/README_UPLOAD.md)

### 5. **Personalitzar l'episodi**
Editar `_episodes/XXX-nom-episodi.md`:

```yaml
---
title: "Episodi X: Títol Personalitzat"
date: 2025-XX-XX
duration: "XX:XX"  # Actualitzar amb durada real (obtenir amb ffprobe)
audio_file: "https://archive.org/download/podcast-del-doctor-XXX-nom-episodi/XXX-nom-episodi.mp3"
description: "Descripció personalitzada basada en el contingut"
sources:
  - title: "Font principal"
    url: "URL_real"
    description: "Descripció de la font"
  - title: "Transcripció automàtica de l'episodi"
    url: "/sources/XXX-nom-episodi-transcripcio.txt"
    description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
---
```

**Obtenir durada real de l'episodi:**
```bash
# Opció 1: Format curt (recomanat)
ffprobe -i episodes/XXX-nom-episodi.mp3 -show_entries format=duration -v quiet -of csv="p=0"

# Opció 2: Informació completa
ffmpeg -i episodes/XXX-nom-episodi.mp3 2>&1 | grep Duration

# Conversió a MM:SS (si cal):
python3 -c "import math; seconds = 837.459592; minutes = int(seconds // 60); secs = int(seconds % 60); print(f'{minutes:02d}:{secs:02d}')"
```

**Contingut a actualitzar:**
- Títol més descriptiu
- Descripció basada en transcripció
- **Durada exacta de l'episodi** (amb ffprobe)
- **`audio_file`**: URL COMPLETA d'archive.org (no només el nom del fitxer)
- Fonts reals utilitzades
- Contingut principal de l'episodi
- **Referències creuades** a episodis anteriors relacionats (si n'hi ha)

### 6. **Afegir fonts utilitzades**
Sempre especificar:
- **Article/document principal** (nom publicació, URL)
- **Vídeos** (URL YouTube si escau)
- **Transcripcions manuals** (si n'hi ha)
- **Documentació tècnica** (URLs oficials)

### 7. **Deploy** ⚠️ FER SEMPRE AL FINAL
```bash
git add _episodes/XXX-nom-episodi.md
git commit -m "Add episode XXX: [títol]"
git push
```

**IMPORTANT:**
- Sempre executar aquest pas al final per publicar l'episodi
- No deixar canvis sense commit
- Els fitxers MP3 a `episodes/` NO es pugen a GitHub (estan al .gitignore)
- Només es puja el markdown amb la URL d'archive.org
- El RSS s'actualitza automàticament amb el push

## Consideracions Importants

### **Disclaimer sempre present**
Tots els episodis han d'incloure:
- Contingut generat amb intel·ligència artificial
- Fonts sempre transparents i accessibles

### **Format de fitxers**
- **MP3**: `XXX-nom-descriptiu.mp3`
- **Episodis**: `_episodes/XXX-nom-descriptiu.md`
- **Transcripcions**: `sources/XXX-nom-descriptiu-transcripcio.txt`
- **Subtítols (SRT)**: `sources/XXX-nom-descriptiu-transcripcio.srt`
- **Capítols**: `sources/XXX-nom-descriptiu-chapters.json`
- **Thumbnails**: `assets/thumbnails/XXX-nom-descriptiu.png`

### **Qualitat MP3**
- **Bitrate**: 128 kbps
- **Durada**: ~10 minuts
- **Mida**: ~10-12 MB

## Scripts Disponibles

### **Transcripció**
- `scripts/quick_transcribe.sh` - Script ràpid
- `scripts/transcribe_episode.py` - Script principal amb opcions
- `scripts/generate_all_srt.sh` - Genera SRTs per a tots els episodis (retroactiu)
- Models Whisper: `tiny`, `small`, `medium` (recomanat), `large`

### **Thumbnails**
- `scripts/generate_thumbnail.py` - Genera thumbnail per a un episodi
- `scripts/generate_all_thumbnails.py` - Genera thumbnails per a tots els episodis
- Model: `ollama x/z-image-turbo` (cal tenir ollama instal·lat)

### **Verificació** ✅
- `scripts/check_episode.py` - Verifica que cada pas del workflow ha quedat bé i es queixa amb el que cal corregir

```bash
python scripts/check_episode.py 019              # checks locals complets d'un episodi
python scripts/check_episode.py 019 --pas 5d     # només fins a un pas concret (durant la generació)
python scripts/check_episode.py 019 --remot      # inclou archive.org, web publicada i feed RSS
python scripts/check_episode.py --tots           # tots els episodis (salut general del repositori)
```

Comprova, entre d'altres: fitxers presents (`.txt`, `.srt`, chapters, thumbnail),
durada real contra ffprobe, `audio_size`, `description` curta (~650 caràcters màxim),
soundbite dins de rang, capítols vàlids, enllaços interns amb `/episodi/` (singular)
que existeixen, disclaimer únic, episodi a la llista d'`upload_to_archive.py`, i
`audio_file` amb el format d'archive.org. Codi de sortida 1 si hi ha errors.

### **Models i Backends de Whisper**

#### **Acceleració hardware:**
- ✅ **Apple Silicon (M1/M2/M3)**: GPU accelerat amb **MLX** (recomanat)
  - Backend `mlx`: Usa Neural Engine + GPU (~3-4x més ràpid que CPU)
  - Backend `lightning`: Ultra-optimitzat (~10x més ràpid, pot perdre precisió)
  - ⚠️ Backend `whisper` amb MPS: NO compatible (error SparseMPS)
- ✅ **CUDA (NVIDIA)**: Backend `whisper` amb acceleració GPU
- 💻 **CPU**: Backend `whisper` sense GPU (fallback)

#### **Temps de transcripció (episodi 26 min):**

**M1 MAX (32GB RAM) amb backend MLX:**
- Model `large-v3`: ~2-3 min ⭐ **Recomanat per màxima qualitat**
- Model `large`: ~2 min
- Model `medium`: ~1-1.5 min
- Model `small`: ~45-60 seg

**CPU (sense GPU):**
- Model `small`: ~5:40 min (ràtio ~1:5)
- Model `medium`: ~7-8 min (timeout 10 min per CPU)

#### **Selecció de model i backend:**

**Per M1 MAX (32GB RAM):**
- `large-v3` + `mlx`: **Recomanat** - Millor qualitat, sense timeout
- `medium` + `mlx`: Balanç velocitat/qualitat
- `lightning`: Experimental, màxima velocitat

**Per altres màquines:**
- `medium` + `whisper`: Si tens GPU NVIDIA o episodis curts (≤10 min)
- `small` + `whisper`: Si CPU o episodis llargs (>10 min)
- `tiny`: Només per proves ràpides

**Models disponibles:**
- `large-v3`: Última versió, màxima precisió (recomanat per M1 MAX)
- `large`: Alta precisió
- `medium`: Balanç qualitat/velocitat
- `small`: Ràpid, qualitat acceptable
- `base`: Molt ràpid, qualitat baixa
- `tiny`: Proves ràpides

## Podcast 2.0 (podcast namespace)

El feed RSS utilitza el **Podcast 2.0 namespace** (`xmlns:podcast="https://podcastindex.org/namespace/1.0"`) per oferir funcionalitats avançades en apps compatibles (PodcastAddict, Fountain, Pocket Casts, etc.).

### Tags actius per episodi

| Tag | Què fa | Fitxer font |
|-----|--------|-------------|
| `podcast:transcript` | Subtítols sincronitzats (SRT) | `sources/XXX-transcripcio.srt` |
| `podcast:chapters` | Capítols amb timestamps navegables | `sources/XXX-chapters.json` |
| `podcast:soundbite` | Fragment destacat de 30-90 seg | frontmatter del `.md` |

### Workflow: Generar capítols (Copilot-assisted)

Demanant a Copilot:
```
Llegeix el fitxer sources/XXX-nom-transcripcio.srt i crea el fitxer
sources/XXX-nom-chapters.json amb els capítols principals de l'episodi
en format Podcast 2.0 (version 1.2.0). Primer capítol: Introducció (startTime: 0).
Darrer capítol: Reflexió final. Capítols del mig: els temes principals.
Afegeix el camp chapters_file: "XXX-nom-chapters.json" al frontmatter de _episodes/XXX-nom.md
```

### Workflow: Seleccionar soundbite (Copilot-assisted)

Demanant a Copilot:
```
Llegeix sources/XXX-nom-transcripcio.srt i selecciona un fragment impactant
de 30-90 segons que representi bé l'episodi. Afegeix al frontmatter de
_episodes/XXX-nom.md els camps soundbite_start, soundbite_duration i soundbite_title.
```

### Workflow: Generar thumbnail (ollama)

```bash
# Primer cop: descarregar el model (uns minuts)
ollama pull x/z-image-turbo

# Generar thumbnail per un episodi
python scripts/generate_thumbnail.py \
  --episodi 001 \
  --nom 001-nom-episodi \
  --prompt-suffix "element visual específic en anglès"

# Generar thumbnails per a tots els episodis
python scripts/generate_all_thumbnails.py

# Regenerar un episodi concret
python scripts/generate_all_thumbnails.py 001 --force
```

**Prompt base del thumbnail:** TARDIS (cabina de policia blava de Doctor Who) amb uns grans headphones futuristes, vòrtex temporal de fons. Cada episodi afegeix un element visual específic del seu tema.

### Validació

- **RSS**: Validar a https://podcastindex.org/add o https://podcastvalidator.castos.com/
- **SRT**: Obrir a VLC amb el MP3 corresponent i verificar sincronització
- **Capítols**: Testar en app Podcast 2.0 compatible (PodcastAddict, Fountain)
- **Jekyll**: `bundle exec jekyll build` no ha de generar errors

---

## Paleta de Colors (Doctor Who theme)
- **TARDIS Blue**: `#003B6F`
- **Vortex Purple**: `#7B2FFE`
- **Gallifreyan Gold**: `#D4AF37`
- **Ice Blue**: `#E8F4FD`
- **Blanc Pur**: `#FFFFFF`
- **Deep Space** (dark mode): `#0D1B2A`
- **Time Rotor Cyan** (dark mode): `#00E5FF`

## URLs Importants

- **Web del podcast**: https://david-rodenas.com/podcast-del-doctor
- **RSS feed**: https://david-rodenas.com/podcast-del-doctor/feed.xml
- **Repositori**: https://github.com/drpicox/podcast-del-doctor

## Solució de Problemes

### **Error en transcripció**
```bash
# Verificar Whisper
python -c "import whisper; print('Whisper OK')"

# Reinstal·lar si cal
pip install --upgrade openai-whisper
```

### **Error en RSS feed**
- Comprovar caràcters especials en títols/descripcions
- Verificar que tots els camps XML estan ben escapats

### **Error en GitHub Pages**
- Revisar que el YAML dels episodis és vàlid
- Comprovar que no hi ha caràcters especials en noms de fitxers

## Tasques Recurrents

### **Cada episodi:**
0. **DEMANAR fonts** ⚠️ OBLIGATORI
1. Transcriure automàticament (genera `.txt` + **`.srt`** automàticament)
2. **Generar capítols JSON** (Copilot llegeix el SRT → proposa → `sources/XXX-chapters.json`)
3. **Seleccionar soundbite** (Copilot llegeix el SRT → `soundbite_*` al frontmatter)
4. **Generar thumbnail** (`python scripts/generate_thumbnail.py ...`)
5. **Pujar a archive.org** automàticament
6. Obtenir durada amb ffprobe
7. Personalitzar contingut i verificar fonts
8. Afegir referències creuades a episodis anteriors
9. **Verificar-ho tot** (`python scripts/check_episode.py XXX` — 0 errors abans de continuar)
10. Deploy (commit + push — inclou `.srt`, `.json`, thumbnail)
11. **Verificar la publicació** (`python scripts/check_episode.py XXX --remot` un cop desplegat)

### **Setmanalment:**
- Revisar que RSS funciona
- `python scripts/check_episode.py --tots` per detectar regressions
- Comprovar mètriques web (si n'hi ha)
- Mantenir repositori actualitzat

### **Mensualment:**
- Actualitzar dependències Python
- Revisar documentació
