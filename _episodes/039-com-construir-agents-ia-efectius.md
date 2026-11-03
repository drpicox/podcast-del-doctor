---
audio_file: "https://archive.org/download/podcast-del-doctor-039-com-construir-agents-ia-efectius/039-com-construir-agents-ia-efectius.mp3"
audio_size: 9525672
chapters_file: "039-com-construir-agents-ia-efectius-chapters.json"
date: '2026-11-03'
description: "Programar era conduir un tren per unes vies; treballar amb agents d'IA s'assembla més a domar un cavall salvatge. A partir de dos articles d'Anthropic, la documentació de Claude Code i un fil de beamnxw, veiem per què cal evitar els agents sempre que es pugui, què és la putrefacció del context, com Claude va començar a prendre notes tot sol jugant a Pokémon, per què una eina a prova d'errors val més que mil instruccions i com és un arnès de set capes per a tasques llargues amb Opus 5.5. I una paradoxa final: per fer funcionar la IA hem reinventat la burocràcia."
duration: '19:50'
episode_number: 39
season: 1
soundbite_start: 1073.5
soundbite_duration: 43.9
soundbite_title: "Acabem d'inventar el middle management per a algoritmes"
sources:
- title: "Building effective agents"
  url: "https://www.anthropic.com/research/building-effective-agents"
  description: "Article d'Anthropic (desembre de 2024): la solució més simple possible, fluxos de treball contra agents, la interfície agent-ordinador (ACI) i les eines poka-yoke"
- title: "Effective context engineering for AI agents"
  url: "https://www.anthropic.com/research/effective-context-engineering-for-ai-agents"
  description: "Article d'Anthropic (setembre de 2025): putrefacció del context, pressupost d'atenció, altitud correcta, cerca just a temps, compactació, l'exemple de Pokémon i els subagents"
- title: "Extend Claude Code"
  url: "https://code.claude.com/docs/en/features-overview"
  description: "Documentació de Claude Code sobre CLAUDE.md, skills, subagents, hooks i MCP, i sobre què costa cada peça en context"
- title: "Make Opus 5.5 Finish Long Tasks: A Reusable Harness Engineering Setup"
  url: "https://x.com/beamnxw/status/2107522996046905797"
  description: "Fil de beamnxw a X amb l'arnès de set capes i el fitxer progress.md que l'episodi recorre a la segona meitat"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/039-com-construir-agents-ia-efectius-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Claude Code, Anthropic, beamnxw, SWE-bench, poka-yoke)"
thumbnail: "/assets/thumbnails/039-com-construir-agents-ia-efectius.png"
title: "Episodi 039: Com construir agents d'IA que acabin la feina"
---

## Introducció

Programar sempre havia estat com conduir un tren: tu poses les vies i la màquina les segueix. Amb els agents d'IA, la feina s'assembla més a domar un cavall salvatge. Aquest episodi explica com aconseguir que un agent treballi durant hores en una tasca llarga sense perdre el rumb ni rebentar el pressupost, a partir de dos articles d'Anthropic, la documentació de Claude Code i un fil de beamnxw sobre un arnès de set capes per a Opus 5.5.

## Temes tractats

