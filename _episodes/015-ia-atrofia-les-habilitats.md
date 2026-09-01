---
audio_file: "https://archive.org/download/podcast-del-doctor-015-ia-atrofia-les-habilitats/015-ia-atrofia-les-habilitats.mp3"
audio_size: 9278203
chapters_file: "015-ia-atrofia-les-habilitats-chapters.json"
date: '2026-07-31'
description: "El GPS ens ha atrofiat el sentit de l'orientació —els taxistes de Londres tenien un hipocamp físicament més gran— i la pregunta d'aquest episodi és si la IA està fent el mateix amb les nostres habilitats intel·lectuals. Analitzem a fons l'estudi «How AI Impacts Skill Formation»: un assaig aleatoritzat amb 52 programadors que aprenien la llibreria asíncrona Trio, on els que tenien assistent d'IA van treure un 17% menys al test sense guanyar temps. Parlem de la fricció com a mecanisme d'aprenentatge, dels sis perfils d'interacció, de la il·lusió de competència i del deute intel·lectual corporatiu."
duration: '19:19'
episode_number: 15
season: 1
soundbite_start: 987.0
soundbite_duration: 61.2
soundbite_title: "L'exosquelet cognitiu: si elimines la fricció mental, bloqueges l'aprenentatge"
sources:
- title: "How AI Impacts Skill Formation — Judy Hanwen Shen, Alex Tamkin (arXiv:2601.20245)"
  url: "https://arxiv.org/abs/2601.20245"
  description: "Experiments aleatoritzats sobre com aprenen els desenvolupadors una llibreria de programació asíncrona nova amb i sense assistència d'IA, els sis patrons d'interacció detectats i els efectes sobre comprensió conceptual, lectura de codi i depuració"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/015-ia-atrofia-les-habilitats-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3)"
thumbnail: "/assets/thumbnails/015-ia-atrofia-les-habilitats.png"
title: "Episodi 015: L'IA ens està atrofiant les habilitats"
---

## Introducció

El GPS és una eina meravellosa que ha tingut un efecte secundari curiós: ens ha atrofiat el sentit de l'orientació. Hi ha un estudi clàssic de neurociència sobre els taxistes de Londres que, abans de l'era del GPS, havien de memoritzar milers de carrers d'una ciutat laberíntica: els escàners cerebrals mostraven que el seu **hipocamp** —la part del cervell associada a la memòria espacial— creixia físicament, com un múscul entrenat cada dia. Avui seguim una fletxa blava per una pantalla i el cervell ja no construeix mapes mentals. La pregunta d'aquest episodi és si ens està passant exactament el mateix amb les habilitats intel·lectuals a la feina, ara que hi ha una IA a cada escriptori. El debat públic s'ha centrat de manera gairebé obsessiva en com la IA canvia el **producte final**; aquí posem el focus, exclusivament, en el **procés intern**: què li passa a la ment mentre rep assistència constant.

## Temes tractats

- **L'estudi i el camp de proves**: Analitzem «How AI Impacts Skill Formation», de Judy Hanwen Shen i Alex Tamkin (arXiv:2601.20245). Els investigadors van triar l'enginyeria de programari com a entorn de proves perquè és un sector on la IA generativa ja s'utilitza massivament i on cal aprendre eines noves constantment: el laboratori perfecte.

- **El disseny de l'experiment**: 52 programadors, barrejant perfils júnior i sènior, amb una tasca que cap d'ells no havia fet mai: aprendre a fer servir **Trio**, una llibreria de Python per a programació asíncrona. No és aprendre una fórmula senzilla, és un canvi de paradigma mental —la metàfora de la cuina: poses l'aigua a bullir, mentrestant talles la ceba i respons un correu, i quan sona l'alarma tornes a la pasta. Meitat del grup amb un assistent d'IA d'última generació integrat; l'altra meitat, només internet «de tota la vida»: fòrums i documentació oficial. Trenta-cinc minuts, dos exercicis i, després, un test de **14 preguntes** sobre comprensió conceptual, lectura de codi aliè i, sobretot, *debugging*.

