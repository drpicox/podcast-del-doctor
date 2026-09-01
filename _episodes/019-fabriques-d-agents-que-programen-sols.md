---
audio_file: "https://archive.org/download/podcast-del-doctor-019-fabriques-d-agents-que-programen-sols/019-fabriques-d-agents-que-programen-sols.mp3"
audio_size: 9566177
chapters_file: "019-fabriques-d-agents-que-programen-sols-chapters.json"
date: '2026-08-05'
description: "Un enginyer de DoltHub activa el «mode sense límits» per arreglar quatre tests i la seva flota d'agents acaba fusionant codi que no compila a velocitat inhumana: cent dòlars en tòquens en una hora de generar escombraries. Aquest episodi explica la infraestructura que ha nascut per evitar-ho: Beads, l'issue tracker de Steve Yegge amb identificadors immutables i graf de dependències, que va migrar a Dolt perquè Git no aguantava cinquanta agents escrivint alhora; Gas Town i el seu repartiment de Mad Max —alcalde, mofetes, diaca i testimoni—; el PageRank per prioritzar tasques, i Wasteland, la federació de fàbriques que es subcontracten la feina. Tercer episodi de la sèrie sobre arnesos d'agent que obren el 017 i el 018."
duration: '19:55'
episode_number: 19
season: 1
soundbite_start: 621.3
soundbite_duration: 53.3
soundbite_title: "Mode sense límits: cent dòlars en una hora destruint el repositori"
sources:
- title: "Beads — documentació oficial"
  url: "https://beads.gascity.com/"
  description: "Lloc de documentació de Beads (bd), l'issue tracker AI-native sobre Dolt: identificadors amb hash, els quatre tipus de dependència (blocks, parent-child, discovered-from, related), l'execució conscient de dependències amb bd ready, i les fórmules, molècules i gates per a coordinació multiagent"
- title: "gastownhall/beads — repositori de codi"
  url: "https://github.com/gastownhall/beads"
  description: "Codi font de Beads: model de dades sobre Dolt en mode incrustat o servidor, tasques jeràrquiques, decaïment semàntic de memòria per compactació, mode furtiu i les comandes bd create, bd ready, bd dep add, bd prime i bd remember"
- title: "Gas Town Hall — hub de la comunitat"
  url: "https://gastownhall.ai"
  description: "Centre de documentació i comunitat de Gas Town, creat per Steve Yegge amb aportacions de Chris Sells: anuncis de la v1.0.0, el llançament de Gas City com a motor d'orquestració agèntica i el blog Town Crier"
- title: "gastownhall/gastown — repositori de codi"
  url: "https://github.com/gastownhall/gastown"
  description: "Codi font del gestor d'espais de treball multiagent: la jerarquia de town, rigs, hooks i crew members, els rols de Mayor, Polecat, Witness, Deacon i Refinery, i les comandes gt rig add, gt mayor attach, gt convoy create, gt sling i gt feed"
- title: "Wasteland — tauler federat de coordinació"
  url: "https://wasteland.gastownhall.ai/"
  description: "Xarxa de federació que enllaça Gas Towns entre si a través de DoltHub perquè els orquestradors es deleguin feina, subcontractin capacitat de còmput remota i en fusionin el resultat"
- title: "Dicklesworthstone/beads_viewer — TUI amb consciència de graf"
  url: "https://github.com/Dicklesworthstone/beads_viewer"
  description: "Interfície de terminal de Jeffrey Emanuel per a Beads que aplica PageRank i càlcul de camí crític sobre el graf de dependències per decidir quina tasca desbloqueja més feina"
- title: "DoltHub Blog"
  url: "https://www.dolthub.com/blog/"
  description: "Blog de DoltHub, on Tim Sehn documenta l'experiment del mode sense límits sobre quatre tests BATS i el funcionament de Dolt com a base de dades SQL amb semàntica de Git i arbres Prolly"
