---
id: 454
title: 'Actualizar la versión de Antroid de un HTC Tattoo (I parte)'
date: '2012-02-26T13:14:07+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=454'
permalink: /actualizar-la-version-de-antroid-de-un-htc-tattoo-i-parte/454/
categories:
    - 'Sin categoría'
tags:
    - android
    - como
    - 'dispositivos móviles'
    - hardware
    - 'how to'
    - software
---

Hay muchos foros y tutoriales explicando como actualizar la versión de [Android](es.wikipedia.org/wiki/Android) de un teléfono [HTC Tattoo](http://www.htc.com/es/help/htc-tattoo/). Este es (la primera parte de) el mio. Aunque antes de continuar leyendo deberías saber que todo lo escrito aquí proviene de lo aprendendido en apenas un fin de semana así que puede ser incorrecto.

Los HTC Tattoo vienen con una de las primeras versiones de Android que salió al mercado, la 1.6. Esto impide usar alguna de las aplicaciones actuales más conocidas (leáse Whatsapp), tiene problemillas con el bluetooth, …

El principal desarrollador de [Android es Google](http://www.android.com/). Los fabricantes de teléfonos colaboran en el desarrollo de Android y además hacen algunas adaptaciones propias para sus propios teléfonos. Las compañías de servicio telefónico, tampoco acostumbran a quedar tranquilas con la versión que desarrolla el fabricante y empaquetan su propio software en el teléfono, a veces es simplemente cambiar la pantalla de inicio, a veces cambios más profundos como substituír el Market de Google por uno propio.

En el caso del Tatto ni el fabricante del teléfono ni la compañía que lo distribuye están interesados en sacar una actualización a versiones más modernas de Android; y aquí es donde entra en juego la*[ scene](http://es.wikipedia.org/wiki/Scene)*. Como [Android es (semi) libre](http://www.muycomputer.com/2011/09/20/android-realmente-libre-richard-stallman-dice-no) hay equipos de programadores que lo modifican y adaptan para sus propias necesidades y publican esas modificaciones de forma gratuita. Entre estas modificaciones está el reescribir los drivers necesarios para que teléfonos antiguos puedan ejecutar versiones de Android modernas. Estos programadores acostumbran a especializarse en modelos o [marcas específicas de teléfonos](http://www.htcmania.com). También es habitual que haya quien re-empaquete el código que desarrollan [equipos más o menos consagrados](http://cyanogenmod.com). Los de cyanogenmod por ejemplo tienen el código en github y hay quien se dedica a publicar snapshots de los binarios de ese código y a hacer modificiones

Yendo a lo que nos ocupa que es actualizar el Tattoo hay que tener claros varios conceptos:

- Versión de Android que queremos actualizar. Recomendable la 2.3 por ser la más en uso en estos momentos
- Se denomina ROM al paquete de software binario que contiene el sistema operativo que vamos a instalar. Por problemas de copyright las ROM no vienen con las aplicaciones de Google (Market, sincronización de contactos, …) que deben ser instaladas a parte. El desarrollador de la ROM suele recomendar cuales son las gapps (google applications) que funcionan sobre su ROM.
- Para instalar la ROM (flashear el teléfono) es necesario un sistema intermedio, al que se denomina recovery. El recovery es una especie de sistema operativo muy básico que nos permite hacer un borrado (wipe) de distintas partes del teléfono, instalar la ROM, hacer copia de seguridad de nuestra ROM y datos actuales, … Por supuesto hay un montón de recovery distintos, y en función de la ROM que queramos instalar usaremos uno u otro, generalmente el desarrollador de la ROM recomienda uno.
- GoldCard. Debo decir que no he acabado de entender para que vale esto. Recomiendan hacerlo, porque permite recuperar un teléfono que se queda en modo ladrillo (brick), pero yo sigo sin verlo claro. Por lo que he visto me da la impresión de que la goldcard no tiene nada que ver con el teléfono, si no con la SD.
- Rootear el teléfono. Android es un sistema operativo basado en linux. Tiene por tanto particiones (algunas de las cuales se montan por defecto en sólo lectura), permisos, … A conseguir acceso de root, se lo llama rootear el teléfono.
- Android SDK. Google proporciona lo que se llama un SDK (Software Development Kit). Son un conjunto de aplicaciones que ayudan en las tareas de desarrollo y depuración de software para teléfonos Android. En este caso lo que más nos interesará es el comando «adb» que permite desde el pc abrir una shell (tipo ssh) en el teléfono, subir archivos al teléfono, …

Como siempre hay un montón de tutoriales distintos de como actualizar el teléfono, y como siempre, no te valdrá con seguir ninguno de ellos al pie de la letra, si no que siempre pasará algo y tendrás que acabar combnándolos. Dejo aquí los que yo he leido:

- [Actualiza tu HTC Tattoo a Android 2.1, 2.2 o 2.3](http://www.android.es/tutorial-actualiza-htc-tattoo-a-android-2-1-2-2-o-2-3.html#axzz1m4dje3LN).
- [HTC Tattoo: Full Update Guide](http://wiki.cyanogenmod.com/wiki/HTC_Tattoo:_Full_Update_Guide).
- [Cyanogenmod 7 for the HTC Tattoo](http://forum.cyanogenmod.com/topic/32485-cyanogenmod-7-for-the-htc-tattoo-v7101-10-oct-2011/).

En la segunda parte, voy al grano de como lo hice yo.