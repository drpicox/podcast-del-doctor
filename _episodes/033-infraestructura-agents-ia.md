---
audio_file: "https://archive.org/download/podcast-del-doctor-033-infraestructura-agents-ia/033-infraestructura-agents-ia.mp3"
audio_size: 8827016
chapters_file: "033-infraestructura-agents-ia-chapters.json"
date: '2026-09-29'
description: "Un cotxe conceptual espectacular al garatge, amb un motor que fa por... i sense frens. Així són moltes demos d'agents d'IA quan intenten sortir a producció. Amb la documentació d'AWS, parlem del xassi que els falta: AgentCore i la fontaneria feixuga (credencials, MCP, lambdas), l'API Converse per canviar de model amb una sola línia, les eines i els guardrails com una targeta de crèdit amb límits, el raonament automatitzat que demostra matemàticament que un error és impossible, i l'observabilitat com a caixa negra. I una pregunta final: qui dirigirà els agents quan el mànager també sigui una IA?"
duration: '18:23'
episode_number: 33
season: 1
soundbite_start: 839.0
soundbite_duration: 82.4
soundbite_title: "Seguretat demostrada, no provada: la presó matemàtica dels agents"
sources:
- title: "Amazon Bedrock AgentCore — AWS"
  url: "https://aws.amazon.com/bedrock/agentcore/"
  description: "Pàgina de producte d'AgentCore: runtime, gateway, identitat, memòria, polítiques i observabilitat per portar agents a producció, amb els casos de Druva, Thomson Reuters i Cox Automotive"
- title: "Converse — Amazon Bedrock API Reference"
  url: "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html"
  description: "Referència de l'API Converse: una interfície única per als models de missatgeria de Bedrock, amb toolConfig, guardrailConfig i additionalModelRequestFields"
- title: "Introducing Strands Agents, an Open Source AI Agents SDK — AWS Open Source Blog"
  url: "https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/"
  description: "Clare Liguori (maig de 2025) presenta Strands Agents, l'SDK de codi obert (Apache 2.0) per construir agents amb un enfocament guiat pel model: model, eines i prompt"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/033-infraestructura-agents-ia-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/033-infraestructura-agents-ia.png"
title: "Episodi 033: El xassi dels agents d'IA"
---

## Introducció

