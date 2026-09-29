---
audio_file: "https://archive.org/download/podcast-del-doctor-035-arquitectura-oculta-codi/035-arquitectura-oculta-codi.mp3"
audio_size: 11299662
chapters_file: "035-arquitectura-oculta-codi-chapters.json"
date: '2026-09-29'
description: "El codi no envelleix per culpa d'un mal programador, sinó per lleis de xarxa gairebé ineludibles. Tot programari creix com una xarxa de món petit plena de hubs asimètrics: ho mostren 50 aplicacions Java i també una web escrita per IA. Veiem com els hotspots de CodeScene troben on es concentren l'esforç i els errors, i com un trinquet impedeix que la qualitat reculi. I contraposem la zona de dolor de Robert C. Martin a la crítica d'Oliver Drotbohm: una interfície buida posa el gràfic en verd sense arreglar res."
duration: '23:32'
episode_number: 35
season: 1
soundbite_start: 1095.1
soundbite_duration: 82.5
soundbite_title: "Una interfície buida: el gràfic somriu i l'arquitectura no ha canviat gens"
sources:
- title: "A Generative Model of Software Dependency Graphs to Better Understand Software Evolution"
  url: "https://arxiv.org/pdf/1410.7921"
  description: "Vincenzo Musco, Martin Monperrus i Philippe Preux: estudi empíric de 50 aplicacions Java (23.178 nodes) que mostra que els graus d'entrada i de sortida segueixen distribucions diferents, i un model generatiu de com evolucionen aquests grafs"
- title: "Software package metrics — Wikipedia"
  url: "https://en.wikipedia.org/wiki/Software_package_metrics"
  description: "Les mètriques de paquets de Robert C. Martin: acoblament aferent (Ca) i eferent (Ce), inestabilitat, abstracció, distància a la seqüència principal i la zona de dolor"
- title: "The Instability-Abstractness-Relationship: An Alternative View — Oliver Drotbohm"
  url: "http://odrotbohm.de/2024/09/the-instability-abstractness-relationsship-an-alternative-view/"
  description: "Crítica de la relació inestabilitat-abstracció de Martin: mesurar l'abstracció com a tipus abstractes confon una propietat del llenguatge amb el disseny d'abstraccions amb sentit"
- title: "Hotspots — CodeScene 2.8.0 Documentation"
  url: "https://docs.enterprise.codescene.io/versions/2.8.0/guides/technical/hotspots.html"
  description: "Els hotspots de CodeScene: codi complex que es modifica sovint, la densitat de defectes que concentren i el churn relatiu de codi"
- title: "Small-world network — Wikipedia"
  url: "https://en.wikipedia.org/wiki/Small-world_network"
  description: "Xarxes de món petit: alt coeficient d'agrupament, distàncies que creixen amb el logaritme del nombre de nodes, hubs i la seva robustesa i vulnerabilitat"
- title: "How this site is built — David Rodenas"
  url: "https://david-rodenas.com/projects/architecture/"
  description: "L'arquitectura d'una web escrita per Claude com a xarxa de dependències: 528 fitxers, més de 1.300 fletxes, índex de món petit 29,7 i el trinquet de mètriques"
- title: "How this site changes — David Rodenas"
  url: "https://david-rodenas.com/projects/changes/"
  description: "L'evolució del mateix codi a partir dels commits: hotspots sense proves, estabilitat de Robert C. Martin i la zona de dolor"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/035-arquitectura-oculta-codi-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/035-arquitectura-oculta-codi.png"
title: "Episodi 035: L'arquitectura oculta que col·lapsa el codi"
---

## Introducció

Tot programari amaga una bomba de rellotgeria. Normalment no és culpa d'un mal programador ni d'una errada puntual. És el resultat d'una regla estructural gairebé ineludible: el codi envelleix i es trenca seguint patrons molt clars. Aquest episodi busca l'arquitectura oculta i les lleis d'evolució del programari. Hi creuem la teoria de xarxes de món petit, un estudi empíric sobre 50 aplicacions Java, la documentació de CodeScene sobre hotspots i les notes de David Rodenas sobre una web escrita per IA. Tanquem amb el gran debat sobre les mètriques d'arquitectura: la teoria clàssica de Robert C. Martin contra la crítica d'Oliver Drotbohm. És la continuació natural de l'[Episodi 034: Urbanistes del codi que escriu la IA](/podcast-del-doctor/episodi/034-urbanisme-digital-codi-ia), ara amb el marc teòric al costat.

## Temes tractats

- **El codi com a xarxa de món petit**: solem imaginar el codi com un arbre ordenat de carpetes, però s'assembla molt més a una xarxa elèctrica caòtica. Les xarxes de món petit, les dels famosos sis graus de separació, tenen dues característiques: un agrupament molt dens en clústers i distàncies molt curtes entre nodes. La distància típica creix amb el logaritme del nombre de nodes (L ∝ log N). Si un projecte passa de 1.000 a 10 milions de fitxers, qualsevol part continua a pocs salts de qualsevol altra.

- **50 aplicacions Java i els seus hubs**: l'estudi de Musco, Monperrus i Preux analitza 50 aplicacions Java amb 23.178 nodes, en què cada node és una classe. Hi troben sempre la mateixa asimetria: una classe pot ser utilitzada per mil altres i, en canvi, ella només en necessita dues. Com que el programari evoluciona reutilitzant unes poques classes existents per construir funcions noves, apareixen hubs de manera inevitable. És com una xarxa de carreteres on tots els camins rurals desemboquen en una gran autopista. Si cau una carretera petita, el país continua circulant. Si hi ha un accident al hub, tot queda paralitzat.

