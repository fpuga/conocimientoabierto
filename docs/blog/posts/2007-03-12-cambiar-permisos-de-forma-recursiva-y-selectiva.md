---
categories:
- migracion
- scripting
- shell
date: 2007-03-12
permalink: /cambiar-permisos-de-forma-recursiva-y-selectiva/7/
slug: cambiar-permisos-de-forma-recursiva-y-selectiva
---

# Cambiar permisos de forma recursiva y selectiva

Por culpa de un modem con drivers propietarios (y mi ineptitud para instalar unos libres) llevaba unos 6 meses usando Windows. En otro artículo hablaré de mi odisea particular con los drivers, pero en este quiero hablar de uno de los problemas que nos asaltan cuando migramos de sistema operativo, traspasar los datos que tengamos almacenados en el antiguo sistema al nuevo.

Cambiar de Windows a Linux implica cambiar de [sistema de ficheros](http://es.wikipedia.org/wiki/Sistema_de_ficheros). Si somos un poco meticulosos enseguida nos damos cuenta de que no vale simplemente con *copiar y pegar* puesto que los permisos de los ficheros que hayamos copiado quedaran descolocados. El esquema de permisos será algo como esto *-r-xr-xr-x*, es decir, sin permisos para poder modificar los ficheros ya creados y todos con la posibilidad de ser ejecutados. Además todos los usuarios del sistema pueden leer los datos del resto de usuario, con los peligros de seguridad que ello conlleva.

Migrar entre sistemas Unix (o entre distintas distribuciones de GNU/Linux) no nos dará esta clase de problemas a no ser que no copiemos los datos de una partición del disco duro a otra, sino que lo que hagamos sea hacer una copia de los ficheros a DVD y de ahí de nuevo al disco duro. En este caso, también aplicable a cuando hacemos copias de seguridad, lo más sencillo es empaquetar nuestros datos en un archivo comprimido mediante la utilidad *tar* pasándole las opciones adecuadas en la línea de comandos para indicarle que preserve los permisos originales de los ficheros.

Para crear la copia.  
`$tar --create --bzip2 --file=copia.tar.bz2 /home/fran/Documentos`

Para restaurarla  
`$tar --extract --bzip2 --atime-preserve --same-permissions --file=copia.tar.bz2`

Las opciones aquí empleadas y más información pueden encontrarse como siempre en la ayuda del programa  
`$man tar`

Lo que pretendía explicar era de todas formas otra cosa. En el momento en que tenemos los ficheros copiados y con los permisos establecidos de manera no adecuada debemos tirar del comando *chmod* para cambiarlos. Para cambiar de manera recursiva los permisos de todos los ficheros y directorios a partir del que elijamos usaremos:  
`$chmod -R 0777 `

El probema es que chmod no discrimina tipos de archivo, estaremos asignando los mismos permisos a directorios, documentos de texto, ficheros que nos gustaria que fuesen de solo lectura como fotos, etc. La solución nos la da el comando *find*. Las posibilidades del comando find son muy amplias aunque para nuestro objetivo expongo aquí las más interesantes:

- -type d : Devuelve los nombres de los directorios
- ! : Niega la siguiente expresión. Así, *! -type d* Devuelve los nombres de los ficheros no directorios
- -iname <u>patron</u> : Devuelve los nombres de ficheros (sin distinguir mayúsculas y minúsculas) que coinciden con un determinado patrón, podemos usar los comodines \* y ?
- -iregex <u>patron</u> : Como el anterior pero patrón es una expresión regular.
- -exec <u>comando</u> {} ; : Ejecuta el comando <u>comando</u>. {} Representa los nombres de archivo devueltos por find, es decir que ejecutamos el comando para cada fichero devuelto por find. ; Es usado por la shell para reconocer el final del comando.

Así para el caso más habitual en que deseamos otorgar permisos de lectura, escritura y ejecución para directorios, y de lectura y escritura para el resto de archivos (y ninguno para el resto de usuarios) los comandos serían:  
` find <u>directorio</u> -type d -exec chmod 0700 {} ;<br></br>find <u>directorio</u> ! -type d -exec chmod 0600 {} ;`

Para aquellos con pocas ganas de jugar con los comandos, he escrito un pequeño script. Para ejecutarlo sólo hay que copiar el código y guardarlo en un fichero de texto de nombre cambiar\_permisos.sh (por ejemplo). Abrir una consola y escribir:  
`$sh cambiar_permisos.sh <u>directorio</u>`  
En el script se distinguen tres tipos de archivos:

- ficheros con las extensiones .\*pdf .\*jpg .\*jpeg .\*bmp .\*png .\*gif .\*avi .\*mpg .\*mpeg .\*mp3 .\*ogg a los que se asignan los permisos 0400
- directorios, a los que se asignan los permisos 0700
- resto de ficheros, a los que se asignan los permisos 0600

```
<br></br>#!/bin/sh<br></br><br></br># Francisco Puga Alonso.<br></br># 10/03/2007  v 0.2<br></br><br></br># Este software se distribuye sin ninguna garantía.<br></br># El autor no se hace responsable de los posibles daños de su uso<br></br># Este software pertenece al dominio público<br></br># Para consultar la ayuda del script ejecute ./cambiar_permisos -h<br></br><br></br># Este script cambia los permisos de los ficheros y directorios a partir del<br></br># directario de entrada que nosotros le indiquemos. A la hora de cambiar los<br></br># permisos, asigna permisos separados a directorios, ficheros de sólo lectura<br></br># y resto de ficheros. Si quiere saber que se consideran ficheros de sólo<br></br># ejecute ./cambiar_permisos -h o consulte el valor de la variable EXT_READ<br></br><br></br># Se comprueba que el directorio origen existe, pero no comprueba que tengamos<br></br># los permisos adecuados para cambiarlos<br></br><br></br><br></br>#Ficheros considerados de sólo lectura.<br></br>EXT_READ=".*pdf .*jpg .*jpeg .*bmp .*png .*gif .*avi .*mpg .*mpeg .*mp3 .*ogg"<br></br>#EXT_REGEX contiene la expresión regular que identificará estos ficheros<br></br>EXT_REGEX=".*pdf|.*jpg|.*jpeg|.*bmp|.*png|.*gif|.*avi|.*mpg|.*mpeg|.*mp3|.*ogg"<br></br><br></br>#Permisos por defecto aplicados a los distintos tipos de fichero considerados<br></br>PDIRS="0700"<br></br>PREAD="0400"<br></br>POTHERS="0600"<br></br>DIR="/dev/null"<br></br><br></br><br></br>ayuda() {<br></br>#Imprime la información de ayuda<br></br>echo "Usage: $0  [-d ] [-r ] [-o ]"<br></br>echo "-d :: Permisos aplicados a directorios y subdirectorios. Por defecto 0700"<br></br>echo -e "-r :: Permisos aplicados a los siguientes formatos de archivo "<br></br>       echo -e "(Por defecto 0400):n$EXT_READ"<br></br>echo "-o :: Permisos aplicados al resto de ficheros. Por defecto 0600"<br></br>echo "-h :: Imprime esta ayuda"<br></br>exit<br></br>}<br></br><br></br><br></br>if [ $# = "0" ] ; then<br></br>    echo "Debe especificar un directorio. Use . para referirse al directorio actual"<br></br>ayuda $0<br></br><br></br>else<br></br>if ! [ -d $1 ] ; then <br></br> echo "El primer parametro debe ser un directorio"<br></br> ayuda $0<br></br>else DIR="$1"<br></br>fi<br></br><br></br>shift<br></br><br></br>while (( $# )) ; do<br></br> case $1 in<br></br>  -d ) PDIRS="$1";;<br></br>  -r ) PREAD="$1";;<br></br>  -o ) POTHERS="$1";;<br></br>  -h ) ayuda $0 ;;<br></br>  * ) echo "Opción Incorrecta" ; ayuda $0 ;;<br></br> esac<br></br> shift<br></br>done<br></br>fi<br></br><br></br><br></br>find "$DIR" -mount -type d -exec chmod "$PDIRS" {} ;<br></br>find "$DIR" -mount ! -type d -and -iregex "$EXT_NOW" -exec chmod "$PREAD" {} ;<br></br>find "$DIR" -mount ! -type d -and ! -iregex "$EXT_NOW" -exec chmod "$POTHERS" {} ;<br></br>
```

El código no me ha quedado demasiado bien maquetado pero aún tengo que mejorar mi CSS. Para la realización de este script me he inspirado en este post de [Javier Sancho](http://www.jsancho.org/2004/01/28/18/trackback/)