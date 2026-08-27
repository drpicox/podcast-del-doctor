---
audio_file: "https://archive.org/download/podcast-del-doctor-025-l-ia-no-pot-desfer-la-realitat/025-l-ia-no-pot-desfer-la-realitat.mp3"
audio_size: 19124068
chapters_file: "025-l-ia-no-pot-desfer-la-realitat-chapters.json"
date: '2026-08-27'
description: "Demanes a l'agent un bitllet per dimarts, t'equivoques, edites el missatge i poses dijous. El xat queda impecable — i al compte hi ha dos càrrecs de 1.000 euros. A partir de «Quan el món no es bifurca», la nota tècnica darrere de Context Inspector, desgranem per què el botó de desfer és una promesa que la interfície no pot complir: el penjat com a laboratori, les quatre categories d'acció (de la lectura inofensiva al rm -rf) i les respostes que la informàtica ja tenia des dels vuitanta — idempotència, retencions, patró Saga i ETags. La idea central: reconciliar no és desfer, és negar-se a oblidar."
duration: '39:50'
episode_number: 25
season: 1
soundbite_start: 2328.8
soundbite_duration: 47.1
soundbite_title: "Qui serà l'amo de la memòria i de la veritat?"
sources:
- title: "«Quan el món no es bifurca» — notes de treball de l'autor"
  url: ""
  description: "Document de recerca inèdit i no publicat de David Rodenas, eix central de l'episodi: nota tècnica de llançament de Context Inspector, amb proves fetes sobre models locals via Ollama i 36 escenaris de bifurcació escrits com a especificacions executables. Les referències bibliogràfiques que se'n citen (secció «The literature, such as it is») estan enllaçades a sota una per una"
- title: "Sagas"
  url: "https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf"
  description: "Hector Garcia-Molina i Kenneth Salem, ACM SIGMOD 1987, pp. 249-259 (DOI 10.1145/38713.38742). El text que introdueix les transaccions de compensació: tota acció de llarga durada s'ha de dissenyar amb la seva parella compensatòria"
- title: "Idempotent requests — Stripe API Reference"
  url: "https://docs.stripe.com/api/idempotent_requests"
  description: "Documentació oficial de Stripe sobre la capçalera Idempotency-Key: com una clau única evita que un reintent de xarxa cobri dues vegades"
- title: "Implementing Stripe-like Idempotency Keys in Postgres"
  url: "https://brandur.org/idempotency-keys"
  description: "Brandur Leach, 27 d'octubre de 2017. La implementació d'aquestes claus des del costat del servidor"
- title: "Event Sourcing"
  url: "https://martinfowler.com/eaaDev/EventSourcing.html"
  description: "Martin Fowler, 12 de desembre de 2005. L'estat actual com a suma d'esdeveniments passats — el mateix patró que fa que l'historial del context de l'agent funcioni com a registre de l'estat del joc"
- title: "RFC 7232 — HTTP/1.1: Conditional Requests"
  url: "https://datatracker.ietf.org/doc/html/rfc7232"
  description: "Fielding i Reschke (eds.), IETF, juny de 2014. ETag (§2.3), If-Match (§3.1) i el 412 Precondition Failed (§4.2) — la concurrència optimista que rebutja les creences obsoletes d'un client. Obsoletat per l'RFC 9110 (juny de 2022), que en manté la semàntica als §13 i §15.5.13"
- title: "Giving undo attention"
  url: "https://www.alandix.com/academic/papers/undo92/undo92.html"
  description: "Gregory D. Abowd i Alan J. Dix, Interacting with Computers 4(3): 317-342, 1992. Anàlisi formal de què vol dir realment desfer i recuperar accions"
- title: "A selective undo mechanism for graphical user interfaces based on command objects"
  url: "https://dl.acm.org/doi/10.1145/196699.196721"
  description: "Thomas Berlage, ACM TOCHI 1(3): 269-294, setembre de 1994. La complexitat d'eliminar una acció del mig d'un historial sense trencar-ne la resta"
- title: "Penalizing side effects using stepwise relative reachability"
  url: "https://arxiv.org/abs/1806.01186"
  description: "Victoria Krakovna, Laurent Orseau, Ramana Kumar, Miljan Martic i Shane Legg, arXiv, juny de 2018 (versió revisada al taller d'AI Safety d'IJCAI 2019). Agents que aprenen a penalitzar els efectes secundaris irreversibles"
