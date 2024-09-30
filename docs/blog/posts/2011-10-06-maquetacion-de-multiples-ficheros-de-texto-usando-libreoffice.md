---
id: 396
title: 'Maquetación de múltiples ficheros de texto usando LibreOffice'
date: '2011-10-06T13:02:57+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=396'
permalink: /maquetacion-de-multiples-ficheros-de-texto-usando-libreoffice/396/
categories:
    - General
tags:
    - como
    - 'how to'
    - 'identidad corporativa'
    - libreoffice
    - ofimática
---

[Cartolab](http://cartolab.udc.es) está colaborando con [Ingeniería Sin Fronteras](http://www.isf.es) en un proyecto financiado por la [Xunta de Galicia](http://www.xunta.es/) para la elaboración de materiales para un curso de Sistemas de Información Geográfica y Cooperación al Desarrollo. En la elaboración del curso tenemos la suerte de colaborar también con [iCarto](http://icarto.es/) y con el [Laborate](http://laborate.usc.es/es/). Además el [SIGTE](http://www.sigte.udg.edu/sigte_es/) se encarga de revisar el trabajo y poner la plataforma de teleformación. Gracias a todos ellos por hacer posible este artículo.

## Maquetar múltiples ficheros con LibreOffice

Uno de los puntos que defendemos en el curso es de la importancia del uso de software libre en los proyectos de cooperación, y por coherencia, tratamos en la medida de los posible de emplear unicamente herramientas libres para elaborar los contenidos. Nos encontramos por tanto con un equipo de alrededor de 9 personas en varias instituciones distintas editando cerca de 20 ficheros de texto distintos con LibreOffice, lo cual entre otras cosas genera el problema de obtener al final una maquetación coherente. Está claro que existen soluciones más imaginativas por ejemplo usar latex con git como repositorio de información pero en ciertos contextos esto es simplemente imposible.

Cuando queremos que un documento de texto tenga un formato consistente empleamos [estilos](http://wiki.documentfoundation.org/cgi_img_auth.php/c/cc/0206WG3-IntroductionToStyles.pdf), cuando necesitamos un formato consistente en múltiples ficheros empleamos [plantillas](http://wiki.documentfoundation.org/cgi_img_auth.php/6/6e/0103GS3-StylesAndTemplates.pdf).

## Que es una plantilla y como se crea

Apurando la definición se podría decir que una plantilla no es más que un documento de texto de LibreOffice con extensión .ott en lugar de .odt en el que se han definido los estilos del documento, las cabeceras, ciertos textos, … El truco está en que cuando creamos un nuevo documento a partir de una plantilla este documento se queda en cierta manera vinculado a la plantilla. Por tanto cuando modifiquemos la plantilla se modificarán los documentos asociados.

Al menos esa es la teoría en realidad hay algunos handicaps:  
– No todo lo modificado en la plantilla se actualiza en los documentos. Los estilos si que son actualizados pero textos que podamos tener por las páginas por ejemplo una portada no se actualizan. [Aunque hay una extensión que lo arregla](http://extensions.services.openoffice.org/en/project/templatechanger).  
– La actualización no es automática. Cuando abrimos el documento vinculado, si la plantilla ha cambiado nos pregunta si queremos actualizar los estilos, no se actualizan por si mismos.  
– Las plantillas pueden ser compartidas pero no es lo más cómodo del mundo.  
– Una precaución que habría que tener es que en general no debemos modificar el estilo en el documento. Debemos: Cerrar el documento, modificar la plantilla y volver a abrir el documento para que se actualicen.

A pesar de estos handicaps el disponer de plantillas para los documentos corporativos de tu empresa puede acabar ahorrándote mucho tiempo.

- Para crear una plantilla lo más fácil es crear un nuevo documento de texto y luego *Archivo -&gt; Plantilla -&gt; Guardar*.
- Para crear un documento a partir de una plantilla *Archivo -&gt; Nuevo -&gt; Plantillas de documentos*.
- Para editar una plantilla, desde cualquier documento, *Archivo -&gt; Plantilla -&gt; Administrar, seleccionamos la que nos interese y en botón desplegable llamado Comandos le damos a editar*. Para guardarla usamos el mismo procedimiento que para crear una nueva (*Archivo -&gt; Plantilla -&gt; Guardar*) pero seleccionando la ya existente para que la sobreescriba.

## Compartir la plantilla

Compartir la plantilla no es del todo necesario. Si una persona tiene la plantilla en su ordenador y maqueta todos los documentos, aunque el resto no tengan la plantilla cada documento individual si que conservará los atributos de los estilos. Por tanto se puede continuar editando el documento usando los estilos predefinidos. Pero no podrá crear nuevos estilos o modificarlos porque creará inconsistencias. Tendrá que solicitar a quien tiene la plantilla que la modifique y abra todos los documentos para que estos se actualicen.

Si no disponemos de la plantilla en nuestro ordenador tampoco podremos crear nuevos documentos a partir de la plantilla. Una solución por supuesto es mandarla por correo-e cada vez que haya un cambio, pero existe un método algo más sofisticado.

En nuestro caso concreto empleamos DropBox (nadie es perfecto) para compartir los materiales del curso, de modo que podemos dejar la propia plantilla en una carpeta compartida. La persona que crea la plantilla la exporta (*Archivo -&gt; Plantilla -&gt; Administrar, seleccionamos la que queremos y en el botón de Comandos-&gt;Exportar*).

LibreOffice nos da la oportunidad de importar plantillas (misma secuencia de menus que para exportar) pero si hacemos esto creará una copia local de la plantilla y las modificaciones en el original no se verán reflejadas. Lo que debemos hacer es decirle que consideré la carpeta que nosotros queramos como una carpeta válida de plantillas. Para ello:

*Herramientas -&gt; Opciones -&gt; Rutas -&gt; Marcamos plantillas, le damos a editar, agregamos como ruta nueva la de nuestra carpeta compartida y la seleccionamos.*

Por desgracia, la cosa no iba a ser tan fácil, las plantillas que pueda haber en esa carpeta no son reconocidas automáticamente y ni no vale con importalas así que hay que hacer un pequeño truco.

1. Configuramos la ruta a la carpeta compartida si no lo hemos hecho todavía
2. Cortamos y pegamos en otro sitio la plantilla que está en la carpeta compartida. Es importante por tanto que no haya en en la carpeta de plantillas una que ya tenga el nombre que vamos a usar, si no LibreOffice le asignará otro distinto y el fichero compartido tendrá un nombre distinto por tanto.
3. Abrimos mediante doble click el fichero que contiene la plantilla y guardamos la plantilla a partir de él (*Archivo -&gt; plantilla -&gt; guardar*). De nombre le pondremos el que hayamos acordado con el resto de gente respetando mayúsculas etc … Muy importante respetar escrupulosamente el nombre
4. Con eso estaría listo. Ya tendriamos esa plantilla disponible en nuestro sistema y cada vez que la modificáramos estaríamos tocando el fichero compartido de modo que se le actualizaría a los demás.

En próximos artículos seguiremos contando algunos trucos de los estilos que podemos usar a la hora de hacer la plantilla el uso de campos, …