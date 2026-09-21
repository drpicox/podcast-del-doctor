# Script de Pujada Automàtica a Archive.org

Aquest script automatitza completament el procés de pujar episodis del podcast a archive.org.

## Configuració Inicial (només primera vegada)

```bash
# 1. Instal·lar dependències
pip install -r requirements.txt

# 2. Configurar credencials d'archive.org
ia configure
```

T'ha demanarà:
- **Email**: El teu email d'archive.org
- **Password**: La teva contrasenya

Les credencials es guarden a `~/.config/ia.ini` i no cal tornar-les a introduir.

## Ús

### Mode DRY-RUN (recomanat primer cop)

```bash
python scripts/upload_to_archive.py --dry-run
```

Mostra què faria **sense pujar res realment**. Útil per verificar que tot és correcte.

### Pujar tots els episodis

```bash
python scripts/upload_to_archive.py
```

Això:
- Puja els 9 episodis a archive.org
- Crea els ítems amb totes les metadades correctes
- Genera les URLs públiques
- Actualitza automàticament el camp `audio_file` de cada markdown

### Pujar només un episodi específic

```bash
python scripts/upload_to_archive.py --episodi 009
```

### Pujar sense actualitzar els markdowns

```bash
python scripts/upload_to_archive.py --no-update-md
```

## Què fa l'script automàticament?

Per cada episodi:

1. ✅ **Comprova** si el fitxer MP3 existeix
2. ✅ **Crea les metadades** amb format correcte:
   - Title: `Podcast del Doctor - Episodi XXX: Títol`
   - Creator: `David Rodenas`
   - Description amb disclaimer d'IA
   - Tags apropiats
   - Llicència CC BY 4.0
   - Data, durada, idioma...
3. ✅ **Comprova** si l'ítem ja existeix a archive.org
4. ✅ **Puja** el fitxer amb `queue_derive=True` (processament automàtic)
5. ✅ **Genera la URL** pública: `https://archive.org/download/[identifier]/[fitxer].mp3`
6. ✅ **Actualitza** el markdown corresponent amb la nova URL
7. ✅ **Mostra resum** amb totes les URLs generades

## Exemple de sortida

```
🎙️  Script de pujada automàtica a archive.org
============================================================

📋 Episodis a processar: 9

📦 Pujant episodi 001: Què es va dir realment sobre els Títol Exemple?
   Fitxer: /path/to/episodes/001-exemple-episodi.mp3
   Identifier: podcast-del-doctor-001-exemple-episodi
   ✅ Pujat correctament!
   📍 URL: https://archive.org/download/podcast-del-doctor-001-exemple-episodi/001-exemple-episodi.mp3
   🌐 Pàgina: https://archive.org/details/podcast-del-doctor-001-exemple-episodi
   ✏️  Actualitzat markdown

...

============================================================
📊 RESUM
============================================================
✅ Episodis processats: 9/9

📍 URLs generades:
   001: https://archive.org/download/podcast-del-doctor-001-exemple-episodi/001-exemple-episodi.mp3
   002: https://archive.org/download/podcast-del-doctor-002-exemple-episodi/002-exemple-episodi.mp3
   ...

💡 Recorda fer:
   git add _episodes/
   git commit -m 'Migrar URLs a archive.org'
   git push
```

## Després de pujar

```bash
# Verificar els canvis
git status

# Veure les diferències
git diff _episodes/

# Commit i push
git add _episodes/
git commit -m "Migrar episodis a archive.org"
git push
```

## Gestió d'errors

### Si un ítem ja existeix

L'script preguntarà:
```
⚠️  L'ítem ja existeix a archive.org
Vols sobreescriure'l? (s/N):
```

- `s` → Sobreescriu
- `N` → Salta aquest episodi

### Si falta un fitxer MP3

```
❌ ERROR: No s'ha trobat el fitxer /path/to/episodes/XXX.mp3
```

Verifica que el fitxer existeix a `episodes/`.

### Si falla la pujada

L'script reintentarà fins a 3 vegades automàticament. Si continua fallant, mostra l'error i continua amb el següent episodi.

### Si l'script es queda esperant archive.org

És normal que esperi una estona: després de pujar, archive.org ha de processar
els fitxers i fer el *derive*. L'script sondeja amb **esperes creixents**
(15 s, 30 s, 1 min, 2 min, 4 min), mai a interval fix curt, per no semblar un
atac a archive.org. Amb la sortida línia a línia es veu cada espera:

