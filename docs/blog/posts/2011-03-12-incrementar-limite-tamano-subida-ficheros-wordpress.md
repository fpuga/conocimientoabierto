---
id: 288
title: 'Incrementar el límite de tamaño de subida de ficheros en WordPress'
date: '2011-03-12T13:28:59+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=288'
permalink: /incrementar-limite-tamano-subida-ficheros-wordpress/288/
categories:
    - General
tags:
    - como
    - 'how to'
    - odiseus
    - wordpress
---

Cuando monta una WordPress Network el límite de tamaño de los ficheros que los distintos blogs/usuarios pueden subir mediante wordpress está fijado a 1500 KB y el máximo total de ficheros subidos está limitado a 10MB.

Para aumentar estos valores hay que ir a *Administrador del sitio -&gt; Ajustes* y modificar los valores de *Site upload space* y *Max upload file size*. De paso podemos activar la posibilidad de que los usuarios suban fotos, vídeos y música. Por defecto está activada la opción de subir ficheros en general, pero al activar estos checkboxes esos tipos de ficheros serán tratados de forma especial.

Si al aumentar el *Max upload file size* seguimos teniendo limitaciones a la subida de ficheros seguramente es un límite impuesto por php.Para modificarlo habría que tocar el fichero php.ini, [modificando estos valores](http://wordpress.org/support/topic/how-to-increase-the-max-upload-size#post-1523748). Por desgracia ese fichero sólo estará accesible cuando tengamos acceso a todos los parámetros del servidor y raramente en un hosting compartido. Pero siempre hay opciones …

1. Si tu proveedor de hosting es Dreamhost lo primero que debes hacer es [activar para tu dominio php 5.3](http://wiki.dreamhost.com/Installing_PHP5#PHP_5.3).
2. Independientemente de tu proveedor si tienes php 5.3 puedes [modificar de formal local la configuración](http://wiki.dreamhost.com/PHP.ini#PHP_5.3).
3. Añadir al fichero phprc creado en el paso anterior [las opciones que nos interesen](http://techtastico.com/post/parametros-php.ini/trackback/).