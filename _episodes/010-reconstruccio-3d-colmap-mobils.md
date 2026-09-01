---
audio_file: "https://archive.org/download/podcast-del-doctor-010-reconstruccio-3d-colmap-mobils/010-reconstruccio-3d-colmap-mobils.mp3"
audio_size: 9272561
chapters_file: "010-reconstruccio-3d-colmap-mobils-chapters.json"
date: '2026-04-20'
description: "Com pot un simple telèfon mòbil capturar espais exteriors gegantins en 3D sense drons ni GPS? En aquest tercer episodi de la sèrie sobre COLMAP — en català — repassem tot el pipeline de reconstrucció 3D des de la perspectiva pràctica: extracció SIFT amb descriptors de 128 dimensions, distorsió radial de lents (K1/K2), estratègies d'emparellament (exhaustiva, seqüencial, arbre de vocabulari), triangulació i paral·laxi, bundle adjustment, el drama CPU vs GPU, GLOMAP amb loop closures, i una reflexió final sobre privacitat i reconstrucció 3D de fotos turístiques."
duration: '19:18'
episode_number: 10
season: 1
soundbite_start: 832.3
soundbite_duration: 60.0
soundbite_title: "3.000€ en GPU i el detectiu solitari de la CPU fa tota la feina"
sources:
- title: "NotebookLM: Com COLMAP reconstrueix el món en 3D"
  url: "https://notebooklm.google.com/notebook/890be841-3cb2-4bb4-87c9-15e6c9d4d7c6"
  description: "Notebook de Google NotebookLM amb les fonts i la generació del contingut d'aquest episodi"
- title: "COLMAP Explained - Everypoint (YouTube)"
  url: "https://www.youtube.com/watch?v=EdIuDLicU0c"
  description: "Vídeo detallat del canal Everypoint que explica pas a pas el funcionament intern de COLMAP"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/010-reconstruccio-3d-colmap-mobils-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/010-reconstruccio-3d-colmap-mobils.png"
title: "Episodi 010: Reconstrucció 3D amb COLMAP i mòbils"
---

## Introducció

Tercer i últim episodi de la sèrie sobre reconstrucció 3D amb COLMAP. Després d'introduir els fonaments a l'[Episodi 008: Com COLMAP reconstrueix el món en 3D](/podcast-del-doctor/episodi/008-colmap-reconstrueix-mon-3d) i aprofundir en la captura terrestre en anglès a l'[Episodi 009: Construir mons 3D sense drons](/podcast-del-doctor/episodi/009-construir-mons-3d-sense-drons), ara repassem tot el pipeline complet — **en català** — amb un enfocament pràctic i accessible: des de com l'algorisme SIFT crea empremtes dactilars de 128 dimensions per a cada punt d'interès fins a la reflexió inquietant sobre què implica per a la privacitat que qualsevol persona amb un mòbil pugui generar models 3D d'espais públics.

## Temes tractats

- **La ceguesa dimensional de l'ordinador**: Un ordinador no veu espai — veu una graella plana de píxels. La missió: transformar fotos 2D en geometria 3D navegable, sense drons ni topografia professional, només caminant amb un telèfon mòbil.

- **De MAVMap a COLMAP**: Johannes Schönberger va crear primer MAVMap (per drons) i va reconèixer les limitacions de la captura aèria estructurada. COLMAP (Collection Mapper) va néixer per processar col·leccions d'imatges completament desordenades — fins a 100 milions d'imatges en un sol PC.

- **Extracció de característiques amb SIFT**: L'algorisme busca gradients de contrast brusc a la graella de píxels. Per cada punt clau crea un descriptor — un vector de 128 dimensions que codifica la distribució de llum al voltant — una "empremta dactilar numèrica" única i invariant a l'escala.

- **Distorsió radial i model de càmera**: Les lents de mòbils i GoPros deformen l'espai brutalment. Sense els paràmetres K1/K2 de distorsió radial, el programari calcularia columnes físicament corbades com si fossin bananes. COLMAP incorpora la correcció directament a les equacions matemàtiques.

- **Estratègies d'emparellament**: Tres opcions amb compensacions molt diferents:
  - **Exhaustiva**: compara tot amb tot (N², inviable amb milers de fotos — setmanes de càlcul)
  - **Seqüencial**: compara fotos adjacents cronològicament (ultraràpida, però vulnerable a interrupcions)
  - **Arbre de vocabulari (vocab tree)**: crea un índex de "paraules visuals" — com un motor de cerca intern que filtra les 10.000 fotos i només emparella les 50 rellevants

- **Triangulació i reconstrucció incremental**: No començar mai per la foto 1 i la 2 (línia base massa petita, sense paral·laxi). El programa busca dues fotos amb milers de punts en comú però amb una distància física gran — potser la foto 12 i la 90 — i va afegint càmeres una per una.

- **Bundle adjustment (ajust de feixos)**: Optimització que combat la deriva acumulada. Com un muntador que no només aprèta els cargols de la cadira, sinó que simultàniament reavalua les rajoles del terra i el vidre del mòbil — modifica coordenades de milions de punts, rotació de càmeres i distorsió de lent alhora.

- **El drama CPU vs GPU**: La GPU (exèrcit de policies buscant pistes en paral·lel) és genial per a l'extracció de features. Però l'ajust incremental és seqüencial — la feina d'un sol detectiu solitari que no pot resoldre el cas 80 sense haver tancat el 79. Per això una GPU de 3.000€ resta inactiva mentre la CPU pateix durant hores.

- **GLOMAP: reconstrucció global**: Abandona la seqüència — calcula totes les rotacions de càmera simultàniament amb promig de rotació. Però exigeix **loop closures** (tancar el cercle tornant al punt d'inici). Sense ells, el model col·lapsa en blocs inútils.

- **Conclusió pràctica**: No aprendre amb datasets estèrils. Surt al carrer, grava una font real, i descobreix com el sol, els reflexos i la gent destrocen la geometria. L'error és el millor mestre.

- **Reflexió sobre privacitat**: Si qualsevol persona amb un mòbil pot generar models 3D d'espais públics, milers de fotos turístiques poden processar-se per congelar vianants en tres dimensions sense el seu permís — una implicació inquietant d'una tecnologia fascinant.

## Fonts

- [NotebookLM: Com COLMAP reconstrueix el món en 3D](https://notebooklm.google.com/notebook/890be841-3cb2-4bb4-87c9-15e6c9d4d7c6) — Notebook de Google NotebookLM amb les fonts originals del contingut
- [COLMAP Explained - Everypoint (YouTube)](https://www.youtube.com/watch?v=EdIuDLicU0c) — Vídeo detallat del canal Everypoint que serveix de base per a l'episodi
- [Transcripció automàtica](/podcast-del-doctor/sources/010-reconstruccio-3d-colmap-mobils-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
