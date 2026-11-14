---
audio_file: "https://archive.org/download/podcast-del-doctor-041-sistema-de-recerca-multiagent-de-claude/041-sistema-de-recerca-multiagent-de-claude.mp3"
audio_size: 6894410
chapters_file: "041-sistema-de-recerca-multiagent-de-claude-chapters.json"
date: '2026-11-14'
description: "Fins ara, preguntar a la IA era com consultar una enciclopèdia molt ràpida; el sistema Research de Claude s'assembla més a una agència de detectius. A partir de l'article d'Anthropic sobre com el van construir, veiem per què un agent líder amb subagents en paral·lel supera un sol agent i què costa en tòquens, com se li ensenya a delegar sense crear 50 subagents per a una pregunta simple, com s'avalua un sistema que mai no fa dues vegades el mateix camí i què cal per dur-lo a producció: reprendre la feina després d'un error, desplegaments arc de Sant Martí i fitxers per evitar el telèfon espatllat."
duration: '14:21'
episode_number: 41
season: 1
soundbite_start: 696.4
soundbite_duration: 63.1
soundbite_title: "Com evitar el telèfon espatllat entre agents"
sources:
- title: "How we built our multi-agent research system"
  url: "https://www.anthropic.com/research/multi-agent-research-system"
  description: "Article de l'equip d'enginyeria d'Anthropic (13 de juny de 2025), de Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox i Daniel Ford: l'arquitectura orquestrador-treballador de Research, els principis per fer prompts d'agents, l'avaluació amb un LLM com a jutge i els reptes de portar-ho a producció"
- title: "Model Context Protocol (MCP)"
  url: "https://modelcontextprotocol.io/introduction"
  description: "Introducció al protocol obert que connecta els agents amb eines i dades externes; l'article hi apunta perquè, amb servidors MCP, els agents es troben eines que no han vist mai i amb descripcions de qualitat molt desigual"
- title: "Interleaved thinking (documentació d'Anthropic)"
  url: "https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking"
  description: "Documentació del pensament estès i del pensament intercalat, el que fan servir els subagents per avaluar cada resultat d'eina abans de decidir la cerca següent"
- title: "Anthropic Cookbook: patrons d'agents"
  url: "https://platform.claude.com/cookbook/patterns-agents-basic-workflows"
  description: "Receptes d'Anthropic amb els patrons bàsics de fluxos de treball i agents; l'article hi remet per consultar prompts d'exemple del seu sistema"
- title: "BrowseComp (OpenAI)"
  url: "https://openai.com/index/browsecomp/"
  description: "Benchmark d'OpenAI que mesura la capacitat dels agents de navegació per trobar informació difícil de localitzar; és on Anthropic va veure que l'ús de tòquens explica per si sol el 80% de la variància del rendiment"
- title: "Code execution with MCP: Building more efficient agents"
  url: "https://www.anthropic.com/research/code-execution-with-mcp"
  description: "Article relacionat d'Anthropic (novembre de 2025) sobre com fer agents més eficients fent-los escriure codi contra els servidors MCP en lloc de cridar les eines una a una"
- title: "Anthropic Console"
  url: "https://console.anthropic.com/"
  description: "La consola on l'equip va muntar simulacions amb els prompts i les eines exactes del sistema per veure com treballaven els agents pas a pas"
- title: "Rainbow Deploys with Kubernetes"
  url: "https://brandon.dimcheff.com/2018/02/rainbow-deploys-with-kubernetes/"
  description: "Article de Brandon Dimcheff (2018) sobre els desplegaments arc de Sant Martí: diverses versions vives alhora i el trànsit que passa de mica en mica a la nova, la tècnica que Anthropic fa servir per no trencar els agents que ja estan treballant"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/041-sistema-de-recerca-multiagent-de-claude-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Anthropic, Claude, Sonnet, l'agent, RAG, SEO)"
