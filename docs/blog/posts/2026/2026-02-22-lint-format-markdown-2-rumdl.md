---
categories:
  - Sin categoría
date: 2026-02-28
permalink: /lint-format-rumdl
slug: lint-format-rumdl
tags:
  - herramientas
  - desarrollo
  - markdown
---

# Lint y Format para Markdown (rumdl)

Después del [post anterior](./2026-02-20-lint-format-markdown.md) gracias a [Antón](https://www.galiglobal.com/) descubro una nueva herramienta

## rumdl

[rumdl](https://github.com/rvben/rumdl) es un formatter y linter de Markdown escrito en Rust siguiendo las ideas de `ruff`.

El primer commit es de Febrero de 2025, así que es un proyecto muy reciente con unas 800 estrellas en este momento. Parecen pocas pero para una herramienta que sigue siendo de nicho no está mal. Markdownlint tiene 2k y mdformat 600. Además ha sido adoptado por proyectos como lucene, ULauncher o pyo3.

No usaría este proyecto si fuera una dependencia _core_ porqué para mi tiene varios _red flags_:

- El proyecto tiene apenas un año y muchas features. Tiene pinta de haber mucho LLM y eso necesita mucha destreza para que el mantenimiento no se complique.
- Tiene 25 _contributors_, pero el 98% de los commits son de la misma persona.
- El README (que es gigante) está desincronizado con la documentación. Y la web no está enlazada desde el repositorio.

La herramienta promete mucho y, cumple más requisitos que las herramientas analizados en el anterior post:

- Escrito en rust, es un binario instalable por todos los métodos habituales: uv, npm, curl, ...
- Paridad de reglas con Markdownlint (con algunas extra) y opción para importar la configuración
- Formatter y Linter en la misma herramienta, en un estilo muy `ruff`, parámetros parecidos en la CLI, el formato de configuración, ... lo que se agradece.
- Soporta por defecto varios formatos de Markdown
- Plugins para los editores habituales (LSP en el propio binario) e integración con pre-commit y sistemas varios de CI

Pero, a poco que la he probado hay muchos detalles que no encajan bien con mi forma de trabajo:

- [Es muy agresiva en los `auto-fix`](https://github.com/rvben/rumdl/issues/472)
- La configuración de las reglas se vuelve complicada. Por ejemplo hay varios bugs en torno a la regla [blanks-around-headings](https://rumdl.dev/md022/) y después de varias pruebas no he conseguido que simplemente me elimine todas las líneas en blanco antes el `H1` que prettier hace sin problemas.

## Conclusiones

`rumld` es una herramienta con potencial. Merece la pena probarla y ver si encaja, pero en mi caso, esperaré un par de meses antes de volver a probarla.
