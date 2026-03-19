---
categories:
  - Sin categoría
date: 2025-12-11
permalink: /agents-md-and-at-character-to-reference-documents
slug: agents-md-and-at-character-to-reference-documents
tags:
  - llm
  - ai
  - coding-agents
---

# AGENTS.md and the @ to reference documents

This article is just a quick experiment on:

- The difference between referencing a document that the agent reads with the `@` symbol in front or simply by including the path. `@./docs/rule1.md` vs simple `./docs/rule1.md`.
- How to split the rules of the LLM into different documents to avoid "burning" context".

The ideas are based on these two articles:

- [Stop Getting Average Code from Your LLM](https://merowing.info/posts/stop-getting-average-code-from-your-llm/)
- [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)

The first test is with gemini-cli, which by default does not use `AGENTS.md`. [In this ticket](https://github.com/google-gemini/gemini-cli/discussions/1471), there are also people asking if the use of `@` is inherent to the model or the tool.

```console
mkdir -p /tmp/experiment/docs
cd /tmp/experiment
echo "Start all your answers with 'Hello fpuga'.

If the user ask any question about Spain read ./docs/foo.md
" > GEMINI.md
echo "Always add a joke at the end of your answers" > docs/foo.md

gemini "What is the capital of France"

>>> Hello fpuga
>>> Paris.

gemini "What is the capital of Spain"

>>> Hello fpuga
>>> Hello fpuga
>>> I need to find the capital of Spain. I will use a web search tool for this.
>>> Hello fpuga
>>> The capital of Spain is Madrid.
>>>
>>> Why did the invisible man turn down the job offer?
>>>
>>> He couldn't see himself doing it!
```

We see that when we don't use `@`, the tool/model only loads `GEMINI.md`, but it's able to load the additional rules when needed.

Let's try it with `@`.

```console

echo "Start all your answers with 'Hello fpuga'.

If the user ask any question about Spain read @./docs/foo.md
" > GEMINI.md

gemini "What is the capital of France"

>>> Hello fpuga,
>>> The capital of France is Paris.
>>>
>>> Why don't scientists trust atoms? Because they make up everything!
```

And indeed, when we use `@` it follows the references and loads them automatically into the context.

I replicated the experiment with Cursor and Cursor CLI, and in this case, the use of the `@` symbol has no effect. It only reads `foo.md` when asked for Spain. I open [a feature request about this](https://forum.cursor.com/t/automatically-follow-file-paths-preceded-by-in-agents-md/145915).

## Conclusions

- It's a shame there isn't more standardization in how the tools work.
- If the `@` trick were standardized, it would prevent duplication. From `AGENTS.md`, we could link a simple `CONTRIBUTING.md` with rules like "Before committing, run `./scripts/format.sh` and `./scripts/lint.sh`; it must not return any errors." Or "All contributions must maintain test coverage above 75%."
- The idea of ​​a rules index telling the model when to load additional documents is really good for avoiding context clutter.
