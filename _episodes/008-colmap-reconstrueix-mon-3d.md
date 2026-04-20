---
audio_file: "https://archive.org/download/podcast-del-doctor-008-colmap-reconstrueix-mon-3d/008-colmap-reconstrueix-mon-3d.mp3"
audio_size: 7707931
chapters_file: "008-colmap-reconstrueix-mon-3d-chapters.json"
date: '2026-04-19'
description: "Com pot un ordinador reconstruir un espai tridimensional a partir de simples fotografies planes? Analitzem a fons COLMAP, el programari de codi obert creat per Johannes Schönberger que s'ha convertit en l'estàndard de la indústria per a la reconstrucció 3D a partir d'imatges. Des de l'algorisme SIFT fins al bundle adjustment, passant pel drama CPU vs GPU i l'alternativa moderna GLOMAP."
duration: '16:03'
episode_number: 8
season: 1
soundbite_start: 645.6
soundbite_duration: 69.1
soundbite_title: "2.000€ en GPU i no fa res: el drama CPU vs GPU de la reconstrucció 3D"
sources:
- title: "NotebookLM: Com COLMAP reconstrueix el món en 3D"
  url: "https://notebooklm.google.com/notebook/890be841-3cb2-4bb4-87c9-15e6c9d4d7c6"
  description: "Notebook de Google NotebookLM amb les fonts i la generació del contingut d'aquest episodi"
- title: "COLMAP Explained - Everypoint (YouTube)"
  url: "https://www.youtube.com/watch?v=EdIuDLicU0c"
  description: "Vídeo detallat del canal Everypoint que explica pas a pas el funcionament intern de COLMAP"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/008-colmap-reconstrueix-mon-3d-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/008-colmap-reconstrueix-mon-3d.png"
title: "Episodi 008: Com COLMAP reconstrueix el món en 3D"
---

## Introducció

El nostre cervell biològic entén l'espai tridimensional en mil·lisegons, gastant tot just uns pocs watts d'energia. Però per a un ordinador, un grapat de fotografies no és més que una llista plana de milions de píxels en 2D — un buit absolut d'informació espacial. En aquest episodi analitzem a fons **COLMAP** (Collection Mapper), el programari de codi obert creat per Johannes Schönberger a la Universitat UNC Chapel Hill que s'ha convertit en l'estàndard de la indústria per reconstruir el món en 3D a partir de simples fotografies. Ens basem en un vídeo extremadament detallat del canal de YouTube **Everypoint**.

## Temes tractats

- **COLMAP i el seu origen**: Creat per Johannes Schönberger, que durant el seu doctorat va arribar a processar 100 milions d'imatges en un sol PC. És un mapejador de col·leccions d'imatges de codi obert i un estàndard total a la indústria de la reconstrucció 3D.

- **Extracció de característiques amb SIFT**: El primer pas és trobar punts de referència a cada foto amb l'algorisme SIFT (Scale-Invariant Feature Transform). Crea una "empremta dactilar numèrica" — un vector matemàtic — per a milers de punts de cada imatge, invariant a l'escala gràcies a una piràmide gaussiana de desenfocament.

- **Emparellament (matching) d'imatges**: Amb milers de fotos i milers d'empremtes per foto, comparar-ho tot és computacionalment devastador. COLMAP ofereix estratègies: seqüencial (fotos en ordre), arbre de vocabulari (resum visual ràpid per descartar fotos sense relació) i mètodes espacials basats en GPS/EXIF.

- **Verificació geomètrica i falsos positius**: Patrons repetits com maons o finestres generen correspondències falses. COLMAP aplica la restricció epipolar per descartar punts que no tenen sentit físicament. La correcta definició del model de càmera (longitud focal, distorsió K1/K2, dades EXIF) és crítica.

- **El salt al 3D i la reconstrucció incremental**: En lloc de començar per la foto 1 i sumar la 2 (error fatal), COLMAP busca la parella perfecta amb màxima paral·laxi — potser la foto 12 i la 85 — per inicialitzar l'univers tridimensional i anar afegint càmeres una per una.

- **Bundle Adjustment (ajust de feixos)**: Optimització no lineal que equilibra els errors acumulats. Com teixir una taranyaina: cada fil nou pot deformar la xarxa, i l'ajust de feixos reequilibra totes les tensions a la vegada, revisant càmeres, punts i distorsió de lents.

- **El drama CPU vs GPU**: Algú gasta 2.000€ en una GPU d'última generació, però durant la reconstrucció incremental la GPU està morta de riure mentre la CPU pateix 5 hores al 100%. La reconstrucció és seqüencial per definició — no es pot calcular la càmera 80 sense haver resolt la 79.

- **GLOMAP: la solució global moderna**: Del mateix Schönberger, canvia la filosofia: en lloc d'anar foto per foto, mira tot el món de cop amb mitjanes de rotacions. Permet paral·lelitzar amb GPU i reduir el temps a una desena part, però requereix molta connexió entre fotos — si no, genera blocs de punts inútils (els "Cupsborg").

- **L'impacte: del 3D Gaussian Splatting al cinema**: Tota la revolució visual actual — 3D Gaussian Splatting, realitat augmentada, bessons digitals — depèn d'aquesta estimació mil·limètrica de les càmeres. Sense COLMAP, entren escombràries i surten escombràries.

- **Consell pràctic**: No utilitzar datasets acadèmics perfectes per aprendre. Cal sortir al món real, fer fotos a una font d'aigua esquivant gent i reflexos, i veure on es trenca tot.

## Fonts

- [NotebookLM: Com COLMAP reconstrueix el món en 3D](https://notebooklm.google.com/notebook/890be841-3cb2-4bb4-87c9-15e6c9d4d7c6) — Notebook de Google NotebookLM amb les fonts originals del contingut
- [COLMAP Explained - Everypoint (YouTube)](https://www.youtube.com/watch?v=EdIuDLicU0c) — Vídeo detallat del canal Everypoint que serveix de base per a l'episodi
- Transcripció automàtica (`/podcast-del-doctor/sources/008-colmap-reconstrueix-mon-3d-transcripcio.txt`) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper. Consulta sempre les fonts originals per obtenir la informació completa.
