---
id: 650
title: 'Charlas del FOSS4G 13'
date: '2014-01-05T09:00:32+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=650'
permalink: /charlas-del-foss4g-13/650/
categories:
    - 'Sin categoría'
tags:
    - charlas
    - foss4g
    - gis
    - videos
---

Estoy viendo algunas (la mayoría) de las charlas del FOSS4G que hay [en esta lista de youtube](https://www.youtube.com/playlist?list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2). Llevo las primeras 25, y comparto en dos grupos las que me han parecido más interesantes y otras que he visto con una mínima descripción.

## Recomendables

- [TileServer](https://www.youtube.com/watch?v=YXBpZ6Ai2q0&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=5). Buena introducción a que es WMTS y cuando usarlo. Así como una demo de lo fácil que es convertir un ráster a tiles y servirlo como tileserver-php. Recomendable si no sabes lo que es WMTS.
- [Leaflet: Past, Present, Future](https://www.youtube.com/watch?v=_P2SaCPbJ4w). Charla divertida donde cuentan la historia de leaflet y lo que esperan del futuro. Nada técnico pero interesante para estar al día del mundillo. De paso deja un par de lecciones de como conseguir que un proyecto de software libre triunfe.
- [OpenLayers 3: Under The Hood. Recomendable](https://www.youtube.com/watch?v=dCAq1UHRjUg&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=11). Es interesante ver como han repensando la librería, y lo que hay alrededor de la misma, integración continua, como hacen los builds,…
- [Application Development With OpenLayers 3](https://www.youtube.com/watch?v=SPPhpLTkWX8&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=13). Es un resumen de como usar la api de ol3 para hacer tus propias aplicaciones.

## Otras

- [Concurrent Online Webgis](https://www.youtube.com/watch?v=-ezzjGghdgE&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=2). La aplicación parece bastante espectacular pero el vídeo resulta un poco aburrido de ver. Han usado un montón de las nuevas características de html5, para hacer un «google docs para mapas».
- [Raster Data In GeoServer And GeoTools](https://www.youtube.com/watch?v=M-rVdlkRCq4&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=3). Explica una serie de desarrollos hechos por geosolutions para ráster en geoserver entre los que se incluye mejoras para jai e imageio. En resumen lo interesante es echarle un ojo a los siguientes enlaces: 
    - [imageio-ext](https://github.com/geosolutions-it/imageio-ext/wiki). Un reemplazo de imageio
    - [jai-ext](https://github.com/geosolutions-it/jai-ext) un reemplazo de jai. Todavía no funcional.
    - [jaitools](http://jaitools.org/).
    - [turbojpeg](https://github.com/geosolutions-it/imageio-ext/wiki/TurboJPEG-plugin).
- [Managing update of tiles of dynamic data](< https://www.youtube.com/watch?v=Cl1trRVieU4&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=6>). Demasiado específica del proyecto que comenta.
- [Getting The Best Performance For GeoJSON Map Visualizations](https://www.youtube.com/watch?v=LlXWg1aRR40&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=9). Hace una introducción a topogeojson y a generalizar preservando topología sin profundizar demasiado. A partir del minuto 13 empieza con los resultados de explicar que en los test que han hecho en general postgis es más rápido que couchdb. Lo más interesante de la charla es simplemente darse cuenta de que hay que medir las «optimizaciones» que se hacen para nuestro caso particular y no basarse en subjetividades.
- [Real-time Data Analysis And Rendering With HTML5 Canvas](https://www.youtube.com/watch?v=15G53qJFKnc&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=12)… El contenido en sí era interesante pero la charla me pareció un poco aburrida no acabé de verlo. Trata de describir la infraestructura que montaron con geoserver y openlayers para rasterizar en el servidor un montón de geometrías y servirlas al cliente.
- [OpenLayers 3 Showcase. Parecida a OpenLayers Under The hood](https://www.youtube.com/watch?v=GKrif4fswfg&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=14). La verdad es que viendo los dos vídeos que pusimos como recomendables este se hace repetitivo. No llegué a verlo entero.
- [OpenLayers 3 – How To Successfully Run A Crowdfunding Campaign](https://www.youtube.com/watch?v=i-fm6sRnbZo&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=15). Da un repaso a posibles modos de hacer crowdfunding y como fue el proceso para financiar ol3. Lo más interesante es ese proceso de co-financiación entre una administración pública y un crowdfunding.
- [Analysis Of Realtime Stream Data With Anvil](https://www.youtube.com/watch?v=e1LOSZFPgk8&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=16). Una charla de ESRI acerca de como son open, una parrafada política acerca de porque GPL es «menos libres» que otras licencias y comentar un par de las cosas que tienen publicadas. Sobre «Anvil» el producto del que en teoría va la charla para análisis de datos en tiempo real, no cuentan demasiado al margen de una demo analizando tweets.
- [Old Maps Online And Georeferencer](https://www.youtube.com/watch?v=DWNxeZIi7EU&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=18). La charla no es especialmente interesante pero presenta una [página web](http://www.oldmapsonline.org/) muy chula que te permite consultar los mapas históricos que tenga indexados de diversas fuentes para un determinado lugar, fecha, … También presenta [georeferencer](http://www.georeferencer.com/) un servicio para georefenciar de forma colaborativa mapas antiguos.
- [How To Create A Geocoded Town](https://www.youtube.com/watch?v=k-Qpx15zPYo&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=17). Son dos personas y a una de ellas se la escucha mal, además los primeros minutos van sobre la wikipedia, así que no la acabé, pero la idea parece buena.
- [GIS For All: Exploring The Barriers And Opportunities For Underexploited GIS Applications](https://www.youtube.com/watch?v=wY8CXnikZ-g&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=21). Da algunos numeros de una encuesta barreras de entrada al GIS y algunas opiniones de como superarlas.
- [ESA User Services Powered By Open Source](https://www.youtube.com/watch?v=Wg8KQ_MGJGA&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=22). Stack que está empleando la ESA para servir imágenes de algunas de sus misiones y algunas de las mejoras que hicieron a Mapcache y que publicaron.
- [Open Source Software For Land Cover Mapping From Remote Sensing Data](https://www.youtube.com/watch?v=PEg0Tvl26Fg&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2). Un ejemplo de como usar gdal/ogr y [pktools](http://pktools.nongnu.org/) para hacer una clasificación basada en métodos de machine learning.
- [Towards Big Earth Data Analytics: The EarthServer Approach](https://www.youtube.com/watch?v=2QcFMsirmDY&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2). Un FP7 (financiación de la Unión Europea) de 5 millones de Euros para hacer un [servidor distribuido](http://earthserver.eu/) que permita analizar grandes cantidades de información y visualizarlas en clientes web (2 y 3d)
- [Implementation Of Standard Web Services For GOCE Data Exploitation](https://www.youtube.com/watch?v=rgyypeOezwo&list=PLWW0CjV-TafaBjkroiOxcQw8NdOQ_fhu2&index=25).