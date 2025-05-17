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

Cambiar de Windows a Linux implica cambiar de [sistema de ficheros](http://es.wikipedia.org/wiki/Sistema_de_ficheros). Si somos un poco meticulosos enseguida nos damos cuenta de que no vale simplemente con _copiar y pegar_ puesto que los permisos de los ficheros que hayamos copiado quedaran descolocados. El esquema de permisos será algo como esto `-r-xr-xr-x`, es decir, sin permisos para poder modificar los ficheros ya creados y todos con la posibilidad de ser ejecutados. Además todos los usuarios del sistema pueden leer los datos del resto de usuario, con los peligros de seguridad que ello conlleva.

Migrar entre sistemas Unix (o entre distintas distribuciones de GNU/Linux) no nos dará esta clase de problemas a no ser que no copiemos los datos de una partición del disco duro a otra, sino que lo que hagamos sea hacer una copia de los ficheros a DVD y de ahí de nuevo al disco duro. En este caso, también aplicable a cuando hacemos copias de seguridad, lo más sencillo es empaquetar nuestros datos en un archivo comprimido mediante la utilidad _tar_ pasándole las opciones adecuadas en la línea de comandos para indicarle que preserve los permisos originales de los ficheros.

```shell
# Para crear la copia.
$tar --create --bzip2 --file=copia.tar.bz2 ${HOME}/Documentos

# Para restaurarla
$tar --extract --bzip2 --atime-preserve --same-permissions --file=copia.tar.bz2
```

Las opciones aquí empleadas y más información pueden encontrarse como siempre en la ayuda del programa  
`man tar`

Lo que pretendía explicar era de todas formas otra cosa. En el momento en que tenemos los ficheros copiados y con los permisos establecidos de manera no adecuada debemos tirar del comando `chmod` para cambiarlos. Para cambiar de manera recursiva los permisos de todos los ficheros y directorios a partir del que elijamos usaremos:

```shell
chmod -R 0777
```

El problema es que `chmod` no discrimina tipos de archivo, estaremos asignando los mismos permisos a directorios, documentos de texto, ficheros que nos gustaría que fuesen de solo lectura como fotos, etc. La solución nos la da el comando `find`. Las posibilidades del comando `find` son muy amplias aunque para nuestro objetivo expongo aquí las más interesantes:

-   `-type d`: Devuelve los nombres de los directorios
-   `!`: Niega la siguiente expresión. Así, `! -type d` Devuelve los nombres de los ficheros no directorios
-   `-iname <patron>`: Devuelve los nombres de ficheros (sin distinguir mayúsculas y minúsculas) que coinciden con un determinado patrón, podemos usar los comodines `*` y `?`
-   `-iregex <patron>`: Como el anterior pero patrón es una expresión regular
-   `-exec <comando> {} ;`: Ejecuta el comando `<comando>`. `{}` Representa los nombres de archivo devueltos por find, es decir que ejecutamos el comando para cada fichero devuelto por find. `;` Es usado por la shell para reconocer el final del comando.

Así para el caso más habitual en que deseamos otorgar permisos de lectura, escritura y ejecución para directorios, y de lectura y escritura para el resto de archivos (y ninguno para el resto de usuarios) los comandos serían:

```shell
find <directorio> -type d -exec chmod 0700 {} ;
find <directorio> ! -type d -exec chmod 0600 {} ;
```

Para aquellos con pocas ganas de jugar con los comandos, he escrito un pequeño script. Para ejecutarlo sólo hay que copiar el código y guardarlo en un fichero de texto de nombre `cambiar_permisos.sh` (por ejemplo). Abrir una consola y escribir:

```shell
bash cambiar_permisos.sh <directorio>
```

En el script se distinguen tres tipos de archivos:

-   ficheros con las extensiones `.pdf .jpg .jpeg .bmp .png .gif .avi .mpg .mpeg .mp3 .ogg` a los que se asignan los permisos `0400`
-   directorios, a los que se asignan los permisos `0700`
-   resto de ficheros, a los que se asignan los permisos `0600`

```bash
#!/bin/sh
# (C) 2007. Francisco Puga Alonso.
# Este software se distribuye sin ninguna garantía.
# El autor no se hace responsable de los posibles daños de su uso
# Este software pertenece al dominio público

# Para consultar la ayuda del script ejecute ./cambiar_permisos -h
# Este script cambia los permisos de los ficheros y directorios a partir del directorio
# de entrada que nosotros le indiquemos. A la hora de cambiar los permisos, asigna
# permisos separados a directorios, ficheros de sólo lectura y resto de ficheros. Si
# quiere saber que se consideran ficheros de sólo ejecute ./cambiar_permisos -h o
# consulte el valor de la variable EXT_READ

# Se comprueba que el directorio origen existe, pero no comprueba que tengamos
# los permisos adecuados para cambiarlos

# Ficheros considerados de sólo lectura.
EXT_READ=".*pdf .*jpg .*jpeg .*bmp .*png .*gif .*avi .*mpg .*mpeg .*mp3 .*ogg"

#EXT_REGEX contiene la expresión regular que identificará estos ficheros
EXT_REGEX=".*pdf|.*jpg|.*jpeg|.*bmp|.*png|.*gif|.*avi|.*mpg|.*mpeg|.*mp3|.*ogg"

#Permisos por defecto aplicados a los distintos tipos de fichero considerados
PDIRS="0700"
PREAD="0400"
POTHERS="0600"
DIR="/dev/null"

ayuda() {
    #Imprime la información de ayuda
    echo "Usage: $0  [-d ] [-r ] [-o ]"
    echo "-d :: Permisos aplicados a directorios y subdirectorios. Por defecto 0700"
    echo -e "-r :: Permisos aplicados a los siguientes formatos de archivo "
    echo -e "(Por defecto 0400):n$EXT_READ"
    echo "-o :: Permisos aplicados al resto de ficheros. Por defecto 0600"
    echo "-h :: Imprime esta ayuda"
    exit
}

if [ $# = "0" ] ; then
    echo "Debe especificar un directorio. Use . para referirse al directorio actual"
    ayuda $0
else
    if ! [ -d $1 ] ; then
        echo "El primer parámetro debe ser un directorio"
        ayuda $0
    else
        DIR="$1"
    fi

    shift

    while (( $# )) ; do
        case $1 in
            -d ) PDIRS="$1";;
            -r ) PREAD="$1";;
            -o ) POTHERS="$1";;
            -h ) ayuda $0 ;;
            * ) echo "Opción Incorrecta" ; ayuda $0 ;;
        esac
        shift
    done
fi

find "$DIR" -mount -type d -exec chmod "$PDIRS" {} ;
find "$DIR" -mount ! -type d -and -iregex "$EXT_NOW" -exec chmod "$PREAD" {} ;
find "$DIR" -mount ! -type d -and ! -iregex "$EXT_NOW" -exec chmod "$POTHERS" {} ;
```

Para la realización de este script me he inspirado en este post de [Javier Sancho](http://www.jsancho.org/2004/01/28/18/trackback/)
