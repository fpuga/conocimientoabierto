---
categories:
  - Sin categoría
date: 2026-01-04
permalink: /tool-config-file-formats
slug: tool-config-file-formats
tags:
  - cli
  - desarrollo
  - herramientas

draft: true
---

# Formatos para ficheros de configuración de herramientas

En cualquier repositorio de código de una aplicación web es fácil que nos encontremos una decena de ficheros de configuración para las herramientas de desarrollo: git; linters y formatters de python, js, bash, md; pre-comit, package.json y pyproject.toml, ...

Cada una de estas herramientas puede ir desde no tener un fichero propio [cómo shfmt que usa .editorconfig](https://github.com/patrickvane/shfmt?tab=readme-ov-file#description), hasta una herramienta con pocas opciones de configuración cómo [prettier que se puede configurar](https://prettier.io/docs/configuration) a través de aproximadamente 6 formatos con cuatro nombres distintos (sin contar extensiones).

Por desgracia, desde mi punto de vista, existe poca estandarización en este punto y pocas (ruff) [implementan mi sistema preferido](https://docs.astral.sh/ruff/configuration/#config-file-discovery), configurar overrides en el fichero del lenguaje (pyproject.toml) y extender de un fichero en una ruta predeterminada, o cómo prettier poder publicar paquetes con la configuración.

No es que sea crítico para la experiencia de desarrollo pero últimamente me ha dado por pensar si hay una forma de organizarlo que:

- Mejore la consistencia y por tanto reduzca la carga cognitiva
- Reduzca los errores a la hora de escribir la configuración
- Facilite actualizar configuraciones y herramientas cuando tienes una docena de repositorios activos a la vez

Las reglas que estoy empezando a seguir son:

## Formato del fichero

En primer lugar escojo lenguajes de programación: `prettier.config.js` y no `.prettierrc.json`

- Si en algún momento necesito una configuración dinámica no es necesario cambiar el formato
- Admite comentarios
- Funciona el formatter que se esté usando
- El linter y type checking del LSP en general funcionará sin problemas. Aunque según el lenguaje/editor/formato puede ser necesario descargar un esquema adicional.
- Es [a lo que tienden las herramientas](https://eslint.org/docs/latest/use/configure/configuration-files-deprecated), sobre todo en javascript.

Sólo uso JSON si no hay otra opción. Fundamentalmente porqué no admite comentarios.

En general prefiero TOML sobre YAML, pero teniendo en cuenta que hay mucho YAML obligatorio, en realidad me da un poco igual

## Nombre del fichero

Usar extensiones siempre que sea posible: `.prettierrc.json` y no `.prettierrc`. Confunde menos a los editores.

Uso `.yaml` y no `yml`, no entiendo las ganas de abreviar esto, es cómo si pusiéramos `.jsn`.

Uso los nombres preferidos [en la documentación](https://docs.docker.com/compose/intro/compose-application-model/#the-compose-file) si hay alguno: `compose.yaml` y no `docker-compose.yml`

Intento mantener nombres lo más consistentes posibles. Dado que tengo un `vite.config.js` y un `eslint.config.js` _obligatorios_ uso también `prettier.config.js`.

Prefiero evitar el `.` al principio:

- Hay herramientas que herramientas que directamente lo evitan
- Encuentro difícil justificar tener un `jsconfig.json` pero luego tener un `.ruff.toml`

## Documentación de varias herramientas.

- https://github.com/koalaman/shellcheck/blob/master/shellcheck.1.md#rc-files .shellcheckrc y shellcheckrc algo tipo ini file
- shfmt https://github.com/mvdan/sh/blob/master/cmd/shfmt/shfmt.1.scd#description a través de .editorconfig
- https://docs.astral.sh/ruff/configuration/ pyproject.toml, ruff.toml, or .ruff.toml
- https://prettier.io/docs/configuration muchas opciones
- https://github.com/DavidAnson/markdownlint-cli2?tab=readme-ov-file#configuration varios nombres usamos https://github.com/DavidAnson/markdownlint-cli2/blob/main/test/markdownlint-cli2-mjs/.markdownlint-cli2.mjs
- eslint.config.js
