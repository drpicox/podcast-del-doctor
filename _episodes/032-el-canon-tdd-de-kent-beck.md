---
audio_file: "https://archive.org/download/podcast-del-doctor-032-el-canon-tdd-de-kent-beck/032-el-canon-tdd-de-kent-beck.mp3"
audio_size: 8725869
chapters_file: "032-el-canon-tdd-de-kent-beck-chapters.json"
date: '2026-09-27'
description: "Qui odiaria cuinar perquè abans cal escriure un receptari de 300 pàgines? Doncs és la caricatura amb què molts programadors critiquen el TDD. Kent Beck la desmunta a «Canon TDD»: una llista de comportaments, una sola prova començant per l'asserció, fer-la passar amb el canvi mínim, refactoritzar amb un sol barret i tornar a començar. Parlem del disseny lògic contra el físic, dels errors que maten el mètode, de per què l'ordre de les proves pot acabar en un bubble sort o en un quicksort, i de la recompensa final: convertir la por en avorriment."
duration: '18:10'
episode_number: 32
season: 1
soundbite_start: 656.8
soundbite_duration: 55.7
soundbite_title: "Mateixes proves, ordre diferent: d'un bubble sort a un quicksort"
sources:
- title: "Canon TDD — Kent Beck (Software Design: Tidy First?)"
  url: "https://newsletter.kentbeck.com/p/canon-tdd"
  description: "L'article que vertebra l'episodi (11 de desembre de 2023): els cinc passos del TDD tal com el va definir el seu autor, els errors habituals i la distinció entre disseny d'interfície i disseny d'implementació"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/032-el-canon-tdd-de-kent-beck-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/032-el-canon-tdd-de-kent-beck.png"
title: "Episodi 032: El cànon TDD de Kent Beck"
---

## Introducció

Imaginem algú que diu que detesta cuinar perquè abans d'encendre els fogons ha d'escriure un receptari de 300 pàgines. Absurd, oi? Doncs és l'argument amb què molts desenvolupadors justifiquen el seu rebuig al desenvolupament guiat per proves. Kent Beck, que el va redescobrir i popularitzar, va escriure «Canon TDD» per deixar clar què és el TDD i què no ho ha estat mai: la indústria porta dècades atacant un home de palla. Aquest episodi repassa l'article pas a pas i mostra que, més que un manual per picar codi, és un flux de treball per canviar el comportament d'un sistema d'una manera que el nostre cervell pugui gestionar.

## Temes tractats

- **L'home de palla**: la crítica habitual al TDD diu que obliga a planificar i escriure centenars de proves abans de teclejar una sola línia de codi funcional. El TDD original no ho ha proposat mai. Segons Beck, és un flux de treball per garantir que el que ja funcionava ho continuï fent i que el comportament nou sigui correcte.

- **Context històric**: Beck va escriure SUnit el 1994 i l'octubre de 1995 va ensenyar el TDD a Ward Cunningham a l'OOPSLA d'Austin, que en aquells anys era l'epicentre de la programació orientada a objectes. L'episodi també explica que Beck va endarrerir molt de temps el llibre *Test-Driven Development: By Example* per por que algú se li avancés.

- **Disseny lògic i disseny físic**: aquí hi ha l'arrel de la confusió. Una cosa és la interfície, és a dir, com s'invoca un comportament (el nom, els paràmetres i el resultat esperat). Una altra és la implementació, com el sistema fa aquest comportament per dins. Si intentem resoldre totes dues coses alhora, ens saturem: els humans som uns ordinadors pèssims, i el cànon posa baranes perquè no ens hi perdem.

- **Pas 1, la llista de proves**: abans d'obrir l'editor, llistem totes les variants esperades del comportament nou. En un sistema d'autenticació serien la contrasenya correcta, el servidor que cau o la clau inexistent o caducada. És anàlisi de comportament des de fora i es pot fer en un tovalló de bar. No és un gran disseny inicial: la llista no conté decisions d'implementació, ni bases de dades ni patrons. Només serveix per buidar la memòria a curt termini.

- **Pas 2, una sola prova**: triem un únic element de la llista i n'escrivim una prova automatitzada de veritat, amb preparació, invocació i comprovació. El consell de Beck és escriure-la a l'inrevés, començant per l'asserció, perquè així fixem l'objectiu abans de perdre'ns en configuracions i dades simulades. Els errors típics són escriure proves sense assercions, que només fan de teatre de cobertura, i convertir tota la llista en proves de cop. Si a la primera descobreixes que la interfície no tenia sentit, has de llençar les altres cinc.

- **L'ordre importa (i molt)**: l'ordre en què triem les proves canvia el resultat. En els comentaris de l'article, Vic Wu va dibuixar el flux sencer en un diagrama i Philipp Rembold va esmentar la *wardrobe kata* i un article d'Uncle Bob sobre aquest tema. Amb els mateixos requisits, un ordre de proves porta cap a bucles i un bubble sort, i un altre cap a la recursivitat i un quicksort. La pregunta oberta que deixa Beck és si el codi és sensible a les condicions inicials.

- **Pas 3, fer-la passar**: amb el canvi més petit possible, per ridícul que sembli, encara que a l'ego no li agradi. Les trampes a evitar: esborrar o comentar l'asserció, que és com arrencar els cables de l'alarma d'incendis mentre crema el menjador, i deixar-se els valors copiats de la prova al codi, que trenca la triangulació. Si durant la feina surt un cas nou (i si hi posen un emoji de flameta?), s'afegeix a la llista i es continua amb la prova actual. Només si el descobriment invalida el que hem fet, cal esborrar i tornar a començar amb un altre ordre.

- **Pas 4, refactoritzar (opcionalment)**: ara sí que és el moment de les decisions d'implementació. L'error greu és portar dos barrets alhora i voler que el codi funcioni i quedi bonic al mateix temps: seria com polir els metalls d'una casa en flames. L'altra trampa és l'abstracció prematura. Com diu Beck, «la duplicació és una pista, no una ordre», i sovint surt més a compte aguantar una mica de codi repetit que construir una gàbia d'abstraccions. El mateix Beck admet que ell també s'ha encallat en un projecte personal sense saber quina prova escriure després.

- **Pas 5, repetir fins a buidar la llista**: la recompensa és psicològica. La por pel comportament del codi es converteix en avorriment. No és apatia, sinó l'avorriment de la fiabilitat, el que et deixa dormir tranquil i t'allibera energia per innovar.

- **Reflexió final**: si l'ordre en què imaginem les proves dona forma a l'arquitectura, fins a quin punt un sistema és el registre de l'estat d'ànim i dels biaixos del programador el dia que va escriure la llista? I en l'era de la IA, potser el TDD acabarà sent la millor eina d'auditoria per entendre'ns amb les màquines. És la idea que ja apuntàvem a l'[Episodi 012: L'especificació és el nou codi](/podcast-del-doctor/episodi/012-especificacio-nou-codi). La visió de Dave Farley sobre el TDD com a eina de disseny la trobareu a l'[Episodi 003: Test-Driven Development amb Dave Farley](/podcast-del-doctor/episodi/003-spacex-ingenyeria-software-aprendre).

## Fonts

- [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd): Kent Beck, *Software Design: Tidy First?* (desembre de 2023), l'article que vertebra l'episodi
- [Transcripció automàtica](/podcast-del-doctor/sources/032-el-canon-tdd-de-kent-beck-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
