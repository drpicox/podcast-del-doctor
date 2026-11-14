---
audio_file: "https://archive.org/download/podcast-del-doctor-043-principis-d-enginyeria-per-a-agents-ia/043-principis-d-enginyeria-per-a-agents-ia.mp3"
audio_size: 7529499
chapters_file: "043-principis-d-enginyeria-per-a-agents-ia-chapters.json"
date: '2026-11-14'
description: "Detectes que l'agent s'oblida d'aplicar un descompte obligatori per llei una de cada 50 converses, i el primer instint és escriure-ho en majúscules al prompt: just la resposta que et fa suspendre. Segon de tres episodis sobre l'examen Claude Certified Architect – Foundations (CCAR-F), ara des de l'ull del programador clàssic: deu principis d'enginyeria convertits en paranys. El hook en lloc del prompt, la sessió desfasada que cal tornar a començar, la factura que no quadra i no s'arregla en silenci, el client enfadat que no cal escalar, el 95% de confiança que no prova res i la recepta de cuina contra la investigació policial."
duration: '15:41'
episode_number: 43
season: 1
soundbite_start: 574.2
soundbite_duration: 75.0
soundbite_title: "La factura que no quadra: per què arreglar-la en silenci amb Tipp-Ex et fa suspendre"
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
  url: "/podcast-del-doctor/sources/043-principis-d-enginyeria-per-a-agents-ia-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Claude, l'agent, la IA, PreToolUse, hub-and-spoke, few-shot, JSON, Tipp-Ex)"
thumbnail: "/assets/thumbnails/043-principis-d-enginyeria-per-a-agents-ia.png"
title: "Episodi 043: Principis d'enginyeria per a agents d'IA, quan l'instint de programador et fa suspendre"
---

## Introducció

Durant dècades, programar s'assemblava a construir un rellotge suís: escrius «fes A i després B» i la màquina ho fa, sense preguntes. Si alguna cosa petava, era un error de sintaxi o una variable mal definida. Era un món determinista i previsible. Amb els agents d'IA generativa, aquell rellotge de sobte s'assembla més a un organisme viu, que interpreta el que li demanes. I aquí hi ha el problema: molts dels reflexos que un bon programador ha après durant anys (escriure l'ordre més clara, passar-li-ho tot, arreglar les anomalies en silenci perquè res no peti) són exactament les respostes equivocades.

Aquest és el segon de tres episodis sobre la certificació **Claude Certified Architect – Foundations** (CCAR-F), l'examen d'Anthropic per a qui dissenya aplicacions de producció amb Claude. El primer, l'[Episodi 042: Agents d'IA autònoms i segurs, deixar-los pensar i lligar-los curt](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs), mirava els mateixos deu principis des de l'equilibri entre llibertat i baranes, i també hi trobareu les dades oficials de l'examen (format, escenaris, nota d'aprovat i pes de cada domini). El tercer de la sèrie és «Arquitectura de sistemes amb Claude».

Aquest episodi els recorre des de l'ull del programador clàssic. Cada principi arriba amb un cas pràctic d'examen, l'opció que l'instint et fa triar i la que és correcta. L'avís de partida és que, si véns de models petits, potser creus que cal escriure guions rígids, i la guia demana tot el contrari: donar objectius a un model capaç i blindar només el que és crític. Els deu principis són la manera com l'episodi ordena el temari, no una llista de la guia oficial; les respostes, en canvi, segueixen el que diu la guia.

## Temes tractats

- **Principi 1. El parany del prompt en majúscules**: un agent d'atenció al client s'oblida, en una de cada 50 converses, d'aplicar un descompte que és obligatori per llei. L'instint és obrir el *system prompt* i escriure «APLICA SEMPRE EL DESCOMPTE», subratllat i repetit al final. És l'opció que sembla més ràpida i lògica, i és la incorrecta: les instruccions del prompt tenen una taxa d'error que no és zero, i si una regla té conseqüències legals o econòmiques, «gairebé sempre» no n'hi ha prou. La resposta és fer-la complir amb codi: una condició prèvia programada (*prerequisite gate*) o un hook `PreToolUse` que bloqueja l'acció abans que s'executi si la condició no es compleix. L'episodi ho atribueix a la dilució de l'atenció en converses llargues; la guia no entra en el mecanisme, només constata que el compliment per prompt és probabilístic. L'analogia del cartell de la discoteca i el porter ja la vam explicar a l'[Episodi 042](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs), i la manca de determinisme com a verí per a l'enginyeria, a l'[Episodi 012: L'especificació és el nou codi](/podcast-del-doctor/episodi/012-especificacio-nou-codi).