- **Hotspots, el codi com a escena del crim**: inspirat en Adam Tornhill (*Your Code as a Crime Scene*), CodeScene defineix un hotspot creuant dues variables: la complexitat del codi i la freqüència amb què l'equip l'ha de tocar. Un fitxer gegant que ningú modifica en anys no és un hotspot, és un fòssil. En un cas industrial real, el 5,5% del codi acaparava el 18% de l'esforç de desenvolupament i concentrava el 23% dels errors. L'objectiu no és eliminar els hubs, que la xarxa necessita, sinó detectar els que s'han convertit en un coll d'ampolla. El *relative code churn* pondera les línies canviades respecte a la mida del fitxer per no confondre un programador nerviós que fa commits cada cinc minuts amb un fitxer en flames.

- **Una web escrita per IA amb els mateixos mals**: la web de David Rodenas, escrita pràcticament tota amb Claude Code, té 528 fitxers i més de 1.300 fletxes de dependència. El seu índex de món petit és de 29,7. La IA, programant a velocitat de vertigen, genera els mateixos hubs orgànics que els humans. Alguns eren hotspots que no es refredaven mai i no tenien cap test.

- **El trinquet**: en lloc d'escriure un manual de bones pràctiques que ningú no llegirà, un fitxer desa les pitjors mètriques actuals, com els fitxers sense tests o la profunditat màxima de les dependències. Un test automàtic rebutja qualsevol canvi que les empitjori. També falla quan algú les millora, fins que s'actualitza el fitxer al nou rècord. És el clic-clic-clic de la barra de seguretat d'una muntanya russa: la pressa comercial estira cap avall, però el vagó només pot pujar. La disciplina arquitectònica deixa de dependre de l'heroïcitat d'un programador cansat a les sis de la tarda.

- **Robert C. Martin i la zona de dolor**: l'acoblament aferent (Ca) compta quants components depenen del teu. L'eferent (Ce) compta de quants depens tu. Amb aquestes dues forces, Martin calcula la inestabilitat i la compara amb l'abstracció. La zona de dolor és on hi ha els paquets molt concrets dels quals depèn tothom: columnes de formigó enmig de l'edifici que, si les toques, provoquen terratrèmols. La solució ortodoxa era convertir-les en interfícies abstractes perquè la mètrica donés llum verda.

- **La crítica de Drotbohm i la llei de Goodhart**: Oliver Drotbohm argumenta que la fórmula confon l'«abstractesa» tècnica, que és una simple mesura que pot fer el compilador, amb el procés humà de dissenyar una abstracció amb sentit. Si a una classe de la zona de dolor li extreus una interfície buida amb una drecera de l'editor, el número millora i el gràfic somriu. L'arquitectura, però, no és ni una mica més adaptable. És la llei de Goodhart: quan una mesura es converteix en objectiu, deixa de ser una bona mesura. El perill és la falsa seguretat d'un gràfic en verd amb un hub que continua col·lapsat. La mètrica real és la fricció humana: costa afegir aquesta funció nova?

- **Reflexió final: arquitectures alienígenes?**: les mateixes lleis valen per a qualsevol sistema interconnectat, des d'una gran empresa fins a les rutes logístiques que passen pel canal de Panamà. El codi fet amb models com Claude, de moment, imita els patrons humans. Quan la IA construeixi ciutats senceres de codi sense la limitació de l'amplada de banda mental humana, continuarà seguint les mateixes regles? O dissenyarà xarxes sense hubs, incomprensibles per als nostres radars i hotspots? Per aprofundir en la mateixa web i el seu trinquet, vegeu l'[Episodi 034: Urbanistes del codi que escriu la IA](/podcast-del-doctor/episodi/034-urbanisme-digital-codi-ia). Sobre per què cada canvi ha de venir amb la seva prova, l'[Episodi 032: El cànon TDD de Kent Beck](/podcast-del-doctor/episodi/032-el-canon-tdd-de-kent-beck).

## Fonts

- [A Generative Model of Software Dependency Graphs to Better Understand Software Evolution](https://arxiv.org/pdf/1410.7921): Musco, Monperrus i Preux estudien empíricament els grafs de dependències de 50 aplicacions Java
- [Software package metrics](https://en.wikipedia.org/wiki/Software_package_metrics) (Wikipedia): les mètriques d'acoblament, inestabilitat i abstracció de Robert C. Martin
- [The Instability-Abstractness-Relationship: An Alternative View](http://odrotbohm.de/2024/09/the-instability-abstractness-relationsship-an-alternative-view/): la crítica d'Oliver Drotbohm a la relació inestabilitat-abstracció
- [Hotspots](https://docs.enterprise.codescene.io/versions/2.8.0/guides/technical/hotspots.html) (CodeScene 2.8.0): documentació sobre com es detecten i es prioritzen els hotspots
- [Small-world network](https://en.wikipedia.org/wiki/Small-world_network) (Wikipedia): teoria de les xarxes de món petit
- [How this site is built](https://david-rodenas.com/projects/architecture/): David Rodenas analitza l'arquitectura d'una web escrita per Claude i el seu trinquet de mètriques
- [How this site changes](https://david-rodenas.com/projects/changes/): David Rodenas estudia com evoluciona aquest codi, amb els seus hotspots i la zona de dolor
- [Transcripció automàtica](/podcast-del-doctor/sources/035-arquitectura-oculta-codi-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