- **Si pots, no construeixis un agent**: la primera recomanació d'Anthropic és buscar la solució més simple possible i afegir complexitat només quan calgui. Un flux de treball és un tren amb les estacions fixades; un agent és un tot terreny amb un mapa, i consumeix molta més benzina en forma de latència i tòquens. Entremig hi ha tot un espectre: un LLM amb eines, l'encadenament d'instruccions, l'enrutament (un porter de discoteca que envia l'horari de la botiga al model barat i la queixa complexa al gran) i la paral·lelització amb orquestrador i treballadors.

- **La putrefacció del context**: per què un model que llegeix un llibre en segons oblida la instrucció principal al cap de dues hores? Cada tòquen pot atendre tots els altres, cosa que genera n² relacions, i el context funciona com un banquet de 50 persones on ja no sents qui tens al costat. Anthropic en diu pressupost d'atenció. Afegir-hi deu paràgrafs més d'excepcions, doncs, sovint empitjora les coses. La regla d'or és trobar el conjunt més petit possible de tòquens d'alt valor, a l'altitud correcta: ni tan rígid com un codi ple de condicionals ni tan vague que l'agent s'hagi d'inventar el que falta.

- **La memòria de les tasques llargues**: en lloc de carregar-ho tot al principi, l'agent busca just a temps amb eines com `grep` o `head`, igual que nosaltres en una biblioteca. Quan la conversa s'infla, la compactació en resumeix l'historial i neteja els resultats vells. I amb Pokémon, Claude va començar a prendre notes tot sol, com ara que Pikachu havia guanyat 8 nivells, per recordar què feia hores abans. Els subagents completen l'estratègia: un treballador amb la memòria en blanc pot llegir desenes de fitxers i retornar només un resum condensat, que segons Anthropic sol ser d'entre 1.000 i 2.000 tòquens.

- **Eines a prova d'errors**: la interfície agent-ordinador (ACI) mereix tant d'esforç com la que fem servir els humans. El concepte clau és el *poka-yoke*, de la indústria japonesa. A SWE-bench, els agents es perdien amb les rutes relatives, i la solució no va ser cap instrucció més: van canviar l'eina perquè exigís rutes absolutes i el problema va desaparèixer.

- **Els hooks**: els ganxos de Claude Code són codi tradicional que s'executa fora del raonament del model. Si l'agent intenta esborrar una carpeta important, un hook previ a l'ús de l'eina pot bloquejar-ho abans que passi. Com diu la documentació, una instrucció al `CLAUDE.md` és una petició, i un hook és una garantia.

- **L'arnès de set capes**: el fil de beamnxw ho ordena així: (1) `CLAUDE.md` només per a regles permanents; (2) skills per als procediments recurrents; (3) MCP per connectar fonts externes com Notion amb un conducte net i controlat; (4) permisos a l'entorn, no al prompt, per denegar carpetes sensibles; (5) un subagent revisor separat, que amb el context net veu els errors que l'autor ja no veu; (6) esforç de raonament mitjà per defecte i alt només per revisar o dissenyar el nucli d'un sistema; i (7) un objectiu definit amb fets comprovables, com ara que existeixi un `resum.txt` amb una estructura exacta, i un límit de torns.

- **`progress.md`, el testimoni de la cursa de relleus**: abans de tancar una sessió, l'agent ha d'escriure què ha fet, què funciona, què estava a punt de fer i amb quin error s'ha trobat. La sessió següent comença llegint aquest fitxer i continua on l'anterior ho havia deixat, en lloc de començar de zero.

- **Reflexió final**: revisors independents, polítiques intocables, carpetes bloquejades i informes d'estat. Ens hem passat dècades queixant-nos d'aquesta burocràcia i ara l'hem hagut de ficar dins de la màquina: acabem d'inventar el *middle management* per a algoritmes. Potser separar funcions, documentar processos i auditar de manera independent no eren defectes humans, sinó les úniques maneres estables de gestionar un sistema complex.

## Episodis relacionats

- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): la base d'aquest episodi, amb l'equació agent = model + arnès i els seus pilars.
- [Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols): què passa quan es passa d'un agent a tota una flota.
- [Episodi 033: El xassi dels agents d'IA](/podcast-del-doctor/episodi/033-infraestructura-agents-ia): el mateix problema de portar agents a producció, vist des de la documentació d'AWS.

## Fonts

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents): article d'Anthropic sobre fluxos de treball, agents i eines
- [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents): article d'Anthropic sobre enginyeria de context
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview): documentació de Claude Code
- [Make Opus 5.5 Finish Long Tasks: A Reusable Harness Engineering Setup](https://x.com/beamnxw/status/2107522996046905797): fil de beamnxw a X
- [Transcripció automàtica](/podcast-del-doctor/sources/039-com-construir-agents-ia-efectius-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