```
🔎 verificant la caràtula…
   ⏳ esperant 15s abans de comprovar…
   ⏳ esperant 30s abans de comprovar…
✅ Caràtula confirmada!
```

Si passa dels 8 minuts sense confirmar, entra al camí lent: espera que l'ítem
no tingui tasques pendents, torna a pujar la caràtula i torna a sondejar.
Per comprovar-ho a mà mentre espera:

```bash
curl -s https://archive.org/metadata/<identifier> | python3 -c "
import sys, json
d = json.load(sys.stdin)
print([(f['name'], f.get('source'), f.get('size')) for f in d['files'] if f['name'].endswith(('.mp3', '.png'))])
print('pending_tasks:', d.get('pending_tasks'))"
```

Si l'MP3 i el PNG hi surten com a `source: original` i la mida del PNG és la
del fitxer local (`stat -f%z assets/thumbnails/XXX-nom.png`), la pujada és bona:
es pot aturar l'script i posar `audio_file` a mà al markdown.

#### Apunts de l'incident del 2026-09-20 (episodis 028 i 029)

- **Símptoma:** pujar el 028, un MP3 de 0,7 MB, va trigar 18 minuts. El 029
  portava 11 minuts esperant quan es va aturar a mà. De 41 minuts de procés,
  29 eren aquesta espera.
- **Causa:** l'script pujava MP3 i PNG junts, feia `sleep(30)` i comprovava la
  caràtula **un sol cop**. Als 30 s l'API de metadades encara no llistava els
  fitxers, i aquell fals negatiu es prenia per «caràtula perduda».
- **Conseqüència:** entrava a `pujar_cover`, que espera que acabi el *derive*
  per no perdre la pujada. Aquell vespre el *derive* va trigar uns 14 minuts.
  Després re-pujava una caràtula que ja hi era i disparava un segon *derive*.
- **Prova:** el registre de tasques d'archive.org (`ia tasks <identifier>`)
  mostra el PNG pujat a les 21:51:53 amb la primera pujada, i una segona
  pujada redundant a les 22:08:05.
- **Fix:** `esperar_cover()` sondeja `cover_arribada()` amb
  `esperes_creixents()`; `esperar_sense_tasques()` fa servir el mateix patró.
  En el pitjor cas, el camí ràpid fa cinc peticions en 7:45.
- **Primera prova real (episodi 030, 2026-09-21):** el fix funciona. Una sola
  pujada de caràtula, cap re-pujada i cap segon *derive*, tot i que el *derive*
  d'archive.org seguia en marxa dues hores després. Els fitxers van sortir a
  l'API uns 2 minuts després de pujar: les comprovacions dels 15 s, 45 s i 1:45
  van fallar, i la dels 3:45 és la que ho hauria confirmat. El temps total no
  es va poder mesurar perquè el Mac es va adormir a mitja espera (de les 13:14
  a les 14:50); en despertar-se va confirmar a la comprovació següent.
  Durada esperable d'una pujada: **uns 4 minuts**.
- **De passada:** `requirements.txt` demanava `lightning-whisper-mlx>=0.1.0`
  (no existeix; la darrera és la 0.0.10) i el `.venv` apuntava a una ruta
  antiga. El `.venv` s'ha de crear amb **Python 3.11**: amb 3.12 falla la
  compilació del `tiktoken` antic que fixa `lightning-whisper-mlx`.

## Opcions avançades

```bash
# Ajuda
python scripts/upload_to_archive.py --help

# Mode verbós (ja està actiu per defecte)
python scripts/upload_to_archive.py --verbose
```

## Estructura de les metadades

Cada episodi es puja amb:

- **Identifier**: `podcast-del-doctor-XXX-nom-episodi` (únic)
- **Title**: Títol complet amb "Podcast del Doctor"
- **MediaType**: `audio`
- **Collection**: `community_audio`
- **Creator**: `David Rodenas`
- **Description**: Descripció + disclaimer IA + enllaços
- **Date**: Data de publicació original
- **Language**: `cat` (Català)
- **License**: CC BY 4.0
- **Subject**: Tags separats per `;`
- **Duration**: Durada de l'episodi
- **External-ID**: URN únic del podcast

## Recursos

- [Documentació Archive.org API](https://archive.org/services/docs/api/)
- [internetarchive CLI](https://github.com/jjjake/internetarchive)
- [ARCHIVE_ORG.md](../ARCHIVE_ORG.md) - Guia completa d'archive.org
- [ARCHIVE_ORG_METADADES_EPISODIS.md](../ARCHIVE_ORG_METADADES_EPISODIS.md) - Metadades de cada episodi
