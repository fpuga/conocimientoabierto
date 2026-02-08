---
categories:
  - Sin categoría
date: 2025-09-28
permalink: /estilo-markdown-producido-llm
slug: estilo-markdown-producido-llm
tags:
  - markdown
  - documentation
---

# Estilo de Markdown generado por los LLM

He hecho un estudio no científico del estilo de Markdown que emplean los modelos/aplicaciones más populares.

## Claude.ai - Sonnet 4

- CommonMark
- backticks para código inline y triple backticks (fenced blocks) para bloques de código
- `*` y `**` para italic emphasis y bold emphasis y no `_`
- `- ` para listas, con un sólo espacio de separación
- ` -` listas anidadas con dos espacios
- `1. uno \n 2. dos` para listas ordenadas
- `#` para cabeceras y `underline style`

## Gemini 2.5

Cuando le preguntas a 2.5 tanto flash cómo pro es poco claro dice por ejemplo `Unordered Lists (bullet points) with hyphens (-) or asterisks (*).`. Si insistes dice que usa `-`, pero si luego copias una de sus salidas en realidad usa `*`.

Parece menos consistente que Claude

En general lo que parece ser es:

- No declara un tipo concreto de sabor de markdown
- backticks para código inline y triple backticks (fenced blocks) para bloques de código
- `*` y `**` para italic emphasis y bold emphasis y no `_`
- `* ` para listas, con un sólo espacio de separación
- `   *` listas anidadas con cuatro espacios
- Curiosamente gemini parece usar `1.    mi texto`, pero `* mi texto`, mezcla indentación para ordenadas y desordenadas
- `1. uno \n 2. dos` para listas ordenadas
- `#` para cabeceras y `underline style`

## ChatGPT - GPT5

La respuesta de ChatGPT parece buena pero no lo es. Indica que no tiene reglas claras pero que OpenAI le da unas `system level rules` que seguir. Pero luego dice que usa `*` y `-` indistintamente. Si insistes dice que usa `-` para listas siempre cuando es mentira.

En general lo que parece ser es:

- Prefiere GFM
- backticks para código inline y triple backticks (fenced blocks) para bloques de código
- `*` y `**` para italic emphasis y bold emphasis y no `_`
- `* ` para listas, con un sólo espacio de separación
- `  *` listas anidadas con dos espacios
- `1. uno \n 2. dos` para listas ordenadas
- `#` para cabeceras y `underline style`

## Conclusiones

No he conseguido extraer reglas claras en esta prueba rápida. El objetivo era saber que usaban para configurar el linter/formatter de un modo que los diff no lancen muchas diferencias.

En general este sería el estilo más compatible que se podría usar:

```markdown
# Ejemplo de texto

Un texto con _italic emphasis_ y también **bold emphasis**, en el que tenemos:

- Una lista desordenada
- Con sólo dos items
  - y anidación

## Y una lista ordenada

1. Primer item

- lista desordenada anidada
- con otro item

2. Segundo item con `codigo inline`

## Blockquotes

> Siguen este
> estilo

## Tablas

| Column A | Column B |
| -------- | -------- |
| A1       | B1       |
| A2       | B2       |
```
