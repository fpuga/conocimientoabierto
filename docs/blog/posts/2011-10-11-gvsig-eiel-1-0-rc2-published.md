---
id: 406
title: 'gvSIG-EIEL 1.0 RC2 Published'
date: '2011-10-11T22:13:06+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=406'
permalink: /gvsig-eiel-1-0-rc2-published/406/
categories:
    - General
tags:
    - cartolab
    - gvsig
---

Last week, [Cartolab](http://cartolab.udc.es), the university lab where i work, released a new version of [gvSIG-EIEL](cartolab.udc.es/cartoweb/gvsig-eiel).

gvSIG-EIEL is a portable version of gvSIG bundled with some new extensions and some changes in the image designs. The application is focused to accomplish the requirements of the [EIEL](http://www.mpt.gob.es/areas/politica_local/coop_econom_local_estado_fondos_europeos/informacion_socieconomica_local/eiel.html), an infrastructure inventory that some spanish public administration should do.

Some of this extensions like eye candy forms to introduce the data, or tools to verify that the data follow the established rules are specific for the eiel but others can be useful for any gvSIG’s user. As i think that the tools developed by Cartolab for gvSIG-EIEL ([OpenCADTools](http://forge.osor.eu/projects/opencadtools/), …) are already known i want to talk a bit of a new extension and the work done on Sextante.

The new extension is [MapSheets](http://www.prodevelop.es/en/blog/11/09/14/automatically-creating-map-series-gvsig-eiel-printing-module) developed by prodevelop in coordination with the gvSIG Association and ourselves to allow release it as a [official gvSIG extension](http://www.gvsig.org/web/projects/contrib/gvsig-mapsheets). MapSheets allows create map series in a really easy way. For those who comes from ESRI software it is something like MapBook but free and with some new features.

<div class="ngg-gallery-singlepic-image ngg-left" style="max-width: 250px"> [ ![sextante-toolbox](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/cache/sextante-toolbox.png-nggid0215-ngg0dyn-250x300x100-00f0w010c010r110f110r010t010.png "sextante-toolbox") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/sextante-toolbox.png) </div> Under the [umbrella of gvSIG-EIEL, Victor Olalla](http://sextantegis.blogspot.com/2011/03/nuevas-funcionalidades-para-opengis.html) develops some new algorithms like the *line properties* that obtains some statistics for line shapefiles and can get the slope between two points of the line if a DEM is present. Also a useful improvement of the use of Sextante in gvSIG-EIEL is that it comes with two buttons to open the toolbox. The algorithms that appears in the second toolbox are easily configured editing the file alglist.txt that is in the sextante folder (es.unex.sextante) inside the gvSIG extensions folder. Just write in that file the names of the algorithms that you want to see in that file. If you only work with a subset of the algorithms this helps you to localize and use it. MapSheet and the work on Sextante have been funded by the Spanish public administrations [Deputación de Pontevedra](http://www.depontevedra.es/) and [Dirección Xeral de Sostibilidade e Paisaxe](http://cmati.xunta.es/portal/cidadan/lang/gl/pid/2450) de la Consellería de Medio Ambiente, Transporte e Infraestruturas de la Xunta de Galicia