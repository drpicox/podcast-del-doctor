---
audio_file: "https://archive.org/download/podcast-del-doctor-034-urbanisme-digital-codi-ia/034-urbanisme-digital-codi-ia.mp3"
audio_size: 12107995
chapters_file: "034-urbanisme-digital-codi-ia-chapters.json"
date: '2026-09-29'
description: "Si una IA aixeca tot l'edifici, a l'humà només li queda fer d'urbanista. Analitzem dos assajos de David Rodenas sobre una web escrita íntegrament per Claude: 528 fitxers que formen una xarxa de món petit, hubs com Feature.ts que fan d'aeroport de Frankfurt, hotspots sense cap prova, acoblaments lògics que es mouen junts com dos pares divorciats, la zona de dolor de Robert C. Martin i el trinquet, un test que només deixa que la qualitat vagi endavant. I una pregunta final: què hem d'ensenyar si ja no piquem codi?"
duration: '25:13'
episode_number: 34
season: 1
soundbite_start: 1124.76
soundbite_duration: 61.4
soundbite_title: "El trinquet: una roda que només pot girar cap endavant"
sources:
- title: "How this site is built — David Rodenas"
  url: "https://david-rodenas.com/projects/architecture/"
  description: "L'arquitectura de la web com a xarxa de dependències: 528 fitxers, 1.314 fletxes, propietat de món petit, hubs, regles d'arquitectura imposades amb tests i el trinquet de mètriques (architecture.ratchet.json)"
- title: "How this site changes — David Rodenas"
  url: "https://david-rodenas.com/projects/changes/"
  description: "L'evolució del mateix codi a partir de 150 commits (7-29 de setembre de 2026): hotspots, propagació dels canvis entre veïns, acoblament lògic, estabilitat de Robert C. Martin i la zona de dolor"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/034-urbanisme-digital-codi-ia-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/034-urbanisme-digital-codi-ia.png"
title: "Episodi 034: Urbanistes del codi que escriu la IA"
---

## Introducció

Imaginem que som l'arquitecte en cap d'un gratacel, però que no toquem mai ni una gota de ciment: una IA aixeca l'edifici sencer, pis a pis, en qüestió de segons. L'única feina humana és dictar les lleis de la física perquè tot plegat no s'enfonsi. Aquest episodi analitza dos assajos interactius de David Rodenas, «How this site is built» i «How this site changes», que estudien l'arquitectura d'una web escrita íntegrament per Claude. No cal saber programar per seguir-lo: parla de com evolucionen els sistemes complexos, on es formen els colls d'ampolla i com es propaguen els errors que no veiem. Són lliçons que també valen per a una empresa, un hospital o qualsevol equip.

## Temes tractats

- **El mapa del territori**: no pots protegir el que no veus. El primer assaig dibuixa el codi com una xarxa: 528 fitxers en 42 carpetes, units per 1.314 fletxes de dependència. Cada fletxa vol dir «aquest element necessita aquell altre per funcionar», com el departament de vendes que necessita la llista de preus de màrqueting.

- **Una xarxa de món petit**: és el concepte de Watts i Strogatz, pensat per estudiar les xarxes socials humanes (els famosos sis graus de separació). La xarxa té un índex de món petit de 29,7: està 34 vegades més agrupada que una xarxa aleatòria, en barris petits on tothom es coneix, però els camins per creuar-la només són una mica més llargs. Ordre local i connexió global alhora.

- **Els hubs, com els grans aeroports**: igual que no hi ha vols directes entre tots els pobles del món, el codi fa servir superaeroports. `Feature.ts` el necessiten 59 fitxers i és al mig del 39% dels camins més curts entre dos fitxers. És l'aeroport de Frankfurt del projecte, i té la mateixa debilitat: la xarxa aguanta bé els errors petits, però si cau un hub, mig sistema queda aïllat.

- **La geografia del canvi**: el segon assaig analitza 150 commits entre el 7 i el 29 de setembre de 2026. La majoria de fitxers neixen, s'ajusten de pressa els primers dies i després es queden congelats perquè ja fan la seva feina. Moure molt les coses no vol dir treballar bé: sovint l'eficiència és deixar-les tranquil·les.