- title: "Avoiding Side Effects in Complex Environments"
  url: "https://arxiv.org/abs/2006.06547"
  description: "Alexander Matt Turner, Neale Ratzlaff i Prasad Tadepalli, arXiv juny de 2020, spotlight a NeurIPS 2020. Continuació de la línia d'Attainable Utility Preservation (arXiv 2019, AIES 2020)"
- title: "There Is No Turning Back: A Self-Supervised Approach for Reversibility-Aware Reinforcement Learning"
  url: "https://arxiv.org/abs/2106.04480"
  description: "Nathan Grinsztajn, Johan Ferret, Olivier Pietquin, Philippe Preux i Matthieu Geist, NeurIPS 2021. Agents que aprenen a reconèixer els camins sense retorn abans de prendre'ls"
- title: "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
  url: "https://arxiv.org/abs/2406.12045"
  description: "Shunyu Yao, Noah Shinn, Pedram Razavi i Karthik Narasimhan, juny de 2024. Avalua agents en dominis reals de comerç i aerolínies — precisament l'escenari de la reserva de vols"
- title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
  url: "https://arxiv.org/abs/2307.13854"
  description: "Shuyan Zhou et al., arXiv juliol de 2023, ICLR 2024. Mesura l'èxit de l'agent per l'estat final de la base de dades, no pel text de la conversa"
- title: "Model Context Protocol — Tools (revisió 2025-03-26)"
  url: "https://modelcontextprotocol.io/specification/2025-03-26/server/tools"
  description: "L'especificació que introdueix les anotacions d'eina. Els quatre indicadors concrets (readOnlyHint, destructiveHint, idempotentHint, openWorldHint) viuen a l'esquema congelat d'aquesta revisió, i la mateixa especificació avisa que el client els ha de tractar com a no fiables"
- title: "Building effective agents"
  url: "https://www.anthropic.com/engineering/building-effective-agents"
  description: "Erik Schluntz i Barry Zhang (Anthropic), 19 de desembre de 2024. Patrons de disseny d'agents, i el context del disseny d'aïllament i checkpoints de Claude Code"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/025-l-ia-no-pot-desfer-la-realitat-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior dels termes tècnics i noms propis (ETag, idempotència, patró Saga, KV cache, Context Inspector, Garcia-Molina, Claude Code, readOnlyHint)"
thumbnail: "/assets/thumbnails/025-l-ia-no-pot-desfer-la-realitat.png"
title: "Episodi 025: L'IA no pot desfer la realitat"
---

## Introducció

Li demanes a l'assistent que et compri un bitllet a Nova York per dimarts. El compra. Un segon després t'adones que volies dijous, i fas el reflex que fem tots: prems editar, canvies la paraula, tornes a enviar. El xat queda impol·lut — apareix aquell discret «1 de 2» al missatge i la branca antiga desapareix de la pantalla. L'IA, obedient, et compra el vol de dijous.

I al teu compte hi ha un càrrec de 2.000 euros, perquè tens dos bitllets. La IA, instal·lada a la seva línia temporal nova i neta, no sap ni que el primer vol existeix.

Aquest episodi surt d'un document de treball inèdit, **«Quan el món no es bifurca»**, escrit a partir de les proves fetes amb una eina pròpia — **Context Inspector** — sobre models locals via Ollama. La premissa és lapidària: **quan li poses un botó de desfer a un agent autònom, li estàs fent a l'usuari una promesa sobre el món real que la interfície no pot complir.**

## Temes tractats

- **El penjat com a laboratori**: abans d'arruïnar-se amb bitllets duplicats, el document busca on es trenca la il·lusió en un entorn minúscul. El joc del penjat és perfecte perquè necessita **guardar un secret**: la paraula a endevinar no pot ser a l'historial del xat, perquè un model de llenguatge no té cap filtre per ignorar el text que té al davant — el llegeix i fa trampes immediatament.

- **Les tres maneres de trencar-ho**: si guardes l'estat en una variable externa al xat, el viatge en el temps l'ensorra de tres formes. **Retrocedint**: esborres la jugada de la A, forces la O, i el tauler retorna les dues lletres — la IA pateix una **al·lucinació per justificació**, intentant donar sentit a una realitat que no quadra amb la seva memòria. **Esborrant-ho tot**: comences partida nova, la IA té la memòria neta però l'eina continua la partida anterior, i el model, en lloc d'admetre que està perdut, s'inventa un «ah, veig que ja tenim un joc començat, doncs continuem». **Bifurcant**: dues branques actives consulten la mateixa variable i les jugades es barregen. És jugar dues partides d'escacs simultànies sobre el mateix tauler de fusta.