- **El resultat contraintuïtiu: un 17% menys**: El grup que va utilitzar la IA va obtenir un **17% menys de puntuació**. No és un marge d'error estadístic: és baixar dos graus sencers de nota. Van entendre pitjor la base de l'asincronia i van ser incapaços de trobar solucions davant d'un codi trencat.

- **I tampoc no van guanyar temps**: L'objecció òbvia —«accepto perdre un 17% d'aprenentatge si enllesteixen la feina en 10 minuts en lloc de 35»— se sosté fins que mires les dades. No hi va haver guany de temps significatiu. Les gravacions de pantalla mostren una **transferència massiva** del temps de treball: l'esforç que el grup tradicional dedicava a picar codi, llegir i provar coses, el grup de la IA el dedicava a interactuar amb la màquina. Alguns participants van passar fins a **11 minuts només redactant prompts**: escrivien, rebien una cosa rara, demanaven canvis, tornaven a escriure. Hem canviat temps productiu per temps de gestió de la màquina que ens havia de salvar.

- **La fricció és el mecanisme, no l'obstacle**: El grup sense IA va topar amb una mitjana de **3 errors severs** per exercici; els de la IA, amb un de sol. I aquests errors ho aporten tot: no són comes oblidades, són *run-time warnings* i *type errors* específics d'un entorn nou. Quan el professional s'hi encalla, el cervell detecta una anomalia —la realitat no quadra amb la seva lògica—, s'ha d'aturar, llegir paràgrafs avorrits, entendre què falla i corregir-ho ell mateix. Això és **metacognició**: adonar-te d'allò que no saps i reconstruir la teva idea. La IA, en eliminar el problema d'arrel i donar la solució mastegada, roba tot aquest procés.

- **El problema de la verificació**: L'amenaça més gran de l'estudi. Tothom assumeix que hi haurà supervisió humana —«l'humà en el bucle»— per validar el que produeix la màquina. Però per verificar si el codi d'un banc o de l'ordinador d'un avió és correcte necessites un ull clínic espectacular, la capacitat de detectar errors minúsculs. Si els treballadors aprenen la professió delegant tota la feina bruta des del primer dia, **mai no construiran aquest ull crític**. Estaríem formant generacions de supervisors incapaços de supervisar res: quan la màquina al·lucini un concepte de manera subtil, l'humà ho mirarà per sobre, dirà «té bona pinta» i ho aprovarà.

- **Els tres patrons que fracassen**: L'estudi no diu que la IA sigui dolenta per aprendre, sinó que el que mana és **com s'utilitza**. Van classificar els usuaris en sis perfils d'interacció segons la implicació cognitiva, i tres treien notes per sota del 40%. La **delegació a l'IA**: actuar com un simple encaminador humà, copiar l'enunciat, enganxar-lo, demanar el resultat final i lliurar-lo. La **dependència progressiva**: començar llegint i intentant entendre-ho, però claudicar quan l'exercici es complica —«acaba-ho tu». I la **depuració iterativa**: cada cop que surt un error, no preguntar-se per què falla, sinó copiar el text vermell de la pantalla i llençar-lo a la IA amb un «arregla-ho», com si fos el corrector del Word.

- **El mite de la memòria muscular, fulminat**: Van comprovar si transcriure manualment el codi de la IA, lletra a lletra, donava millors notes que copiar i enganxar. **Zero diferència.** Prémer tecles sense pensar és una acció buida: és com passar mecànicament els apunts del company més llest el dia abans de l'examen. Tens els papers, però al teu cervell no hi ha res estructurat.

- **Els tres patrons que sí que funcionen**: Alguns perfils, amb exactament la mateixa eina, van superar el **65%** al test, igualant el grup sense IA. Havien entès que la IA no és un becari a qui delegues, sinó un tutor hiperintel·ligent. La **generació i després comprensió**: demanar el codi sencer, però invertir tot el temps guanyat a interrogar-la («per què has fet servir aquesta funció aquí?», «què passa si canvio això?») fins a entendre l'arquitectura — buscant deliberadament la fricció que s'havien saltat. L'**híbrid**: demanar codi i explicació teòrica alhora. I la **indagació conceptual**, la més efectiva: negar-se rotundament a demanar codi i fer servir la IA només com un cercador avançat («què vol dir exactament l'asincronia aquí?»); un cop clar el concepte, tancar el xat i escriure-ho tot des de zero. La màquina és un mirall: si vols escaquejar-te, t'ho posa en safata; si vols ser un expert, és el millor llibre interactiu del món.

