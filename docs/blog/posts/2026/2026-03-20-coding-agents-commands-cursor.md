---
categories:
    - Sin categoría
date: 2026-03-19T22:00:00
permalink: /coding-agents-commands-cursor
slug: coding-agents-commands-cursor
tags:
    - llm
    - ai
    - coding-agents
---

# Coding Agentes: Commands en Cursor

??? info "Serie de artículos sobre funcionalidades para inyectar contexto en los coding agents:"

    1. [Funcionalidades de "inyección de contexto"](./2026-03-19-coding-agents-features-for-context-injection.md)
    2. [Commands en Cursor](./2026-03-20-coding-agents-commands-cursor.md)

En esté artículo nos centramos cómo funcionan los _commands_ en Cursor. Las pruebas han sido hechas sobre la versión 2.5.

Saber que hace Cursor _under the hood_ es muy difícil. He probado con HTTP Toolkit pero es difícil de saber que información se envía realmente. Así que no va a ser un proceso científico sino basado en un par de pruebas y en la documentación.

Los commands se introdujeron en [septiembre de 2025](https://cursor.com/changelog/1-6) y recomiendan [substituirlos por skills](https://cursor.com/help/customization/skills#how-do-i-migrate-commands-to-skills) desde [enero de 2026](https://cursor.com/changelog/2-4).

Prácticamente han eliminado toda la documentación referida a los commands:

- Sólo queda una [nota sobre su formato](https://cursor.com/docs/reference/plugins#commands-format) cuando hablan de crear plugins.
- El artículo [Best practices for coding agents](https://cursor.com/blog/agent-best-practices#git-workflows) (de 9 de enero) da una pista de cual es el caso de uso para los _commands_ según Cursor.

Los _commands_ son:

- Ficheros markdown que pueden contener un frontmatter de `name` y `description`. Que no parece valer para nada.
- Van en el `.cursor/commands` del proyecto o de `~`. No busca en subdirectorios.
- Se invocan a demanda del usuario en el chat con `/nombre-del-comando`
- Y una cosa chula es que son _composables_: `/check-compiler-errors and /commit, then create a /pr`.

## Cual es la diferencia con las reglas

Las reglas se usan:

- Siempre
- Bajo criterio del agente
- Cuando lo fuerza el usuario.
- Combinación de patrones sobre los nombres de archivos, criterio del agente, ...

Los comandos funcionan estrictamente bajo demanda del usuario.

Además en Cursor [parece haber cierta lógica interna](https://forum.cursor.com/t/commands-vs-rules-how-are-they-different/133796) asociado al uso de un comando.

Las reglas deberían usarse para definir estándares, _guidelines_, ... que el LLM debe seguir. En definitiva "reglas". Sería un _follow this rules when making a refactor_

Los comandos deberían usarse para pedir al LLM que lleve a cabo una acción y definir los pasos para ejecutarla. Sería un _make a refactor_

Por supuesto hay _overlap_ pero al menos la intención debería ser clara.

## Cual es la diferencia con las skills

El metadata de las skill se carga siempre y el agente decide cuando usar una skill o puede ser forzado por el usuario.

Las skills pueden ser muy complejas y encapsular scripts, ...

Las skills en teoría son un estándar, mientras que los comandos no.

Si hay alguna diferencia a nivel resultado de la ejecución `/commit` vs `skill/commit/SKILL.md` queda para artículos futuros.

## Hay alguna diferencia con referenciar un documento

Una de las cosas que más preocupan es cómo mantener _agent stuff_ compatible entre herramientas. Así que, ¿hay alguna diferencia entre referenciar un documento en el chat con `@` y usar un comando?.

Para comprobarlo he creado un fichero `refine-english.md`

```markdown
# refine-english

## Task

Refine the English prose in the provided file.

- Clarity: Simplify wording to be accessible for non-native speakers. Avoid flowery language.
- Correction: Fix all grammar, spelling, and punctuation errors.
- Constraint: Maintain the original structure and core intent. Focus strictly on clarity and consistency.

## Output Instructions

- Agent must edit the file directly.
- In the agent chat response:
    - Do not summarize minor edits. Only mention changes if they significantly alter the meaning.
    - Refinements & Critiques: Point out logical inconsistencies, suggest deeper structural improvements, or critique the overall flow.
```

Cuando lo uso cómo comando `/refine-english @mydoc.md`:

- Es muy directo (se ve en la cadena de pensamiento). Sabe que tiene que ejecutar unas instrucciones sobre un fichero.
- Sigue bien las instrucciones.
    - Algún documento tenía mezclaba inglés y español. Dejo el texto en castellano intacto y el chat lo indicó directamente "The document is mostly Spanish, consider ..." o veladas "Updated the English parts of ". Hay que estar fino para darse cuenta de "English parts".
    - Había un cacho pequeño de código con un bug. Lo mencionó en la conversación pero no lo corrigió.

Cuando lo uso cómo referencia `@refine-english.md for @mydoc.md`

- Se pasa un tiempo al inicio intentando interpretar que es lo que se está pidiendo.
- Varias veces que lo probé tuvo problemas aplicando parches. ¿Quizá sea porqué estaba en modo "Auto" y no escogió el modelo adecuado para la tarea?
- Directamente tradujo los textos a inglés en todas las ocasiones, y en alguna corrigió por su cuenta los errores en el código.
- Usa un 1% de contexto más (acorde al indicador del chat de cursor)

Cuando lo uso cómo: `please do the tasks followed by @refine-english.md in document @mydoc.md`

- El resultado se parece más al uso del comando y el % de contexto usado es similar.
- Cómo en la referencia decide por su cuenta traducir los textos en español
- Sin problemas aplicando los parches.

Las pruebas anteriores era con el modelo en `Auto`. Al pasarlo a `Sonnet 4.6`

- Las tres formas de usarlo traducen el texto a inglés.
- El contexto es similar pero un 4% superior a usarlo en modo `Auto`.
- Sin problemas aplicando los parches.
- Es difícil de determinar pero el modo comando parece seguir mejor las instrucciones, sobre todo en el formato de salida.
- En ninguno de los casos mencionó el bug en el código

## Conclusiones

En Cursor usar un comando (parece que) frente a referenciar un documento:

- Activa cierta lógica interna que consume menos tokens y sigue mejor las instrucciones.
- En modo `Auto` selecciona modelos distintos que con la referencia.
- No he notado mucha diferencia entre usar `@mydoc.md` y 'mydoc.md'.
- Influye más el modelo que usarlo cómo comando o cómo `@`

Este es uno de los mejores comentaros que he encontrado sobre cómo funcionan estas herramientas:

!!! quote "[Alexandros alexandrosandre](https://forum.cursor.com/t/skills-vs-commands-vs-rules/148875/9), en el foro de Cursor"

    To my understanding you aren't missing anything. What helps myself get through this caos is the following simplified rationale "It is all a lie. Everything is just another prompt." Therefore your usage might not be standard or documented but can work just as fine.

    Not trying to be disrespectful at all with the "lie" here. Product is trying to name and build use cases and follow standards the best they can. And it’s tough.

    It just helps me understand that all we are doing is telling LLMs what to do in a prompt or where to find the longer instructions (aka prompt) to avoid filling up the context. The rest on top is a essentially looping/harnessing/if-this-then-that nothing else.