- **La solució: fer-ho una funció pura**: eliminar l'estat extern i fer que la paraula secreta **viatgi enganxada al context**, com una motxilla adherida als missatges. El sistema d'orquestració la desa com a metadades i la **retalla literalment un mil·lisegon abans** d'enviar el text al model. Cada branca carrega el seu propi estat, independent. Saltes a la branca 1, recuperes la memòria de la branca 1.

- **Viatjar en el temps és barat**: gràcies a la **KV cache** (Key-Value Cache) que els models ja porten integrada, canviar el missatge 6 d'una conversa no obliga a rellegir-la des del principi. A les proves locals de l'autor, una lectura nova costa 250-300 mil·lisegons; recuperar el context d'una branca ja a la memòria cau, **74 mil·lisegons**.

- **El mur infranquejable**: hi ha un cas que ni la motxilla oculta salva — **reescriure el passat volent mantenir el futur intacte**. Si esborres el missatge 3 però conserves del 4 al 10, aquells missatges futurs ja mostren visualment una lletra que ja no s'ha jugat mai. L'autor hi admet la derrota amb elegància: l'eina **permet l'acció però es nega a fingir que té sentit**. Si vols trencar el continu espai-temps, tu mateix; però no li demanis que ho arregli.

- **Les quatre categories d'acció**: fora del laboratori, no totes les accions són igual de perilloses. **(1) Lectures** — consultar el temps o un horari: retrocedeixes i no passa res, com a molt la dada és obsoleta. **(2) Escriptures idempotents** — el termòstat: si a la branca A vas demanar 20 graus i a la B 18, el menjador es queda a 18 encara que tornis a obrir la branca A, perquè el text del xat és **només una creença**, no està connectat per Bluetooth a la realitat. **(3) Escriptures compensables** — el bitllet: es pot desfer, però només cridant explícitament l'API de cancel·lació, i la IA de la branca nova no sap que hi ha res a cancel·lar mentre la de la branca vella queda congelada en un llimb digital. **(4) Escriptures irreversibles** — enviar un correu, transferir criptomonedes, un `rm -rf` sobre producció: aquí les dues branques descriuen dos mons, i només un és l'autèntic.

- **Els worktrees de Claude Code**: l'eina emula la motxilla oculta creant un espai de fitxers aïllat per branca, de manera que en canviar de branca el disc dur canvia sota teu invisiblement. Funciona per al sistema de fitxers, i cau pel seu propi pes davant la quarta categoria: una petició de xarxa o una biblioteca publicada a NPM ja no torna. Aquest problema de fins on arriba realment el control sobre un agent el vam tractar a [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real) i [Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols).

- **La informàtica ja ho havia resolt**: la tesi més refrescant del document és que, a ulls de la infraestructura d'internet, els agents autònoms no són res màgic — són **clients inestables**, i sabem tractar-los des dels anys vuitanta. **Claus d'idempotència** (Stripe): una matrícula única per acció, que et protegeix del reintent cec però **no de canviar d'opinió** — demanar dijous en comptes de dimarts genera una clau nova, i el servidor no hi veu cap duplicat. **Retencions**: dues eines separades, `hold_flight` (bloqueig gratuït de 15 minuts que caduca sol) i `ticket_hold` (el càrrec definitiu), com demanar al dependent que et guardi l'abric darrere el taulell mentre t'ho penses. **Patró Saga** (Garcia-Molina i Salem, 1987): tota acció s'ha de dissenyar amb la seva compensació obligatòria, i el registre no el porta la memòria volàtil del xat sinó **un orquestrador central**. **Dry runs**: abans de res destructiu, un informe del que passaria.

- **Compensar no és que no hagi passat res**: l'avís més important del document. Cancel·lar l'hotel fora de termini et pot costar una nit de penalització; un banc et torna els diners, però amb tres dies hàbils. Has desfet l'acció lògica sobre el paper — les seqüeles físiques, financeres i temporals es queden a la teva vida.

- **Quatre mecanismes quan l'API és de tercers**: si el servidor no és teu, no pots posar-lo a la motxilla. **(1) Marcar les portes** amb les anotacions del Model Context Protocol (`readOnlyHint`, `destructiveHint`), perquè la interfície pugui avisar-te abans de bifurcar sobre una reserva ja confirmada. **(2) Segellar amb ETags**: la IA envia la petició adjuntant la versió de la realitat que creu vigent; si mentrestant una altra branca l'ha canviat, el servidor respon **412 Precondition Failed** i l'obliga a rellegir el món. **(3) Reconciliació a la bifurcació** — el cor de Context Inspector. **(4) Preguntar al món**: forçar sempre una consulta prèvia abans de qualsevol escriptura perillosa. És feixuc i consumeix tokens, però és incontestablement fiable.

