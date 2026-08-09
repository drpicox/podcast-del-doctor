---
audio_file: "https://archive.org/download/podcast-del-doctor-012-especificacio-nou-codi/012-especificacio-nou-codi.mp3"
audio_size: 6746625
chapters_file: "012-especificacio-nou-codi-chapters.json"
date: '2026-06-16'
description: "Per què una IA capaç d'escriure codi a la velocitat de la llum no ens estalvia la part difícil de programar? Basant-nos en un vídeo del canal Modern Software Engineering, on Dave Farley conversa amb Stefan Ellisdorfer i Christian Gassel, explorem el desenvolupament dirigit per especificacions amb IA agèntica: per què la manca de determinisme dels models és un verí per a l'enginyeria, com l'ATDD i el BDD converteixen les proves en el contracte executable de la IA, què és l'efecte mirall que ens obliga a ser més específics, l'índex Farley per puntuar la qualitat dels tests, i com passem de programadors a enginyers de comportaments. L'especificació, no el codi, és ara la feina humana."
duration: '14:03'
episode_number: 12
season: 1
soundbite_start: 455.4
soundbite_duration: 27.2
soundbite_title: "La IA: un geni de la làmpada extremadament literal"
sources:
- title: "Automating Agentic AI Success Using This SECRET Workflow — Modern Software Engineering (Dave Farley)"
  url: "https://www.youtube.com/watch?v=hlxeiSzde5A"
  description: "Vídeo del canal de Dave Farley on conversa amb Stefan Ellisdorfer (Smarter Software, autor de The Effective Software Engineer) i Christian Gassel (Rohde & Schwarz) sobre desenvolupament dirigit per especificacions amb IA agèntica"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/012-especificacio-nou-codi-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/012-especificacio-nou-codi.png"
title: "Episodi 012: L'especificació és el nou codi"
---

## Introducció

La intel·ligència artificial escriu codi a la velocitat de la llum, però sorprenentment no ajuda gaire amb la part difícil: entendre i explorar el problema real. En aquest episodi desgranem un vídeo del canal *Modern Software Engineering* de Dave Farley, amb Stefan Ellisdorfer (consultora Smarter Software, autor de *The Effective Software Engineer*) i Christian Gassel (Rohde & Schwarz), per defensar una tesi incòmoda: quan la màquina pica el codi, la feina humana es desplaça cap a definir-lo amb un rigor gairebé matemàtic. L'especificació passa a ser el nou codi font.

## Temes tractats

- **El xef ultraràpid**: Tenir una IA que programa avui és com tenir un xef que talla i cou els ingredients en mil·lisegons; però si no li dones una recepta increïblement precisa i mil·limetrada, acabes amb un pastís caòtic i incomestible. La velocitat de la màquina no és el problema, ho és com la dirigim.

- **La manca de determinisme**: El defecte principal d'aquests models és que són probabilístics i, per tant, impredictibles. I a l'enginyeria de programari, la impredictibilitat és un verí: un dia et fa una cosa i l'endemà una altra. L'única manera de pal·liar-ho és afegir estructura.

- **El llenguatge natural com a nou llenguatge de programació**: Es defensa que el llenguatge natural humà és el gran candidat a la pròxima generació de llenguatges de programació, però amb un parany: necessita molta més estructura de la que ens venien quan prometien que n'hi hauria prou amb dir "fes-me un botó verd que faci això".

- **ATDD i BDD: les especificacions executables**: Metodologies que no són noves però que ara prenen un valor brutal. L'ATDD (desenvolupament guiat per proves d'acceptació) i el BDD (per comportament) defineixen primer les proves, centrant-se en resultats precisos i verificables. No expliques *com* fer una cosa: crees especificacions executables que s'emmagatzemen al control de versions i es converteixen en la veritat absoluta.

- **El contracte de la IA i "zero humans en el bucle"**: Quan aquestes proves estan ben descrites, esdevenen el contracte que la IA ha de complir. Si el codi generat supera les proves de seguretat i rendiment, no cal intervenció humana per revisar-lo. El codi en Python o Java passa a tractar-se com el codi assemblador que generen els compiladors: ja no te'l mires.

