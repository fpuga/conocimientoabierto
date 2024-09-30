---
categories:
- comunicaciong
- linux
- receta
- recomendacion
date: 2008-01-10
permalink: /hacer-presentaciones-de-fotos-en-formato-video/35/
slug: hacer-presentaciones-de-fotos-en-formato-video
---

# Hacer presentaciones de fotos en formato vídeo

He estado buscando programas para linux que de manera sencilla permitan crear presentaciones de foto en formato vídeo, con la posibilidad de añadirle música y algún efecto para que quede bonito. Los dos últimos son [servicios web](http://es.wikipedia.org/wiki/Servicio_Web#Ventajas_de_los_servicios_Web) con los que he quedado realmente contento y que os recomiendo probar.

[cinelerra](http://barnadriva.net/staticpages/index.php?page=20051101191815211). Un programa muy potente para la edición de vídeo. Tal vez es complicarse demasiado la vida para hacer un vídeo a partir de fotos.

[dir2slideshow + dvd-slideshow](http://zenon.wordpress.com/2005/06/21/haciendo-una-pelicula-con-fotos/). <span style="font-style: italic">(Aviso que no lo he probado, hablo de oídas)</span> Dos comandos para consola de linux que nos permiten crear un DVD con las fotos. Lo bueno es que es rápido, lo malo es que no permite efectos, hay que ordenar las fotos a mano (cambiando el nombre de las fotos por números por ejemplo), y que a mi particularmente no me gustan los DVD. Para reproducirlos en el ordenador hay que tener los programas adecuados, ocupan mucho, … y cualquier reproductor de salón moderno puede leer vídeo mpg, no hace falta que esté en formato DVD. También tenemos software con [interfaz gráfico](http://blogdrake.net/node/7998#comment-35926) que hace lo mismo o más.

[Digikam](http://digikam.org/) es un magnífico programa para la visualización y la gestión de fotos (clasificación mediante etiquetas, álbumes,…). Además es el software predefinido de KDE para la descarga de fotos de la cámara digital. Posee un sistema de plugins que permite retocar fácilmente las imágenes. El paquete kipi-plugins añade a digikam la posibilidad de convertir pases de imágenes en un vídeo mpg y añadirle audio (herramientas -&gt; crear presentación mpeg). Si buscamos un todo en uno digikam + kipi-plugins es nuestra opción, aunque tiene varios defectos:

- El único efecto que permite añadir es que la foto que estamos viendo se vaya difuminando para aparecer debajo la siguiente. Conseguimos esto indicando en «velocidad de transición entre las imágenes» un valor distinto de cero.
- Con determinadas versiones de programas la [codificación de vídeo no funciona correctamente](http://blogdrake.net/node/3438).
- El único parámetro del formato del vídeo que podemos controlar es si queremos que sea VCD, SVCD, XVCD o DVD. Entiendo que los de más calidad serán XVCD y DVD y que ambos se pueden leer sin problemas en los reproductores de salón.
- He tenido problemas con algunos mp3 y he tenido que pasarlos a wav para que funcionara.

Recordemos que aunque un programa este diseñado para KDE, esto no significa que no funcione en otro entorno gráfico para linux como Gnome (el predefinido en ubuntu), es simplemente que será menos eficiente por tener que cargar librerías adicionales (además de tener que instalar esas librerías adicionales, cuestión que hoy en día se hace de manera transparente al usuario gracias a los sistemas de gestión de paquetes de las distintas distribuciones). Creo que Picasa también [tiene algo parecido](http://picasa.google.com/support/bin/topic.py?topic=9402).

Como ejemplo de lo que hace este programa podéis ver el vídeo de mi [post anterior](http://conocimientoabierto.blogspot.com/2008/01/imgenes-del-ao-2007-por-reuters.html).

[Manslide](http://kde-apps.org/content/show.php/Manslide?content=72739) parece el programa definitivo de KDE para crear presentaciones de fotos en formatos de vídeo, pero desgraciadamente por algún problema relacionado con los drivers de la tarjeta gráfica no he podido probarlo. Aún así os aconsejo intentar usarlo porque tiene muy buena pinta.

[Animoto](http://animoto.com/) es un servicio web que permite crear presentaciones muy chulas de manera automática, pero tiene varios inconvenientes:

- En la versión gratuita la duración máxima de los vídeos es de 30 segundos y no se pueden descargar.
- No tienes control sobre el resultado final, es decir tu simplemente subes las imágenes (en función del número de imágenes que subas así será la duración final del vídeo) y escoges la música, el resto lo hace él.
- No he conseguido ni remezclar ni editar un video desde firefox+linux (en windows+firefox sin funciona). En teoría cuando estás viendo un vídeo y le das a <span style="font-style: italic">«remix»</span> aparecen dos opciones <span style="font-style: italic">«one-click remix»</span> y <span style="font-style: italic">«editing remix»</span>. Con la primera obtendremos un vídeo nuevo (con las mismas imágenes y música) con la segunda podremos cambiar las imágenes o la música.
- La creación del vídeo tarda unos 10 minutos, durante los cuales parece como si se hubiera quedado colgado. A la derecha aparece un reloj pero no se mueve, por lo que no puedes determinar cuanto queda para que acabe. Lo compensan porque puedes cerrar el navegador sin peligro, y cuando el vídeo está listo te mandan un correo.

Para un vídeo de 30 segundos hacen falta unas 15 o 20 imágenes, aunque la música también influye, si es tranquila las imágenes aparecerán más despacio que si tiene más ritmo. Podemos hacer que una o varias de nuestras imágenes salgan resaltadas en el vídeo, para ello una vez que las hemos subido las seleccionamos y pinchamos sobre <span style="font-style: italic">«spotligth»</span>.

Algo que me gusta mucho de este servicio es que promociona el uso de música copyleft, de hecho permite usar varias canciones copyleft que ya tienen almacenadas en lugar de subir la música desde tu ordenador. Si la subimos, cuando ya está cargada tenemos la opción de fijar cual será el fragmento de audio que suene en nuestro vídeo. Cuando esté subida tenemos la opción de escucharla, cuando detectemos el inicio del fragmento que nos interesa pulsamos pausa y le damos a continuar. De la [faq](http://animoto.com/help/faq) de animoto.

<div><div class="faq_question"></div>> <div class="faq_question" style="font-weight: bold">What’s the point of changing the start point of the music?</div><div class="faq_answer">Many songs start with some dead time or with a build-up that you might not want to include in your ANIMOTO video. With the song Start Point Slider, you can tell us where to start your song. Press ‘PLAY’ and wait until just the right moment; then press ‘PAUSE’. If you are making an **Animoto Short** and have selected a song from our collection, the Start Point Slider will be disabled since a customized 30-second version of the song has already been edited for you.
> 
> </div>

<div class="faq_answer">Con esta herramienta he creado dos vídeos que podéis ver [aquí](http://augaconfronteiras.blogspot.com/2008/01/recopilacin-de-fotos-da-campaa.html) y [aquí](http://www.marinerosbouzas.com/). [  
Jumpcut](http://www.jumpcut.com/) es un servicio web para la edición y compartición de vídeo (como youtube pero que además permite crear y remezclar. Para mi es el rey, no sólo por las posibilidades que aporta y lo sencillo que es sino por [lo que implica](http://www.deugarte.com/la-revolucion-de-corta-y-pega/trackback).

</div></div>