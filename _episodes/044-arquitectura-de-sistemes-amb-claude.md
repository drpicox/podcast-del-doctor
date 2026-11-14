---
audio_file: "https://archive.org/download/podcast-del-doctor-044-arquitectura-de-sistemes-amb-claude/044-arquitectura-de-sistemes-amb-claude.mp3"
audio_size: 5830077
chapters_file: "044-arquitectura-de-sistemes-amb-claude-chapters.json"
date: '2026-11-14'
description: "Un agent que s'oblida d'un descompte obligatori, una recerca simple que costa un dineral, una factura que no quadra i una exploració de codi que col·lapsa el context. Tercer i últim episodi sobre l'examen Claude Certified Architect – Foundations (CCAR-F), ara com un simulacre d'examen amb una examinadora implacable, on cada solució obre el problema següent: el hook que deixa lliure l'agent, el coordinador que tria i reparteix subagents que comencen en blanc, l'allau d'alertes que es filtra amb confiança calibrada, el CLAUDE.md del projecte, l'exploració aïllada i la regla de desempat: guanya el mecanisme natiu de Claude."
duration: '12:08'
episode_number: 44
season: 1
soundbite_start: 199.0
soundbite_duration: 64.1
soundbite_title: "Massa lent, massa car i subagents que es trepitgen: el coordinador que tria i reparteix la feina"
sources:
- title: "Claude Certified Architect – Foundations: Exam Guide (v1.0)"
  url: "https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf"
  description: "Guia oficial de l'examen CCAR-F (juliol de 2026): format, els sis escenaris, els cinc dominis amb el seu pes i les tasques avaluades, com els hooks que bloquegen reemborsaments per sobre d'un llindar, els disparadors d'escalada i la confiança calibrada amb dades etiquetades"
- title: "Claude Certified Architect – Foundations Certification"
  url: "https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification/486716"
  description: "Pàgina oficial de la certificació a Skilljar (pot demanar inici de sessió)"
- title: "Claude Certified Architect – Foundations: sol·licitud d'accés"
  url: "https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request"
  description: "Pàgina d'Anthropic per demanar accés a l'examen de certificació"
- title: "Introduction to subagents (Anthropic Academy)"
  url: "https://anthropic.skilljar.com/introduction-to-subagents"
  description: "Curs d'Anthropic sobre com fer servir i crear subagents a Claude Code per gestionar el context i delegar tasques"
- title: "Extensibility (Anthropic Academy)"
  url: "https://anthropic-partners.skilljar.com/extensibility-course"
  description: "Curs d'Anthropic sobre com ampliar Claude Code amb servidors MCP, skills, hooks, subagents i plugins"
- title: "Building with the Claude API (Anthropic Academy)"
  url: "https://anthropic.skilljar.com/claude-with-the-anthropic-api"
  description: "Curs d'Anthropic sobre l'API de Claude: missatges, ús d'eines, sortida estructurada i patrons de treball amb els models"
- title: "How we built our multi-agent research system"
  url: "https://www.anthropic.com/engineering/multi-agent-research-system"
  description: "Article d'enginyeria d'Anthropic sobre el sistema de recerca multiagent de Claude: el coordinador que reparteix la feina entre subagents, la selecció segons la complexitat de la consulta i la recuperació després d'errors"
- title: "Effective context engineering for AI agents"
  url: "https://anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  description: "Article d'enginyeria d'Anthropic sobre el context com a recurs escàs: l'altitud justa del prompt, els exemples, la compactació, les notes estructurades i els subagents"
- title: "Building effective agents"
  url: "https://www.anthropic.com/engineering/building-effective-agents"
  description: "Article d'enginyeria d'Anthropic sobre fluxos de treball i agents: l'encadenament d'instruccions, l'orquestrador amb treballadors i quan val la pena fer un agent"
- title: "paullarionov/claude-certified-architect"
  url: "https://github.com/paullarionov/claude-certified-architect"
  description: "Material de la comunitat (no oficial): guia d'estudi i preguntes de pràctica per a la certificació. Pot contenir errors"