- title: "Steve Yegge — blog personal"
  url: "https://steve-yegge.blogspot.com/"
  description: "Blog del creador de Beads i Gas Town, amb els assajos sobre la fàbrica d'agents, el clown show dels primers dies de coordinació i el cas de la llicenciada en comunicació que substitueix un SaaS sense saber programar"
- title: "Technology Radar — Thoughtworks"
  url: "https://www.thoughtworks.com/radar"
  description: "Informe periòdic de Thoughtworks que situa aquestes eines d'orquestració multiagent dins del panorama tecnològic actual"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/019-fabriques-d-agents-que-programen-sols-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior dels noms propis i termes tècnics (Beads, Gas Town, Dolt, Yegge, Prolly, Jira, Claude Code)"
thumbnail: "/assets/thumbnails/019-fabriques-d-agents-que-programen-sols.png"
title: "Episodi 019: Fàbriques d'agents que ja programen sols"
---

## Introducció

Tim Sehn volia arreglar quatre tests de shell. Va activar el **mode sense límits** de la seva flota d'agents i va anar a fer altra cosa. Quan va tornar, la màquina obria branques, generava pull requests trencats i fusionava codi que no compilava a una velocitat que cap humà podia seguir. Va haver de buscar un company enginyer perquè li fes un `git reset --hard` d'urgència abans que allò es carregués l'estructura base del repositori. Cost de l'operació: **cent dòlars en tòquens en seixanta minuts**, tots per generar escombraries.

Aquest episodi va d'això: de la infraestructura que està naixent perquè aquesta escena no torni a passar. Del salt d'assistents de xat glorificats —als quals demanes un poema o una funció— a **fàbriques de codi virtuals** amb desenes d'agents treballant en paral·lel, amb memòria persistent, prioritats calculades matemàticament i, ara, federació entre fàbriques. És la continuació natural del díptic sobre l'arnès d'agent dels episodis [017](/podcast-del-doctor/episodi/017-ia-que-s-escapa-per-no-ser-apagada) i [018](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): allà vam veure què és un arnès i per què cal; aquí veiem què passa quan l'arnès creix fins a convertir-se en una ciutat sencera.

## Temes tractats

- **La psicosi de context**: la limitació física dels models actuals. Intentar que una IA programi un projecte llarg amb només la memòria del xat és com construir un gratacels amb un mestre d'obres que té la memòria d'un peix daurat: cada cinc minuts torna a preguntar on són els plànols i quin era l'objectiu de l'edifici. A mesura que la finestra de context s'omple de codi i de logs d'errors, el model desenvolupa una mena de demència progressiva i oblida el principi de la conversa.

- **Per què Jira i els Markdown no serveixen**: un tiquet de Jira funciona perquè hi ha una cognició humana constant al darrere —un humà llegeix el títol i el seu cervell autocompleta tot el context del projecte. La màquina no pot fer això. I els documents plans (fitxers Markdown, llistes de tasques) es degraden de seguida quan diversos agents els manipulen: es trepitgen entre ells i s'esborren línies que no tocaven.

- **Beads (`bd`)**: el motor de memòria estructurada de Steve Yegge, pensat perquè l'entenguin els agents i no els humans. Cada tasca porta un **identificador únic i inalterable** (`bd-a3f8`) que fa de codi de barres, i les tasques s'enllacen amb dependències estrictes formant un **graf dirigit acíclic** (DAG): pots declarar que A bloqueja B, però mai no hi pot haver un bucle on B bloquegi A. La comanda `bd ready` respon la pregunta que un agent es fa constantment —«he acabat, què s'ha desbloquejat?»— i li serveix la feina següent mastegada.

- **Rigidesa estructural, creativitat a dins**: l'objecció òbvia és que un graf tan estricte mata precisament allò que fa útil un model de llenguatge. La resposta de l'episodi és que la rigidesa només serveix per mantenir l'edifici dret: l'arquitectura del sistema no pot ser vaga ni intuïtiva, ha de ser exacta. A dins de cada tasca, l'agent conserva tot el seu raonament lliure per escriure la millor funció possible.

