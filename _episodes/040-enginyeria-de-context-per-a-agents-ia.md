---
audio_file: "https://archive.org/download/podcast-del-doctor-040-enginyeria-de-context-per-a-agents-ia/040-enginyeria-de-context-per-a-agents-ia.mp3"
audio_size: 9100608
chapters_file: "040-enginyeria-de-context-per-a-agents-ia-chapters.json"
date: '2026-11-14'
description: "Un agent que juga a Pokémon perd la memòria cada poques hores i, per no començar de zero, porta un diari de camp. A partir de l'article d'Anthropic sobre enginyeria de context, veiem per què una finestra de context gegant no ho resol (la podridura del context i el pressupost d'atenció), com trobar l'altitud justa del prompt de sistema, per què calen eines sense solapaments i pocs exemples canònics, com busca Claude Code just a temps, i les tres tècniques per a tasques llargues: compactació, notes estructurades i subagents."
duration: '18:57'
episode_number: 40
season: 1
soundbite_start: 200.9
soundbite_duration: 65.4
soundbite_title: "Per què una finestra de context gegant no ho resol tot"
sources:
- title: "Effective context engineering for AI agents"
  url: "https://www.anthropic.com/research/effective-context-engineering-for-ai-agents"
  description: "Article de l'equip d'Applied AI d'Anthropic (29 de setembre de 2025): podridura del context, pressupost d'atenció, altitud del prompt de sistema, eines, exemples, context just a temps, compactació, notes estructurades i subagents"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/040-enginyeria-de-context-per-a-agents-ia-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Anthropic, Claude Code, context rot, l'agent)"
thumbnail: "/assets/thumbnails/040-enginyeria-de-context-per-a-agents-ia.png"
title: "Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA"
---

## Introducció

Imagina un jugador de Pokémon que pateix amnèsia cada poques hores i que, per no haver de començar de zero, s'escriu un diari de camp amb el nivell del seu Pikachu i el camí que seguia. No és ciència-ficció: és el que fan els agents d'IA més avançats per esquivar els límits de la seva memòria. Aquest episodi es dedica sencer a l'article d'Anthropic *Effective context engineering for AI agents* (setembre de 2025), que l'[Episodi 039](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius) només va tocar de passada: per què ja no n'hi ha prou de trobar la frase perfecta del prompt, i com s'ha de gestionar tot el que entra a la finestra de context d'un agent que treballa hores seguides.

## Temes tractats

- **De la recepta a la cuina**: l'enginyeria de prompts buscava la formulació perfecta per a una tasca d'un sol pas, com resumir o traduir un text. Un agent, en canvi, és un model que fa servir eines en bucle, i cada acció canvia el que necessita saber a la passa següent. L'episodi ho compara amb la diferència entre donar una bona recepta a un cuiner i dissenyar tota la cuina d'un restaurant en hora punta. Anthropic defineix el context com el conjunt de tòquens que el model té davant quan respon (prompt de sistema, eines, dades externes i historial) i l'enginyeria de context com la feina iterativa de triar-los a cada pas.

- **La podridura del context**: si les finestres ja hi caben llibres sencers, per què no hi aboquem tota la base de dades? Perquè, com més tòquens hi ha, pitjor recorda el model el que té a dins. És el *context rot*, i passa a tots els models, en més o menys grau. La causa és l'arquitectura: en un transformer cada tòquen atén tots els altres, cosa que fa créixer les relacions com n², i els models s'entrenen amb menys seqüències llargues. La interpolació de la codificació de posició, que és com estirar una imatge de baixa resolució per cobrir una paret, fa que la degradació sigui gradual, no un precipici. Per això Anthropic parla d'un **pressupost d'atenció**, i el principi que en treu és trobar el conjunt més petit possible de tòquens d'alt senyal que maximitzi el resultat.

- **L'altitud justa del prompt de sistema**: l'article busca una zona Rínxols d'Or entre dos errors. D'una banda, programar el prompt com una cadena d'*if-else* rígida, que es trenca davant de qualsevol cas imprevist. De l'altra, donar indicacions tan vagues que pressuposen un sentit comú que el model no té. L'episodi ho compara amb incorporar algú nou a un projecte: ni microgestió ni «fes la feina i ja està». Les seccions s'organitzen amb etiquetes XML o capçaleres Markdown, i *mínim* no vol dir *curt*: es comença amb un prompt mínim al millor model disponible i s'hi afegeixen instruccions a partir dels errors observats.

- **Eines clares i exemples canònics**: les eines són el contracte de l'agent amb el seu entorn, i han de ser eficients en tòquens, autocontingudes, robustes davant d'errors i sense solapaments. La prova de l'article: si un enginyer humà no sap dir amb seguretat quina eina toca fer servir, l'agent tampoc no ho sabrà. Amb els exemples (*few-shot*) passa una cosa semblant: millor un grapat d'exemples diversos i canònics que una enciclopèdia de casos límit, que roba atenció per entendre el cas normal.