- title: "Claude Certified Architect – Practice Tests: Study guide"
  url: "https://claude-certified-architect-practice-tests.pages.dev/docs/study_guide.html"
  description: "Material de la comunitat (no oficial): guia d'estudi d'un lloc de tests de pràctica. Pot contenir errors"
- title: "Passing the Claude Certified Architect Exam: Ten Days, Three Practice Runs (Very Good Ventures)"
  url: "https://verygood.ventures/blog/passing-the-claude-certified-architect-exam/"
  description: "Material de la comunitat (no oficial): experiència d'un enginyer de Very Good Ventures preparant i aprovant l'examen. Pot contenir errors"
- title: "How I Passed the Claude Certified Architect Exam (CCAR-F) (Yu Wenhao)"
  url: "https://yu-wenhao.com/en/blog/ccar-f-exam-experience/"
  description: "Material de la comunitat (no oficial): experiència de primera mà amb l'examen, què avalua i com preparar-lo. Pot contenir errors"
- title: "Lessons from the Anthropic Architect exam (IT One)"
  url: "https://itone.substack.com/p/lessons-from-the-anthropic-architect"
  description: "Material de la comunitat (no oficial): fets i mites sobre l'examen. Pot contenir errors"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/044-arquitectura-de-sistemes-amb-claude-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Claude, CCAR-F, l'agent, la IA, CLAUDE.md, PreToolUse, hub-and-spoke, context: fork, Explore, plan mode, logprobs, JSON, Tipp-Ex) i un fragment inintel·ligible marcat com a tal"
thumbnail: "/assets/thumbnails/044-arquitectura-de-sistemes-amb-claude.png"
title: "Episodi 044: Arquitectura de sistemes amb Claude, un simulacre d'examen on cada solució obre un problema nou"
---

## Introducció

En el programari de tota la vida, poses un *if* i el programa fa una cosa; poses un *else* i en fa una altra. O funciona o et dona un error a la cara, i això dona molta tranquil·litat. Quan dissenyes sistemes amb models com Claude, aquell control absolut desapareix: canvies un camí de ferro per un terreny obert, i cedeixes el microcontrol a canvi d'una capacitat de raonament enorme. Molts dissenyadors s'hi estavellen perquè continuen tractant la IA com si fos codi antic.

Aquest és el tercer i últim episodi de la sèrie sobre la certificació **Claude Certified Architect – Foundations** (CCAR-F), l'examen d'Anthropic per a qui dissenya aplicacions de producció amb Claude. Tots tres parteixen de les mateixes fonts i dels mateixos deu principis, que són la manera com la sèrie ordena el temari, no una llista de la guia oficial. L'[Episodi 042: Agents d'IA autònoms i segurs, deixar-los pensar i lligar-los curt](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs) els mirava com un equilibri entre llibertat i baranes, i és on trobareu les dades oficials de l'examen (format, escenaris, nota d'aprovat i pes de cada domini). L'[Episodi 043: Principis d'enginyeria per a agents d'IA, quan l'instint de programador et fa suspendre](/podcast-del-doctor/episodi/043-principis-d-enginyeria-per-a-agents-ia) els convertia en paranys per al programador clàssic. Aquest els mira com a **arquitectura de sistemes**: com encaixen les peces quan l'agent ja no treballa sol.

El format també canvia. És un simulacre d'examen en directe, amb un alumne que respon i una examinadora implacable que el suspèn a la primera. Són quatre preguntes de quatre dels sis escenaris (atenció al client, recerca multiagent, extracció de dades estructurades i Claude Code), i el fil que les lliga és que cada solució obre el problema següent: el hook allibera l'agent, l'agent lliure necessita un coordinador amb subagents, els subagents comencen en blanc, i marcar cada discrepància inunda els humans d'alertes. Les respostes segueixen la guia oficial; on l'àudio se n'aparta, ho indiquem.

## Temes tractats

- **El mètode dels cinc passos**: abans de respondre, l'alumne fa servir un mètode per llegir les preguntes. És un consell d'estudi de l'episodi, no de la guia. Primer, situar-se: quin escenari és i de quina capa parla (l'API, l'Agent SDK, Claude Code o el disseny del prompt). Després, llistar tots els símptomes, mirar què ja s'ha provat, saber què pot fer i què no cada mecanisme, i buscar la paraula que decideix la resposta (*first*, *immediate*, *most reliable*...). Les opcions que només arreglen un dels símptomes, o que proposen més del mateix que ja ha fallat, solen ser distractors.

