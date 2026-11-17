---
audio_file: "https://archive.org/download/podcast-del-doctor-047-el-mite-dels-agents-d-ia-complexos/047-el-mite-dels-agents-d-ia-complexos.mp3"
audio_size: 8770002
chapters_file: "047-el-mite-dels-agents-d-ia-complexos-chapters.json"
date: '2026-11-17'
description: "Centenars de persones construint naus espacials per penjar un quadre, quan n'hi ha prou amb un martell i uns claus. A partir de l'article d'Anthropic «Building effective agents», veiem la diferència entre un flux de treball (un tren sobre vies fixes) i un agent (un cotxe autònom), per què els frameworks t'amaguen el prompt, els cinc patrons de flux (encadenament, enrutament, paral·lelització, orquestrador-treballadors i avaluador-optimitzador), quan val la pena un agent autònom i per què les eines que li dones, l'ACI, importen tant com el prompt."
duration: '18:16'
episode_number: 47
season: 1
soundbite_start: 195.7
soundbite_duration: 61.9
soundbite_title: "Un tren o un cotxe autònom? La majoria de problemes es resolen millor amb el tren"
sources:
- title: "Building effective agents (Anthropic)"
  url: "https://www.anthropic.com/research/building-effective-agents"
  description: "Article d'Erik Schluntz i Barry Zhang publicat per Anthropic el desembre del 2024 i revisat després: la distinció entre fluxos de treball i agents, els patrons de composició (LLM augmentat, encadenament, enrutament, paral·lelització, orquestrador-treballadors, avaluador-optimitzador i agents autònoms), els tres principis i dos apèndixs sobre agents en producció i sobre com fer enginyeria de prompts de les eines"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/047-el-mite-dels-agents-d-ia-complexos-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Anthropic, Claude, Claude Haiku 4.5, Claude Sonnet 4.5, Rivet, SWE-bench, l'agent, reemborsament, paral·lelització)"
thumbnail: "/assets/thumbnails/047-el-mite-dels-agents-d-ia-complexos.png"
title: "Episodi 047: El mite dels agents d'IA complexos, el tren abans que el cotxe autònom"
---

## Introducció

Entrar avui al món de la IA és com entrar en un taller enorme i caòtic, ple de gent construint naus espacials amb milers de peces mòbils... només per penjar un quadre a la paret, quan n'hi hauria prou amb un martell i uns quants claus. Aquest episodi parteix de l'article d'Anthropic **«Building effective agents»**, que ho diu sense embuts: l'èxit amb els models de llenguatge no és construir el sistema més sofisticat, sinó el que la feina necessita, i només s'hi ha d'afegir complexitat quan es pot demostrar que millora els resultats.

L'àudio en diu «el nou informe tècnic», però és un article del blog d'Anthropic del desembre del 2024, revisat després (ja parla de Claude Haiku 4.5 i Sonnet 4.5). És l'article fundacional de la sèrie que hem anat seguint: l'[Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia), l'[Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude) i els cinc episodis sobre l'examen Claude Certified Architect (del [042](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs) al [046](/podcast-del-doctor/episodi/046-guia-de-l-examen-claude-certified-architect)) en parteixen, conscientment o no. La metàfora del tren i del cotxe autònom és de l'àudio, no de l'article.

## Temes tractats

- **Fluxos de treball i agents: el tren i el cotxe autònom**: Anthropic agrupa tot el que es ven com a «agent» sota el paraigua de **sistemes agèntics**, però hi fa una distinció d'arquitectura. Un **flux de treball** (*workflow*) orquestra models i eines per camins de codi predefinits: el programador ha decidit quin pas va primer i en quines condicions s'avança. Un **agent** decideix sobre la marxa quines eines fa servir i en quin ordre. El primer és un tren sobre vies fixes: saps on surt, on para i on arriba, i si hi ha un obstacle s'atura. El segon és un cotxe autònom: li dones el destí i, si troba un carrer tallat, busca una alternativa. La tesi de l'article és que la majoria de problemes es resolen millor amb el tren, perquè en producció vols predictibilitat, i que sovint n'hi ha prou amb una sola crida al model ben feta, amb recuperació d'informació i exemples.

- **Frameworks: les caixes negres**: el Claude Agent SDK, Rivet o Vellum (l'article també cita el Strands Agents SDK d'AWS) prometen ser un kit de muntatge. Estalvien codi, però afegeixen capes d'abstracció que amaguen el prompt que surt i la resposta que entra, de manera que quan el model respon una bajanada no saps si és el model o el framework que ha traduït malament la petició. La recomanació és començar amb l'API dels models directament, perquè molts patrons són quatre línies de codi, i, si fas servir un framework, entendre què fa per sota.

- **L'LLM augmentat i l'encadenament de peticions**: la peça bàsica és el model connectat a eines, memòria i cerca, per exemple a través del Model Context Protocol (MCP). El primer patró és l'**encadenament** (*prompt chaining*): dividir una tasca en passos seqüencials on la sortida d'un és l'entrada del següent, amb comprovacions programàtiques entremig. Si demanes de cop un document de màrqueting de deu pàgines, en to corporatiu i traduït al francès, el model perd el fil; en tres passos (esborrany, revisió del to, traducció) cada crida és fàcil. Es canvia latència per precisió.

