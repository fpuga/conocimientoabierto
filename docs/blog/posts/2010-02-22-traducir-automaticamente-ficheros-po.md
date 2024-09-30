---
categories:
- General
date: 2010-02-22
permalink: /traducir-automaticamente-ficheros-po/207/
slug: traducir-automaticamente-ficheros-po
tags:
- i18n
- poss-gl
- python
- script
- traducción
---

# Traducir automáticamente ficheros .po

Ultimamente estoy dedicando parte de mi tiempo libre a algunos trabajos relacionados con la traducción. En concreto he portado a windows la última versión del [software de traducción gtranslator](http://gtranslator.sourceforge.net/) y estoy participando en un proyecto para [traducir de forma colaborativa al gallego el libro Producing Open Source Software](http://producingoss.ghandalf.org/).

Uno de los aspectos interesantes del proyecto poss-gl es que estamos usando una metodología propia de la traducción de software para un libro, con bastante buen resultado. Cada capítulo del libro se ha convertido en un [fichero .po](http://es.wikipedia.org/wiki/Gettext), que son los ficheros estándar de traducción en Software Libre. De este modo en lugar de ir traduciendo cada línea con un procesador de texto podemos emplear una herramienta avanzada como gtranslator para ello. Una de las características de gtranslator es que se puede visualizar además del texto original el contenido de otro fichero .po que contenga por ejemplo la traducción a un tercer idioma que nos sirva para comparar como han hecho otros traductores.

Basándome en esa posibilidad acabo de escribir un programita que permite traducir automaticamente un fichero po haciendo consultas a un [servicio de traducción web](http://www.opentrad.com/). Las traducciones automáticas, a no ser que sean entre lenguas similares como castellano y gallego, son bastante malas pero, cargándolas como idioma alternativo en gtranslator pueden sernos de ayuda en nuestra propia traducción.

El programa se trata de un script programado en python y liberado con licencia GPL v3 que podeis [descargar directamente](http://repo.or.cz/w/fpuga.git/blob_plain/HEAD:/localizacion/translatePO.py) desde [mi repositorio de software](http://repo.or.cz/w/fpuga.git). Para que funcione es necesario instalar también los módulos de python [polib](http://bitbucket.org/izi/polib/src/) y [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/).

Para ejecutarlo escribiremos en una consola de linux:

`python translatePO.py -d [dirección] -i [fichero.po]`

La dirección indica de que idioma a que idioma queremos traducirlo, por ejemplo en-es para traducir de inglés a castellano o gl-fr para hacerlo de gallego a francés.