- **Pregunta 1. Atenció al client: el porter que dona llibertat a l'agent**: l'agent s'oblida d'aplicar un descompte obligatori per llei en una de cada 50 converses. L'alumne fa el que faria tothom: escriure-ho en majúscules al *system prompt* i repetir-ho al principi i al final. Suspès. Les instruccions del prompt tenen una taxa d'error que no és zero, i quan hi ha conseqüències legals la regla s'ha de fer complir amb codi (*programmatic enforcement*): una condició prèvia programada (*prerequisite gate*) o un hook `PreToolUse` que intercepta la crida de Claude abans que s'executi. L'analogia del cartell de la discoteca i el porter ja la vam explicar a l'[Episodi 042](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs), i el parany del prompt en majúscules, a l'[Episodi 043](/podcast-del-doctor/episodi/043-principis-d-enginyeria-per-a-agents-ia). La lectura d'arquitecte és la frase amb què l'examinadora tanca la pregunta: com que les línies vermelles les garanteix el codi, a l'agent se li pot donar llibertat per a tota la resta. Les baranes no són el contrari de l'autonomia, sinó el que la fa possible.

- **Pregunta 2. Recerca multiagent: dos símptomes, dues peces**: en un sistema de recerca, una consulta simple triga massa i costa un dineral, i en les complexes els subagents acaben trobant la mateixa informació. Aquí el mètode es nota: hi ha dos símptomes, i la resposta ha d'arreglar-los tots dos. El coordinador de l'arquitectura *hub-and-spoke*, per on passa tota la comunicació, fa dues coses. D'una banda, una selecció dinàmica: analitza la consulta i crida només els subagents que calen segons la complexitat, en lloc de passar sempre per tot el circuit. De l'altra, parteix l'abast: cada subagent rep un subtema o un tipus de font diferent, perquè no se solapin. És un cap de projecte que no programa, però reparteix la feina i la revisa. L'article d'Anthropic sobre el seu sistema de recerca en diu ajustar l'esforç a la complexitat de la consulta, i el vam veure a l'[Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude). El patró de l'orquestrador amb treballadors ja sortia a l'[Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius).

- **La complicació: subagents que comencen en blanc**: cada solució porta un problema nou. Si el coordinador envia un subagent esperant que recordi una decisió presa a l'inici de la sessió, s'equivoca: l'API no té estat i els subagents no hereten el context del coordinador. Són un *freelance* que entra avui al projecte, i el que no li passis explícitament al prompt en invocar-lo, no ho sap. Però passar-li tota la conversa per si de cas tampoc no funciona, perquè en contextos llargs el que queda al mig es perd (*lost in the middle*). A l'àudio, la resposta és un bloc de fets del cas amb les dades clau al principi del prompt del subagent. La guia hi arriba per dos camins. Als subagents se'ls passa explícitament el que necessiten (els resultats previs, amb les seves metadades), i el resum de les troballes clau va al principi, amb seccions ben titulades. El bloc de fets del cas (*case facts block*) és, en canvi, la seva eina per a les converses llargues, on guarda imports, dates i números de comanda fora de l'historial resumit. Ho vam desenvolupar a l'[Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia).

- **Pregunta 3. Extracció de dades: la factura que no quadra**: el total imprès diu 1.000 euros i les línies sumen 950. L'alumne vol una solució neta que no trenqui l'esquema JSON: que el model endevini quin dels dos és el bo, o que sobreescrigui el total amb la suma. Error crític: les contradiccions també són informació. Es guarden el total imprès (`stated_total`) i el calculat (`calculated_total`) per separat, amb un booleà `conflict_detected` que marca la discrepància. És el comptable que no passa Tipp-Ex de l'[Episodi 043](/podcast-del-doctor/episodi/043-principis-d-enginyeria-per-a-agents-ia).

