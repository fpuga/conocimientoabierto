---
categories:
    - Sin categoría
date: 2026-03-19T14:00:00
permalink: /coding-agents-features-for-context-injection
slug: coding-agents-features-for-context-injection
tags:
    - llm
    - ai
    - coding-agents
---

# Coding Agentes: Funcionalidades de "inyección de contexto"

??? info "Serie de artículos sobre funcionalidades para inyectar contexto en los coding agents:"

    1. [Funcionalidades de "inyección de contexto"](./2026-03-19-coding-agents-features-for-context-injection.md)
    2. [Commands en Cursor](./2026-03-20-coding-agents-commands-cursor.md)

Los _coding agents_ ofrecen varias funcionalidades para lo que podemos llamar inyectar contexto explicita o implicitamente:

- **prompt**: Ya sea _user prompt_, _system prompt_, ...
- **referencias**: En el prompt también podemos pedir a la herramienta que incluya el contenido de un fichero con `@` o con instrucciones.
    - Los modelos y las herramientas son complejos. No se comportan todas igual, ni el mismo modelo hace siempre lo mismo. Tampoco es lo mismo referencia una imagen binaria que se suele hacer en peticiones distintas que un md.
    - La forma en que la herramienta marca o incluye este contexto adicional también puede variar.
    - El concepto de [memory banks](https://tweag.github.io/agentic-coding-handbook/WORKFLOW_MEMORY_BANK/) encaja aquí y en `AGENTS.md`
- **AGENTS.md**: Siempre introduce en el contexto el fichero en la raíz del repo. Algunas herramientas admiten ficheros en subdirectorios y los adjuntan cuando se accede a un fichero en ese directorio. Puede actuar cómo un [índice que adjunte otros documentos](../2025/2025-12-11-agents-md-and-at-character-to-reference-documents.md):
    - Con `@`. Debería leerlo e incluirlo siempre.
    - Condicionalmente mediante instrucciones `read 'testing.md' when writing tests`
- **commands**: Escribimos en el chat `/fix-bug in my_file.py`, y envía al modelo `fix-bug.md` que está en una ruta predeterminada junto al resto del contexto.
- **rules**: No todas las herramientas las tienen. Suelen ser ficheros md con un frontmatter que indica cuando se debe usar la regla. Es la herramienta y el modelo quien decide que reglas leer, pero el usuario puede forzarlo.
- **hooks**: Las incluyo porqué son un buen substituto a ciertas instrucciones (estén donde estén). En lugar de `execute format.sh and lint.sh after making changes", un hook puede correrlos. De hecho las instrucciones pueden ser ignoradas y el hook no.
- **MCP**
- **Skills**. Un directorio, en una ruta predefinida de la herramienta, que tiene dentro un fichero `SKILL.md` y otros _assets_. Tienen metadatos cortos de nombre y descripción que se inyectan siempre en el contexto. El LLM decide cuando una skill aplica en base a los metadatos o el usuario puede forzar su uso.
    - Hay un par de cosas que no me gustan de los skill. O que si se retocara la spec podrían ser un total substituto a los comandos. Los comandos se cargan y ejecutan exclusivamente bajo demanda del usuario. Las skills no.
    - [La spec](https://agentskills.io/specification#progressive-disclosure) dice que los metadatos se cargan siempre.
    - El LLM decide cuando cuando leer y aplicar la skill en base a la vaga descripción
    - No se pueden tener "infinitas" skills. Para que el LLM no se lie decidiendo, y para no consumir contexto. A pongamos 20 tokens por skill, 100 skill es un 1% del contexto habitual de 200k.
- **Extensiones o Plugins**. Depende de la herramienta, pero la mayoría incluye alguna forma de empaquetar combinaciones de lo anterior y otras extensiones de comportamiento.

En próximos artículos iremos viendo con más detalle algunas de estas funcionalidades, cómo se comportan en distintas herramientas y cómo se relacionan entre sí.