- **Els guardrails de titani**: Davant l'objecció de confiar cegament en una caixa negra, la resposta són les baranes de seguretat. Els tests no poden ser desitjos vagues ("el sistema hauria de funcionar"), sinó criteris d'acceptació exhaustius i programàticament validats: "el sistema ha de respondre sota una càrrega de 1.000 usuaris en menys de 200 ms amb la base de dades bloquejada". Requereix una disciplina humana brutal.

- **L'efecte mirall**: La gran paradoxa és que els agents d'IA ens exigeixen —i ens entrenen— per ser específics. Christian Gassel ho remarca: per conduir un agent autònom cal una comprensió compartida perfecta del que volem, i un bon prompt s'assembla moltíssim a una bona especificació. La IA ens està educant a nosaltres.

- **El flux de treball ideal i el TDD de doble bucle**: Formular l'especificació de manera assistida (sovint amb exemples), crear els casos de prova i donar llibertat a l'agent perquè es verifiqui a si mateix executant aquells tests, com una *fitness function* alineada amb el que necessita la IA. Tot plegat empeny el TDD de doble bucle: el bucle gran dels requisits i el bucle petit de la IA picant codi i refactoritzant.

- **El geni literal de la làmpada**: La IA és com un geni extremadament literal. Si li demanes "vull un milió de dòlars", te'ls pot llançar en monedes d'un cèntim des del sostre i aixafar-te. Has de ser impecable amb els teus desitjos: "vull un milió de dòlars, en bitllets petits, ingressats legalment i lliures d'impostos".

- **L'índex Farley**: Per governar les muntanyes de codi i tests que genera el bucle interior, apareix l'índex Farley, una eina de puntuació per a les pròpies proves. No avalua el codi de producció, sinó propietats d'una bona prova com l'atomicitat (que comprovi una única cosa, de manera aïllada i eficient). S'utilitza com a bucle de retroalimentació perquè la IA s'autoavaluï com el seu propi professor i dissenyi millors tests i millor arquitectura.

- **Enginyers de comportaments**: El nivell d'abstracció puja. El nostre paper és dissenyar les regles del joc, no jugar la partida teclejant-ho tot. Farley anticipa fins i tot un *skill* específic de TDD instal·lat en els assistents autònoms perquè treballin colze a colze amb els humans sota aquestes regles. El programador es transforma en enginyer de comportaments: modela el comportament desitjat i audita el procés a alt nivell.

- **Reflexió final — què ens quedarà per explorar?**: Si avui el nostre valor afegit és traduir necessitats vagues en criteris d'acceptació concrets, què passarà el dia que la IA tingui prou empatia i context per deduir-los ella mateixa a partir d'una simple conversa de cafè? Si arriba a entendre els nostres problemes millor que nosaltres, quin serà el paper dels "exploradors de problemes" que ara diem que som?

Aquest episodi entronca amb la sèrie sobre treballar amb IA del podcast: la disciplina de proves de Dave Farley ja va aparèixer a l'[Episodi 003: Test-Driven Development amb Dave Farley](/podcast-del-doctor/episodi/003-spacex-ingenyeria-software-aprendre), la idea de dirigir la IA amb precisió a l'[Episodi 004: Domar la IA per programar amb precisió](/podcast-del-doctor/episodi/004-domar-ia-precisio), i l'analogia del geni literal reprèn el fil de l'[Episodi 007: Com domar el geni trampós](/podcast-del-doctor/episodi/007-com-domar-el-geni-trampos).

## Fonts

- [Automating Agentic AI Success Using This SECRET Workflow — Modern Software Engineering (Dave Farley)](https://www.youtube.com/watch?v=hlxeiSzde5A) — Conversa amb Stefan Ellisdorfer i Christian Gassel sobre desenvolupament dirigit per especificacions amb IA agèntica
- Transcripció automàtica (`/podcast-del-doctor/sources/012-especificacio-nou-codi-transcripcio.txt`) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