- **Enrutament i paral·lelització**: l'**enrutament** (*routing*) posa un recepcionista al davant que classifica la petició i l'envia al procés especialitzat; l'article proposa enviar les preguntes fàcils a un model petit i barat com Claude Haiku 4.5 i les difícils a un de gran com Claude Sonnet 4.5. La **paral·lelització** té dues variants: el **seccionament**, tasques independents que corren alhora (un model respon l'usuari mentre un altre fa de filtre de seguretat), i la **votació**, la mateixa tasca diverses vegades, per exemple diversos prompts buscant vulnerabilitats al mateix codi. Multiplicar el cost per tres o quatre té sentit quan l'error és car: la factura de tokens és ridícula al costat d'una fallada de seguretat.

- **Orquestrador-treballadors i avaluador-optimitzador**: a l'**orquestrador-treballadors**, un model central desglossa la tasca, delega en treballadors i en sintetitza els resultats. S'assembla a la paral·lelització, però les subtasques no estan predefinides: les decideix l'orquestrador segons l'entrada. L'exemple del botó de pagament d'una web és de l'àudio; l'article parla de productes de programació que fan canvis a diversos fitxers i de cerques que recullen informació de moltes fonts. Ho vam veure amb un sistema real a l'[Episodi 041](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude). L'**avaluador-optimitzador** és un escriptor i un editor exigents passant-se el manuscrit, ideal per a la traducció literària o les cerques complexes. Perquè no sigui un bucle infinit calen criteris d'avaluació clars i que la retroacció articulada millori de debò la resposta.

- **Agents autònoms i l'humà en el bucle**: els agents de debò són per a problemes oberts, on no pots codificar els passos: un model que fa servir eines en un bucle, mirant a cada pas el resultat real de l'entorn. Els exemples són l'agent de programació que resol incidències reals de SWE-bench Verified només a partir de la descripció, la demostració de *computer use* que mou el ratolí per la pantalla, i els agents d'atenció al client que consulten comandes i poden emetre reemborsaments. Una precisió: l'àudio diu que l'agent de SWE-bench ho fa tot sol, «sense cap intervenció externa»; l'article insisteix que la revisió humana continua sent imprescindible per comprovar que la solució encaixa amb la resta del sistema. L'autonomia porta **errors compostos** (si el pas 1 falla, el pas 10 és un desastre), i per això cal provar-ho tot en *sandboxes*, posar condicions d'aturada com un màxim d'iteracions i punts de control on l'agent demana permís, com vam explicar amb els hooks a l'[Episodi 042: Agents d'IA autònoms i segurs, deixar-los pensar i lligar-los curt](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs).

- **L'ACI i les rutes absolutes**: el secret menys glamurós de l'article és que les eines mereixen tanta enginyeria de prompts com el prompt principal. Com durant anys hem cuidat la interfície persona-ordinador (HCI), ara cal cuidar la **interfície agent-ordinador (ACI)**: si la documentació d'una eina no l'entendria un programador júnior, el model tampoc. Calen formats propers al text natural (escriure codi dins de JSON obliga a escapar cometes i salts de línia, i en Markdown no), donar-li tokens per pensar abans d'escriure i no obligar-lo a comptar milers de línies. I sobretot **poka-yoke**, el disseny que fa impossible l'error: a SWE-bench, l'agent s'equivocava amb les rutes relatives quan sortia del directori arrel, i en lloc de demanar-li que anés amb compte van fer que l'eina exigís rutes absolutes. A partir d'aquí, no va fallar mai més. És la mateixa idea de l'[Episodi 046](/podcast-del-doctor/episodi/046-guia-de-l-examen-claude-certified-architect): el model tria les eines llegint-ne la descripció, no el codi.

- **Els tres principis**: **simplicitat** en el disseny de l'agent; **transparència**, mostrant explícitament els passos de planificació perquè, si falla, sàpigues on i per què; i una **ACI** feta amb documentació i proves acurades. La sofisticació de debò no és un laberint que funciona de miracle, sinó un sistema predictible i auditable.

- **Reflexió final**: si comencem a redissenyar el programari i les API perquè les entenguin millor els agents, prioritzant l'ACI per sobre de les persones, arribarà un dia que la manera com els humans fem servir els ordinadors l'hauran modelada les preferències de les IA? Qui s'acabarà adaptant a qui? La pregunta és de l'àudio, no de l'article.

## Fonts

- [Building effective agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents) — Article d'Erik Schluntz i Barry Zhang (desembre del 2024, revisat després) sobre fluxos de treball, agents, patrons de composició, els tres principis i l'enginyeria de prompts de les eines
- [Transcripció automàtica](/podcast-del-doctor/sources/047-el-mite-dels-agents-d-ia-complexos-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3), amb correcció posterior d'alguns noms propis i termes

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
