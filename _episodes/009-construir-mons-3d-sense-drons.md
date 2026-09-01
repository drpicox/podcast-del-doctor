---
audio_file: "https://archive.org/download/podcast-del-doctor-009-construir-mons-3d-sense-drons/009-construir-mons-3d-sense-drons.mp3"
audio_size: 21886569
chapters_file: "009-construir-mons-3d-sense-drons-chapters.json"
date: '2026-04-20'
description: "Podem construir mons tridimensionals a partir de simples fotos fetes amb el mòbil, sense drons ni GPS? En aquest episodi — en anglès — aprofundim en el pipeline complet de COLMAP des de la perspectiva de la captura a peu: extracció SIFT, mascarament de soroll dinàmic, model de càmera amb distorsió radial, estratègies de matching (seqüencial, vocab tree, espacial), verificació geomètrica, reconstrucció incremental, bundle adjustment, el drama CPU vs GPU, i la revolució de GLOMAP amb les seves espectaculars fallades en forma de 'Borg cubes'."
duration: '45:35'
episode_number: 9
season: 1
soundbite_start: 2452
soundbite_duration: 50
soundbite_title: "Borg cubes: quan GLOMAP col·lapsa en un cub de càmeres"
sources:
- title: "NotebookLM: Com COLMAP reconstrueix el món en 3D"
  url: "https://notebooklm.google.com/notebook/890be841-3cb2-4bb4-87c9-15e6c9d4d7c6"
  description: "Notebook de Google NotebookLM amb les fonts i la generació del contingut d'aquest episodi"
- title: "COLMAP Explained - Everypoint (YouTube)"
  url: "https://www.youtube.com/watch?v=EdIuDLicU0c"
  description: "Vídeo detallat del canal Everypoint que explica pas a pas el funcionament intern de COLMAP"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/009-construir-mons-3d-sense-drons-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/009-construir-mons-3d-sense-drons.png"
title: "Episodi 009: Construir mons 3D sense drons"
---

## Introducció

Per al nostre cervell biològic, entendre la profunditat d'una fotografia és trivial. Per a un ordinador, una imatge no és més que una graella plana de píxels de colors — completament cec a les tres dimensions. En aquest episodi — **en anglès** — aprofundim en com curar aquesta "ceguesa dimensional" utilitzant **COLMAP** des de la perspectiva més difícil: la captura a peu, sense drons, sense GPS d'alta precisió, sense cap dels "codis trampa" dels vehicles aeris. Continuem l'exploració de COLMAP iniciada a l'[Episodi 008: Com COLMAP reconstrueix el món en 3D](/podcast-del-doctor/episodi/008-colmap-reconstrueix-mon-3d), però ara amb molt més detall tècnic i centrant-nos exclusivament en els reptes de la captura terrestre.

## Temes tractats

- **La ceguesa dimensional**: Un ordinador no veu paisatges ni profunditat — només veu píxels. La missió: transformar fotos planes en geometria 3D navegable, sense cap ajuda de drons.

- **COLMAP: de MAVMap a Collection Mapper**: Johannes Schönberger va crear primer MAVMap (per drons amb GPS mil·limètric) i després va reconèixer les limitacions d'aquest enfocament. Va crear COLMAP per processar col·leccions d'imatges totalment desordenades — fins a 100 milions d'imatges en un sol PC durant el seu doctorat.

- **Extracció de característiques amb SIFT**: L'algorisme Scale-Invariant Feature Transform busca anomalies de gran contrast (blobs) a múltiples escales mitjançant piràmides de Diferència de Gaussianes. Cada punt d'interès rep un descriptor numèric únic — una empremta dactilar visual invariant a l'escala.

- **El caos de la captura a terra**: Sense la perspectiva ordenada d'un dron, tot és caòtic: persones que creuen, cotxes que passen, gossos que corren. SIFT no té sentit comú i tractaria la jaqueta d'un vianant com a punt de referència estructural. La solució: **masques** que bloquegen píxels dinàmics.

- **Model de càmera i distorsió radial**: Els paràmetres K1 i K2 de distorsió radial són crítics per a lents gran angular. Sense correcció, el programari calcularia columnes físicament corbades com si fossin realment bananes. El model de càmera desfa matemàticament la curvatura de la lent.

- **Estratègies de matching**: Quatre opcions amb compensacions molt diferents:
  - **Exhaustiu**: compara tot amb tot (N², inviable amb >100 fotos)
  - **Seqüencial**: compara fotos adjacents (ràpid, però vulnerable a interrupcions — l'exemple del gos)
  - **Vocab tree**: crea un índex de "paraules visuals" per trobar candidats ràpidament (elegant per a col·leccions desordenades)
  - **Espacial**: basat en GPS (domini dels drons, inútil a terra per culpa dels rebots de senyal)

- **Verificació geomètrica**: Els falsos positius (maons idèntics, finestres repetitives) forçarien el model a plegar-se com un taco. La verificació amb homografies i matrius essencials descarta qualsevol punt que violi les lleis de la física.

- **Reconstrucció incremental i inicialització**: NO començar amb les dues primeres fotos consecutives — la línia de base és massa petita i la paral·laxi inexistent. Cal un canvi dràstic de perspectiva (l'estratègia dels investigadors d'Oregon: un cercle a alçada de cap + un cercle a alçada de pit). Després, càmera per càmera, punt per punt.

- **Bundle adjustment**: Optimització que combat la deriva acumulada. L'ajust local corregeix el veïnatge immediat. L'ajust global para tot el procés i reequilibra tota la geometria a la vegada — fins i tot refinant els paràmetres de distorsió de la lent basant-se en l'evidència 3D.

- **El drama CPU vs GPU**: Algú compra una GPU de 2.000€ i la GPU està al 4% d'utilització mentre la CPU pateix al 100% durant 5 hores. L'extracció de features és paralel·litzable (milió de policies novells), però la reconstrucció incremental és seqüencial per definició (un sol detectiu mestre que resol pas a pas).

- **GLOMAP: reconstrucció global**: Abandona la reconstrucció seqüencial. Calcula totes les rotacions de càmera simultàniament (rotation averaging), després llisca totes les càmeres fins que convergeixen. Instantani amb loop closures, però catastròfic amb captures lineals — genera els espectaculars "Borg cubes": cubs densos de càmeres col·lapsades en l'espai buit.

- **Reflexió final**: Què passaria si alimentéssim COLMAP amb milions de fotos turístiques històriques dels anys 80? Podríem reconstruir en 3D monuments destruïts o places desaparegudes, curant la ceguesa dimensional de la història.

## Fonts

- [NotebookLM: Com COLMAP reconstrueix el món en 3D](https://notebooklm.google.com/notebook/890be841-3cb2-4bb4-87c9-15e6c9d4d7c6) — Notebook de Google NotebookLM amb les fonts originals del contingut
- [COLMAP Explained - Everypoint (YouTube)](https://www.youtube.com/watch?v=EdIuDLicU0c) — Vídeo detallat del canal Everypoint que serveix de base per a l'episodi
- [Transcripció automàtica](/podcast-del-doctor/sources/009-construir-mons-3d-sense-drons-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques i està en **anglès**. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