- **Principi 2. El parany de la microgestió**: si la seguretat la fa el porter, com es tracta la intel·ligència del model? Com un enginyer sènior acabat de fitxar. A un sènior no li dius «clica aquí, obre aquest enllaç i copia el segon paràgraf», perquè el dia que la informació és al quart enllaç el guió falla. La guia demana prompts amb objectius i criteris de qualitat en lloc d'instruccions pas a pas, criteris explícits en lloc de consignes vagues, i dos a quatre exemples *few-shot* que mostrin per què es tria una acció i no una altra en els casos ambigus. És l'altitud justa del prompt de l'[Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia).

- **Principis 3 i 4. El parany de donar-li-ho tot**: l'instint diu que, si ha de decidir bé, li has de passar tots els manuals i tots els historials. L'episodi en diu el mite de l'omnisciència. D'una banda, l'API no té estat: cada petició ha de portar tota la conversa, i el que no li passes no existeix. De l'altra, si els models poden llegir milers de pàgines, per què preocupar-se per l'espai? Perquè el problema no és la mida de la finestra de context, sinó el soroll: en entrades llargues, el que queda al mig es pot perdre (*lost in the middle*). Per això la guia demana retallar els resultats de les eines als camps rellevants i guardar els valors exactes en un bloc de fets del cas (*case facts block*), fora del resum. Ja en parlàvem a l'[Episodi 007: Com domar el geni trampós](/podcast-del-doctor/episodi/007-com-domar-el-geni-trampos), amb l'amnèsia digital i la conversa que es podreix.

- **La sessió desfasada**: un desenvolupador vol reprendre una sessió d'exploració de codi, però des de llavors han canviat gairebé tots els fitxers. L'opció temptadora és reprendre l'historial antic «perquè ja té tot el context». Error: l'agent dona per bones les lectures velles, no torna a llegir els fitxers i acaba escrivint codi sobre estructures que ja no existeixen. La guia diferencia els dos casos. Si el context antic encara és vàlid en bona part, es reprèn la sessió (`--resume`) i se li diu quins fitxers han canviat. Si els resultats de les eines han quedat desfasats, és més fiable començar una sessió nova amb un resum estructurat del que encara és vàlid. És l'analogia de la mudança: no t'emportes els mobles trencats, sinó la llista del que vols conservar.

- **Principis 5 i 7. El parany del telèfon espatllat**: si no ho podem posar tot en un sol context, cal un sistema multiagent, i coordinar-lo sense que les dades es deformin de mà en mà. L'arquitectura *hub-and-spoke* posa un coordinador al centre de la roda. Decideix quins subagents calen segons la consulta, reparteix la feina i en revisa el resultat, però no fa la feina feixuga. Els subagents no parlen entre ells: tot passa pel coordinador. I el que pugen ha d'arribar en traspassos estructurats, no en tres paràgrafs de text lliure. La guia hi afegeix el detall que manté la traçabilitat: cada afirmació, lligada a la seva font (URL, document, extracte i data). Ho vam veure en detall a l'[Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude).

- **Principi 6. El parany d'arreglar-ho en silenci**: és el que més xoca amb l'ofici de programador, acostumat a polir anomalies perquè el programa no peti. Una factura escanejada diu que el total és de 1.000 euros, però les línies sumen 950. Hi ha tres opcions netes i boniques, i totes tres són distractors. Una és forçar la suma i guardar 950, una altra fer la mitjana salomònica de 975, i la tercera retornar un èxit amb el cos buit perquè la cadena no s'aturi. La resposta correcta és guardar els dos valors per separat (el total imprès i el calculat), marcar el conflicte i enviar la factura a revisió humana. La guia ho anomena `stated_total` i `calculated_total`, amb un booleà `conflict_detected`, i recorda que un esquema JSON estricte elimina els errors de sintaxi però no els semàntics, com unes línies que no sumen el total. L'analogia és el comptable que no passa Tipp-Ex per quadrar els números.