thumbnail: "/assets/thumbnails/041-sistema-de-recerca-multiagent-de-claude.png"
title: "Episodi 041: Recerca multiagent, l'agència de detectius de Claude"
---

## Introducció

Fins ara, fer servir la IA era com consultar una enciclopèdia molt ràpida: feies una pregunta i et tornava un paràgraf. El sistema Research de Claude, que busca al web, a Google Workspace i a qualsevol integració, s'assembla més a contractar una agència de detectius sencera, on cadascú segueix una pista diferent alhora. Aquest episodi recorre l'article en què l'equip d'enginyeria d'Anthropic explica com el va construir: per què diversos agents rendeixen més que un de sol, quant costa, com se'ls ensenya a repartir-se la feina, com s'avalua un sistema que mai no fa dues vegades el mateix camí i què cal per fer-lo fiable en producció. És la continuació natural de l'[Episodi 040](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia), que ja feia servir aquest sistema com a exemple de l'arquitectura de subagents.

## Temes tractats

- **La recerca no és lineal**: quan investiguem un tema complex no podem fixar d'entrada els passos que farem. Llegim una cosa, canviem d'idea i tirem per una altra banda. Per això, diu l'article, un *pipeline* lineal d'una sola passada no hi serveix, i els agents, que decideixen torn rere torn quina direcció seguir segons el que van trobant, hi encaixen tan bé.

- **Per què molts agents rendeixen més que un**: l'essència de cercar és comprimir, és a dir, destil·lar el que importa d'un corpus enorme. Cada subagent explora una part de la pregunta amb la seva pròpia finestra de context i només en passa al líder els tòquens més importants. A l'avaluació interna d'Anthropic, un sistema amb Claude Opus 4 de líder i subagents Claude Sonnet 4 va superar un sol agent Opus 4 en un 90,2%. L'exemple: trobar tots els membres dels consells d'administració de les empreses del sector de tecnologia de l'S&P 500. El sistema multiagent ho va resoldre repartint-ho en subtasques, i l'agent sol no va trobar la resposta amb cerques lentes i seqüencials. Amb el benchmark BrowseComp, tres factors expliquen el 95% de la variància del rendiment, i el primer, l'ús de tòquens, n'explica per si sol el 80%. Els altres dos són el nombre de crides a eines i el model triat: passar a Claude Sonnet 4 dona més rendiment que doblar el pressupost de tòquens de Claude Sonnet 3.7.

- **El preu: tòquens a dojo**: un agent sol gasta unes 4 vegades més tòquens que una conversa de xat, i un sistema multiagent, unes 15 vegades més. Només surt a compte en tasques valuoses, que es poden repartir molt en paral·lel, que no caben en una sola finestra de context o que necessiten moltes eines complexes. No serveix quan tots els agents han de compartir el mateix context o hi ha moltes dependències entre ells: la majoria de tasques de programació tenen menys parts realment paral·lelitzables que la recerca, i els agents encara no saben coordinar-se ni delegar bé en temps real.

- **Orquestrador i treballadors**: l'agent principal (LeadResearcher) analitza la consulta, pensa una estratègia i desa el pla a una memòria externa, perquè quan el context passa de 200.000 tòquens es trunca i el pla no es pot perdre. Després crea tants subagents com calguin, cadascun amb una tasca de recerca concreta. Cada subagent cerca pel seu compte, fa servir el pensament intercalat (*interleaved thinking*) per avaluar cada resultat abans de la cerca següent i torna el que ha trobat. El líder ho sintetitza i decideix si cal investigar més. Quan ja n'hi ha prou, un CitationAgent repassa els documents i l'informe per lligar cada afirmació amb la seva font. A diferència del RAG clàssic, que recupera d'una sola vegada els fragments més semblants a la pregunta, aquí la cerca es fa en diversos passos i s'adapta al que va apareixent.

