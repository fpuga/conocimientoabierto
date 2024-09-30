---
id: 89
title: 'hostings, dominios, traslados y dns de manera informal e inexacta'
date: '2009-06-18T11:32:53+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=89'
permalink: /hosting-dominio-traslado-dns/89/
categories:
    - cooperacion
    - General
---

Se llama **hosting** al ordenador que está en internet al que subimos los contenidos de nuestra web. Este ordenador nos proporcionará diversas funcionalidades, pueden darnos acceso a 1 base de datos o a 10 o a cero, un espacio limitado o ilimitado, … todo depende de lo que contratemos.

Se llama **dominio** a lo que tecleamos en la barra de direcciones del navegador para acceder a una web, por ejemplo para acceder a esta tienes que teclear conocimientoabierto.es. El hosting y el dominio no los tenemos por que contratar en la misma empresa y ahí es donde entran en juego las dns.

Las **dns** son una especie de agenda de contactos distribuída en varias libretas. Cuando queremos llamar a alguien (acceder a una página):

1. miramos en una agenda general (servidor dns principal), en esa agenda aparece que nuestro dominio está registrado con tal empresa,
2. entonces se va a mirar la agenda de esa empresa (servidor dns secundario). Si el hosting lo tenemos contratado en la misma empresa que el domino, en la agenda de la empresa ya aparecerá el número al que hay que llamar para acceder a la página deseada.
3. Si el hosting lo tenemos en otra, en la agenda de la empresa del dominio nos dirijirán a la agenda/dns de la empresa de hosting, y está si que nos dará definitivamente el número al que debemos llamar para acceder a la págin

Un paso importante a la hora de crear una página web o cambiar de proveedor es que para que el paso 2 sea posible, somos nosotros los que debemos cambiar los datos en la agenda de nuestro *registrador* de dominio. El *registrador* nos dará un nombre de usurio y una clave, con esos datos accederemos a un panel de control y en una opción de nombre parecido a «gestión de dns» pondremos las dns de nuestro proveedor de hosting, es lo que se llama **redireccionamiento o redirección de dns**. Si algún día cambiamos de proveedor de hosting, deberemos volver a cambiar las dns asociadas a nuestro dominio.

Otro punto muy importante, es que una vez registramos nuestro dominio, accedemos al panel de control y modifiquemos los datos del propietario y el contacto administrativo. Sobre todo el nombre y la dirección de correo-e deben ser reales y estar en funcionamiento. Esa dirección de correo no debe tener relación con el propio dominio, es decir, es mejor optar por gmail, yahoo,… Si perdemos alguna vez el acceso a esa dirección de correo debemos volver a cambiar los datos. Si el dueño de la empresa o el propietario del dominio cambia debemos actualizar los datos. Hacer esto nos ahorrá muchísimos problemas después.

La información de ayuda de los proveedores suele ser bastante completa, así que allí debemos dirigirnos para ver como hacer en nuestro caso concreto.

El **traslado de un dominio** consiste en cambiar la empresa a la que le pagamos por mantener nuestro dominio. Antes de contratar el dominio en la nueva empresa debemos leer bien lo que nos piden para hacer efectivo el traslado. Para dominios .com, .org, .net esto será en general que el [dominio no esté bloqueado](http://dinahosting.com/Video/CaduDomOK/CaduDomOK.html) y que tengamos el [auth code](http://www.wdbc.com/domain/transfer-authcode.cfm). Para los .es es un poco distinto, pero sencillo y no hay problema si el email de contacto es correcto.

Una vez tengamos el auth code podemos ir al nuevo registrador y haciendo uso de la opción traslado contratar con él el servicio. Debemos acordarnos, en cuanto tengamos acceso al panel de control de cambiar las dns para que apunten a nuestro hosting y los datos de contacto.

Este artículo viene a cuento de otro que escribiré en un par de días, como ejemplo de lo que pasa cuando no se hace las cosas correctamente o se escoge un mal proveedor…