---
categories:
- Sin categoría
date: 2012-04-03
permalink: /herramientas-analisis-codigo-estatico-python/468/
slug: herramientas-analisis-codigo-estatico-python
tags:
- análisis estático de código
- comparativa
- desarrollo sofware
- python
---

# Herramientas de análisis de código estático en Python

Programar es fácil, y puede hacerse con el bloc de notas. Escribir buen código es bastante más complicado, por ello existen un montón de herramientas que pueden ayudarnos. Un tipo de herramientas que he empezado a usar (en python) ultimamente son las de [análisis estático de código](http://en.wikipedia.org/wiki/Static_program_analysis). [Estas herramientas](http://www.embedded.com/design/prototyping-and-development/4006735/Integrate-static-analysis-into-a-software-development-process) examinan tu código (sin ejecutarlo) en busca de ciertos patrones, alertando de «code smells», incroguencias de estilo, posibles bugs, código repetido e incluso dando consejos sobre rendimiento o encapsulamiento en algunos casos.

En python tenemos disponibles [distintos analizadores de código](http://www.doughellmann.com/articles/pythonmagazine/completely-different/2008-03-linters/), y es habitual [ver preguntas](http://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes) sobre cual [es mejor](http://stackoverflow.com/questions/35470/are-there-any-static-analysis-tools-for-python). Las cuatro herramientas de este tipo para python están actualizadas a las últimas versiones en los repositorios de ubuntu. Para instalarlas:

`sudo apt-get install pyflakes pep8 pychecker pylint`

## Pyflakes

[Pyflakes](http://pypi.python.org/pypi/pyflakes) parece la más sencilla de las cuatro herramientas que he usado. Hace pocas comprobaciones del tipo, imports no usados, variables asignadas y no empleadas, …  
No chequea el estilo, ni advierte sobre posibles bugs, aunque dicen que es de las más rápidas, por lo que es la que la gente suele usar como «chequeador de código automático» en IDEs como PyDev o emacs.

## pep8

[pep8](http://pypi.python.org/pypi/pep8) valida el estilo de nuestro código (de forma bastante rigurosa) contra el estándar de estilo PEP8 de Python. Puede ayudar a detectar «code smells», pero no chequea «errores». Comprueba cosas como que las líneas no tengan más de 80 caracteres, los nombres de variables tengan un determinado formato, …

Para chequear un fichero llega con hacer:  
`pep8 nombre_de_ficheros.py`

Aunque habitualmente se lanza con más opciones para obtener más información:  
`pep8 --show-source --show-pep8 nombre_de_ficheros.py`

Cuando lo lanzamos con *–show-pep8* proporciona bastante información sobre la regla de estilo que estamos rompiendo por lo que resulta útil para ir interiorizándolas.

## Pychecker

[Pychecker](http://pychecker.sourceforge.net/) es la más antigua pero ahora está algo parado. La última versión 0.8.19 es de enero de 2011 y la anterior del 2008. PyChecker si que es bastante potente en cuanto a la detección de posibles bugs o errores como el de usar una variable antes de asignales un valor, llamar a un método que no existe, … En general detecta bastantes de esos errores que se cometen en python (cuando no se usa un IDE que ya detecte estas cosas)  
Parámetros interesantes.  
*–blacklist*=unittest Este módulo de python saca algún error con pychecker, así que para evitar ruido le decimos que no lo chequee.

Pychecker tiene, [imho](http://es.wiktionary.org/wiki/IMHO), un problema gordo, y es que ejecuta el código para chequearlo, no es realmente una herramienta de análisis estático, por lo que su uso es más bien **desaconsejable**.

## Pylint

P[ylint](http://www.logilab.org/project/pylint) es una especie de mezcla entre pep8 y pychecker puesto que hace análisis tanto del estilo del código como de posibles bugs. Tiene un [montón de características](http://blog.milmazz.com.ve/archivos/2010/03/13/pylint-analisis-estatico-del-codigo-en-python), es extensible mediante plugins, …

El informe que proporciona sobre el código es bastante extenso, clasifica los errores por su gravedad, … Como tiene muchas opciones es conveniente echarle un ojo al [tutorial](http://www.logilab.org/card/pylint_tutorial) y al [manual](http://www.logilab.org/card/pylint_manual) aunque no hace falta para ver su potencial.

Los parámetros más interesantes de pyling son:

- *–reports=n* Para que sólo nos saque los posibles errores y no imprima las estadísticas e informes. Puede ser útil ver el informe de vez en cuando, pero si vamos a pasar el chequeo muchas veces sólo mete ruido.
- *–include-ids=y* Por defecto no nos muestra el código de error completo. Con esto hacemos que nos lo muestre para poder obtener más información sobre él si no lo entendemos (Esto lo haríamos con pyling *–help-msg=ERROR\_CODE*)
- *–disable=C0111* Esto hace que no se chequeen, los errores C0111, que indican que todos los métodos deberían tener un docstring. Me gusta eliminarlos porque soy de los que piensan que «los comentarios apestan»

Para que la línea de comandos no se vuelva muy complicada estás opciones pueden indicarse en un fichero de configuración para que sean usadas por defecto

## Como y cuando usarlas

Lo que me gusta de estas cuatro herramientas es que no hay excusa para no usarlas. Son realmente sencillas, rápidas, y ayudan a hacer un código más legible y mantenible.

Por ahora, para acostumbrarme a ellas, lo que hago es al inicio de cada sesión de trabajo paso las cuatro herramientas en el siguiente orden:

1. pep8 –show-source –show-pep8 \*.py
2. pylint –reports=n –include-ids=y –disable=C0111 \*.py
3. pychecker –blacklist=unittest \*.py
4. pyflakes \*.py

Lo hago así porque me gusta la información sobre el estilo que proporciona pep8, y tras solucionar los errores de pylint ni pychecker ni pyflakes me están proporcionando ayuda adicional así que es probable que pronto deje de usarlos. De hecho cuando me acostumbre a la guía de estilo de pep8 es probable que sólo use pylint.

Como el proyecto en el que la estoy probando apenas son 6 o 7 clases de alrededor de 200 líneas, está forma de trabajar me resulta cómoda y me permite aprender a usarlas, pero está claro que en otros contextos puede no ser lo más adecuado.

En el próximo artículo de esta serie hablaremos sobre como integrar estas herramientas en emacs, al estilo de las sugerencias de eclipse u otros IDE, y otras aproximaciones un poco más sofisticadas de como integrarlas en nuestro flujo de trabajo.

¡Prueba y cuéntame!

***Actualización 20/Julio**: He añadido algún enlace y desaconsejado el uso de pychecker por las razones que ya están incluídas en el propio artículo.*