Algú dissenya al garatge un cotxe conceptual increïble: aerodinàmic, amb un motor que fa por i un vídeo de demostració que sembla de l'any 2050. Però quan el volen treure a l'autopista en hora punta, descobreixen que no té cinturons, que la transmissió no s'ha provat i, sobretot, que no té frens. Aquesta és la crisi silenciosa de la IA a les empreses. Fer una demo d'agent en un cap de setmana és fàcil; portar-la a un entorn de producció on consulta bases de dades i executa accions reals és un abisme. L'episodi repassa la documentació d'AWS (Amazon Bedrock AgentCore, l'API Converse i Strands Agents) per entendre quin xassi necessita aquest motor.

## Temes tractats

- **Del prototip a la producció**: un prototip només demostra que una idea és possible en condicions controlades. Un agent que modifica registres de clients en una base de dades activa multiplica el risc. El coll d'ampolla no és fer la IA més intel·ligent, sinó integrar-la als sistemes vells de l'empresa sense trencar-ho tot. Qui li dona permisos? Com detectes una connexió que falla en mil·lisegons?

- **AgentCore i la feina feixuga no diferenciada**: és tot aquell codi de fontaneria que no millora el producte, però que evita que exploti. Per exemple, connectar-se a fonts de dades a través de MCP, executar funcions lambda al núvol i gestionar les credencials de l'agent, que també ha d'ensenyar la placa a l'entrada. Si la IA és el motor, AgentCore és el xassi de titani amb la transmissió i els cinturons ja instal·lats: unifica l'autenticació perquè no calgui muntar una barrera de seguretat nova per a cada eina.

- **El 0% del màrqueting**: la còpia de la pàgina de producte que es va fer servir per generar l'episodi mostrava «0% menys de temps dedicat a la infraestructura» i un desplegament «0.0 vegades més ràpid». A l'episodi es llegeix com un text de prova que algú es va oblidar d'omplir. A la pàgina actual hi ha xifres animades, així que el més probable és que fossin comptadors que encara no s'havien carregat.

- **Casos reals**: Druva resol el 68% de les incidències de suport sense intervenció humana, Thomson Reuters arriba a un 70% d'automatització a l'enginyeria de plataforma i Cox Automotive va passar de zero a 17 agents en producció en menys d'un any. La clau és l'estandardització: amb 17 agents fets a mà, una clau caducada vol dir buscar-la en 17 codis diferents. La plataforma també accepta el codi que ja feien servir els equips, com ara LangChain o les eines d'OpenAI.

- **L'API Converse contra el bloqueig de proveïdor**: surten models nous gairebé cada setmana. Si tot el cablejat parla l'idioma d'un sol model, l'arquitectura queda obsoleta de seguida. Converse fa de traductor universal: escrius la lògica una vegada i, per canviar de model, només canvies l'identificador. L'exemple de la documentació demana un article sobre com afecta la inflació al PIB i afegeix un *system prompt* («actua com un economista expert»). Tot plegat es pot enviar a Claude 3 Sonnet o a qualsevol altre model sense tocar l'aplicació.

- **I el mínim comú denominador?**: la crítica habitual a les capes d'abstracció és que retallen les capacitats específiques de cada model. La resposta és `additionalModelRequestFields`, un calaix de sastre on es pot posar un JSON que l'API transporta sense tocar-lo fins al model que el sap interpretar. Així tens una base estable i, a més, pots aprofitar les funcions exclusives de cada proveïdor.

- **Eines i guardrails**: donar eines (`toolConfig`) a un agent és com donar una targeta de crèdit corporativa a algú que acaba d'entrar a l'empresa. Els guardrails (`guardrailConfig`) són els límits que hi posa el departament financer. Si l'agent intenta una acció que incompleix la norma, la infraestructura talla la connexió abans que l'ordre surti. Pel que fa a la privacitat, AWS afirma que no fa servir els documents, les imatges ni les converses dels clients per entrenar models, una condició imprescindible perquè bancs i hospitals s'hi acostin.

- **Raonament automatitzat**: els tests no poden cobrir les variacions infinites d'una IA. En canvi, el raonament automatitzat tradueix el sistema a fórmules lògiques formals i demostra matemàticament que un estat prohibit és inabastable. No es tracta de provar-ho 10.000 vegades, sinó de tancar aquell camí. És la mateixa tecnologia que AWS fa servir des de fa anys per protegir IAM i S3. En comptes de confiar que l'agent es porti bé, el tanques en una presó matemàtica.

- **Observabilitat**: quan un agent s'encalla o dona voltes, el desenvolupador no rep un error genèric. Veu el rastre del raonament pas a pas: quina deducció va fer, per què va triar una eina i no una altra i quins paràmetres va enviar. Funciona com la caixa negra d'un avió i permet distingir entre un error de la IA i una base de dades que havia caigut un minut.

- **Reflexió final: la IA que contracta i acomiada IA**: si ajuntem una xarxa que connecta models, dades i eines, un sistema que mesura l'eficiència en temps real i la possibilitat de canviar de model amb una sola línia, tenim totes les peces d'un supervisor autònom. Seria un agent mànager capaç de dir «aquest model avui va lent, l'acomiado» i de desviar el trànsit cap a un altre proveïdor més ràpid i barat. Una jerarquia corporativa invisible de models. Per què els agents necessiten un arnès i no només un model, ho explicàvem a l'[Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real). El fracàs dels pilots d'IA corporativa, amb la mateixa metàfora del motor de Fórmula 1 sobre un carro de fusta, surt a l'[Episodi 021: La IA agencial contra el fracàs corporatiu](/podcast-del-doctor/episodi/021-ia-agencial-contra-el-fracas-corporatiu). I per què les accions reals d'un agent no es poden desfer, a l'[Episodi 025: L'IA no pot desfer la realitat](/podcast-del-doctor/episodi/025-l-ia-no-pot-desfer-la-realitat).

## Fonts

- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/): pàgina de producte d'AWS amb els components de la plataforma i els casos de clients
- [Converse — Amazon Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html): referència de l'API unificada per conversar amb els models de Bedrock
- [Introducing Strands Agents, an Open Source AI Agents SDK](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/): Clare Liguori, AWS Open Source Blog (maig de 2025)
- [Transcripció automàtica](/podcast-del-doctor/sources/033-infraestructura-agents-ia-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
