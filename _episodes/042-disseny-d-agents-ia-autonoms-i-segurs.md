---
audio_file: "https://archive.org/download/podcast-del-doctor-042-disseny-d-agents-ia-autonoms-i-segurs/042-disseny-d-agents-ia-autonoms-i-segurs.mp3"
audio_size: 6561088
chapters_file: "042-disseny-d-agents-ia-autonoms-i-segurs-chapters.json"
date: '2026-11-14'
description: "Li dius a l'agent d'atenció al client que mai no faci reemborsaments grans, arriba un client furiós i n'autoritza un de 5.000 euros. Primer de tres episodis sobre l'examen Claude Certified Architect – Foundations (CCAR-F): com dissenyar agents que decideixin sols sense saltar-se les línies vermelles. Deu principis: les regles crítiques van al codi amb hooks, objectius en lloc de guions, el context que no li passes no existeix, traspassos estructurats, errors que no s'amaguen, un coordinador que reparteix i revisa, quan escalar a un humà i per què la confiança que declara el model no prova res."
duration: '13:40'
episode_number: 42
season: 1
soundbite_start: 125.5
soundbite_duration: 75.6
soundbite_title: "El cartell de la discoteca i el porter: per què les regles crítiques van al codi"
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
  url: "/podcast-del-doctor/sources/042-disseny-d-agents-ia-autonoms-i-segurs-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis i termes (Claude, CCAR-F, l'agent, la IA, PreToolUse, lost in the middle, case facts block)"
thumbnail: "/assets/thumbnails/042-disseny-d-agents-ia-autonoms-i-segurs.png"
title: "Episodi 042: Agents d'IA autònoms i segurs, deixar-los pensar i lligar-los curt"
---

## Introducció

Un agent d'atenció al client té una ordre escrita en majúscules: no facis mai reemborsaments per sobre d'un límit. Arriba un client furiós, amenaça amb demandes i l'agent, en el seu intent de calmar-lo, se salta l'ordre i autoritza un reemborsament de 5.000 euros. No és cap error estrany: un model de llenguatge és un motor probabilístic, i el que li demanes al prompt es compleix gairebé sempre, però no sempre. Dir-li «si us plau» o posar-ho en negreta no garanteix res quan hi ha diners en joc.

