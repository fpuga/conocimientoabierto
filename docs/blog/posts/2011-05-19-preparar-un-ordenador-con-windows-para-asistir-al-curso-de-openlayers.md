---
id: 342
title: 'Preparar un ordenador con Windows para asistir al curso de OpenLayers.'
date: '2011-05-19T18:25:17+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=342'
permalink: /preparar-un-ordenador-con-windows-para-asistir-al-curso-de-openlayers/342/
categories:
    - General
tags:
    - apache
    - cartolab
    - como
    - 'how to'
    - mod_python
    - openlayers
    - sistemas
    - windows
---

Un par de instrucciones rápidas para el [curso de OpenLayers que habrá mañana en la Escuela de Caminos en Coruña impulsado por xeoinquedos](http://xeoinquedos.wordpress.com/), No te asustes por el texto es mucho más fácil de lo que parece. En resumen baja los archivos que se enlazan en este post y haz doble click sobre ellos :) Los enlaces son para Windows de 32bits, si usas 64 deja un comentario y te ayudamos.

## 1.- Instalar Apache.

La forma más sencilla es [descargar Xampp desde esta dirección](http://www.apachefriends.org/download.php?xampp-win32-1.7.4-VC6-installer.exe) \[1\] e instalarlo haciendo doble click. Las opciones que trae por defecto son adecuadas para la mayoría de los equipos.

Para lanzar Apache ejecuta el acceso directo que aparece en tu escritorio y luego pulsa en el botón «Start» que está a la derecha de Apache. Si salta un mensaje del antivirus pulsa en desbloquear. Para comprobar que funciona abre un navegador y escribe en la barra de direcciones http://localhost

Si se abre una página naranja ya lo tienes :)

Si tienes algún problema, tienes [instrucciones más detalladas en este enlace](http://www.apachefriends.org/en/xampp-windows.html) \[3\]

## 2.- Instalar un intérprete de Python

Descarga[ python 2.7.1 para windows desde este enlace](http://www.python.org/ftp/python/2.7.1/python-2.7.1.msi) \[2\]. Instálalo mediante doble click, las opciones por defecto son una vez más adecuadas para la mayoría de los equipos.

## 3.- Instalar python como módulo cgi para Apache.

[Descárgate este fichero](http://modwsgi.googlecode.com/files/mod_wsgi-win32-ap22py27-3.3.so) \[4\] y cópialo dentro de la carpeta c:xamppapachemodules. Cámbiale el nombre de mod\_wsgi-win32-ap22py27-3.3.so a mod\_wsgi.so

A continuación abre con el WordPad el fichero c:xamppapacheconfighttpd.conf Localiza el conjunto de líneas que empiezan por el texto LoadModule y añade al final

LoadModule wsgi\_module modules/mod\_wsgi.so

Salva el fichero y vuelve a probar si funciona Apache.

## 4.- Firebug.

Lo mejor es que traigas instalado un navegador como firefox con el complemento firebug. [Para instalar firebug simplemente pincha en este enlace](http://getfirebug.com/downloads) \[5\] desde firefox y sigue las instrucciones.

Si usas firefox 3.6 debes descargar la versión 1.6, si usas firefox 4 debes usar la 1.7 preferiblemente. Para saber que versión de firefox tienes instalada pincha en Ayuda -&gt; Acerca de

Aviso: En este momento la página de firebug parece caida así que si no funciona [prueba con este otro enlace](http://firebug.softonic.com/descargar) \[8\]

## 5.- Editor de texto

Con el bloc de notas o el WordPad es suficiente para lo que vamos a hacer pero si quieres instalar uno más potente [puedes probar notepad++](http://download.tuxfamily.org/notepadplus/5.9/npp.5.9.Installer.exe) \[9\]

## 6.- Copia el archivo proxy.cgi que se proporciona en los materiales del curso al directorio c:xamppcgi-bin

Y listo. Como es habitual en estas cosas, esto más difícil de escribir que de hacer.

Por último agradecer a [Micho](http://twitter.com/michogar), [Xurxo](http://blog.sonxurxo.com/), Gracia, [Cartolab](http://cartolab.udc.es/cartoweb/) y la [Escuela de Caminos](http://caminos.udc.es/), sin los que esté curso no sería posible.

- \[1\] <http://www.apachefriends.org/download.php?xampp-win32-1.7.4-VC6-installer.exe>
- \[2\] <http://www.python.org/ftp/python/2.7.1/python-2.7.1.msi>
- \[3\] <http://www.apachefriends.org/en/xampp-windows.html>
- \[4\] [http://modwsgi.googlecode.com/files/mod\_wsgi-win32-ap22py27-3.3.so](http://modwsgi.googlecode.com/files/mod_wsgi-win32-ap22py27-3.3.so)
- \[5\] <http://getfirebug.com/downloads>
- \[8\] <http://firebug.softonic.com/descargar>
- \[9\] <http://download.tuxfamily.org/notepadplus/5.9/npp.5.9.Installer.exe>