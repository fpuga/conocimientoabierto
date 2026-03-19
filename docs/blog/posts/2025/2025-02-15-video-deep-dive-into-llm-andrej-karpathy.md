---
categories:
  - Sin categoría
date: 2025-02-15
permalink: /video-deep-dive-into-llm-andrej-karpathy
slug: video-deep-dive-into-llm-andrej-karpathy
tags:
  - ai
  - andrej karpathy
---

# Vídeo: Deep Dive into LLMs like ChatGPT. By Andrej Karpathy

[Andrej Karpathy](https://karpathy.ai/) fue uno de los fundadores de OpenAI y Director de IA en Tesla.

En este vídeo de tres horas y media desgrana todo el funcionamiento de un LLM, desde que descargas los datos de internet hasta que puedes conversar con ella. Si hace unas semanas enlazaba la interesante, pero complicada explicación de [Stephen Wolfram](https://franciscopuga.es/blog/2025/01/19/como-funciona-un-llm-y-porque-mienten/) este es un vídeo para todos los públicos.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7xTGNNLPyMI?si=AO97C63oAmv0CpVQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Uno de los pocos momentos en que sale sale de la parte "técnica" es sobre la 1h:10min. Explica que tras el pre-training (entrenar al modelo con todo internet), se pasa al post-training. En el post-training "especialistas humanos" redactan conversaciones en base a unas ideas generales de "personalidad" que la empresa que construye el modelo quiere que tenga. Más o menos dice los siguiente:

> lo que pasa cuando abres chatgpt y haces una pregunta, no es que una especie de IA mágica te responda, es un proceso estadístico en la que las respuestas se parecen a lo que unos editores humanos siguiendo las instrucciones de una empresa han decidido que es correcto.
>
> Si preguntas "Cuales son los 5 lugares que no me puedo perder de París", la respuesta no se basa en una comparativa "científica" de que lugar es mejor y porqué, se parece más bien a la respuesta que estatisticamente habría respondido el editor.