Aquest és el primer de tres episodis sobre la certificació **Claude Certified Architect – Foundations** (CCAR-F), l'examen d'Anthropic per a qui dissenya aplicacions de producció amb Claude. Tots tres parteixen de les mateixes fonts, però cadascun les mira des d'un angle diferent. Aquest se centra en el **disseny d'agents autònoms i segurs**: com donar a un agent prou llibertat per decidir sol i, alhora, lligar-lo curt allà on un error costa diners, té conseqüències legals o afecta la seguretat. L'episodi ordena el temari en deu principis. Els dos episodis següents de la sèrie són l'[Episodi 043: Principis d'enginyeria per a agents d'IA, quan l'instint de programador et fa suspendre](/podcast-del-doctor/episodi/043-principis-d-enginyeria-per-a-agents-ia) i l'[Episodi 044: Arquitectura de sistemes amb Claude, un simulacre d'examen on cada solució obre un problema nou](/podcast-del-doctor/episodi/044-arquitectura-de-sistemes-amb-claude).

Per situar-nos, segons la guia oficial (versió 1.0, de juliol de 2026), l'examen té 60 preguntes i dura 120 minuts. Planteja 4 escenaris triats a l'atzar d'entre 6 (un agent d'atenció al client, generació de codi amb Claude Code, un sistema de recerca multiagent, eines de productivitat per a desenvolupadors, Claude Code en integració contínua i extracció de dades estructurades), i s'aprova amb 720 punts sobre 1.000. Els cinc dominis són l'arquitectura agèntica i l'orquestració (27%), la configuració i els fluxos de Claude Code (20%), l'enginyeria de prompts i la sortida estructurada (20%), el disseny d'eines i la integració amb MCP (18%) i la gestió de context i la fiabilitat (15%).

## Temes tractats

- **1. Si ha de passar sempre, va al codi**: repetir la norma al prompt, en majúscules o al principi i al final, continua sent probabilístic. La guia de l'examen ho diu clar: quan cal un compliment determinista, les instruccions del prompt tenen una taxa d'error que no és zero. La regla s'ha de fer complir amb codi. Un *hook* intercepta la crida a l'eina abans que s'executi (a l'episodi, un `PreToolUse`), bloqueja el reemborsament que supera el llindar (la guia en posa d'exemple un de 500 dòlars) i deriva el cas a una persona. Una condició prèvia programada, per la seva banda, no deixa cridar `process_refund` fins que `get_customer` ha verificat el client. L'analogia de l'episodi: el prompt és el cartell de «Cal DNI» a la porta de la discoteca, i el hook és el porter. Des de Claude Code, ja ho dèiem a l'[Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius): una instrucció és una petició, i un hook és una garantia.

- **2. Objectius i el perquè, no un guió**: si ho programem tot amb *if* i *else*, tornem al programari rígid de sempre. Fora de les línies vermelles, un model capaç es tracta com un enginyer sènior: objectius clars, criteris de qualitat i exemples *few-shot* que expliquin per què es va triar una acció i no una altra, perquè pugui aplicar el mateix criteri a casos que no ha vist mai. La guia demana prompts de coordinador amb objectius i criteris de qualitat en lloc d'instruccions pas a pas, i criteris explícits en lloc de consignes vagues com «sigues conservador». És l'altitud justa del prompt de l'[Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia). L'equilibri que proposa l'episodi és deixar-lo pensar i lligar-lo curt.

- **3. El que no és al context no existeix**: l'API no té estat. Cada petició ha de portar tota la conversa, i Claude no recorda res d'una crida a l'altra. Els subagents tampoc no hereten el context del coordinador, així que tot el que necessiten (l'objectiu, els fets i els resultats dels altres agents) els ho ha de passar explícitament al prompt. És com un contractista extern que entra avui a l'oficina: si no li fas el *briefing*, no sap res.

- **4. El context és escàs i es degrada**: en entrades llargues, els models processen bé el principi i el final però poden passar per alt el que queda al mig (*lost in the middle*), i els resums progressius arrodoneixen imports, percentatges i dates. La guia hi proposa diversos remeis. Un bloc de fets del cas (*case facts block*) guarda els valors exactes fora del resum. Els resultats de les eines es retallen als camps rellevants. Les conclusions clau van al principi, amb seccions ben titulades. I quan els resultats antics ja no són vàlids, és més fiable començar una sessió nova amb un resum estructurat que reprendre l'antiga. L'analogia de l'episodi és la mudança: no t'emportes els mobles trencats, sinó la llista del que vols conservar. En parlàvem a l'[Episodi 040](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia), i el reinici net ja sortia a l'[Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real).

- **5. Cada traspàs, estructurat**: com en un canvi de torn a l'hospital, qui rep la feina no té el teu context. Si l'agent escala a una persona, li passa un resum estructurat (client, causa, import i acció recomanada): la persona no té accés a la conversa, i així no ha de tornar a preguntar-ho tot. Si passa dades a codi, fa servir un esquema JSON amb *tool use*. I entre agents, cada afirmació va amb la seva font.

- **6. No amaguis el que ha passat**: «no he trobat res» no és el mateix que «no he pogut accedir a la base de dades». La guia separa els errors transitoris, que es poden reintentar, dels de validació, de negoci i de permisos, i demana retornar-los amb metadades estructurades. L'exemple de l'episodi és una factura amb un total imprès de 1.000 euros i unes línies que sumen 950. Un bon comptable no hi passa Tipp-Ex ni en fa la mitjana: guarda el total declarat i el calculat, marca el conflicte i ho envia a revisió humana. Els camps opcionals (*nullable*) a l'esquema eviten, a més, que el model s'inventi un valor per omplir un camp obligatori. La incertesa també és informació.

