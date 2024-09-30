---
categories:
- Sin categoría
date: 2017-11-15
permalink: /libro-think-python-how-to-think-like-a-computer-scientist/941/
slug: libro-think-python-how-to-think-like-a-computer-scientist
tags:
- desarrollo sofware
- libro
- programación
- python
- recomendaciones
---

# Libro: Think Python: How to Think Like a Computer Scientist

How to Think Like a Computer Scientist es un libro clásico entre los recomendados para comenzar a programar en python. La primera edición es de 2002, escrito por Jeffrey Elkner, Allen B. Downey y Chris Meyers bajo licencia GNU FDL. El ser tan «antiguo» y el estar publicado bajo licencia libre ha hecho que a lo largo del tiempo hayan aparecido diversas versiones del libro.

Tenemos dos versiones del libro para python 2

- [How to Think Like a Computer Scientist: Learning with Python 2nd edition](http://www.openbookproject.net/thinkcs/python/english2e/), sería la última edición para python 2 del libro original, y está fechada en 2012. Las soluciones a algunos ejercicios se pueden encontrar en [wikibooks](https://en.wikibooks.org/wiki/How_to_Think_Like_a_Computer_Scientist:_Learning_with_Python_2nd_Edition) (y seguramente valgan para otras versiones).
- La [primera edición](http://greenteapress.com/wp/learning-with-python/) (2002) de ese mismo libro la podemos encontrar en [Green Tea Press](http://greenteapress.com/wp/) la página personal (y «editorial») de Allen B. Downey uno de los autores originales
- Y también en Green Tea Press podemos encontrar una reedición distinta del mismo libro para python, renombrada simplemente a [Think Python](http://greenteapress.com/wp/think-python/). Revisando el github donde se mantiene el libro los últimos cambios serios parecen ser de 2015

También tenemos varias versiones del libro enfocadas a python 3.

1. La que podríamos considerar primera, de 2012, es [How to Think Like a Computer Scientist: Learning with Python 3](http://openbookproject.net/thinkcs/python/english3e/), reeditada fundamentalmente por Peter Wentworth como libro de texto para un primer curso de programación.
2. Otra versión sería una adaptación de la de Peter Wentworth, hecha por varios profesores de la Universidad de Groningen, para emplearla también como [libro de texto para sus clases](https://howtothink.readthedocs.io/en/latest/). En el prólogo declaran que su idea era cambiar la filosofía del libro, de «how to think like a computer scientist» to «how to think as a scientist with a computer», pero revisándolo en mi opinión, los cambios no son tan significativos como para conseguirlo. Está en readthedocs por lo que también se puede [descargar](https://readthedocs.org/projects/howtothink/)
3. En Green Tea Press también encontramos una versión (los últimos cambios serios en el github son de 2016). Esta sería algo así como la [segunda edición de Think Python](http://greenteapress.com/wp/think-python-2e/)
4. Por último, un experimento interesante. [Un libro interactivo](https://interactivepython.org/courselib/static/thinkcspy/index.html), que parece basado fundamentalmente la versión de Wentworth. Consiste en una aplicación web que permite ejecutar código en el propio navegador, depurar paso a paso a modo educativo y responder a cuestionarios

En la página de Green Tea Press hay un dos artículos explicando porqué publicar [«free books»](http://greenteapress.com/free_books.html), y su [filosofía](http://greenteapress.com/wp/textbook-manifesto/) a la hora de escribir libros de texto. Además en el prólogo del libro se puede leer [algo sobre su historia](http://greenteapress.com/thinkpython2/html/thinkpython2001.html#sec2) para entender los autores y los cambios a lo largo del tiempo.

Todas las versiones (inluída la interactiva) están en repositorios de código en github o launchpad, por lo que es posible colaborar en su mejora. Y están escritos en reStructuredText o Markdown y convertidos a libros con sphinx u otras herramientas.

No resulta sencillo decir «cual es mejor», cada una de las veriones tiene sus puntos fuertes y débiles:

- Los que hemos hemos numerado como dos y como tres son los que tienen para mi un orden de capítulos más lógico. Por ejemplo trata listas, tuplas y diccionarios en capítulos contiguos mientras que en las otras versiones los diccionarios están separados del resto de tipos de datos. Pero en dos han juntado varios capítulos en uno sólo por lo que su lectura se hace algo más difícil. Además los capítulos sobre numpy, matplotlib y data handling no encajan muy bien como están escritos en un libro para principiantes. Por tanto a pesar de ser el más actualizado yo en principio descartaría esta versión.
El uno tiene algún material adicional respecto a los otros como capítulos sobre estructuras de datos más avanzadas (pilas, colas y árboles). Si bien creo que estos capítulos son de interés, tampoco pasa nada por prescindir de ellos en un primer contacto, porque hay otros libros más avanzados o más específicos que tratan mejor este tipo de temas.

- El número tres ([Think Python](http://greenteapress.com/wp/think-python-2e/)) tiene para mi otros alicientes como que algunos de los problemas y soluciones están resueltos [en el github del autor](https://github.com/AllenDowney/ThinkPython2/tree/master/code). Es de los que siguen un orden más lógico, capítulos cortos, y una sección «debugging» al final de cada capítulo que explica «técnicas mentales» a la hora de depurar y construír un programa que resultan útiles. Además se puede comprar a través de Amazon, descargar gratuitamente en PDF, leer en html… Así que seguramente esta es la versión más recomendable.
- La versión interactiva también me ha sorprendido gratamente. El texto no es tan bueno como el de Think Python, pero el poder jugar con el código mientras leemos el texto, da muchas opciones a alguien que se introduce en el lenguaje y le permite aprender sin tener que liarse con el entorno. Además la opción de debug (*codelens* en su terminología es especialmente útil para ver lo que pasa en el programa). Esta tambień es un opción recomendable.

Entre la opción interactiva y Think Python es difícil decidirse, si quieres avanzar rápido y tener una panorámica general, el libro seguramente es mejor, y la irrupción de cajas y botones en medio del texto menos molesta. Depende del estilo de aprendizaje de cada uno. Leer un par de capítulos de cada uno y decide tu mismo.

Si está revisión te ha ahorrado tiempo y quieres agradacerme el esfuerzo planteate donar usando el botón de la derecha, o simplemente dejar un comentario en esta entrada.