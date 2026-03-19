---
categories:
  - Sin categoría
date: 2026-02-20
permalink: /lint-format-markdown
slug: lint-format-markdown
tags:
  - herramientas
  - desarrollo
  - markdown
---

# Herramientas de Lint y Format para Markdown

!!! note

    No te pierdas la continuación de este artículo [hablando de la herramienta rumdl](./2026-02-22-lint-format-markdown-2-rumdl.md)

Llevo bastante tiempo usando `markdownlint-cli2` y `prettier` para linting y formatting de Markdown, pero no tenía un análisis de las herramientas disponibles, para ver si había mejores opciones.

## Requisitos Deseables

- Integración con el IDE. Una buena extensión para VSCode y derivados
- Integración con pre-commit (oficial en el repo, no sólo ejecución local)
- Una sola herramienta mejor que varias herramientas. En todo caso el linter y el formatter deben ser compatibles.
- Bien mantenida, popular, ...
- Rápida
- Rust > Python > Javascript
  - Prefiero herramientas en lenguajes que generan binarios como Rust porqué son más fáciles de instalar y mantener. Luego en Python porqué conozco mejor el ecosistema
- Formato:
  - Mucho Markdown es para LLMs o producido por LLMs. Así que prefiero un [estilo que concuerde](https://franciscopuga.es/blog/2025/09/28/estilo-markdown-producido-llm/).
  - Que se lleve bien con MkDocs, que tiene su propio sabor ([python-markdown](https://github.com/Python-Markdown/markdown), y [python-markdown-extensions](https://github.com/facelessuser/pymdown-extensions))

Aunque preparando el artículo me entero de que [MkDocs está _deprecated_](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/) y Zensical del mismo equipo usará en el futuro (1) CommonMark
{ .annotate }

1. :pray: !Gracias!

## Herramientas

### mdformat

[mdformat](https://github.com/hukkin/mdformat) es un formatter escrito en Python.

- Usa markdown-it-py cómo parser.
- 643 estrellas
- Soporta CommonMark, GFM, MysT
- Tiene plugins para soportar casos particulares como Admonitions, formatear código dentro de fenced blocks, ...
- Opinionated. Pocas opciones de configuración
- Soporta MkDocs [a través de plugin](https://github.com/KyleKing/mdformat-mkdocs):
  - Aunque [hay que probar bien](https://github.com/mkdocs/mkdocs/issues/1835).
- Plugin [no oficial para vscode](https://github.com/hukkin/mdformat/issues/528).
- Tiene soporte para pre-comit

No me acaba de convencer.

### prettier

[Prettier](https://github.com/prettier/prettier) es el estándar para formatear en el ecosistema JavaScript.

- Usa remark-parser como parser
- 50k estrellas
- Soporte para CommonMark, GFM y MDXv1
- Muy buena integración con el IDE
- Es _opinionated_. La única opción específica markdown es [prose-wrap](https://prettier.io/docs/options#prose-wrap)
- No hay [soporte oficial para pre-commit](https://github.com/prettier/prettier/discussions/16227), ni para prek

Una opción que nunca es mala, aunque puede no ser la mejor.

### markdownlint

Bajo este nombre encontramos varias herramientas de lint:

- [Una herramienta escrita en Ruby](https://github.com/markdownlint/markdownlint)
- [Una librería escrita en NodeJS](https://github.com/DavidAnson/markdownlint). Es uno de los linters más populares para markdown
- [Una ClI sobre markdown lint](https://github.com/igorshubovych/markdownlint-cli).
- [Otra CLI sobre markdown lint](https://github.com/DavidAnson/markdownlint-cli2) escrita por la [misma persona](https://dlaa.me/blog/post/markdownlintcli2) que markdownlint.

La que nos interesa es `markdownlint-cli2`.

- Markdown/CommonMark
- pre-commit, github action, [extensión para vscode](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).
- Distintos formatos de salida (xml, json, consola, con colores, ...)
- La configuración es algo confusa, pero los ficheros `.markdownlint-cli2.*` permiten configurar tanto la CLI, cómo la extensión para code, cómo la librería
- El linter usa por debajo el parse [markdown-it](https://www.npmjs.com/package/markdown-it).

[Un artículo sobre la herramienta](https://blog.scottlowe.org/2024/03/01/linting-your-markdown-files/).

A pesar de las confusiones de nombres, y la documentación dispersa no es una mala opción.

### remark

[Remark](https://github.com/remarkjs/remark) no es una herramienta si no un ecosistema en torno a Markdown que a su vez forma forma parte de [unifiedjs](https://unifiedjs.com/).

Por defecto trabaja con ConmmonMark pero tiene plugins para otras versiones.

Es muy configurable, tanto, que entender bien cómo funciona, escoger los plugins y configurar las opciones adecuadas se vuelve complicado.

[Sin soporte oficial para pre-commit](https://github.com/remarkjs/remark-lint/issues/227).

La [extensión de remark-lint para vscode](https://github.com/drewbourne/vscode-remark-lint) que aparece en el README no se actualiza desde 2018. Hay otra [extensión que parece oficial](https://github.com/remarkjs/vscode-remark) que en el momento de escribir esto lleva más de año y medio (Abril/2024) sin actualizarse.

- [remark-parse](https://github.com/remarkjs/remark/tree/main/packages/remark-parse) es la librería que convierte markdown a AST. Es usada también por prettier.
- [remark-stringify](https://github.com/remarkjs/remark/tree/main/packages/remark-stringify). Es la librería que se encarga de convertir el AST a Markdown. Cuando formateamos Markdown remark-parse lo convierte a AST, y remark-stringify lo convierte de nuevo a Markdown. Las reglas que queremos para el formatter son las que admita esta librería más plugins.
- [remark-lint](https://github.com/remarkjs/remark-lint). Es un monorepo que contiene la librería básica de linting y un montón de reglas que están por separadas o en conjuntos llamados "[presets](https://github.com/remarkjs/remark-lint?tab=readme-ov-file#rules)". Pero no es una herramienta, el uso de la librería es a través de remark-cli. Cuando instalamos un preset el paquete base remark-lint va cómo dependencia. Los presets más habituales:
  - [remark-preset-lint-consistent](https://github.com/remarkjs/remark-lint/tree/main/packages/remark-preset-lint-consistent) — rules that enforce consistency
  - [remark-preset-lint-markdown-style-guide](https://github.com/remarkjs/remark-lint/tree/main/packages/remark-preset-lint-markdown-style-guide) — rules that enforce the markdown style guide
  - [remark-preset-lint-recommended](https://github.com/remarkjs/remark-lint/tree/main/packages/remark-preset-lint-recommended) — rules that prevent mistakes or stuff that fails across vendors.
- [remark-cli](https://github.com/remarkjs/remark/tree/main/packages/remark-cli), es la herramienta de línea de comandos para llevar a cabo operaciones.
- [plugins](https://github.com/remarkjs/remark?tab=readme-ov-file#plugins) para casi todo lo que podamos imaginar. Otras versiones de markdown cómo remark-gfm, manipulaciones cómo remark-toc, linting cómo remark-lint, ...

#### Un ejemplo de instalación y uso

```bash
# Instalar la línea de comandos genérica
npm install --save-dev remark-cli

# Instalar plugins cómo remark-toc o un conjunto de reglas
npm install --save-dev remark-preset-lint-markdown-style-guide remark-toc

# Format de un fichero
remark --output readme.md

# Format de un fichero añadiendo el TOC
remark --output --use remark-toc readme.md

# Lint de todos los ficheros acorde a remark-preset-lint-markdown-style-guide
remark --use remark-preset-lint-markdown-style-guide .

# Format de todos los ficheros markdown en el directorio actual
remark . --output

# Lint de todos los ficheros markdown en el directorio actual
remark .

```

#### Un ejemplo de configuración

```yaml
// .remarkrc.yaml
plugins:
  # Check that markdown is consistent.
  - remark-preset-lint-consistent
  # Few recommended rules.
  - remark-preset-lint-recommended
  # Generate a table of contents in `## Contents`
  - - remark-toc
    - heading: contents
settings:
  bullet: "*"
  emphasis: "_"
  strong: "*"
```

## Herramientas Descartadas

### Biome

[Biome](https://github.com/biomejs/biome) es la alternativa a prettier y eslint escrita en rust, pero todavía no implementa todas las reglas ni todos los lenguajes que soporta prettier. No soporta Markdown [por ahora](https://github.com/biomejs/biome/issues/3718).

### PyMarkdown

[PyMarkdown](https://github.com/jackdewinter/pymarkdown) es un linter escrito en Python que cumple pocos de los requisitos.

- Usan su propio parser.
- 109 estrellas
- Soporta CommonMark y GFM
- Tiene soporte para pre-commit
- No parece tener extensión para vscode, ni ningún otro IDE
- Tienen muchas opciones y reglas y es muy configurable

#### dprint

[dprint](https://github.com/dprint/dprint) no es un proyecto al que le hubiera prestado mucha atención si no fuera porqué lo usan Deno y Helix.

Es un "framework" para formatting escrito en Rust que soporta muchos lenguajes a través de plugins, entre ellos Markdown. Por ejemplo tienen un plugin para ruff para formatear Python.

Para markdown usa un [parser](https://github.com/pulldown-cmark/pulldown-cmark) centrado en CommonMark con soporte parcial para GFM. Las reglas de formato son poco configurables. Parece tener integración con pre-commit (no oficial) y vscode, pero no muy mantenida:

Bugs a los que prestar atención:

- [#859](https://github.com/dprint/dprint/issues/859)
- [#442](https://github.com/dprint/dprint/issues/442)

## Otras referencias

- [A brief analysis of markdownlint rule popularity](https://dlaa.me/blog/post/markdownlintanalyzeconfig)

## Conclusiones

Prettier y Markdownlint son las mejores opciones en este momento. Habrá que estar atentos a la evolución de otras herramientas cómo dprint, biome u [Oxc](https://oxc.rs/), y también a lo que salga de Zensical.

Si manipular el Markdown mediante línea de comandos también es de interés remark es una opción a estudiar.