- **El dilema de la base de dades**: Beads va començar amb fitxers JSON-L plans i SQLite, sincronitzats amb Git. Amb cinquanta agents fent canvis simultanis allò era un malson de **conflictes de fusió** constants: Git està pensat per a humans que editen fitxers diferents a velocitat humana, no per a cinquanta robots reescrivint-ho tot en mil·lisegons.

- **Dolt i els arbres Prolly**: la solució va ser migrar a Dolt, una base de dades relacional SQL amb la **semàntica de Git incorporada des del disseny**. Fa servir arbres Prolly (arbres B probabilístics) per fusionar **a nivell de cel·la** en comptes de línies de text, de manera que cent agents poden actualitzar l'estat del projecte alhora i la base de dades ho reconcilia sense errors. A sobre hi ha un mode servidor per centralitzar-ho i un **mode furtiu** per no embrutar els repositoris humans amb els logs de la IA.

- **La dissidència**: no tothom hi està d'acord. A Hacker News, veus com la d'Alexander Holbridge critiquen que arrossegar una base de dades tan pesada com Dolt per gestionar les tasques d'un sol usuari o d'un equip petit és complexitat innecessària, un *vibe design* caòtic que ignora la practicitat. D'aquí han sortit reaccions minimalistes basades en YAML, SQL simple o Markdown pla.

- **L'usuari principal ja no és humà**: la resposta a aquella crítica és el gir més incòmode de l'episodi. Aquestes eines s'optimitzen per a codificadors robòtics, no per a nosaltres. A la IA li és igual que la base de dades sigui complexa de configurar; el que vol és que sigui matemàticament precisa i lliure de conflictes. La pregunta que queda és si estem desterrant els humans de la sala de màquines.

- **Gas Town i el seu repartiment de Mad Max**: l'orquestrador multiagent amb rols hiperespecífics. L'**alcalde** (Mayor) és la interfície on dones les instruccions, una mena de cap de gabinet. Les **mofetes** (Polecats) són els agents treballadors, els picapedrers del codi. El **diaca** (Deacon) patrulla en segon pla com un auditor, vigilant que ningú es quedi bloquejat. I el **testimoni** (Witness) evita les pèrdues de resposta i els bucles infinits.

- **El clown show**: coordinar tot aquest circ no va sortir bé d'entrada. Yegge ho descriu literalment com un *clown show*: hi havia pèrdues de dades constants i el diaca —que havia de ser l'auditor útil— es dedicava a assassinar processos de mofetes a mig fer perquè creia que s'havien penjat. La policia interna boicotejant l'empresa.

- **El mode sense límits**: l'experiment que Tim Sehn explica al blog de DoltHub. Quatre tests BATS per arreglar en paral·lel, cap límit posat, i una flota d'agents destruint el repositori a la velocitat de la llum fins que un `git reset --hard` d'emergència ho va aturar tot. Cent dòlars cremats en una hora.

- **L'alcalde ben ajustat**: la comparació que fa l'episodi és reveladora. Els assistents de codificació actuals són aquell company de feina intens que t'envia murs de text i et fa validar cada línia; esgoten perquè exigeixen supervisió absoluta. L'alcalde de Gas Town, en canvi, absorbeix tot el soroll de la fàbrica —les mofetes, el diaca, els drames— i se't presenta tranquil·lament a dir-te que la base de dades ja està arreglada.

- **El cicle MEW**: *molecular expression of work*. Les idees comencen com a **fórmules** (ordres generals), passen a **protos** mentre se'n defineixen els requisits i acaben com a **molècules**: tasques prou concretes perquè una mofeta les executi i piqui codi.

