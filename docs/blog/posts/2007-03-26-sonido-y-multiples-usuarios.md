---
categories:
- General
date: 2007-03-26
permalink: /sonido-y-multiples-usuarios/8/
slug: sonido-y-multiples-usuarios
---

# Sonido y múltiples usuarios

Antes de entrar en el título del post, me gustaría repasar una de las primeras cosas que se aprenden cuando se empieza a profundizar un poco en GNU/Linux, **cualquier elemento del sistema es tratado como si fuese un fichero**. Es decir, desde la foto que hemos descargado de la cámara hasta nuestra tarjeta de sonido pasando por el disco duro tienen una representación (un nombre) dentro del sistema de ficheros.

[Comprender La estructura del árbol de directorios](http://moranar.com.ar/lin/ldtree.html) no es necesario en la práctica, pero nos ayudará a entendernos mejor con el ordenador. Esta estructura dicta por tanto donde debería ir colocado cada elemento del sistema. Nuestros archivos personales estarán en alguna subcarpeta de /home mientras que nuestro disco duro será representado por /dev/hda.

Nuestra tarjeta de sonido estará representada mediante los ficheros */dev/dsp* o */dev/audio*, que por supuesto tendrán establecidos unos determinados permisos y pertenecerán a un determinado usuario y grupo. Lo que viene a continuación está comprobado en una Mandriva 2007 pero entiendo que será extrapolable a la mayoría de distribuciones de Linux.

`crw-rw---- 1 fran audio 14, 4 mar 26 10:37 /dev/audio<br></br>crw-rw---- 1 fran audio 14, 3 mar 26 10:37 /dev/dsp`

Cuando nos identificamos como un determinado usuario el sistema define como propietario de */dev/audio* al usuario con el que hemos identificado, el grupo *audio* es creado durante la instalación del sistema operativo. Si estando identificados como *usuario1* lanzamos algún proceso (mediante el comando *su* por ejemplo) como *usuario2* que requiera usar la tarjeta de sonido habrá un error puesto que el segundo usuario no tendrá los permisos adecuados para escribir en el fichero que representa a la tarjeta de sonido.

La solución más sencilla y elegante (si el grupo *audio* existe) será agregar a todos los usuarios que nos interese a ese grupo. Podemos hacerlo mediante la interfaz gráfica (en Mandriva *Sistema-&gt;Configuración-&gt;Otro-&gt;Administrar Usuarios* o abriendo un terminal de root y tecleando   
`gpasswd -a fran audio`

Nuestra otra opción es aplicar permisos de escritura y lectura para todos sobre esos ficheros *chmod a+r a+w /dev/audio*