---
audio_file: "https://archive.org/download/podcast-del-doctor-037-com-et-rastreja-la-teva-smart-tv/037-com-et-rastreja-la-teva-smart-tv.mp3"
audio_size: 7702743
chapters_file: "037-com-et-rastreja-la-teva-smart-tv-chapters.json"
date: '2026-10-18'
description: "La Smart TV envia un quilobyte per minut i amb això en té prou per saber què mires, encara que vingui d'una PlayStation per HDMI. A partir del vídeo de Slidebean, desgranem l'ACR (un Shazam per a la imatge que redueix cada fotograma a 8 bytes), com la IP de casa uneix el que mires amb el que compres, l'origen de la tecnologia a Vizio, les demandes de Texas contra Samsung, LG i TCL, i els números que ho expliquen tot: Roku perd diners amb el maquinari i en guanya 26 vegades més amb els anuncis."
duration: '16:02'
episode_number: 37
season: 1
soundbite_start: 724.2
soundbite_duration: 59.1
soundbite_title: "Roku perd 82 milions amb els televisors i en guanya 2.150 amb els anuncis: el producte ets tu"
sources:
- title: "Slidebean: The Most Profitable Part of Your TV"
  url: "https://www.youtube.com/watch?v=t_GK06_3UY8"
  description: "Vídeo de Slidebean (octubre de 2026), eix central de l'episodi: com funciona l'ACR, qui compra les dades, les demandes contra els fabricants i el model de negoci de les Smart TV"
- title: "UCL & UC Davis: Watching TV with the Second-Party: A First Look at Automatic Content Recognition Tracking in Smart TVs"
  url: "https://arxiv.org/html/2409.06203v1"
  description: "Estudi acadèmic del 2024 que mesura el trànsit ACR de televisors Samsung i LG segons la font de vídeo i la configuració de privacitat"
- title: "Samsung Ads: ACR Guide"
  url: "https://iabcanada.com/wp-content/uploads/2022/09/Samsung-Ads-ACR-Guide-CA.pdf"
  description: "Guia comercial de Samsung Ads sobre com fa servir el reconeixement automàtic de contingut per a publicitat"
- title: "ProPublica: Own a Vizio Smart TV? It's Watching You"
  url: "https://www.propublica.org/article/own-a-vizio-smart-tv-its-watching-you"
  description: "Reportatge del 2015 que va destapar el rastreig dels televisors Vizio"
- title: "TVREV: Zeev Neumeier and the Origins of TV Analytics"
  url: "https://www.tvrev.com/news/zeev-neumeier-inscape-vizio-tv-analytics-interview"
  description: "Entrevista amb el creador de la tecnologia ACR de Cognitive Networks (després Inscape, de Vizio)"
- title: "Samsung Ads & Experian"
  url: "https://www.samsung.com/us/business/samsungads/blog/samsung-ads-and-experian"
  description: "Acord entre Samsung Ads i l'agregador de dades Experian"
- title: "Texas Attorney General: acord amb Samsung"
  url: "https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-secures-major-agreement-samsung-ensure-texans-are-protected-smart-tvs"
  description: "Acord de privacitat entre l'estat de Texas i Samsung sobre les Smart TV"
- title: "Texas Attorney General: acord amb LG"
  url: "https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-major-agreement-lg-protect-texans-privacy-and-stop-data-being"
  description: "Acord de privacitat entre l'estat de Texas i LG"
- title: "Gamers Nexus: 216,000,000 Spy TVs | The LG Smart TV Problem"
  url: "https://www.youtube.com/watch?v=6IFVTcM28KA"
  description: "Investigació de Gamers Nexus sobre el que recullen els televisors LG"
- title: "Decrypt: LG TV Privacy and Arbitration"
  url: "https://decrypt.co/377637/lg-tv-might-be-listening-even-when-off"
  description: "Article sobre la privacitat dels televisors LG i la clàusula d'arbitratge forçós"
- title: "Roku: Form 10-K 2025"
  url: "https://image.roku.com/bWFya2V0aW5n/Roku-2025-Form10-K.pdf"
  description: "Informe anual de Roku a la SEC, amb els resultats del maquinari i de la plataforma publicitària"
- title: "Avery Wang: An Industrial-Strength Audio Search Algorithm (Shazam)"
  url: "https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf"
  description: "Article original de l'empremta d'àudio de Shazam, la idea en què es basa l'ACR"
