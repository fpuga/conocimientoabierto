---
categories:
- Sin categoría
date: 2020-06-29
permalink: /circular-dependencies-webcast-por-miguel-grinberg/1007/
slug: circular-dependencies-webcast-por-miguel-grinberg
tags:
- dependencies
- flask
- python
- refactoring
---

# Circular Dependencies Webcast por Miguel Grinberg

Un [Webcast de Miguel Grinberg sobre como evitar Dependencias Circulares](https://blog.miguelgrinberg.com/post/flask-webcast-3-circular-dependencies) en una aplicación Python / Flask.

<iframe allowfullscreen="allowfullscreen" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/NH-8oLHUyDc" width="560"></iframe>

## My Metadata

- Descripción: Un webcast de 1h en el que se refactoriza una aplicación Flask que empieza con un único fichero a varios paquetes y módulos.
- Calificación: 3 sobre 5
- Día de Visualización: 2020-06-28
- Año de publicación: 2018
- Duración: 68 minutos
- Velocidad de reproducción recomendada: 1.75
- Etiquetas: python; flask; dependencies; refactoring

## Lecciones aprendidas

- Mantener el *entry point* tan limpio como sea posible. Incluso con un único import.
- El módulo que es ejecutado inicialmente por Python adquiere el nombre de `__main__` a nivel interno, por ello los «nombres» que se definan en este módulo, no se identificarán inicialmente a efectos de dependencias como `myfile.myvar` si no como `__main__.myvar`, lo que es más fácil que genere un error de dependencias circulares
- No usar los \_\_init\_\_.py como mecanismo para acortar los imports. Hay tantas opiniones a favor como en contra sobre el tema. A mi me ha generado más problemas que soluciones.
- Usar imports desde la «raíz» `from myapp.models.user import User` y no estilo `from user import User`.
- No pasa nada por no poner los `import` al inicio del fichero cuando tenga sentido que sea de otra forma, por ejemplo para evitar dependencias circulares. Usar `# noqa` para que no pite el linter en estos casos es aceptable.