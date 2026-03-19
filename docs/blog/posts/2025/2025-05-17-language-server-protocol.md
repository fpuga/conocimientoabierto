---
categories:
  - Sin categoría
date: 2025-05-17
permalink: /language-server-protocol
slug: language-server-protocol
tags:
  - lsp
  - desarrollo
  - herramientas
---

# Language Server Protocol

Language Server Protocol (LSP) define un conjunto de mensajes JSON-RPC y estructuras de datos que permiten que el servidor (Language Server) exponga que capacidades (_language services_) ofrece y un cliente (generalmente un IDE) las consuma.

Estas capacidades son las habituales para una herramienta de programación: autocomplete, refactoring, navegación (go to definition, ...), type checking, ...

_Este no es un artículo en profundidad sobre herramientas de desarrollo, me he tomado algunas licencias poéticas porqué sólo quiero situar el contexto para artículos posteriores_.

## Antes de LSP

Se puede argumentar que, antes, la diferencia principal entre un IDE y un editor, era que el IDE incluía de serie y dentro de su propio código funcionalidades que interpretaban el texto cómo "código fuente" y no cómo otro texto cualquiera. Así proporcionaban capacidades de formateado del código, análisis estático (lint), autocomplete, moverse entre la definición y el uso de un símbolo, ...

Los editores en cambio no tenían estas capacidades de forma nativa. Pensemos en PyCharm o PyDev (alguien se acuerda de la versión de Eclipse para Python), frente a Vim, Emacs o incluso Atom.

Lo que había era librerías (o aplicaciones) que daban estas capacidades en el "terminal". En el mundo Python teníamos (tenemos) cosas cómo jedi (para autocomplete y navegación), rope (para refactorings y autocomplete), flake8 (para linting), yapf (para formateado), ...

La solución natural era que los editores tuvieran plugins que usando la API nativa de cada editor se comunicaran de alguna forma no estándar con la herramienta de turno. Así aparecieron millones de plugins. Podíamos tener cosas cómo (_nombres inventados_) atom-yapf (que sólo daba formato con yaps), atom-python-linter (que te dejaba escoger entre flake8 o pylint o los dos a la vez), atom-formatter (que vale para distintos lenguajes), ...

Mantener ese ecosistema tanto a nivel desarrollo cómo a nivel uso, que funciona con que, que instala el plugin y que tengo que instalar yo, ... era un caos. Y cada implementación era específica para un servidor y una librería.

## Porqué un linter es mejor que un IDE

Hay acciones cómo el autocomplete, navegación o refactoring que sólo tiene sentido en el entorno de desarrollo. Cada persona del equipo decide que herramientas se le adaptan mejor.

Pero también hay acciones, lint y format sobre todo, que son decisiones de equipo y hay valor en que estén disponibles en cualquier entorno: editor, pre-commit, ci, ...

Por ello resulta útil que ciertas herramientas sean independientes del IDE y se puedan usar vía plugin o LSP.

## Nace LSP

En 2016 de la mano de VSCode, Microsoft publica LSP que se acaba convirtiendo en un estándar abierto _de facto_ de la industria.

La principal ventaja es desacoplar las herramientas de los editores:

- Consistencia en diferentes entornos: Las mismas reglas pueden aplicarse en distintos editores, pre-commit, ...
- Evita duplicación de esfuerzos
  - Los desarrolladores de lenguajes solo necesitan crear un servidor de lenguaje y funcionará con cualquier editor
  - Los editores sólo necesitan implementar soporte para LSP y no para cada herramienta por separado
- No sólo lenguajes de programación. Un LSP puede servir para DSL y otros, por ejemplo la configuración de Ansible.
- Arquitectura cliente servidor. El servidor ni siquiera tiene que correr en el mismo entorno que el cliente

## Descripción de alto nivel

[Este artículo de VSCode](https://code.visualstudio.com/blogs/2016/06/27/common-language-protocol) nos da una buena idea del funcionamiento a alto nivel:

> Here’s an example of how a tool and a language server could communicate semantic information during a routine editing session:
>
> The user opens a file (referred to as a _document_) in the tool: The tool notifies the language server that a document is open (`didOpen`) and that the information about that document is maintained by the tool in memory.
>
> The user makes edits: The tool notifies the server about the document change (`didChange`) and the semantic information of the program is updated by the language server. As this happens, the language server analyses this information and notifies the tool with the errors and warnings (`diagnostics`) that are found.
>
> The user executes 'Go To Definition' on a symbol: The tool sends a `definition` request to the server. The server responds with a `uri` of the document that holds the definition and the `range` inside the document. Based on this information, the tool can open the corresponding document at the defining position.
>
> The user closes the document (file): A `didClose` notification is sent from the tool, informing the language server that the document is now no longer in memory and instead maintained by (i.e. stored on) the file system.
>
> This communication, which takes place over JSON-RPC, happens many times over the course of a typical session.

## Capacidades del LSP y el Editor

En [este artículo](https://medium.com/@malintha1996/understanding-the-language-server-protocol-5c0ba3ac83d2) se describe bastante bien el proceso de inicialización e intercambio de capacidades.

Ni el editor, ni el LS tienen porqué implementar todas las posibles capacidades definidas en el estándar. Cuando arranca el servidor se lleva a cabo un intercambio de mensajes en el que cada parte dice lo que quiere y lo que puede hacer.

Imaginemos por ejemplo un LS puede tener la capacidad de hacer un refactoring de _Extract function_ pero en la GUI no hay ese menú.

Tenemos un ejemplo claro en el mundo Python, ruff incorpora su propio LS, pero (a día de hoy) sólo provee capacidades de format y lint, y no por ejemplo de refactoring. El editor (y la desarrolladora que tiene que configurar el editor) es responsable de no liarse y coordinar que el refactoring debe hacerse a través de un LS (PyLance, python-lsp-server, ...) y el formateado a través de ruff.

## Fragmentación

Los LSP suenan [al conocido comic de XKCD sobre los standards](https://xkcd.com/927/). Es una nueva tecnología y port tanto fragmenta más al mercado porqué nadie está obligado a usarla.

Sigue habiendo editores con plugins independientes, en Python hay un montón de LS: ruff, PyLance, BasedPyRight, jedi-language-server, python-lsp-server, [PyDev](https://www.pydev.org/vscode/index.html).

Además en muchos casos los LS no implementan las capacidades por si mismos. Algunas las implementan y otras las delegan a otras herramientas de forma "nativa" o mediante plugins.

Por ejemplo PyLance es un LS privativo de Microsoft para Python que sólo funciona en VSCode (y no en otras versiones como Cursor o VSCodium). Muchas funcionalidades (syntax errors, ...) provienen de PyRight que es una librería libre también de Microsoft pero hay funcionalidades como los imports automáticos que están sólo en PyLance, y otras funcionalidades cómo formateado PyLance las ofrece a través de integración con yapf, ruff, ...

## Conclusión

Entender cómo funcionan las herramientas que usamos para desarrollar no está de más, y los LS se han convertido en una de las más útiles.

## Referencias

- [Language Server Protocol en Wikipedia](https://en.wikipedia.org/wiki/Language_Server_Protocol)
- [Página oficial de LSP](https://microsoft.github.io/language-server-protocol/)