- **Hotspots sense xarxa**: la idea d'Adam Tornhill dels punts calents són fitxers que canvien setmana rere setmana. `allFeatures.ts`, el registre de totes les funcionalitats, va canviar 21 vegades amb una cobertura de proves del 0%. Que canviï és normal; el perill és canviar-lo sense proves. Claude escriu una sintaxi impecable, però té límits de context: no pot tenir al cap els altres 500 fitxers. És com un cirurgià que talla una artèria amb un tall perfecte sense saber que cinc òrgans en depenien.

- **Fins on arriba l'ona expansiva**: quan un fitxer canvia, el veí directe també ha de canviar un 24% de les vegades. Un salt més enllà, la xifra cau cap al 5%, perquè l'arquitectura amortitza el cop.

- **Acoblament lògic, els fantasmes del sistema**: és el concepte de Harald Gall, Karin Hajek i Mehdi Jazayeri (1998). Hi ha fitxers sense cap fletxa entre ells que, tot i així, canvien sempre junts. L'exemple de l'episodi és el que genera l'HTML al servidor i el que hi treballa al navegador. Són com dos pares divorciats que no es parlen, però arriben a la mateixa hora a l'escola: el fill que els lliga és l'estructura de les etiquetes HTML. L'assaig considera significatives les parelles que canvien juntes tres cops o més. La solució és convertir aquest pacte invisible en un contracte visible amb una prova, com anar al notari a registrar l'acord de custòdia.

- **La zona de dolor de Robert C. Martin**: la fórmula d'inestabilitat I = Ce / (Ca + Ce) compara quants components en depenen i de quants en depèn cadascun. La zona de dolor és ser imprescindible per a tothom i alhora concret i canviant. És com la fotocopiadora de la planta: 40 persones la necessiten i s'encalla cada cop que algú obre la tapa. `platform/plugin` la necessiten 59 caixes i té una estabilitat mínima. La recepta és la inversió de dependències: amb fletxes només de tipus, els canvis que salten entre caixes baixen del 24% al 13%.

- **El trinquet**: és la roda dentada que fa clic i només gira endavant. `architecture.ratchet.json` desa quatre mètriques que només poden millorar: les fletxes que violen l'estabilitat, la profunditat del nucli de dependències, la cadena més llarga (12 fletxes) i els fitxers executables sense proves (156). Si un canvi en porta un a 157, el test falla. Si en deixa 155, cal actualitzar la marca en el mateix commit, i ja no es pot tornar enrere. S'acaba el «és només un pedaç, ja ho netejaré». Quan una IA genera codi més de pressa del que cap humà pot revisar, les normes han de ser barreres, no manuals.

- **Reflexió final: urbanistes digitals**: si les IA fan tota l'execució bruta i nosaltres només fem de reguladors, com en una ciutat on els robots aixequen els edificis gratis, per què continuem ensenyant a arrebossar la façana a mà? Quines habilitats d'abstracció i de disseny de regles necessitem per continuar tenint una cadira a la taula? Que l'especificació passa a ser la feina humana ho vam explicar a l'[Episodi 012: L'especificació és el nou codi](/podcast-del-doctor/episodi/012-especificacio-nou-codi). Per què un agent necessita un arnès, a l'[Episodi 018: L'arnès d'agent i el control real](/podcast-del-doctor/episodi/018-l-arnes-d-agent-i-el-control-real). Com són els equips on els agents ja programen sols, a l'[Episodi 019: Fàbriques d'agents que ja programen sols](/podcast-del-doctor/episodi/019-fabriques-d-agents-que-programen-sols). I la disciplina de fer que cada canvi vingui amb la seva prova, a l'[Episodi 032: El cànon TDD de Kent Beck](/podcast-del-doctor/episodi/032-el-canon-tdd-de-kent-beck).

## Fonts

- [How this site is built](https://david-rodenas.com/projects/architecture/): David Rodenas explica l'arquitectura de la seva web, escrita per Claude, com a xarxa de dependències, amb les regles imposades amb tests i el trinquet de mètriques
- [How this site changes](https://david-rodenas.com/projects/changes/): David Rodenas analitza com ha evolucionat aquest codi amb 150 commits (setembre de 2026)
- [Transcripció automàtica](/podcast-del-doctor/sources/034-urbanisme-digital-codi-ia-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