- title: "pHash: Perceptual Hashing"
  url: "https://www.phash.org/docs/design.html"
  description: "Disseny dels hashos perceptuals d'imatge, com el que redueix un fotograma a 64 bits"
- title: "Transcripció automàtica de l'episodi"
  url: "/podcast-del-doctor/sources/037-com-et-rastreja-la-teva-smart-tv-transcripcio.txt"
  description: "Transcripció completa generada amb OpenAI Whisper (model large-v3), amb una passada de correcció posterior d'alguns noms propis (Slidebean, Vizio, Zeev Neumeier, Gracenote)"
thumbnail: "/assets/thumbnails/037-com-et-rastreja-la-teva-smart-tv.png"
title: "Episodi 037: Com et rastreja la teva Smart TV"
---

## Introducció

Desconfiem del mòbil, tapem la càmera del portàtil i mirem de reüll els altaveus intel·ligents, però després pengem un televisor enorme al menjador, el connectem a la wifi i acceptem els termes sense llegir-los. Aquest episodi segueix la investigació de Slidebean, que va comprar televisors de diverses marques, els va connectar a la xarxa i va trobar que continuaven enviant dades fins i tot mentre s'hi veia una Apple TV o una PlayStation. Expliquem què envien, qui ho rep i per què, per a molts fabricants, el televisor és només l'excusa per entrar a casa.

## Temes tractats

- **ACR, el Shazam de la imatge**: la tele envia un quilobyte per minut, massa poc per a cap imatge. El truc és el reconeixement automàtic de contingut (ACR). Igual que Shazam no envia la cançó sinó una empremta, el televisor redueix un fotograma 4K de 8,3 milions de píxels a una quadrícula de 32×32, hi fa 64 comparacions de brillantor i textura, i en surt una cadena de 64 bits: 8 bytes. Aquesta empremta es compara amb bases de dades com la de Gracenote, que ja tenen indexades pel·lícules i programes.

- **Per què l'HDMI xifrat no protegeix res**: el senyal d'un Blu-ray o d'una consola arriba xifrat, però el processador del televisor l'ha de desxifrar per encendre la pantalla. L'ACR l'analitza just en aquest punt. L'estudi del 2024 de la University College London i la UC Davis ho confirma: l'ACR envia dades tant si mires l'antena com si jugues per HDMI. Només s'atura a la pantalla d'inici, compartint el mòbil o dins d'apps com Netflix, que ja recullen les seves pròpies dades.

- **La IP com a pegament**: no cal iniciar sessió perquè t'identifiquin. Agregadors com Experian compren galetes, compres i registres de moltes fonts i els lliguen a l'adreça IP de casa. Quan la tele envia l'empremta des de la mateixa IP, el que mires s'uneix al que compres. Plataformes com The Trade Desk, amb dades de Samba TV, poden vendre anuncis per a perfils tan concrets com aficionats a la ciència-ficció que se senten sols. I l'anunciant ja no paga per estimacions d'audiència: l'ACR li confirma el minut exacte en què l'anunci ha sortit a la teva pantalla.

- **L'origen: un cavall de Troia anomenat interactivitat**: la tecnologia ve de Zeev Neumeier i Cognitive Networks. Es va presentar als televisors Vizio com a televisió interactiva, amb finestres per votar mentre miraves *Dexter* o *Homeland*. El mateix Neumeier va dir a Vizio que les dades valien molt més que l'experiència. ProPublica ho va destapar el 2015, i la FTC va acabar multant Vizio amb 2,2 milions de dòlars. El negoci no es va aturar: només es van omplir els menús de textos legals.

- **Texas contra els fabricants**: el desembre de 2025, Texas va demandar els cinc grans fabricants. Samsung va pactar el febrer de 2026, i una tele Samsung configurada com a «tele muda», rebutjant-ho tot, no envia res, però queda gairebé inservible. TCL es va escapar de la demanda per un tecnicisme de jurisdicció i obliga a iniciar sessió amb un compte de Google fins i tot per a les funcions bàsiques.

- **LG i Gamers Nexus**: LG va pactar amb Texas el maig de 2026, però el documental de Gamers Nexus va mostrar televisors capaços de recuperar transcripcions de veu i gravacions de càmeres connectades, i d'escanejar la xarxa local per ARP per identificar mòbils i ordinadors que mai no hi han estat connectats. La resposta d'LG als Estats Units va ser afegir una clàusula d'arbitratge forçós per evitar demandes col·lectives.