- **Principi 9. El parany de l'empatia**: un usuari escriu tot en majúscules, amb mil exclamacions. La temptació és escalar-lo de seguida a un humà per apagar el foc. Fals: la frustració, per si sola, no és motiu per escalar, i la guia adverteix que l'anàlisi de sentiment és un mal indicador de la complexitat real d'un cas. Si el problema és senzill, l'agent reconeix el malestar i ofereix la solució, i només escala si el client insisteix a parlar amb una persona. Els disparadors vàlids són tres: que el client demani explícitament un humà, que la política no cobreixi el cas i que l'agent no pugui avançar.

- **Principi 10. El parany de la confiança declarada**: el model diu que està segur al 95% de les seves extraccions. Ja es pot deixar de revisar? Encara no. Aquell número no prova res fins que no l'has contrastat amb un conjunt de validació que algú ja ha etiquetat, i amb això es calibren els llindars que decideixen què revisa una persona. Compte també amb la precisió global (*aggregate accuracy*): una xifra molt alta pot amagar un tipus de document que falla molt més sovint. L'episodi ho il·lustra amb un 99% en què l'1% que falla són justament els contractes legals; la guia en posa d'exemple un 97%. Per això demana desglossar la precisió per tipus de document i per camp abans de reduir la revisió humana, i mantenir un mostreig aleatori estratificat continu dels casos automatitzats.

- **Principi 8. Recepta de cuina o investigació policial**: l'episodi el deixa per al final perquè hi pivota tota l'arquitectura. Si la feina és previsible i en coneixes els passos, una cadena fixa (*prompt chaining*): pas 1, pas 2, com una recepta. Si cada descoberta canvia el pas següent, com quan investigues per què ha caigut un servidor, una descomposició dinàmica i adaptativa, en què l'agent replanifica a cada pista. La guia en posa d'exemples les revisions per aspectes o per fitxer, d'una banda, i afegir tests a un codi heretat sense documentació, de l'altra. És la distinció entre fluxos de treball i agents de l'[Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius).

- **Reflexió final**: construir sistemes d'IA eficaços ja no va d'escriure prompts màgics que semblin conjurs, sinó de dissenyar arquitectures en què el codi fixa les barreres innegociables i el model aporta la flexibilitat per pensar, sense amagar res. La pregunta que deixa l'episodi: si passem de programar cada tecla a donar objectius a una entitat amb criteri, i el nostre codi només fa de mur de contenció, en quin moment el desenvolupador deixa de ser un constructor de màquines per convertir-se en un legislador de polítiques per a intel·ligències digitals? La idea ressona amb els directors d'orquestra de l'[Episodi 004: Domar la IA per programar amb precisió](/podcast-del-doctor/episodi/004-domar-ia-precisio).

## Episodis relacionats

- [Episodi 042: Agents d'IA autònoms i segurs, deixar-los pensar i lligar-los curt](/podcast-del-doctor/episodi/042-disseny-d-agents-ia-autonoms-i-segurs): el primer de la sèrie sobre el CCAR-F, els mateixos deu principis vistos com a llibertat amb baranes, i les dades oficials de l'examen.
- [Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius): l'article *Building effective agents*, la diferència entre fluxos de treball i agents, i els hooks com a garantia.
- [Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia): el context com a recurs escàs, l'altitud justa del prompt i la compactació.
- [Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude): el coordinador amb subagents i la selecció segons la complexitat de la consulta.
- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): el control determinista com a pilar de l'arnès i el reinici net.
- [Episodi 033: El xassi dels agents d'IA](/podcast-del-doctor/episodi/033-infraestructura-agents-ia): les eines i els guardrails vistos des de la documentació d'AWS.
- [Episodi 012: L'especificació és el nou codi](/podcast-del-doctor/episodi/012-especificacio-nou-codi): per què la manca de determinisme dels models és un verí per a l'enginyeria de programari.
- [Episodi 007: Com domar el geni trampós](/podcast-del-doctor/episodi/007-com-domar-el-geni-trampos): l'amnèsia digital i la conversa que es podreix.
- [Episodi 004: Domar la IA per programar amb precisió](/podcast-del-doctor/episodi/004-domar-ia-precisio): de creadors de codi a directors d'orquestra d'agents.

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

- [Transcripció automàtica](/podcast-del-doctor/sources/043-principis-d-enginyeria-per-a-agents-ia-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
