---
audio_file: "https://archive.org/download/podcast-del-doctor-006-raonament-autonom-claude-mythos/006-raonament-autonom-claude-mythos.mp3"
audio_size: 6705037
chapters_file: "006-raonament-autonom-claude-mythos-chapters.json"
date: '2026-04-11'
description: "Una filtració massiva des de l'interior d'Anthropic ha exposat Claude Mythos, un model de llenguatge especulatiu de 10 bilions de paràmetres que combina Mixture of Experts ultradispers amb recurrència latent. Un sistema que rumia en silenci en el seu espai vectorial intern, aconsegueix un 97.6% al benchmark USAMO de matemàtiques i és capaç de trobar zero-days de 27 anys amagats en codi revisat 5 milions de vegades."
duration: '13:58'
episode_number: 6
season: 1
soundbite_start: 353.1
soundbite_duration: 66.0
soundbite_title: "D'autocompletar a pensador continu: USAMO 97.6% i ciberseguretat autònoma"
sources:
- title: "NotebookLM: El raonament autònom de Claude Mythos"
  url: "https://notebooklm.google.com/notebook/535089a4-af65-4cf0-87f2-82f8dbafc18a"
  description: "Notebook de Google NotebookLM amb les fonts i la generació del contingut d'aquest episodi"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/006-raonament-autonom-claude-mythos-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
# TODO: Generar thumbnail quan ollama MLX funcioni (libmlxc.dylib no trobat post-update sistema)
# python scripts/generate_thumbnail.py --episodi 006 --nom 006-raonament-autonom-claude-mythos --prompt-suffix "a glowing TARDIS with a cracked door leaking light, classified documents floating around, neural network nodes forming a brain in the vortex background"
title: "Episodi 006: El raonament autònom de Claude Mythos"
---

## Introducció

Feia temps que la indústria debatia quan arribaríem a tenir màquines veritablement autònomes. Sembla que la resposta podria ser: ja. Un error de configuració als servidors d'Anthropic ha exposat documents confidencials sobre **Claude Mythos** (nom intern: Claude Ibara), un model que trenca les regles del joc no perquè sigui més gran, sinó perquè ha après a **rumiar en secret** abans de dir ni una paraula.

## Temes tractats

- **La filtració i el context**: Un error de configuració als servidors d'Anthropic va exposar esborranys interns, informes del red team i documentació tècnica sobre un model fins ara desconegut. Combinat amb articles científics sobre raonament latent i debats tècnics de la comunitat, la imatge que emergeix és d'un salt generacional en IA.

- **Escala i Mixture of Experts (MoE) ultradispers**: Claude Mythos assoleix els 10 bilions de paràmetres amb una inversió estimada d'entre 5.000 i 15.000 milions de dòlars. Per fer-ho viable, utilitza una arquitectura MoE on només s'activen entre el 2 i el 5% dels pesos per token (120-256 experts actius simultàniament). Com un hospital gegantí on, davant un os trencat, només entren els tres traumatòlegs exactes que calen — la resta ni s'assabenta del pacient.

- **Recurrència latent: pensar sense paraules**: L'eficiència alliberada pel MoE no s'estalvia: s'inverteix en **recurrència latent**. En lloc de generar text pas a pas (chain-of-thought clàssic), el model rumia en el seu espai vectorial intern, donant milers de voltes al problema amb pesos compartits entre iteracions — sense distorsionar-se com les velles xarxes recurrents. Només quan té la resposta obre la porta i escriu. (Relació directa amb l'arquitectura d'[Ouro / LoopLM de l'episodi 005](/podcast-del-doctor/_episodes/005-ouro-ia-pensa-en-bucle).)

- **Resultats que deixen l'equip blanc**: La prova USAMO de matemàtiques olímpiques, on el model anterior Claude Opus treia un 42.3%, Mythos arriba al **97.6%**. El benchmark SWE-bench Verified de programació supera el **93%**. Xifres que el mateix equip d'Anthropic no esperava.

- **Ciberseguretat autònoma i zero-days de dècades**: Claude Mythos ha trobat de forma autònoma un error d'execució remota a OpenBSD que portava **27 anys** amagat, i una corrupció de memòria a FFmpeg de **16 anys** — tots dos en codi revisat 5 milions de vegades per escàners automatitzats sense resultat.

- **Sintaxi vs lògica: la diferència que ho explica tot**: Els escàners clàssics llegeixen sintaxi (faltes d'ortografia informàtiques). Mythos simula mentalment l'execució sencera i veu les interaccions entre parts allunyades del codi — errors de lògica invisibles per a qualsevol anàlisi lineal. Com un guarda que, en lloc d'empènyer la maneta, estudia el metall del pany, fabrica una clau mestre i repara el pany des de dins.

## Fonts

- [NotebookLM: El raonament autònom de Claude Mythos](https://notebooklm.google.com/notebook/535089a4-af65-4cf0-87f2-82f8dbafc18a) — Notebook de Google NotebookLM amb les fonts originals del contingut
- [Transcripció automàtica](/podcast-del-doctor/sources/006-raonament-autonom-claude-mythos-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). El contingut sobre "Claude Mythos" és especulatiu i creatiu, basat en la documentació recopilada al notebook de NotebookLM. Consulta sempre les fonts originals per obtenir la informació completa.