- **El maquinari és l'esquer**: segons el 10-K de Roku a la SEC, l'any fiscal 2025 va perdre 82 milions de dòlars venent dispositius i en va guanyar 2.150 amb anuncis i plataforma, unes 26 vegades més. El seu director executiu ho diu clar: el maquinari és un cost d'adquisició de comptes. La divisió de televisors d'LG treia el 2024 un marge del 2% (uns 230 milions) amb els aparells i uns 730 milions amb la publicitat. El televisor és un dispositiu subvencionat, i el producte ets tu.

- **Què es pot fer**: desactivar l'ACR des dels menús és una mitja mesura, perquè una actualització automàtica o uns termes nous la poden desfer. Les mesures completes són aïllar el televisor en una xarxa separada perquè no pugui veure la resta de dispositius de casa, o, més senzill, no connectar-lo mai a internet i fer-lo servir com a pantalla passiva amb un reproductor extern per HDMI.

- **Reflexió final**: si els fabricants accepten perdre diners amb el maquinari per posar un sensor de perfils al menjador, quins seran els següents? Neveres, rentadores, microones i robots aspiradors connectats i barats poden ser els propers cavalls de Troia per cartografiar els nostres hàbits.

## Episodis relacionats

- [Episodi 038: El teu televisor LG t'espia](/podcast-del-doctor/episodi/038-el-teu-televisor-lg-t-espia): la investigació de Gamers Nexus sobre LG que aquí només s'apunta, vista a fons.
- [Episodi 022: El negoci de l'ansietat dels fills](/podcast-del-doctor/episodi/022-el-negoci-de-l-ansietat-dels-fills): el capitalisme de vigilància des del costat de les xarxes socials i l'EdTech.

## Fonts

- [Slidebean: The Most Profitable Part of Your TV](https://www.youtube.com/watch?v=t_GK06_3UY8): vídeo principal de l'episodi
- [UCL & UC Davis: Watching TV with the Second-Party](https://arxiv.org/html/2409.06203v1): estudi del 2024 sobre el rastreig ACR
- [Samsung Ads: ACR Guide](https://iabcanada.com/wp-content/uploads/2022/09/Samsung-Ads-ACR-Guide-CA.pdf): guia comercial de l'ACR de Samsung
- [ProPublica: Own a Vizio Smart TV? It's Watching You](https://www.propublica.org/article/own-a-vizio-smart-tv-its-watching-you): el reportatge que ho va destapar el 2015
- [TVREV: Zeev Neumeier and the Origins of TV Analytics](https://www.tvrev.com/news/zeev-neumeier-inscape-vizio-tv-analytics-interview): entrevista amb el creador de la tecnologia
- [Samsung Ads & Experian](https://www.samsung.com/us/business/samsungads/blog/samsung-ads-and-experian): l'aliança amb l'agregador de dades
- [Texas Attorney General: acord amb Samsung](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-secures-major-agreement-samsung-ensure-texans-are-protected-smart-tvs)
- [Texas Attorney General: acord amb LG](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-major-agreement-lg-protect-texans-privacy-and-stop-data-being)
- [Gamers Nexus: 216,000,000 Spy TVs | The LG Smart TV Problem](https://www.youtube.com/watch?v=6IFVTcM28KA): investigació sobre els televisors LG
- [Decrypt: LG TV Privacy and Arbitration](https://decrypt.co/377637/lg-tv-might-be-listening-even-when-off): la clàusula d'arbitratge d'LG
- [Roku: Form 10-K 2025](https://image.roku.com/bWFya2V0aW5n/Roku-2025-Form10-K.pdf): resultats de maquinari i publicitat
- [Avery Wang: An Industrial-Strength Audio Search Algorithm](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf): l'algorisme de Shazam
- [pHash: Perceptual Hashing](https://www.phash.org/docs/design.html): hashos perceptuals d'imatge
- [Transcripció automàtica](/podcast-del-doctor/sources/037-com-et-rastreja-la-teva-smart-tv-transcripcio.txt): generada amb OpenAI Whisper (model large-v3)

---

**Important:** Aquest episodi ha estat generat amb intel·ligència artificial basant-se en fonts públiques. La transcripció s'ha generat automàticament amb OpenAI Whisper (model large-v3). Consulta sempre les fonts originals per obtenir la informació completa.
