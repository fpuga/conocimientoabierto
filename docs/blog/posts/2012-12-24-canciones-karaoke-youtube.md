---
categories:
- Sin categoría
date: 2012-12-24
permalink: /canciones-karaoke-youtube/511/
slug: canciones-karaoke-youtube
tags:
- audio
- bash
- como
- karaoke
- receta
- vídeo
- youtube
---

# Canciones de Karaoke a partir de vídeos del Youtube

Llegan las fechas navideñas, lo que implica fiestas hogareñas y con ello, los amantes del Karaoke se vuelven más exigentes. Como hacer para quitar la voz a uno de esos vídeos de Youtube creados en plan Karaoke. Hagamos un ejemplo con [En El mundo genial de las cosas que dices](http://www.youtube.com/watch?v=Xa8Dv6JTRig) de [Maldita Nerea](http://www.malditanerea.com/). Si te gusta el disco y lo [compras a través de este enlace](http://www.amazon.es/gp/product/B00A5Y7GJY/ref=as_li_ss_tl?ie=UTF8&tag=conociabiert-21&linkCode=as2&camp=3626&creative=24822&creativeASIN=B00A5Y7GJY)![](http://www.assoc-amazon.es/e/ir?t=conociabiert-21&l=as2&o=30&a=B00A5Y7GJY)  
yo me llevo un porcentaje que motiva a seguir escribiendo ;).

El primer paso es buscar en youtube o similar un vídeo donde alguien se haya molestado en añadir la letra a la canción. Buscando en el propio youtube el título de la canción + karaoke se encuentran muchos, por ejemplo [este](http://www.youtube.com/watch?v=oCyDegAl-n4).

A continuación descargaremos el vídeo, hay muchas formas de hacerlo, pero una de las más sencillas es a través de [keepvid](http://keepvid.com/). Llega con poner la dirección del vídeo que queremos descargar, y aceptar la ejecución del applet de java. Pasado un ratillo nos dará la opción de descargar el vídeo en varios formatos. Cualquiera de los formatos es válido, [en este ejemplo usaremos MP4](http://keepvid.com/?url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DoCyDegAl-n4).

Para quedarnos con el audio de la canción usaremos la línea de comandos por ser lo más sencillo. Aunque también se puede hacer [de forma gráfica](http://en.kioskea.net/faq/1266-extracting-the-sound-from-a-video-with-vlc).

`ffmpeg -i fichero_original.mp4 -acodec copy audio.aac`

Para tratar de eliminar la voz del cantante de la parte instrumental del canción usaremos [Audacity](http://audacity.wonderhowto.com/how-to/remove-vocals-audacity-298381/). Hay varios tutoriales por ahí, tanto usando el efecto [vocal removal](http://audacity.wonderhowto.com/how-to/remove-vocals-audacity-298381/) como un [poco más manual](http://audacity.wonderhowto.com/how-to/create-karaoke-tracks-by-removing-vocals-audacity-221886/). Como este proceso es muy rápido y sencillo, prueba los dos procedimientos y quedate con el que tenga más calidad. La voz no es completamente eliminada pero si se reduce bastante. Podemos exportar el audio al formato que queramos, ya que el original estaba en AAC, lo exportaremos a este.

Para recombinar audio y vídeo, volvemos a usar la línea de comandos. Con la siguiente orden le estamos diciendo que coja el audio del fichero audio\_sin\_voz.aac, lo mezcle con el vídeo del fichero original (el audio original será descartado automáticamente) y producirá un nuevo vídeo de salida respetando los codecs originales.

`ffmpeg -i audio_sin_voz.aac -i fichero_original.mp4 -vcodec copy -acodec copy Maldita_Nerea-El_mundo_genial_de_las_cosas_que_dices.mp4`

Puedes ver como queda en [mi youtube](http://youtu.be/_OypwHGGgyE).