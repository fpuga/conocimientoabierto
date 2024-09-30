---
id: 1004
title: 'Presentaciones de fotos en formato vídeo (slideshows) desde la línea de comandos'
date: '2020-07-18T11:00:52+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=1004'
permalink: /presentaciones-de-fotos-en-formato-video-slideshows-desde-la-linea-de-comandos/1004/
categories:
    - 'Sin categoría'
tags:
    - linux
    - receta
    - vídeo
---

Hace ya algunos años apareció en este blog como [hacer presentaciones de fotos en formato vídeo](http://conocimientoabierto.es/hacer-presentaciones-de-fotos-en-formato-video/35/). A pesar de que hay muchos programas buenos para editar vídeo en GNU/Linux, esta vez quería tener un proceso sencillo y fácilmente replicable aún a costa de perder un poco de calidad o efectos (como degradado entre imágenes, …).

En este tutorial veremos, sin entrar en muchos detalles (mis conocimientos no dan para ello), una forma muy rápida de crear un slideshow con música usando únicamente el terminal. Como limitante partimos de la base de que todas las imágenes están en el mismo formato (en este caso JPEG)

## Las herramientas

`<br></br>sudo apt-get install --install-recommends rename imagemagick ffmpeg<br></br>`

- [rename](https://www.howtogeek.com/423214/how-to-use-the-rename-command-on-linux/) permite renombrar archivos usando expresiones regulares
- [imagemagick](https://imagemagick.org)
- [ffmpeg](https://ffmpeg.org/)

## Normalizar los nombres y ordenar las imágenes

El primer paso es ordenar las imágenes poniéndolos un «nombre normalizado» que represente ese orden. En este caso partimos de unas imágenes que ya tienen cierto orden, pero arreglamos las mayúsculas, usamos dos caracteres para los números y ajustamos las del medio.

Cada caso será muy particular pero veamos un ejemplo:

`<br></br>$ cp -r original copia<br></br>$ cd copia<br></br>$ ls<br></br>0.JPG   1_1.JPG  12_1.JPG  13.jpg  15.jpg  17.JPG  19.jpg  20.jpg  22.jpg  24.jpg  26.jpg  28.jpg  2.JPG   31.jpg  4.JPG  6.JPG  8.JPG<br></br>10.JPG  11.JPG   12.JPG    14.jpg  16.jpg  18.jpg  1.JPG   21.JPG  23.jpg  25.JPG  27.jpg  29.jpg  30.jpg  3.JPG   5.jpg  7.JPG  9.JPG<br></br>$ rename 's/.JPG/.jpg/' *.JPG<br></br>$ rename 's/3(\d).jpg/5$1.jpg/' 3*.jpg<br></br>$ rename 's/2(\d).jpg/4$1.jpg/' 2*.jpg<br></br>$ rename 's/1([2-9]).jpg/3$1.jpg/' 1*.jpg<br></br>$ ls<br></br>0.jpg   1_1.jpg  12_1.jpg  2.jpg   33.jpg  35.jpg  37.jpg  39.jpg  40.jpg  42.jpg  44.jpg  46.jpg  48.jpg  4.jpg   51.jpg  6.jpg  8.jpg<br></br>10.jpg  11.jpg   1.jpg     32.jpg  34.jpg  36.jpg  38.jpg  3.jpg   41.jpg  43.jpg  45.jpg  47.jpg  49.jpg  50.jpg  5.jpg   7.jpg  9.jpg<br></br>$ mv 12_1.jpg 31.jpg<br></br>$ rename 's/1([0-1]).jpg/2$1.jpg/' 1*.jpg<br></br>$ rename 's/([1-9]).jpg/1$1.jpg/' ?.jpg<br></br>$ mv 0.jpg 00.jpg<br></br>$ mv 1_1.jpg 01.jpg<br></br>$ ls<br></br>00.jpg  11.jpg  13.jpg  15.jpg  17.jpg  19.jpg  21.jpg  32.jpg  34.jpg  36.jpg  38.jpg  40.jpg  42.jpg  44.jpg  46.jpg  48.jpg  50.jpg<br></br>01.jpg  12.jpg  14.jpg  16.jpg  18.jpg  20.jpg  31.jpg  33.jpg  35.jpg  37.jpg  39.jpg  41.jpg  43.jpg  45.jpg  47.jpg  49.jpg  51.jpg<br></br>`

## Rotar las imágenes

A pesar de que en la previsualización del explorador de archivos podamos ver todas las imágenes rectas, alguna de ellas puede estar girada. Esto es por qué muchas herramientas usan por defecto [los metadatos EXIF de la imagen para rotarlas](https://jdhao.github.io/2019/07/31/image_rotation_exif_info/) de la forma lógica.

`<br></br># las que no tengan un `1` están rotadas<br></br>identify -verbose * | grep -E '(Image:|Orientation)'`

\# Rotarlas. https://stackoverflow.com/a/19475281/930271  
\# Esto modifica todas las fotos, por lo que mejor usarlo sólo con la que deben  
\# ser rotadas  
mogrify -auto-orient \*.jpg

identify -verbose \* | grep -E '(Image:(.\*)|exif:Orientation: \[2-9\])'  
mogrify -auto-orient 16.jpg  
mogrify -auto-orient 45.jpg

## Identificar tamaños y «aspect ratio»

Para montar las imágenes en el vídeo debemos investigar sus tamaños y sobre todo la relación de aspecto. El comando [identify](https://imagemagick.org/script/identify.php) de ImageMagick nos puede dar la información más relevante y podemos ordenarla por *aspect ratio*, anchura, …

`<br></br># https://unix.stackexchange.com/questions/50252`

\# ordenadas por aspect ratio  
$ identify -format "%\[fx:w/h\] %w %h %M\\n" \*.jpg | sort -n -k1

1.5 4608 3072 20.jpg  
0.75 1944 2592 15.jpg  
0.75 2304 3072 16.jpg  
0.75 3864 5152 45.jpg  
1.33333 1280 960 44.jpg  
1.33333 1280 960 46.jpg  
1.33333 1280 960 47.jpg  
1.33333 2592 1944 13.jpg  
1.33333 3072 2304 17.jpg  
1.33333 3264 2448 01.jpg  
1.33333 3264 2448 14.jpg  
1.33333 3264 2448 19.jpg  
1.33333 3264 2448 33.jpg  
1.33333 4000 3000 43.jpg  
1.33333 4000 3000 50.jpg  
1.33333 4000 3000 51.jpg  
1.33333 4320 3240 18.jpg  
1.33333 4608 3456 31.jpg  
1.33333 4672 3504 34.jpg  
1.33333 4672 3504 35.jpg  
1.33333 5120 3840 49.jpg  
1.33333 5152 3864 32.jpg  
1.33333 5152 3864 37.jpg  
1.33472 1280 959 38.jpg  
1.33884 2592 1936 00.jpg  
1.33884 2592 1936 11.jpg  
1.49841 3776 2520 21.jpg  
1.77778 3072 1728 12.jpg  
1.77778 3264 1836 39.jpg  
1.77778 3968 2232 41.jpg  
1.77778 5312 2988 36.jpg  
1.77778 5312 2988 40.jpg  
1.77778 5312 2988 42.jpg  
1.77778 5312 2988 48.jpg

\# ordenadas por width  
identify -format "%\[fx:w/h\] %w %h %M\\n" \*.jpg | sort -n -k2

Aquí la clave es:

- Ajustar las imágenes para que tengan todas la misma relación de aspecto y que no salgan deformadas. Cosa que haremos directamente con ffmpeg al crear el vídeo.
- Escoger el tamaño de referencia a usar para las imágenes. La «redimensión» la haremos directamente al crear el vídeo.

Sin entender mucho de vídeos mi criterio es coger el aspect ratio más común a las imágenes, en este caso **1.333**, y un tamaño intermedio, de modo que haya pocas imágenes por debajo de ese tamaño, y que al ampliar no pixelen demasiado, en este caso me quedo con **2592×1936**

## Montar el vídeo

La wiki de ffmpeg da el comando básico para [hacer el slideshow](https://trac.ffmpeg.org/wiki/Slideshow), y en stackoverflow [también](https://stackoverflow.com/questions/24961127/how-to-create-a-video-from-images-with-ffmpeg) hay buenas [respuestas](https://stackoverflow.com/questions/44634765/ffmpeg-aspect-ratio-of-image-in-a-slideshow)

El comando que usaremos en este caso es:

`<br></br>ffmpeg -framerate 1/5 -pattern_type glob -i '*.jpg' -i audio.mp3 -vf 'scale=2592:1936:force_original_aspect_ratio=decrease,pad=2592:1936:(ow-iw)/2:(oh-ih)/2,setsar=1' -c:v libx264 -c:a copy -crf 14 -r 25 -pix_fmt yuv420p -shortest output.mp4<br></br>`

Los parámetros más relevantes para el *slideshow*:

- `-framerate 1/5`: El denominador define cuanto se mostrará cada imagen
- `-pattern_type glob -i '*.jpg'`: Cuando las imágenes no están ordenadas exactamente de forma secuencial con este parámetro las meterá en el video ordenadas por nombre
- `'scale=2592:1936:force_original_aspect_ratio=decrease,pad=2592:1936:(ow-iw)/2:(oh-ih)/2,setsar=1'`: Escala las imágenes a 2592×1936 y mete bandas negras de relleno cuando no se pueda conservar la relación de aspecto