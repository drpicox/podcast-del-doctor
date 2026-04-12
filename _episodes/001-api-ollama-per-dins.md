---
audio_file: "https://archive.org/download/podcast-del-doctor-001-api-ollama-per-dins/001-api-ollama-per-dins.mp3"
audio_size: 9634095
chapters_file: "001-api-ollama-per-dins-chapters.json"
date: '2026-03-31'
description: "Anàlisi a fons de l'API d'Ollama: com gestiona recursos GPU/CPU, els endpoints Generate i Chat, paràmetres de control (temperatura, top_k, top_p), streaming NDJSON, Tool Calling, sortides estructurades i l'emulació d'OpenAI. Tot executant-se localment al teu ordinador."
duration: '20:04'
episode_number: 1
season: 1
soundbite_start: 960.2
soundbite_duration: 82.4
soundbite_title: "El cavall de Troia d'Ollama: emulant OpenAI des del teu escriptori"
sources:
- title: "Contingut generat amb Google NotebookLM"
  url: "https://notebooklm.google.com/notebook/47279983-616d-4704-b3b3-15223b2f726b"
  description: "Notebook amb les fonts utilitzades per generar l'episodi"
- title: "Documentació oficial de l'API d'Ollama"
  url: "https://github.com/ollama/ollama/blob/main/docs/api.md"
  description: "Referència completa de l'API REST d'Ollama"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/001-api-ollama-per-dins-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/001-api-ollama-per-dins.png"
title: "Episodi 001: Com funciona l'API d'Ollama per dins"
---

## Introducció

Què passa realment quan executem Ollama al nostre ordinador? En aquest episodi desgranem la mecànica interna de l'API d'Ollama: el servei que converteix el nostre hardware en una infraestructura d'IA privada i completament local. Des de com fragmenta els models entre GPU i CPU fins a com emula l'API d'OpenAI perquè codi existent funcioni sense canvis.

## Temes tractats

- **Gestió de recursos GPU/CPU**: Ollama analitza la VRAM i RAM disponibles i fragmenta automàticament les capes del model entre targeta gràfica i processador, fent de director d'orquestra durant la inferència. L'endpoint `/api/ps` permet monitoritzar el repartiment en temps real.

- **Endpoints Generate vs Chat**: `/api/generate` per a tasques d'un sol tret sense memòria (extracció de dades, autocompletar codi), i `/api/chat` amb sistema de rols (system/user/assistant) que actua com a traductor universal de plantilles entre famílies de models.

- **Paràmetres de control**: Temperatura (0 = determinista), top_k (retalla les opcions menys probables), top_p (selecció dinàmica per probabilitat acumulada) i num_ctx (finestra de context per optimitzar rendiment).

- **Streaming NDJSON**: Connexió oberta permanent que envia tokens paraula a paraula. Per als models de raonament (com DeepSeek R1), s'ha afegit el camp `thinking` separat que permet auditar la cadena de pensament interna.

- **Tool Calling**: El model pot aturar la generació de text i retornar un objecte `tool_calls` demanant executar funcions externes. Importància de prevenir bucles d'agents amb límits d'iteracions al codi.

- **Sortides estructurades (Structured Outputs)**: L'API restringeix l'espai de tokens per forçar respostes en JSON vàlid. Combinat amb eines de validació com Pydantic o Zod, garanteix robustesa en aplicacions de producció.

- **Emulació d'OpenAI**: L'endpoint `/v1` actua com un "cavall de Troia" que tradueix peticions amb format OpenAI perquè codi existent funcioni apuntant a localhost:11434. Inclou suport per embeddings i formats d'Anthropic.

- **ModelFile i extensió cognitiva**: Reflexió sobre com els arxius ModelFile permeten incrustar historials permanents dins del model, obrint la porta a sistemes d'aprenentatge acumulat totalment privats.

## Fonts

- [Contingut generat amb Google NotebookLM](https://notebooklm.google.com/notebook/47279983-616d-4704-b3b3-15223b2f726b) - Notebook amb les fonts originals
- [Documentació oficial de l'API d'Ollama](https://github.com/ollama/ollama/blob/main/docs/api.md) - Referència completa
- Transcripció automàtica (`/podcast-del-doctor/sources/001-api-ollama-per-dins-transcripcio.txt`) - Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
