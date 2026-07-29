---
agent: agent
description: "Genera un nou episodi del Podcast del Doctor: transcripció, upload a archive.org, personalització i deploy"
tools: [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# Generar Episodi del Podcast del Doctor

> ⚠️ **Aquest fitxer no conté el workflow.** És només un pont cap a la font de
> veritat, perquè abans en teníem dues còpies i divergien en silenci.

**Llegeix ara** [`.claude/commands/generate-episode.md`](../../.claude/commands/generate-episode.md)
i segueix-lo al peu de la lletra. Conté el workflow complet: staging, fonts,
transcripció, capítols, soundbite, thumbnail, archive.org i deploy.

Dues coses a tenir en compte en llegir-lo, perquè està escrit per a Claude Code:

- Hi apareix el token `$ARGUMENTS`. És el marcador d'arguments de Claude Code:
  no és literal. Substitueix-lo pels arguments amb què t'hagin invocat a tu
  (i, com diu allà, són **sempre fonts**: URLs d'articles, papers o vídeos).
- Parla de `TaskCreate`/`TaskUpdate` per fer el seguiment dels passos. Fes servir
  l'equivalent que tinguis (`todo`); el que importa és no saltar-se cap pas.

Si el fitxer no existeix o no el pots llegir, **atura't i digues-ho** — no
intentis reconstruir el workflow de memòria.