- **Ensenyar a delegar**: els primers agents creaven 50 subagents per a preguntes simples, buscaven sense fi fonts que no existien i es distreien entre ells amb massa actualitzacions. Com que cada agent es governa amb un prompt, el prompt va ser la principal palanca. Primer, pensar com els agents: muntar simulacions a l'Anthropic Console amb els prompts i les eines exactes, i mirar-los treballar pas a pas. Segon, encarregar bé la feina: cada subagent necessita un objectiu, un format de sortida, indicacions sobre eines i fonts i uns límits clars. Amb un encàrrec tan vague com «investiga l'escassetat de semiconductors», un subagent va estudiar la crisi dels xips de l'automòbil del 2021 mentre dos més duplicaven la feina mirant les cadenes de subministrament actuals del 2025. Tercer, escalar l'esforç segons la pregunta: una dada simple, un agent amb 3-10 crides a eines; una comparació, 2-4 subagents amb 10-15 crides cadascun; una recerca complexa, més de 10 subagents amb les responsabilitats ben repartides. A més, començar amb cerques curtes i àmplies i anar acotant, fer servir el pensament estès com a llibreta per planificar i treballar en paral·lel: el líder llança 3-5 subagents alhora i cada subagent fa servir 3 o més eines alhora, cosa que retalla fins a un 90% el temps de les recerques complexes. La idea de fons és ensenyar bones heurístiques, no regles rígides.

- **Agents que milloren les seves eines**: la interfície entre l'agent i les eines és tan crítica com la interfície entre persona i ordinador. Un agent que busca al web una informació que només és a Slack està condemnat des del principi, i amb els servidors MCP el problema creix, perquè les descripcions de les eines són de qualitat molt desigual. Els models Claude 4 resulten ser bons enginyers de prompts: amb un prompt i un error, diagnostiquen per què falla l'agent i proposen millores. Anthropic va fer un agent provador d'eines que, davant d'una eina MCP defectuosa, la fa servir desenes de vegades i en reescriu la descripció. Els agents que després van fer servir la descripció nova van acabar les tasques un 40% més ràpid.

- **Avaluar sense un camí correcte**: dos agents poden arribar a la mateixa resposta per camins diferents, l'un mirant tres fonts i l'altre deu, i per tant no es pot comprovar si han seguit els passos «correctes». Cal jutjar el resultat i que el procés sigui raonable. El consell és començar de seguida amb poques proves: al principi, un canvi de prompt pot fer passar l'èxit d'un 30% a un 80%, i van començar amb unes 20 consultes d'ús real. Després, un LLM fa de jutge amb una rúbrica (exactitud dels fets, exactitud de les cites, completesa, qualitat de les fonts i eficiència en l'ús d'eines): una sola crida amb un sol prompt que dona notes de 0,0 a 1,0 i un aprovat o suspès va ser el que més coincidia amb el criteri humà. Però les persones continuen sent imprescindibles: els provadors van veure que els agents preferien les granges de contingut optimitzades per al SEO a fonts amb més autoritat però pitjor posicionades, com PDF acadèmics o blogs personals. I com que els sistemes multiagent tenen comportaments emergents, els millors prompts no són ordres estrictes sinó marcs de col·laboració.

- **De prototip a producció**: en un sistema agèntic, canvis petits provoquen grans canvis de comportament i els errors s'acumulen. Una recerca no es pot tornar a començar de zero cada cop que falla alguna cosa, perquè és car i frustrant, i per això el sistema es reprèn des d'on era l'agent, amb reintents i punts de control, i avisant l'agent quan una eina falla perquè s'hi adapti. Per depurar-lo, amb agents que no fan mai el mateix dues vegades, cal traçabilitat completa en producció; Anthropic vigila els patrons de decisió i l'estructura de les interaccions sense mirar el contingut de les converses, per privadesa. Per desplegar, fa servir desplegaments arc de Sant Martí (*rainbow deployments*): la versió vella i la nova conviuen i el trànsit hi passa de mica en mica, perquè els agents que estan a mitja feina no es trenquin. Com diu l'article, en construir agents, l'última milla acaba sent la major part del camí.