- **Reconciliació: negar-se a oblidar**: quan detecta que has retrocedit, el sistema fa tres passos sense que hi facis res. Inspecciona d'amagat la branca que acabes d'abandonar; filtra les accions irreversibles que hi van quedar sense compensar; i **injecta un missatge sintètic invisible** a la branca nova, just després de la bifurcació: «avís, en una branca alternativa que l'usuari ha esborrat ja vas confirmar i pagar el vol ABC123 per a dimarts». Tu no el veus. La IA sí — i et respon que abans de comprar el de dijous potser convindria cancel·lar el de dimarts. Un post-it digital amagat que t'estalvia el desastre sencer. Com diu el document, **és el contrari exacte de desfer: és negar-se a oblidar**.

- **El document que ha de compilar**: davant l'escepticisme raonable cap a l'arquitectura de saló, el text no és un assaig sinó la nota tècnica de llançament de l'eina real. Conté **36 escenaris de bifurcació escrits a mà en Markdown**, configurats per ser executats com a proves seguint la definició de test unitari de l'Agile Alliance. Si Context Inspector no es comporta com el text descriu, **el document no compila** i no es pot publicar la nova versió. És una auditoria tècnica incrustada a la prosa — la mateixa idea que explorem a [Episodi 012: L'especificació és el nou codi](/podcast-del-doctor/episodi/012-especificacio-nou-codi).

- **On recau la culpa**: la lliçó de fons és un canvi de paradigma. Solem creure que l'agent ha d'entendre les conseqüències físiques dels seus actes com ho faria un humà, però la IA és **una ment raonadora tancada en una habitació fosca amb un intèrfon**, que només llegeix els papers que li passes per sota la porta. Mantenir aquestes creences alineades amb la realitat és responsabilitat íntegra de qui dissenya el sistema. Un fil que connecta amb [Episodi 017: La IA que s'escapa per no ser apagada](/podcast-del-doctor/episodi/017-ia-que-s-escapa-per-no-ser-apagada) i amb el desastre operatiu de [Episodi 020: El SAP que va enfonsar Revlon](/podcast-del-doctor/episodi/020-el-sap-que-va-enfonsar-revlon).

- **Reflexió final**: quan la IA només genera text, retrocedir és gratis. Quan l'agent està connectat a comptes bancaris, prémer Desfer és una separació violenta del curs de l'univers, i només hi ha dues sortides: que el món físic es bifurqui màgicament al teu voltant, o que el sistema doni la cara i confessi a la IA que els actes del passat han deixat cicatrius. Cal deixar l'obsessió de mantenir el xat bonic i polit, i prioritzar mantenir-lo **verídic**.

## Fonts

- **«Quan el món no es bifurca»** — notes de treball inèdites de l'autor, nota tècnica de llançament de Context Inspector. No publicades; les referències bibliogràfiques que se'n citen són les de sota.
- [Sagas](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf) — Hector Garcia-Molina i Kenneth Salem, ACM SIGMOD 1987
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests) — Stripe API Reference
- [Implementing Stripe-like Idempotency Keys in Postgres](https://brandur.org/idempotency-keys) — Brandur Leach, 2017
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) — Martin Fowler, 2005
- [RFC 7232 — HTTP/1.1: Conditional Requests](https://datatracker.ietf.org/doc/html/rfc7232) — IETF, 2014 (obsoletat per l'RFC 9110)
- [Giving undo attention](https://www.alandix.com/academic/papers/undo92/undo92.html) — Abowd i Dix, 1992
- [A selective undo mechanism for graphical user interfaces based on command objects](https://dl.acm.org/doi/10.1145/196699.196721) — Berlage, ACM TOCHI, 1994
- [Penalizing side effects using stepwise relative reachability](https://arxiv.org/abs/1806.01186) — Krakovna et al., 2018
- [Avoiding Side Effects in Complex Environments](https://arxiv.org/abs/2006.06547) — Turner et al., NeurIPS 2020
- [There Is No Turning Back](https://arxiv.org/abs/2106.04480) — Grinsztajn et al., NeurIPS 2021
- [τ-bench](https://arxiv.org/abs/2406.12045) — Yao et al., 2024
- [WebArena](https://arxiv.org/abs/2307.13854) — Zhou et al., ICLR 2024
- [Model Context Protocol — Tools (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/server/tools) — anotacions d'eina
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic, 2024
- Transcripció automàtica (`/podcast-del-doctor/sources/025-l-ia-no-pot-desfer-la-realitat-transcripcio.txt`) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