- **La il·lusió de competència**: La part emocional és reveladora. El grup sense IA va acabar frustrat i perdut, xocant contra murs de codi trencat... i va valorar l'experiència amb notes altíssimes de diversió, amb la dopamina del «he resolt el trencaclosques jo sol». El grup de la IA confessava sentir-se desmotivat i **lazy**, com qui fa trampes al solitari: «tinc la idea general, però em falten massa buits de coneixement». Tenien l'obra acabada sense saber on eren les canonades. Confondre **accés a la informació** amb **possessió de coneixement** és letal.

- **L'exosquelet cognitiu**: La imatge central de l'estudi. Un operari es posa un vestit robòtic i de sobte aixeca tones amb una mà: superproductiu i ràpid. Però si deixa que la màquina faci tota la força cada dia durant anys, els seus músculs biològics s'atrofien; el dia que marxa la llum i s'ha de treure el vestit, no només no és més fort que abans, sinó que està esquelètic i afeblit. La ment funciona amb el mateix principi: la incomoditat de rumiar, d'estar mirant un error fixament una bona estona, és precisament la fàbrica on el cervell crea el talent real. **Si elimines la fricció mental, bloqueges directament el procés d'aprenentatge.**

- **Reflexió final — el deute intel·lectual corporatiu**: Avui les empreses premien la velocitat. Si un treballador entrega el doble delegant-ho tot sense entendre res, se l'aplaudeix. Això genera un **deute intel·lectual corporatiu**: es paga avui en eficiència a canvi de la ignorància de demà. La pregunta incòmoda és quant trigarà una gran tecnològica a patir una caiguda massiva dels seus servidors i adonar-se que no li queda ni un sol humà a l'edifici que sàpiga com funciona l'arquitectura del sistema des de la base — només gent experta a parlar amb l'exosquelet, justament el dia que l'exosquelet està apagat. La propera vegada que engeguem el GPS per anar on ja sabem anar, potser val la pena aturar-se i preguntar-se si aquesta comoditat ens allibera o si ens està esborrant lentament el mapa intern que ens permetria trobar el camí a casa passés el que passés.

Aquest episodi és la versió llarga i en català de la càpsula de l'[Episodi 014: L'impost ocult de la IA](/podcast-del-doctor/episodi/014-impost-ocult-habilitats-ia), que resumeix el mateix estudi en 54 segons. Connecta directament amb l'[Episodi 012: L'especificació és el nou codi](/podcast-del-doctor/episodi/012-especificacio-nou-codi) —si la feina humana es desplaça cap a especificar amb rigor, cal entendre a fons allò que demanes— i amb l'[Episodi 011: El parany dels acomiadaments per IA](/podcast-del-doctor/episodi/011-parany-acomiadaments-ia), on ens preguntàvem quines habilitats humanes conserven valor. També dialoga amb l'[Episodi 007: Com domar el geni trampós](/podcast-del-doctor/episodi/007-com-domar-el-geni-trampos), sobre com tractar la màquina perquè treballi a favor teu i no en contra.

## Fonts

- [How AI Impacts Skill Formation (arXiv:2601.20245)](https://arxiv.org/abs/2601.20245) — Judy Hanwen Shen i Alex Tamkin. Assaig aleatoritzat amb 52 programadors aprenent la llibreria asíncrona Trio amb i sense assistència d'IA: efectes sobre comprensió conceptual, lectura de codi i depuració, i els sis patrons d'interacció detectats
- [Transcripció automàtica](/podcast-del-doctor/sources/015-ia-atrofia-les-habilitats-transcripcio.txt) — Generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
