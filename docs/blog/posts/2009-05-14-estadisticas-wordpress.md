---
id: 66
title: 'Estadísticas para WordPress'
date: '2009-05-14T13:05:03+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=66'
permalink: /estadisticas-wordpress/66/
categories:
    - General
---

Escoger un plugin de estadísticas para WordPress es complicado. Si [buscas en la página de wordpress](http://wordpress.org/extend/plugins/tags/stats) encontraras decenas de ellos, google tampoco ayuda demasiado, porque los primeros resultados en las búsquedas son a [posts antiguos](http://lorelle.wordpress.com/2007/02/12/counting-wordpress-statistics-wordpress-plugins/) o a [recopilatorios](http://mashable.com/2007/08/07/30-wordpress-plugins-for-statistics/) que se dedican a enumerar [«los 15 mejores plugins»](http://ayudawordpress.com/15-sistemas-de-estadisticas-en-wordpress/), escoger aunque sólo sea entre 15 sigue siendo un infierno si tienes que probarlos todos para encontrar el mejor. Si quieres saber como se hace en este blog sigue leyendo.

Tras pasar un par de días leyendo sobre el tema, creo que una buena estrategia de gestión de estadísticas debería tener en cuenta los siguientes puntos:

1. [Usar más de un sistema](http://www.anieto2k.com/2008/07/24/estadisticas-en-el-blog-%C2%BFde-quien-nos-fiamos/) a la vez porque los servicios de estadísticas [no son del todo fiables](http://francoisderbaix.com/2009/02/17/google-analytics-vs-xiti-como-miden-el-origen-de-las-visitas/)
2. Usar al menos un sistema basado en un servicio externo, y otro implementado dentro del propio WordPress. En este punto hay que tener en cuenta que los implentados en WP almacenan mucha información en la base de datos, de modo que si nuestro hosting limita su uso o hay mucho tráfico el rendimiento puede bajar.
3. No olvidarse de recoger estadísticas sobre los feeds RSS. Si se emplea un plugin que haga varias cosas a la vez mejor, porque a mayor número de plugins más tardan las páginas en cargar.
4. Si se trata de un blog comercial o se es muy cotilla es útil disponer de estadísticas en tiempo real, número de visitantes actuales de la página, poder trazar el recorrido de un visitante dentro del blog, …

Con los puntos anteriores en la cabeza en este blog he decidido usar:

**StatPress + Google Analytics for WordPress + WordPress.com Stats + FeedBurner**

Uso [StatPress](http://wordpress.org/extend/plugins/statpress/) **c**omo sistema implementado dentro del propio WP**[](http://wordpress.org/extend/plugins/statpress/)**. Este plugin es sencillo de usar e interpretar, con estadísticas en tiempo real, un widget para poder mostrar un contador de visitas y algunos otros datos en nuestro theme, posibilidad de borrar datos antiguos para aligerar las base de datos, exportar a hoja de cálculo… Es uno de los plugins más populares y [muchos blogs](http://blogsbazaar.com/2008/07/statpress-estadisticas-en-vivo-para-wordpress/) hablan bien de él. También captura datos sobre los feeds pero sólo si usas el feed predeterminado; esta característica no funciona si usas feedburner.

Uso Google Analytics (GA) como servicio externo junto al plugin [Google Analytics for WordPress](http://wordpress.org/extend/plugins/google-analytics-for-wordpress/) para ganar algunas funcionalidades. Si bien existen [mucho servicio externos de estadísticas](http://www.clazh.com/ten-best-free-web-statistics-and-analytics-packages/), GA ya lo conocía de antes y es de los más conocidos. . Lo positivo que tienen este tipo de sistemas es que no gastas recursos propios, lo malo es que pierdes autonomía y cedes el control de tu información a terceros. Para usarlos hace falta abrir una cuenta en el servicio escogido y luego incluír un código especial en la plantilla del blog aunque hay plugins (como GA for WordPress) que evitan tener que editar la plantilla a mano.

Para contrastar la información de GA uso **[WordPress.com Stats](http://wordpress.org/extend/plugins/stats/)**. Se trata de un servicio externo proporcionado por wordpress.com más centrado en las estadísticas para blogs que GA. Para usarlo, al igual que para el plugin Akismet tienes que tener una cuenta en wordpress.com.

Para las estadísticas de los feeds uso Feedburner. **[Feedburner](http://feedburner.com)** es un servicio web que hace de intermediario entre tus feeds y tus lectores. Tu feed se sirve a los subscriptores desde los servidores de feedburner lo que disminuye el ancho de banda usado por tu blog. Lo cierto es que [no ofrece estadísticas demasiado fiables](http://www.adseok.com/herramientas-seo/como-funciona-feedburner/) y supone una perdida de independencia, pero usando la característica de [My Brand](http://www.ianfernando.com/2007/configure-feedburner-mybrand-with-1and1-host/) se adapta muy bien a mis necesidadesz