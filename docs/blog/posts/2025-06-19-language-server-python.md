---
categories:
  - Sin categoría
date: 2025-06-19
permalink: /language-server-python
slug: language-server-python
tags:
  - lsp
  - desarrollo
  - herramientas
  - python
---

# Escoger un Python Language Server

En un [artículo anterior](https://franciscopuga.es/blog/2025/05/17/language-server-protocol/) definimos que era Language Server Protocol y cómo funcionaban los Language Server.

En este nos centramos en escoger un Language Server para Python.

## Criterios

Para escoger algo, hay que definir que criterios priorizamos. En el caso de un LS o herramientas relacionadas los criterios podrían ser:

- Rendimiento. Queremos que la respuesta a la mayoría de acciones sea casi inmediata.
- Software libre. Preferimos que la implementación sea software libre.
- Capacidades. Cuantas más capacidades (que refactorings, ...) nos ofrezca el LS o una determinada combinación de LS mejor.
- Fragmentación. Si un LS o herramienta integrada nos da todo lo que necesitamos, mejor que si tenemos que preocuparnos por ver los changelog de 5 herramientas distintas.
- Mantenido. Con tracción en la comunidad, ...
- Multiples entornos. Al menos el lint y el format debe ser consistente entre múltiples entornos: editor (uses NeoVim, PyCharm o vscode), pre-commit y ci. Cómo gestione un refactoring o la navegación no es necesario que sea consistente.

## Opciones

### Pylance / Pyright

Pylance es el LS privativo de Microsoft para Python, basado en la librería / LS (1) libre de tipado estático [Pyright](https://github.com/microsoft/pyright).
{ .annotate }

1.  :man_raising_hand: La distinción entre librería, LS, ... no siempre es clara

Microsoft mantenía un LS libre [python-language-server](https://github.com/microsoft/python-language-server), pero lo discontinuaron en favor de Pylance. Pylance sólo se puede usar con los productos de Microsoft (vscode) y no con editores derivados como Cursor o VSCodium, ni alternativos [como NeoVim](https://github.com/lithammer/nvim-pylance).

Pyright es una buena librería para tipado estático y si bien se puede usar como LS en cualquier editor, no es una buena alternativa porqué carece de funcionalidades básicas como añadir `imports` de forma automática.

Este dúo tiene más cosas "molestas":

- Están escritos en typescript. No es algo malo de por si, pero no deja de ser extraño
- Las capacidades de refactoring son malas. Rename, Extract Variable, Move Symbol, y a veces se consigue usar el Extract Method.
- Privativo y no usable en otros editores

### basedpyright

[basedpyright](https://github.com/DetachHead/basedpyright) es un fork libre de Pyright que incorpora funcionalidades de Pylance.

Más o menos los mismos comentarios que para Pylance/Pyright

Personalmente he tenido malas experiencias al usarlo en Cursor. Probablemente se deba a una mala configuración, pero tengo la sensación de que se queda trabado a menudo.

### Jedi / Rope

Ni [Jedi](https://github.com/davidhalter/jedi), ni [Rope](https://github.com/python-rope/rope) son LS. Ambas son dos librerías históricas del ecosistema Python. Rope se centra en refactoring y Jedi en análisis estático, autocompletado y navegación.

Ninguna de las dos proporciona formatting, linting o tipado lo que debería alcanzarse mediante otras librerías cómo mypy (tipado) y ruff (formatting y linting).

Si bien no son un LS, si que son la base para varios Language Server.

### python-lsp-server

[python-lsp-server](https://github.com/python-lsp/python-lsp-server) se puede decir que es el LS que proviene de la comunidad. Es mantenido por el equipo de [Spyder IDE](https://www.spyder-ide.org/).

Tras instalarlo proporciona el LS bajo el comando `pylsp`.

Está basado en jedi que proporciona: Completions, Definitions, Hover, References, Signature Help, and Symbols. Si están instaladas en el entorno se integra de forma nativa con otras librerías cómo rope (capacidades básicas) y flake8. Y el propio LS admite plugins para integrarse con más librerías: mypy, ruff, más refactorings de rope, ...

Tiene dos problemas grandes:

- La [configuración](https://github.com/python-lsp/python-lsp-server/blob/develop/CONFIGURATION.md) es un caos, porqué interactúa todo con todo
- [No tiene plugin para vscode](https://github.com/python-lsp/python-lsp-server/issues/614) / cursor / vscodium. Y no tiene pinta de haberlo en el [futuro](https://github.com/python-lsp/python-lsp-server/issues/39)

Al menos en proyectos pequeños, parece ser que con proyectos grandes puede ser lento, no es una mala opción (si hubiera plugin), y es la única alternativa ahora mismo que proporciona un refactoring decente. La mejor forma de probarlo es con [Zed](https://zed.dev/docs/languages/python).

??? note "Notas sobre la configuración no muy ordenadas"

    ¿[Tiene sentido instalar pylsp-ruff o mejor directamente ruff](https://github.com/python-lsp/python-lsp-ruff/issues/89)?. En principio ruff mejor individual

    ```bash
    pip install python-lsp-server pylsp-rope pylsp-mypy

    # ¿Mejor con wesockets?
    # pip install 'python-lsp-server[websockets]'
    # pylsp --ws --port [port]
    ```

    Configuración para usar el plugin externo de rope

    ```text
    pylsp.plugins.pycodestyle.enabled = false
    pylsp.plugins.flake8.enabled = false
    pylsp.plugins.autopep8.enabled	= false
    pylsp.plugins.mccabe.enabled	= false
    pylsp.plugins.pycodestyle.enabled	= false
    pylsp.plugins.pyflakes.enabled	=false
    pylsp.plugins.pylint.enabled	=false
    pylsp.plugins.yapf.enabled	= false

    # set pylsp.plugins.rope_autoimport.enabled to true
    # This enables both completions and code actions. You can switch them off by setting pylsp.plugins.rope_autoimport.completions.enabled and/or pylsp.plugins.rope_autoimport.code_actions.enabled to false

    pylsp.plugins.rope_autoimport.enabled	= ???
    pylsp.plugins.rope_completion.enabled	= ???

    pylsp.plugins.rope_rename.enabled = false
    pylsp.plugins.jedi_rename.enabled = false
    pylsp.plugins.pylsp_rope.rename = true
    ```

    Configuración de rope en pyproject.toml

    ```toml
    # https://rope.readthedocs.io/en/latest/configuration.html
    [tool.rope]
    split_imports = true
    autoimport.aliases = [
        ['dt', 'datetime'],
        ['mp', 'multiprocessing'],
    ]
    ```

### Pyrefly

[Pyrefly](https://pyrefly.org/) es el último en llegar al mercado. CLI, type checker y LS mantenido por Meta.

Es rápido, tiene plugins para Code y derivados y funciona bien.

Lo malo es que no tiene ningún refactoring en este momento.

### Ruff

Ruff tiene desde hace tiempo un LS integrado para el formatting y linting.

En este momento están en proceso de integrar dentro de la propia herramienta el type checker y convertirlo en un posible substituto completo para los otros LS.

### PyCharm

No cumple nuestros requisitos iniciales, pero a día de hoy es el IDE con mejor soporte para Python.

Merece la pena probarlo.

### Otras alternativas

- [jedi-language-server](https://github.com/pappasam/jedi-language-server) es una propuesta minimalista que sólo implementa expone las capacidades que tenga jedi
- [anakin-language-server](https://github.com/muffinmad/anakin-language-server) es poco popular. Se basa en jedi y permite integración con mypy, yapf, pyflakes y pycodestyle
- [PyDev on Visual Studio Code](https://www.pydev.org/vscode/index.html). PyDev es un plugin para trabajar con Python en Eclipse. Al parecer también funciona cómo una extensión para VSCode, pero necesita tener Java instalado.
- [palantir/python-language-server](https://github.com/palantir/python-language-server) Si mantenimiento pylsp es un fork de este.
- [pylyzer](https://github.com/mtshiba/pylyzer) un LS y type checker escrito en rust. Poco mantenimiento.

### Otros LS específicos

Cómo se ve en el caso de ruff, un LS no tiene porqué proporcionar las funcionalidades completas de un lenguaje. Hay LS que cubren aspectos o librerías muy específicas:

- https://github.com/joshuadavidthomas/django-language-server
- https://www.fourdigits.nl/blog/django-template-lsp/

## Conclusiones

PyCharm aparte, y con ánimo de polemizar se puede decir que no hay un soporte tan bueno cómo podría esperarse para Python en los IDEs.

Personalmente en este momento estoy usando Pyrefly con el plugin para Cursor como LS principale, y ruff con su plugin cómo el LS secundario que se encarga del formatting y linting.
