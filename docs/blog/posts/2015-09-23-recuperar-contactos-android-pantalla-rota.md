---
id: 819
title: 'Un sistema como otro cualquiera para recuperar tus contactos en un Android con la pantalla rota'
date: '2015-09-23T21:15:44+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=819'
permalink: /recuperar-contactos-android-pantalla-rota/819/
categories:
    - 'Sin categoría'
tags:
    - android
    - como
    - 'dispositivos móviles'
    - hardware
    - 'how to'
    - receta
---

Uno de esos días cualquiera en que te llega alguien (a quien no puedes mandar a <del>freír puñetas</del> buscar en google) que una semana después de comprarse su primer móvil con Android se le ha caído al suelo, se le ha roto la pantalla y quiere recuperar sus contactos.

La primera respuesta es fácil. No hay problema, estarán en la memoria de la tarjeta, o sincronizados en la cuenta de google. Pero no, ni uno ni otro. Están en la memoria del teléfono.

Las primeras búsquedas en google se refieren a sistemas que necesitan que el teléfono esté *rooteado* para por ejemplo [copiar la base de datos (sqlite) con los contactos](https://chombium.wordpress.com/2012/09/30/android-how-to-backup-contacts-and-sms-messages/). Teniendo el sqlite es fácil sacar un csv o al menos un listado que copiar a mano. Pero por supuesto el teléfono no está rooteado.

Bueno, la pantalla no está del todo muerta, la parte de arriba responde. Así que igual da para hacer pulsar en los sitios clave. El teléfono en sí no puede desbloquearse, pero si se puede llegar al botón de «*Ajustes*«, porque no tiene activado la protección por figura. Jugando con la rotación automática para modificar los sitios a pulsar, podemos llegar de «*Ajustes*» a «*Aplicaciones*«, de ahí a la pestaña de «*Todas*» y desplazarnos hasta «*Contactos*«. Muchas de las apps, como la «*Contactos*» tienen un botón «*Lanzar*» equivalente a como si las abrieras desde el *Launcher*.

Estando en la app de Contactos sólo hay que poder lanzar la opción de «*Exportar*«, pero en este teléfono ese menú se lanza desde la tecla de «*Menu*» que no responde. Teóricamente con el [conector adecuado](https://en.wikipedia.org/wiki/USB_On-The-Go), podríamos conectar un ratón al teléfono para controlarlo, pero a falta de conector resulta que es posible [enviar eventos (como pulsaciones de teclas) al móvil a través de adb](http://thecodeartist.blogspot.de/2011/03/simulating-keyevents-on-android-device.html).

«Pulsamos» la tecla de menú:

`<br></br>$ ./adb shell input keyevent 82<br></br>`

Y un par de veces KEYCODE\_DPAD\_DOWN que actúa como el curso hacia abajo

`<br></br>$ ./adb shell input keyevent 20<br></br>`

Y enviamos el evento KEYCODE\_DPAD\_CENTER para hacer click / pulsar / tap sobre la opción seleccionada

`<br></br>$ ./adb shell input keyevent 23<br></br>`

Y ya tenemos lanzada la la aplicación de exportación. Siguiendo un proceso parecido de ver en que partes de la pantalla de puede pulsar y enviando eventos desde adb, seleccionamos como origen el smartphone, como destino la cuenta de gmail. Y listo. En un par de minutos tenemos los contactos en gmail, desde donde podemos exportarlos a csv, vcard o listos para ser usados desde otro teléfono android.

Espero que a alguien le sea de ayuda. Se admiten otros modos de hacerlo en los comentarios.