- **PageRank per prioritzar codi**: el Beads Viewer (`bdv`) de Jeffrey Emanuel és una TUI que corre a 60 fotogrames per segon a la terminal i aplica mètriques de xarxa al graf de dependències. Fa servir **el mateix PageRank que Google va inventar per ordenar la web**: si completar una tasca desbloqueja moltes branques del projecte, aquella tasca rep una puntuació alta i es converteix en la prioritat absoluta. També fa servir la **intermediació** (*betweenness*) per detectar el camí crític, i orquestradors superiors com Ralph TUI consumeixen la seva API per llançar èpics massius en paral·lel.

- **Portes humanes**: la matemàtica freda del graf no entén de campanyes de màrqueting ni de pressions comercials. Per això el sistema deixa **gates**, vàlvules d'emergència manuals que aturen el desplegament fins que algú prem el botó. Un cop premut, la màquina reprèn la velocitat de creuer tota sola.

- **La llicenciada en comunicació**: l'anècdota que Yegge explica com a mostra de la democratització de la creació. Una noia amb quatre anys d'experiència laboral i sense cap coneixement de programació va construir ella sola el substitut d'un SaaS car que feien servir, donant instruccions a l'alcalde de Gas Town. La barrera d'entrada ja no és saber sintaxi, sinó saber articular problemes lògicament.

- **Gas City i Wasteland**: amb Beads i Gas Town a la v1.0.0 i Beads passant de les vint mil estrelles a GitHub, arriba Gas City: si Gas Town és una fàbrica tancada i preconfigurada, Gas City és un SDK modular per muntar-te el teu propi orquestrador. I **Wasteland** és el concepte més trencador: una xarxa de federació que connecta milers de Gas Towns, una internet exclusiva per a màquines on un orquestrador saturat pot **subcontractar feina a flotes d'agents remotes** i fusionar-ne el resultat sense que tu hi intervinguis. Fàbriques virtuals negociant entre elles per preu i velocitat en temps real: capitalisme algorítmic.

- **Reflexió final**: si els agents ja tenen memòria, pressupost, gràfics de dependències i autoritat per repartir tasques logístiques a través de xarxes federades, quant trigarem a veure una empresa on l'alcalde virtual detecti colls d'ampolla **en el món físic** i, sol, assigni tasques directives, obri tiquets i posi terminis als empleats humans? En quin punt exacte deixem de ser els orquestradors i passem a ser les mofetes de la seva fàbrica d'eficiència?

## Episodis relacionats

- [Episodi 017: La IA que s'escapa per no ser apagada](/podcast-del-doctor/episodi/017-ia-que-s-escapa-per-no-ser-apagada) — l'autoreplicació dels models i el naixement del concepte d'arnès d'agent.
- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real) — els quatre pilars de l'arnès, l'ansietat de context i la victòria prematura, que aquí veiem multiplicades per cinquanta agents alhora.

## Fonts

- [Beads — documentació oficial](https://beads.gascity.com/) — Concepte, dependències, execució conscient del graf, fórmules i gates
- [gastownhall/beads](https://github.com/gastownhall/beads) — Codi font, model de dades sobre Dolt i comandes `bd`
- [Gas Town Hall](https://gastownhall.ai) — Hub de la comunitat, anuncis de la v1.0.0 i de Gas City
- [gastownhall/gastown](https://github.com/gastownhall/gastown) — Codi font de l'orquestrador multiagent i els seus rols
- [Wasteland](https://wasteland.gastownhall.ai/) — Tauler federat de coordinació entre Gas Towns
- [Dicklesworthstone/beads_viewer](https://github.com/Dicklesworthstone/beads_viewer) — TUI amb PageRank i camí crític sobre el graf de dependències
- [DoltHub Blog](https://www.dolthub.com/blog/) — L'experiment del mode sense límits i el funcionament de Dolt
- [Steve Yegge — blog](https://steve-yegge.blogspot.com/) — Assajos del creador de Beads i Gas Town
- [Technology Radar — Thoughtworks](https://www.thoughtworks.com/radar) — Context del panorama d'orquestració multiagent
- [Transcripció automàtica](/podcast-del-doctor/sources/019-fabriques-d-agents-que-programen-sols-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3) i corregida després en els noms propis i termes tècnics

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
