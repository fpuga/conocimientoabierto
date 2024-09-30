---
id: 157
title: 'Como ocultar la dirección de correo para combatir el spam'
date: '2009-09-17T13:51:31+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=157'
permalink: /como-ocultar-direccion-correo-combatir-spam/157/
categories:
    - General
tags:
    - como
    - correo-e
    - 'how to'
    - spam
---

Algo que tenía pendiente desde hace ya demasiado era poner una dirección de correo electrónico de contacto en el blog. Todas las guías sobre blogging hablan de la importancia de incluirlo y resulta lógico el permitir que tus lectores contacten contigo en privado pero hasta ahora, más que nada por vagancia, no me había decidido a hacerlo.

Antes de colocar la dirección tienes que pensar que tipo de blog tienes y el uso que le quieras dar, dependiendo de esto puedes colocar tu dirección de correo habitual o bien crear una a propósito. Independientemente de lo que decidas debes saber que cada vez que publicas tu dirección en algún sitio estás creando una nueva fuente de entrada de spam. Los spammers tienen robots que se dedican a rastrear las páginas web en busca de direcciones de correo-e para añadirlas a sus bases de datos y enviarte (todavía más) spam. Si bien los filtros anti-spam funcionan bastante bien hay una opción sencilla para evitar que los robots puedan reconocer la direcciones de correo, lo único que hay que hacer es **convertir tu dirección de correo en una imagen**. Yo conozco tres servicios web que hacen esto automáticamente:

1. [Hide Text](http://www.hidetext.net/index.php)
2. [Nexodyne](http://services.nexodyne.com/email/index.php)
3. [Safe Mail](http://safemail.justlikeed.net/index.php)

Los tres servicios funcionan igual, introduces tu dirección de correo en el formulario, ajustas alguna opción del tamaño de letra y color del texto y le das a siguiente. Los tres se comprometen a no vender nunca tu dirección y a alojar la imagen de forma indefinida en sus servidores para poder servirla desde su servidor. En el primero de ellos da la opción de borrar la imagen una vez creada, para que no este alojada más en su servidor. En los tres tienes la opción de descargar la imagen para alojarla en tu propio hosting.

Si quieres usarlos simplemente prueba como queda la imagen con unos y con otros y escoge el que más te guste. Luego te recomiendo que la descargues (y si usas Hide Text la borres) y la subas a tu hosting. Es mejor servirla desde tu hosting para minimizar dependencia de terceros y porque el consumo de ancho de banda va a ser muy escaso. Desde ese momento, suponiendo que la imagen esté por ejemplo en http://conocimientoabierto.es/img/correo-e.png, para incluirla en un comentario en un blog [debes usar la etiqueta html img](http://services.nexodyne.com/email/faq.html), quedaría así

> Si quieres puedes probar como queda dejando un comentario en esta entrada o escribiéndome a mi correo &lt;img src=»http://conocimientoabierto.es/img/correo-e.png»&gt;

> Si quieres puedes probar como queda dejando un comentario en esta entrada o escribiéndome a mi correo ![](http://conocimientoabierto.odiseus.org/wp-content/blogs.dir/16/files/galerias/enelblog/correo-e.png)

Por supuesto, en lugar de usar estos servicios puedes arrancar el gimp (o el paint si todavía usas Windows) y crearla la imagen tu mismo porque es muy sencillo. Esta es la mejor opción desde mi punto de vista.

Problemas:

- La opción de pinchar con el botón para que automáticamente se abra el cliente de correo desaparece.
- No se puede copiar y pegar la dirección, lo que es un pequeño incordio.
- La imagen que uses, tamaño, colores, … puede romper la maquetación de la página donde la uses

Existe una técnica más sencilla que la de usar imágenes consistente simplemente en *ofuscar* tu dirección de correo **usando texto en lugar de símbolos** de modo que no sea reconocida por los bots. Por ejemplo en lugar de mail\_falso@hosting\_falso.no usa:

1. mail\_falso &lt;at&gt; hosting\_falso &lt;dot&gt; no
2. mail\_falsoANTISPAM@hosting\_falso.no
3. mail\_falso &lt;ARROBA&gt; hosting\_falso.no
4. o alguna combinación

Si usas este método te recomiendo emplear la tercera opción, puesto que hay mucha gente que puede no reconocer el texto &lt;at&amp;gt como sinónimo de arroba o entender que el texto ANTISPAM no forma parte de la dirección real. Desconozco hasta que punto la opción de ofuscar la dirección es válida, dado que a los spammers no creo que les cueste mucho reprogramar su software para reconocer este tipo de truquillos, pero en principio me parece que esto es más cómodo para el usuario que usar imágenes.

Como siempre la decisión última dependerá del uso que cada uno vaya a darle. Yo personalmente, he decidido pasar de usar imágenes, el spam está ahí y el volumen de tráfico que te va a evitar usar imágenes no creo que compense la incomodidad para el usuario o para ti al tener que usar etiquetas html/[bbcode](http://es.wikipedia.org/wiki/BBCode) para introducir tu correo en lugar de escribir el texto directamente.

Otro día seguiremos con algunas técnicas sencillas para no tener que dar nuestra dirección real cuando nos registramos en un foro o una de esas páginas que apenas vamos a usar un par de veces. [Subscríbete a mi RSS](http://feeds.conocimientoabierto.es) para estar al día.