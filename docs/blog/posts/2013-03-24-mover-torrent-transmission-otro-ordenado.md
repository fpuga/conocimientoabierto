---
id: 544
title: 'Mover un torrent de transmission a otro ordenador'
date: '2013-03-24T16:19:35+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=544'
permalink: /mover-torrent-transmission-otro-ordenado/544/
categories:
    - 'Sin categoría'
tags:
    - como
    - 'how to'
    - receta
    - torrent
    - transmission
---

<div class="ngg-gallery-singlepic-image ngg-left" style="max-width: 240px"> [ ![Logo transmission](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/cache/transmission.png-nggid0217-ngg0dyn-320x240x100-00f0w010c010r110f110r010t010.png "Logo transmission") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/transmission.png) </div> Una nota rápida para explicar como mover una descarga (completa o incompleta) de [transmission](http://www.transmissionbt.com/) a otro ordenador. El escenario es sencillo, tengo los torrents divididos entre dos ordenadores, y se dió el caso de que quería mover uno de los torrents de uno de los ordenadores al otro. Mover toda la información de transmission de un ordenador a otro es sencillo, basta mover los ficheros descargados a la misma ruta en el otro ordenador, y copiar la carpeta *~/.config/transmission*. Mover sólo uno es parecido, simplemente hay que ser un pelín más cuidadoso.

1. Copiar del ordenador 1 a un almacenamiento temporal o similar los ficheros relacionados con nuestro torrent: 
    - El fichero .resume en ~/config/transmission/resume
    - El .torrent en ~/config/transmission/torrent
    - El propio fichero descargado, si está incompleto da igual, reanudará la descarga desde el punto correcto.
    - Anotar la cantidad de datos descargados y enviados para ese fichero
2. Abrir transmission en el ordenador 2 y abrir el .torrent del ordenador 1. Preferiblemente agregarlo en modo pausa para que no comience la descarga automáticamente
3. Copiar a la ubicación del ordenador 2 donde se descargará el fichero, el fichero del ordenador 1
4. En transmission, botón derecho sobre el torrent pausado, y «*Verificar datos locales*«.

Con esto estaría listo, pero si somos un poco más quisquillosos con las estadísticas y las opciones tenemos que efecutar un par de pasos más.

1. Cerrar transmission en el ordenador 2
2. Copiar el .resume del ordenador 1 al directorio adecuado en el ordenador 2
3. Abrir con un editor de texto el fichero *~/config/transmission/stats.json* y actualizar los valores de downloaded-bytes y uploaded-bytes

*stats.json* guarda las estadísticas de ejecución del programa, para actualizar los valores de interes simplemente multiplicaremos las megas descargadas/subidas por 1048576 (1024×1024) para pasar de megas y bytes y lo sumaremos a los valores que ya tenían.

Si es sólo para mover un fichero este procedimiento está bien, si es para mover más habría que hacer un script.

**Referencias**

- [<span style="line-height: 13px;">How to export/import torrent in transmission in Ubuntu?</span>](http://superuser.com/questions/336600/how-to-export-import-torrent-in-transmission-in-ubuntu)
- [What to backup before upgrade (Transmission)?](http://ubuntuforums.org/showthread.php?t=1482470)