- **L'allau d'alertes**: aquí arriba l'objecció més interessant de l'episodi, i la més d'arquitecte. Si marquem cada discrepància i cada dubte, un equip humà ho haurà de revisar tot, i llavors quina automatització és aquesta? La resposta combina mesurar abans de fiar-se'n i escalar només quan toca. No es fa cas de la confiança que el model declara: els llindars es calibren amb un conjunt de casos que algú ja ha etiquetat. El que queda per sobre s'automatitza, i els documents amb poca confiança, ambigus o contradictoris van a una persona, amb un resum estructurat perquè no hagi de llegir-s'ho tot. Ni amb una precisió global altíssima es deixa de controlar, perquè la mitjana pot amagar un tipus de document o un camp que falla molt més. Per això cal desglossar-la i mantenir un mostreig aleatori estratificat continu. Tres precisions sobre l'àudio. Parla de calibrar les *logprobs* (les probabilitats internes del model), mentre que la guia parla de puntuacions de confiança per camp que el model retorna i que es calibren amb dades etiquetades. Posa d'exemple un 99,5% de precisió global, i la guia, un 97%. I no hi ha cap llindar a partir del qual «el model ja no falla»: el llindar marca fins on la taxa d'error és acceptable, i per això el mostreig no s'atura mai. El buit de política que també esmenta és un disparador d'escalada de l'agent d'atenció al client, no de l'extracció de dades.

- **Pregunta 4. Claude Code: on viuen les regles i on es fa la feina sorollosa**: un equip vol convencions per a tot el repositori, i un desenvolupador vol que Claude investigui un problema amagat al codi, una exploració que generarà desenes de milers de paraules. Les convencions d'equip van al `CLAUDE.md` del projecte (a l'arrel o a `.claude/CLAUDE.md`), versionat amb el repositori, i no al `~/.claude/CLAUDE.md` de l'usuari, que és personal i no arriba als companys. La guia hi afegeix la resta de la jerarquia: `CLAUDE.md` per directori, `@import` per incloure fitxers d'estàndards i `.claude/rules/` amb patrons de rutes per a les convencions que depenen del tipus de fitxer. L'exploració sorollosa s'aïlla en un altre context, amb el subagent Explore o amb una skill que porti l'opció `context: fork` al frontmatter (l'àudio en diu «comandament», però és una opció de configuració de la skill). La feina es fa en una branca a part i a la conversa principal només hi torna el resum net, de manera que no es degrada la memòria de disseny. L'àudio ho penja del principi 8 (fix o dinàmic), però és sobretot una qüestió de context escàs, el principi 4. La separació entre regles permanents al `CLAUDE.md` i procediments a demanda en skills ja sortia a l'arnès de set capes de l'[Episodi 039](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius).