- **Context just a temps**: en lloc de precarregar-ho tot, l'agent guarda identificadors lleugers (rutes de fitxers, consultes, enllaços) i carrega les dades quan les necessita, com qui es mou per una biblioteca amb la fitxa de referència en lloc d'apilar dues-centes enciclopèdies a la taula. Claude Code analitza grans volums de dades amb consultes dirigides i comandes com `head` i `tail`, i les metadades també parlen: un `test_utils.py` dins de `tests/` no té el mateix paper que dins de `src/core_logic/`. Té un cost, perquè explorar és més lent, i per això sovint convé una estratègia híbrida: Claude Code carrega els `CLAUDE.md` d'entrada i fa servir `glob` i `grep` per a la resta. En dominis menys dinàmics, com el legal o el financer, l'híbrid hi pot encaixar millor. El consell de fons: fes la cosa més simple que funcioni.

- **Tasques llargues (1): la compactació**: en una migració o una recerca de diverses hores, la finestra s'acaba omplint igualment, i una finestra més gran no treu el soroll. La compactació resumeix la conversa quan s'acosta al límit i continua en una finestra nova. A Claude Code, el resum conserva les decisions d'arquitectura, els errors pendents i els detalls d'implementació, descarta les sortides d'eines redundants, i l'agent continua amb el resum i els cinc fitxers que ha consultat més recentment. El risc és perdre un detall que més tard resulti clau, i per això cal ajustar-la primer per no deixar-se res i després per treure'n el que sobra. La forma més segura i lleugera és esborrar els resultats d'eines antics. A l'[Episodi 018](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real) vam veure, amb un article posterior d'Anthropic, fins on pot arribar aquest risc.

- **Tasques llargues (2): les notes estructurades**: l'agent escriu notes en una memòria persistent, fora de la finestra de context, i les torna a llegir quan les necessita, com la llista de tasques de Claude Code o un fitxer `NOTES.md`. L'exemple estrella és Claude jugant a Pokémon: durant milers de passos porta el compte del que fa (Pikachu ha guanyat 8 dels 10 nivells que es proposava a la Ruta 1), dibuixa mapes de les zones explorades i apunta estratègies de combat. Després de cada reinici del context, rellegeix les notes i continua on ho havia deixat. Anthropic n'ha fet una eina de memòria basada en fitxers per a la seva plataforma de desenvolupadors.

- **Tasques llargues (3): els subagents**: un agent principal manté el pla general amb el context net, com un director en un despatx endreçat, i encarrega les feines concretes a subagents que treballen amb finestres netes. Cada subagent pot gastar desenes de milers de tòquens explorant, però en retorna només un resum condensat, sovint d'entre 1.000 i 2.000 tòquens. Al sistema de recerca multiagent d'Anthropic, aquest patró va millorar clarament els resultats en tasques de recerca complexes. Quan fer servir cada tècnica? La compactació, per a converses amb molt d'anar i venir; les notes, per a desenvolupament iteratiu amb fites clares; els subagents, per a recerca complexa on explorar en paral·lel compensa.

- **Reflexió final**: hem deixat enrere la IA com un oracle a qui només calia preguntar amb les paraules màgiques adequades. Ara l'atenció del model és un recurs preciós i finit, i construir agents vol dir dissenyar tot l'ecosistema que l'envolta. Els models més capaços necessitaran menys enginyeria prescriptiva, però tractar el context com un recurs escàs continuarà sent central. I una pregunta oberta: què passarà el dia que la memòria externa d'aquests agents, milers de llibretes escrites a tota velocitat, superi la nostra pròpia capacitat de seguir la realitat?

## Episodis relacionats

- [Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius): feia servir aquest mateix article com una de les quatre fonts, al costat de *Building effective agents*, la documentació de Claude Code i un arnès de set capes.
- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): la gestió de context com a pilar de l'arnès, l'ansietat de context i per què els agents es deixen notes en fitxers de text.
- [Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols): la memòria estructurada de Beads i què passa quan un agent es converteix en una flota.
- [Episodi 016: OKF, la carpeta de text que ordena el caos de la IA](/podcast-del-doctor/episodi/016-com-okf-ordena-la-ia): l'altra cara del problema, que és quin coneixement trobarà l'agent quan vagi a buscar context.

## Fonts

- [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents): article d'Anthropic sobre enginyeria de context per a agents d'IA (setembre de 2025)
- [Transcripció automàtica](/podcast-del-doctor/sources/040-enginyeria-de-context-per-a-agents-ia-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
