---
id: 865
title: 'Atom: Autocompletado de código en python'
date: '2016-05-08T21:09:38+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=865'
permalink: /atom-autocompletado-codigo-python/865/
categories:
    - 'Sin categoría'
tags:
    - atom
    - desarrollo
    - 'desarrollo sofware'
    - IDE
    - python
---

Al margen del [«Code Completion» de PyCharm](https://confluence.jetbrains.com/display/PYH/Code+completion), y algún otro, el resto de editores/IDEs proveen autocompletado a través de librerías o «servicios externos». Para el caso de python hay fundamentalmente dos, [rope](https://github.com/python-rope/rope) y [jedi](https://jedi.readthedocs.io/en/latest/index.html). Rope está más enfocada a Refactoring y Jedi a Autocompletado, por tanto las dos son complementarias. En la actualidad varios editores que usaban rope están migrando a jedi, su autor ha hecho una [comparación defendiendo su librería](http://jedidjah.ch/code/2013/1/19/why_jedi_not_rope/).

Además de estas librerías cada editor suele proporcionar un plugin base para autocompletado ([autocomplete-plus](https://atom.io/packages/autocomplete-plus) en atom, [auto-complete](http://auto-complete.org/) en emacs) y plugins adicionales para cada lenguaje concreto que actúan como wrapper de las librerías base (rope, jedi,…). Por ejemplo en atom tenemos [autocomplete-python](https://atom.io/packages/autocomplete-python) que es un wrapper para jedi.

## Instalación

Primero hay que instalar jedi sea a nivel global como en el ejemplo, o dentro de un virtualenv.

`<br></br>sudo pip install jedi<br></br>`

Luego se instala el plugin de [autocomplete-pyhon](https://atom.io/packages/autocomplete-python) (que es el más actualizado de los varios que hay). Si usas virtualenv también debería funcionar sin problemas pero si usas algo como virtualenvwrapper donde tu módulo está en un directorio distinto al «entorno virtual de python» puedes haber más problemas.

Lanzado atom desde un virtualenv activado siempre funciona correctamente. Si lo lanzas de otra forma hay que configurar la opción de configuración *Python executable path* del plugin con algo como:

`<br></br>PATH_TO_VIRTUALENV_WRAPPERS_FOLDER/$PROJECT_NAME/bin/python`

o

PATH\_TO\_VIRTUALENV\_WRAPPERS\_FOLDER/$PROJECT/bin/python

Donde PATH\_TO\_VIRTUALENV\_WRAPPERS\_FOLDER es la ruta absoluta al directorio donde se guardan todos los entornos virtuales de virtualenwrapper y $PROJECT\_NAME y $PROJECT son cadenas que debes escribir tal cual. Son variables que entiende el plugin. De la documentación parece deducirse que lo que hay que usar es $PROJECT pero a mi me ha funcionado sólo con $PROJECT\_NAME. Además el directorio padre que se añade a atom a través del «Add project folder» debería llamarse igual que el virtualenv para que $PROJECT\_NAME tome el valor correcto y puedas usar la misma configuración para distintos proyectos.

## Uso

Por la naturaleza dinámica de python muchas veces jedi no es capaz de detectar el tipo de datos de un objeto. Pero podemos ayudarlo [documentado el método](https://jedi.readthedocs.io/en/latest/docs/features.html#recipes). Por ejemplo en un caso como el del ejemplo siguiente con una vista de pyramid, jedi no será capaz de determinar el tipo de datos del parámetro request.

`<br></br>@view_config(route_name='my_route')<br></br>def my_route(request):<br></br>  pass<br></br>`

Pero si hacemos lo siguiente si que autocompletará correctamente los métodos de request:

`<br></br>def cultivos_get(request):<br></br>    """<br></br>    :type request: pyramid.request.Request<br></br>    """<br></br>    pass<br></br>`

No lo he probado con python 3 para ver si soporta el [type hinting](http://blog.jetbrains.com/pycharm/2015/11/python-3-5-type-hinting-in-pycharm-5/) pero este [issue](https://github.com/davidhalter/jedi/pull/661) me hace suponer que si.  
**Teclas principales**

- Sugerencias de autocompletado. `Ctrl+space` Cursores y tab/intro para escoger y aceptar sugerencia
- Go to definition: `Ctrl+Alt+G`
- Show usages: `Ctrl+Shift+P show usages`
- Renombrado en varios ficheros a la vez: Con el cursor encima del símbolo. `Ctrl+Shift+P rename`

## Conclusiones

Las funcionalidades que proporciona son de todas formas muy justas porqué a no ser que documentes los métodos, la mayoría de veces no es capaz de inferir el tipo de datos de una variable. Además las funciones de [autocompletado normal](https://github.com/atom/autocomplete-plus) de atom incluyen habitualmente opciones que no tienen porque corresponder con métodos o propiedades reales del objeto. Y si se desactiva el autocompletado normal para los ficheros python, tendremos muy pocas sugerencias.