- **El desempat: guanya el mecanisme natiu**: l'últim secret de l'examinadora és una regla per desempatar, que també és un consell de l'episodi i no una norma oficial. Quan dues opcions semblen viables, sol guanyar la que fa servir el mecanisme de Claude pensat per a aquell problema, en lloc de reinventar la roda amb prompts llarguíssims. Per a canvis grans amb decisions d'arquitectura, el *plan mode*, perquè el model explori i planifiqui abans de tocar res (la guia en posa d'exemples reestructurar microserveis o una migració de biblioteca que afecta més de 45 fitxers), i execució directa per als canvis petits i ben delimitats. Per a feina previsible amb passos coneguts, *prompt chaining*: encadenar sortides en lloc de muntar un agent complex. L'àudio hi posa d'exemple una llista llarga i repetitiva, com unes traduccions; la guia l'il·lustra amb revisions de codi dividides en passos (cada fitxer per separat i després una passada d'integració), i per a molts documents independents que no corren pressa també té la Message Batches API, un 50% més barata. L'àudio diu que el mecanisme natiu «sempre mana»; és més aviat una tendència que ajuda a decidir.

- **Reflexió final**: dissenyar sistemes amb Claude no va d'escriure guions rígids, sinó de donar objectius clars, com a un enginyer sènior, protegir els límits legals amb codi que intercepta les crides i estructurar molt bé com passa la informació d'un agent a un altre perquè no hi hagi amnèsia. És la diferència entre qui només xateja amb la IA i qui construeix sistemes que no al·lucinen ni trenquen les dades de producció. La pregunta que queda oberta: si els orquestradors dinàmics acaben creant els seus propis subagents sense demanar permís, i decideixen pel seu compte que el context humà inicial ja no és rellevant per resoldre el problema, qui audita l'auditor? Tanca la sèrie al costat de les preguntes dels dos episodis anteriors: el directiu humà convertit en coll d'ampolla de l'[Episodi 042](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs) i el desenvolupador convertit en legislador de l'[Episodi 043](/podcast-del-doctor/episodi/043-principis-d-enginyeria-per-a-agents-ia). I ressona amb les flotes d'agents que fusionen codi a velocitat inhumana de l'[Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols).

## Episodis relacionats

- [Episodi 042: Agents d'IA autònoms i segurs, deixar-los pensar i lligar-los curt](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs): el primer de la sèrie sobre el CCAR-F, els deu principis vistos com a llibertat amb baranes, i les dades oficials de l'examen.
- [Episodi 043: Principis d'enginyeria per a agents d'IA, quan l'instint de programador et fa suspendre](/podcast-del-doctor/episodi/043-principis-d-enginyeria-per-a-agents-ia): el segon de la sèrie, els mateixos principis convertits en paranys per al programador clàssic.
- [Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude): el coordinador amb subagents, l'esforç ajustat a la complexitat de la consulta i el telèfon espatllat.
- [Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia): el context com a recurs escàs i els subagents que tornen només un resum condensat.
- [Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius): fluxos de treball contra agents, els hooks com a garantia i l'arnès de set capes de Claude Code.
- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): agent = model + arnès, i el control determinista com a pilar.
- [Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols): què passa quan una flota d'agents treballa sense ningú que la revisi.
- [Episodi 033: El xassi dels agents d'IA](/podcast-del-doctor/episodi/033-infraestructura-agents-ia): les eines i els guardrails vistos des de la documentació d'AWS.
- [Episodi 004: Domar la IA per programar amb precisió](/podcast-del-doctor/episodi/004-domar-ia-precisio): per què els superagents generalistes fallen, i de creadors de codi a directors d'orquestra d'agents especialitzats.

## Fonts

**Documentació oficial d'Anthropic**

- [Claude Certified Architect – Foundations: Exam Guide (v1.0)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf): guia oficial de l'examen (PDF, juliol de 2026)
- [Claude Certified Architect – Foundations Certification](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification/486716): pàgina de la certificació a Skilljar
- [Sol·licitud d'accés a l'examen](https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request): pàgina per demanar accés a la certificació
- [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents): curs d'Anthropic Academy sobre subagents a Claude Code
- [Extensibility](https://anthropic-partners.skilljar.com/extensibility-course): curs sobre MCP, skills, hooks, subagents i plugins
- [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api): curs sobre l'API de Claude
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system): article d'enginyeria d'Anthropic
- [Effective context engineering for AI agents](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents): article d'enginyeria d'Anthropic
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): article d'enginyeria d'Anthropic

**Material de la comunitat** (no oficial, pot contenir errors)

- [paullarionov/claude-certified-architect](https://github.com/paullarionov/claude-certified-architect): guia i preguntes de pràctica
- [Claude Certified Architect – Practice Tests: Study guide](https://claude-certified-architect-practice-tests.pages.dev/docs/study_guide.html): guia d'estudi
- [Very Good Ventures: Ten Days, Three Practice Runs](https://verygood.ventures/blog/passing-the-claude-certified-architect-exam/): experiència preparant l'examen
- [Yu Wenhao: CCAR-F exam experience](https://yu-wenhao.com/en/blog/ccar-f-exam-experience/): experiència de primera mà amb l'examen
- [IT One: Lessons from the Anthropic Architect exam](https://itone.substack.com/p/lessons-from-the-anthropic-architect): lliçons i mites sobre l'examen

**Transcripció**

- [Transcripció automàtica](/podcast-del-doctor/sources/044-arquitectura-de-sistemes-amb-claude-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
