---
categories:
- Sin categoría
date: 2014-03-13
permalink: /montar-firefox-independiente-desarrollo-web/679/
slug: montar-firefox-independiente-desarrollo-web
tags:
- cartolab
- como
- desarrollo web
- entorno de desarrollo
- firefox
- how to
- web
---

# Montar un firefox independiente para desarrollo web

[![Firefox_Screenshot](http://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/thumbs/thumbs_Firefox_Screenshot.PNG)](http://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/Firefox_Screenshot.PNG "From: http://en.wikipedia.org/wiki/File:Firefox_Screenshot.PNG")En [Cartolab](http://cartolab.udc.es) llevamos ya una temporada investigando en uso de tecnologías web en el ámbito de la ingeniería cvil.

Una de las cosas que me incomodaron durante los primeros experimentos, era no tener un entorno de desarrollo específico. Al margen del IDE, en desarrollo web son fundamentales las herramientas que proporciona el navegador que usas para el testeo. En este caso, me molesta el mezclar plugins de desarrollo, con plugins normales que uso para la navegación. Tengo la sensación que se me descontrola el entorno de trabajo.

La solución es configurar un navegador específico para desarrollo. Lo cual, al menos en el caso de firefox, es más sencillo de lo que parece:

1. Le echamos un ojo a las [instrucciones de mozilla de como instalar firefox a mano](https://support.mozilla.org/en-US/kb/install-firefox-linux). En resumen: descargar y descomprimir. Yo lo descargue en `/usr/local/development`
2. Si ahora simplemente ejecutamos el fichero binario `firefox` veremos que no hemos ganado nada, aún tendremos nuestros marcadores, plugins, etc… Esto es porque firefox, guarda esta información en [perfiles](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data) y usa por defecto el perfil indicado en el fichero `$HOME/.mozilla/firefox/profiles.ini`
3. Debemos por tanto crear un nuevo perfil, pero antes haremos una copia de `profiles.ini`
4. Creamos el [perfil como recomiendan desde mozilla](https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles), ejecutando `firefox -P`. Yo cree el perfil dentro de la propia carpeta del firefox descargado a mano, para poder tener un sistema autocontenido.
5. El paso anterior habrá modificado el fichero profiles.ini, añadiendo el nuevo. Pero lo que nosotros queremos es tener el *modo desarrollo* lo más aislado posible así que restauramos la copia que hicimos anteriormente
6. Creamos un miniscript en nuestro PATH o donde queramos que ejecute nuestro firefox de desarrollo y le pase [el parámetro](http://kb.mozillazine.org/Command_line_arguments) `-profile` y el path al perfil de desarrollo que creamos. Yo cree un script *ffdev* en /usr/local/bin con el siguiente contenido  
    `<br></br>#!/bin/sh<br></br>cd /usr/local/development/firefox<br></br>./firefox -profile development-profile<br></br>`

Los menos puristas habrán observado, que en realidad, no es necesario complicarse tanto la vida bajando un firefox aparte. Llegaría con:

Crear un perfil nuevo en la carpeta por defecto, marcar el antiguo perfil como el que hay que usar por defecto y crear un script que arranque el nuevo perfil `firefox -P "Nombre del Nuevo Perfil"`

Si hemos optado por la primera altenativa y finalmente decidimos pasar a la segunda, un sólo firefox en el sistema que se actualice al ritmo que marca nuestra distribución, el cambio es tan sencillo, como copiar la carpeta de perfil de desarrollo a una nueva ubicación (el  
directorio por defecto de perfiles sería lo lógico) y modificar el script para indicarle la nueva ruta del perfil y que firefox tiene que  
usar. Si quisieramos poder abrirlo desde el Gestor de Perfiles o con la opción -P en lugar de -profile deberemos añadirlo a profiles.ini

¿Creéis que es útil configurar un perfil para desarrollo o no hace falta? ¿Cual de los dos métodos preferís?