- **Contra el telèfon espatllat**: a l'apèndix hi ha tres consells més. Els subagents poden desar el que produeixen (codi, informes, visualitzacions) en un sistema de fitxers extern i passar al coordinador només una referència lleugera, cosa que evita perdre informació d'un traspàs a l'altre i estalvia tòquens. En converses de centenars de torns, els agents resumeixen les fases acabades, les guarden en una memòria externa i, quan s'acosten al límit, engeguen subagents nous amb el context net i un bon traspàs de feina. I quan un agent modifica l'estat del món, s'avalua l'estat final, amb punts de control per als fluxos complexos, en lloc de cada pas intermedi.

- **Per a què es fa servir**: segons l'anàlisi de Clio que acompanya l'article, els usos principals de Research són desenvolupar programari en dominis especialitzats (10%), elaborar i millorar contingut professional i tècnic (8%), estratègies de creixement i d'ingressos per a empreses (8%), recerca acadèmica i material educatiu (7%) i investigar i verificar informació sobre persones, llocs o organitzacions (5%).

- **Reflexió final**: avui l'agent principal executa els subagents de manera síncrona i espera que acabi tot el grup abans de continuar. Així la coordinació és més simple, però el líder no pot reorientar els subagents, els subagents no es poden coordinar entre ells i tot el sistema pot quedar encallat esperant-ne un de sol. Anthropic preveu passar a una execució asíncrona, amb subagents que en creen d'altres quan cal, tot i que això complica la coordinació dels resultats, la coherència de l'estat i la propagació d'errors. La pregunta que queda oberta: on és el límit d'un eixam d'agents que es ramifica sense esperar ningú?

## Episodis relacionats

- [Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia): per què els subagents tornen només un resum condensat d'entre 1.000 i 2.000 tòquens, i quan convé fer-los servir en lloc de la compactació o les notes estructurades.
- [Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius): el patró orquestrador-treballadors dins de l'espectre de fluxos de treball i agents, i per què les eines mereixen tant d'esforç com les interfícies per a persones.
- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): el bucle, les eines, la gestió de context i el control determinista que envolten qualsevol agent.
- [Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols): l'orquestració multiagent aplicada a programar, que és justament el cas que aquest article considera menys adequat.
- [Episodi 033: El xassi dels agents d'IA](/podcast-del-doctor/episodi/033-infraestructura-agents-ia): els mateixos reptes de portar agents a producció, vistos des de la documentació d'AWS.
- [Episodi 026: WebMCP, la web nativa per a la IA](/podcast-del-doctor/episodi/026-webmcp-la-web-nativa-per-a-ia): MCP i per què la qualitat de la descripció de cada eina ho canvia tot per a un agent.

## Fonts

- [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system): article de l'equip d'enginyeria d'Anthropic sobre el sistema de recerca multiagent de Claude (juny de 2025)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction): introducció al protocol que connecta els agents amb eines externes
- [Interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking): documentació d'Anthropic sobre el pensament estès i el pensament intercalat
- [Anthropic Cookbook: patrons d'agents](https://platform.claude.com/cookbook/patterns-agents-basic-workflows): receptes amb patrons de fluxos de treball i agents, i prompts d'exemple
- [BrowseComp](https://openai.com/index/browsecomp/): benchmark d'OpenAI per a agents de navegació
- [Code execution with MCP](https://www.anthropic.com/research/code-execution-with-mcp): article relacionat d'Anthropic sobre agents més eficients amb MCP (novembre de 2025)
- [Anthropic Console](https://console.anthropic.com/): l'entorn on es van simular els agents amb els prompts i les eines reals
- [Rainbow Deploys with Kubernetes](https://brandon.dimcheff.com/2018/02/rainbow-deploys-with-kubernetes/): Brandon Dimcheff explica els desplegaments arc de Sant Martí (2018)
- [Transcripció automàtica](/podcast-del-doctor/sources/041-sistema-de-recerca-multiagent-de-claude-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
