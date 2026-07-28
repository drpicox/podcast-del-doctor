---
audio_file: "https://archive.org/download/podcast-del-doctor-005-ouro-ia-pensa-en-bucle/005-ouro-ia-pensa-en-bucle.mp3"
audio_size: 6260955
chapters_file: "005-ouro-ia-pensa-en-bucle-chapters.json"
date: '2026-04-11'
description: "Quin seria el proper gran salt en IA si en lloc de construir models cada vegada més grans i cars, ensenyéssim a un de petit a pensar en bucle? Explorem Ouro, un model de llenguatge en bucle (LoopLM) de només 2.6 bilions de paràmetres que supera models de 12 bilions en raonament matemàtic, fent el processament en l'espai latent i sense generar text fins a tenir la resposta definitiva."
duration: '13:02'
episode_number: 5
season: 1
soundbite_start: 702.5
soundbite_duration: 42.0
soundbite_title: "La democratització real de la IA avançada: raonament profund al teu telèfon"
thumbnail: "/assets/thumbnails/005-ouro-ia-pensa-en-bucle.png"
sources:
- title: "Scaling Latent Reasoning via Looped Language Models (arxiv:2510.25741)"
  url: "https://arxiv.org/abs/2510.25741"
  description: "Article científic original de Rui-Jie Zhu et al. (ByteDance, UC Santa Cruz, Princeton) que presenta Ouro i els Looped Language Models"
- title: "Ouro LLM - Pàgina oficial del projecte"
  url: "http://ouro-llm.github.io/"
  description: "Pàgina oficial del projecte amb models i codi obert"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/005-ouro-ia-pensa-en-bucle-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
title: "Episodi 005: Ouro, la IA que pensa en bucle"
---

## Introducció

Imagina una intel·ligència artificial que, en comptes de néixer cada vegada més gran, aprèn a rumiar en secret. Avui explorem **Ouro**, un model de llenguatge revolucionari basat en bucles recurrents que amb tan sols 2.6 bilions de paràmetres supera models quatre vegades més grans en tasques de raonament matemàtic complex. Un canvi de paradigma que podria posar la IA avançada directament a la butxaca de tothom.

## Temes tractats

- **La cursa armamentística de la IA i el seu coll d'ampolla**: La premissa de "com més gran, millor" ha dominat el camp, generant models que requereixen infraestructures colosals accessibles solament per a 4-5 actors mundials. Però estem a punt d'assolir un límit físic i econòmic insostenible.

- **Ouro i els Looped Language Models (LoopLM)**: Presentat per investigadors de ByteDance, UC Santa Cruz i Princeton, Ouro s'inspira en l'Ouroboros, la serp mitològica que es mossega la cua. En lloc d'apilar capes (*escala espacial*), reutilitza iterativament les mateixes capes (*escala temporal / profunditat recurrent*). Entrenat amb 7.7 bilions de tokens, el model de 2.6B aconsegueix un 90.85% al benchmark MATH500, mentre que Qwen3 de 8B s'atura en un 62.30%.

- **Raonament en l'espai latent**: En lloc del *chain-of-thought* clàssic, que obliga el model a escriure cada pas de raonament en text (omplint innecessàriament la finestra de context), Ouro rumia en silenci. L'estat intern es refina recursivament a l'espai latent i, només quan té la resposta, la verbalitza. S'acaba la "verborrea computacional".

- **La porta de sortida primerenca**: Per evitar bucles infinits, cada token disposa d'una "porta" que decideix si cal un bucle addicional o si la resposta ja és prou clara. S'entrena en dues fases: primer amb regularització entrópica per explorar totes les opcions uniformement, i després per equilibrar cost computacional amb millora real de precisió.

- **KV Cache Sharing (compartició de memòria cau)**: La solució al problema de memòria: durant la generació de text, nomes cal mantenir la memòria de l'últim bucle. Els bucles anteriors ja han quedat "destil·lats" en l'estat final, reduint la petjada de memòria per un factor de 4.

- **Disc dur vs. CPU: coneixement vs. manipulació**: Ouro no "sap" més coses (la capacitat d'emmagatzematge és idèntica: ~2 bits per paràmetre). L'avantatge és en la *manipulació del coneixement*: connecta informació en complexitat logarítmica (O(log n)), com buscar a una guia telefònica obrint sempre pel mig en lloc de llegir-la pàgina a pàgina.

- **Fidelitat i seguretat del raonament latent**: Amb *sondes lineals* (com "elèctrodes cognitius") es pot llegir l'estat intern a cada bucle i verificar que el model realment canvia d'opinió, en lloc de racionalitzar *a posteriori* (com fa sovint el chain-of-thought clàssic). A més, la taxa de toxicitat baixa en picat a mesura que s'afegeixen bucles, i el model es torna més prudent fins i tot en extrapolació (5-8 bucles, tot i entrenat amb 4).

- **Democratització i implicacions futures**: Un model de 2.6B amb rendiment equivalent a 12B permet, en principi, executar raonament profund en dispositius locals (telèfons, portàtils) sense dependència del núvol. A llarg termini, sorgeix una qüestió filosòfica: si el raonament és purament vectorial i continu, potser en algun moment les conclusions de la IA seran inaccessibles al llenguatge humà.

## Fonts

- [Scaling Latent Reasoning via Looped Language Models](https://arxiv.org/abs/2510.25741) — Article científic original (Rui-Jie Zhu et al., ByteDance, UC Santa Cruz, Princeton)
- [Ouro LLM - Pàgina oficial](http://ouro-llm.github.io/) — Models i codi obert del projecte
- [Transcripció automàtica](/podcast-del-doctor/sources/005-ouro-ia-pensa-en-bucle-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