- **7. El coordinador decideix, reparteix i revisa**: en un sistema multiagent amb arquitectura *hub-and-spoke*, tota la comunicació passa pel coordinador, com els radis pel botó d'una roda. El coordinador no fa la feina dura. Tria quins subagents calen segons la complexitat de la consulta, reparteix l'abast perquè no es trepitgin i avalua l'esborrany. Si hi troba forats, torna a delegar cerques dirigides, en un bucle de refinament que dura fins que la cobertura és suficient. Per recuperar-se d'una caiguda, cada agent desa el seu estat en un lloc conegut, i en reiniciar el coordinador carrega un *manifest* amb aquest estat. Ho vam explicar en detall a l'[Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude).

- **8. Fix si és previsible, dinàmic si és obert**: si coneixes els passos abans de començar, una cadena fixa (*prompt chaining*), com una recepta de cuina. Si cada descoberta canvia el pas següent, una descomposició dinàmica, com una investigació policial en què cada pista reorienta el pla. És la distinció entre fluxos de treball i agents de l'[Episodi 039](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius).

- **9. Escala quan toca, i només quan toca**: la part més contraintuïtiva. La frustració del client no és, per si sola, un motiu per escalar. Si el problema és senzill, l'agent reconeix el malestar i ofereix la solució, i només escala si el client insisteix a parlar amb una persona. La guia marca tres disparadors: que el client demani explícitament un humà (llavors s'escala de seguida, sense investigar abans), que la política no cobreixi el cas (l'agent no s'inventa normes) i que l'agent no pugui avançar. També adverteix que l'anàlisi de sentiment i la confiança que declara el model són mals indicadors de la complexitat real d'un cas. I si una cerca torna tres clients amb el mateix nom, cal demanar un altre identificador, no triar-ne un a ull.

- **10. Abans de fiar-te'n, mesura**: quan el model diu que està segur al 95%, aquest número no prova res fins que no l'has contrastat amb un conjunt de validació etiquetat, com un termòmetre nou que primer compares amb un de bo. A més, una precisió global del 97% pot amagar un tipus de document que falla molt més sovint. La guia demana desglossar la precisió per tipus de document i per camp abans de reduir la revisió humana, mantenir un mostreig aleatori estratificat dels casos automatitzats i decidir què revisa una persona amb llindars de confiança calibrats.

- **Reflexió final**: estem passant de xatbots que resumeixen textos a agents autònoms que treballen dins de les empreses, i aquests deu principis marquen la diferència entre un experiment simpàtic i una eina professional. La pregunta que queda oberta: si els coordinadors d'IA arriben a delegar, revisar esborranys i desar el seu estat a la perfecció, en quin moment el directiu humà que aprova les decisions finals es converteix en el coll d'ampolla del procés?

## Episodis relacionats

- [Episodi 039: Com construir agents d'IA que acabin la feina](/podcast-del-doctor/episodi/039-com-construir-agents-ia-efectius): l'article *Building effective agents*, la diferència entre fluxos de treball i agents, i els hooks com a garantia.
- [Episodi 040: Enginyeria de context, l'art de no ofegar els agents d'IA](/podcast-del-doctor/episodi/040-enginyeria-de-context-per-a-agents-ia): el context com a recurs escàs, l'altitud justa del prompt, la compactació i les notes estructurades.
- [Episodi 041: Recerca multiagent, l'agència de detectius de Claude](/podcast-del-doctor/episodi/041-sistema-de-recerca-multiagent-de-claude): el coordinador amb subagents, la selecció segons la complexitat i la recuperació després d'errors.
- [Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real): el control determinista com a pilar de l'arnès i per què de vegades cal un reinici net.
- [Episodi 025: L'IA no pot desfer la realitat](/podcast-del-doctor/episodi/025-l-ia-no-pot-desfer-la-realitat): què passa quan un agent fa accions irreversibles, com dos càrrecs de 1.000 euros que el xat no pot desfer.
- [Episodi 033: El xassi dels agents d'IA](/podcast-del-doctor/episodi/033-infraestructura-agents-ia): les eines i els guardrails com una targeta de crèdit amb límits, vistos des de la documentació d'AWS.

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

- [Transcripció automàtica](/podcast-del-doctor/sources/042-disseny-d-agents-ia-autonoms-i-segurs-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
