---
id: 223
title: 'Primeros pasos para configurar git'
date: '2010-05-01T14:07:53+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=223'
permalink: /primeros-pasos-configurar-git/223/
categories:
    - General
tags:
    - como
    - git
    - 'how to'
    - programación
    - receta
---

[Git](http://geneura.ugr.es/~jmerelo/tutoriales/git/) es el sistema de control de versiones (SCV) que se está imponiendo en el mundo del software libre. Todo programador que se precie debe aprender a usar un [SCV](http://es.wikipedia.org/wiki/Control_de_versiones) y dado que git puede operar también sobre repositorios svn te recomiendo encarecidamente que lo pruebes. Una de las ventajas de [git](http://git-scm.com/) es que es increíblemente configurable. En este artículo encontraras como realizar esa primera configuración para que sea más cómodo trabajar con git.

La configuración global de git se guarda en el home del usuario en archivo llamado .gitconfig. Además dentro de cada repositorio existe un archivo config dentro del directorio .git donde podemos usar unas configuraciones distintas a las globales o añadir parámetros nuevos. La configuración que deseemos la podemos escribir directamente en esos archivos o usar el comando git config.

## Indicamos a git quien somos

`git config --global user.name "Francisco Puga"<br></br>git config --global user.email "fran.puga@gmail.com"`

Esto generará en el fichero .gitconfig dos nuevas líneas como las que siguen:

`[user]<br></br>email = fran.puga@gmail.com<br></br>name = Francisco Puga`

Si quisiéramos configurar nuestro correo electrónico para un repositorio concreto ejecutaríamos git config sin la opción de –global dentro del directorio que contiene el repositorio.

## Colorear la salida

A continuación añadiremos unas líneas al fichero de configuración global (o mediante ordenes como git config –global color.ui auto) para que nos coloree la salida por pantalla

`[color]<br></br>ui = auto<br></br>diff = auto<br></br>status = auto<br></br>branch = auto`

Con añadir esas líneas empezaríamos a usar los colores por defecto pero estos son personalizables [como se puede](http://scie.nti.st/2007/5/2/colors-in-git) ver en [estos enlaces](http://shallowsky.com/blog/programming/gitcolors.html).

Si tras activar los colores ves algo de basura en la salida añade a ~.bashrc la línea:  
`LESS=-R`

## Ignorar ciertos ficheros

Cuando trabajamos en un proyecto puede haber ciertos directorios, ficheros resultantes de la compilación, … que queremos que git no indexe y no nos aparezcan al hacer un estatus. Para [ignorar ciertos ficheros](http://www.kernel.org/pub/software/scm/git/docs/gitignore.html) tenemos varios métodos:

Si lo que queremos es una configuración global para todos nuestros repositorios añadiremos en el .gitconfig la directiva excludesfile con la ruta completa a un archivo de texto donde definiremos las rutas a ignorar. Por ejemplo en mi caso:

`[core]<br></br>excludesfile = "/home/fpuga/.gitignore"`

Y el contenido de ~.gitignore es

`*.[oa]<br></br>*.lo<br></br>*.la<br></br>*.gmo<br></br>semantic.cache<br></br>*~<br></br>*.pyc<br></br>`  
Si lo que queremos es definir un patrón de exclusión para un repositorio concreto lo haremos en el fichero .git/info/exclude.

La tercera opción es crear un fichero .gitignore dentro algún directorio de nuestro repositorios. Este fichero debería usarse no para las configuraciones personales si no para las de todo el grupo de trabajo. Es decir .gitignore es un fichero que podría subirse al repositorio de modo que todo el equipo de desarrollo comparta esa configuración. La particularidad de .gitignore es que no tiene que colocarse en la raíz del repositorio si no que puede colocarse en algún subdirectorio, así, si en el mismo repositorio tenemos varios proyectos, cada uno en un directorio podemos aplicar configuraciones distintas a cada proyecto.

## Para teclear menos

Los comando de git suelen ser nombres bastante largos y en algunos hay que incluir ademas varios parámetros. Para que tengamos que teclear menos git permite configurar alias. La sección alias de mi .gitconfig es la siguiente:

`[alias]<br></br>unstage = reset HEAD<br></br>st = status<br></br>rma = ls-files --deleted | xargs git rm<br></br>co = checkout<br></br>com = checkout master`

5.- Programas por defecto que se usan. Se puede configurar el programa que se empleará para editar el mensaje de commit (por ejemplo emacs en lugar de vi) y el paginador que se usa para ver el log (por ejemplo most en lugar de less)

Si bien en el caso del editor es más lógico configurar la variable de entorno global EDITOR=emacs en nuestro .bash\_profile, también podemos configurarlo en exlusiva para git con algo como esto

`[core]<br></br>editor=emacs<br></br>pager=moss`

## Evitar meter las claves

Si a los repositorios git que tenemos se accede mediante ssh, cosa bastante habitual, tendremos que teclear nuestra contraseña cada vez que bajemos o subamos algo al repo. Para evitarlo podemos [copiar nuestra clave pública al repositorio remoto](http://crysol.org/node/6). Haciendo esto, cuando queramos trabajar contra el repo, este automáticamente se encargará que nuestra clave privada se corresponde a la clave pública que hemos subido y nos dará acceso.

El proceso es tan sencillo como, crear una nueva clave si todavía no lo hemos hecho:

`ssh-keygen -b 4096 -t rsa`

Si usamos una passphrase nos la preguntarán sólo la primera vez de la sesión que la clave sea usada. Se trata de una contraseña para permitir al sistema acceder a nuestra clave privada, no tiene nada que ver con el servidor remoto.

Una vez tengamos nuestra clave ssh, debemos copiarla al servidor, para ello existe un comando especial que hace todo por nosotros

`ssh-copy-id @servidor`