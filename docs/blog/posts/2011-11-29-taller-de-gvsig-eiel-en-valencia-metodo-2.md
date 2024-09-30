---
id: 425
title: 'Taller de gvSIG-EIEL en Valencia. Método 2'
date: '2011-11-29T17:45:20+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=425'
permalink: /taller-de-gvsig-eiel-en-valencia-metodo-2/425/
categories:
    - General
tags:
    - cartolab
    - como
    - gis
    - gvsig
    - 'how to'
---

Como [comentábamos en la anterior entrada](http://conocimientoabierto.es/taller-gvsig-eiel-valencia-metodo-1/420/) hemos creado un fichero .iso que podéis «quemar» en un pendrive de al menos 4GB para seguir el taller de gvSIG-EIEL. Podéis descargar el .iso desde [este enlace](http://www.adrive.com/public/ef55aaba0e67894a6156d6f1a454dba06ac96790fe8691a241c30515254205e3.html).

Tras quemarla podréis arrancar vuestro ordenador desde el PC [configurando en la BIOS](http://pcsupport.about.com/od/tipstricks/ht/bootusbflash.htm) que arranque en primer lugar desde ahí. Se trata de una versión de ubuntu con gvSIG-EIEL y una base de datos PostGIS con datos de prueba, todo preinstalado.

Para quemar el pendrive [podéis seguir estas instrucciones](http://live.osgeo.org/en/quickstart/usb_quickstart.html). para linux o para windows.

El usuario por defecto es «custom» sin clave. Para conectar a la base de datos usaremos:

- **servidor**: localhost
- **usuario**: user
- **clave**: user
- **puerto**: 5432
- **esquema**: eiel\_map\_municipal

<div>El fichero .iso también debería poder ser ejecutado [desde una máquina virtual](http://live.osgeo.org/en/quickstart/virtualbox_quickstart.html).</div><div>Si tenéis algún problema dejad un comentario o **comentádnoslo antes del taller**. Estaremos todos los días por las jornadas.</div>