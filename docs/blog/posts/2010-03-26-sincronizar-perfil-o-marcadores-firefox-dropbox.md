---
categories:
- General
date: 2010-03-26
permalink: /sincronizar-perfil-o-marcadores-firefox-dropbox/220/
slug: sincronizar-perfil-o-marcadores-firefox-dropbox
tags:
- backup
- como
- dropbox
- firefox
- how to
- receta
- sincronizar
---

# Sincronizar el perfil o los marcadores de Firefox mediante dropbox

Cuando de manera habitual usas más de un ordenador mantener la misma configuración en ambos acaba siendo problemático. Una de las cosas que más echo de menos desde que he dejado de usar mi portátil personal en el trabajo es poder sincronizar los marcadores de Firefox.

## En el cielo o en la tierra

Tal y como yo lo veo hay dos clasificaciones en las que se podrían englobar los métodos para la sincronización:

- Usar un servicio web como [delicious](http://delicious.com/) pensado para trabajar exclusivamente con los marcadores.
- Usar alguna herramienta de sincronización de ficheros como [DropBox](http://www.dropbox.com/).

El depender en exclusiva de un servicio web [no es una opción que me tiente demasiado](http://blog.loretahur.net/2009/03/los-problemas-de-la-nube-informatica-radio-euskadi.html), así que no hablaremos de ella. DropBox en cambio, es una mezcla de servicio web y [rsync](http://es.wikipedia.org/wiki/Rsync) sencillo, donde los ficheros no sólo se guardan en un servidor externo si no también en el nuestro, de modo que podemos abandonarlo cuando queramos a coste casi cero, de hecho, montar [un sistema casero que substituya a DropBox](http://aseodiario.com/2010/03/dropbox-casero/) no es muy complicado.

## Diferentes implementaciones con Dropbox

Decidido que usaremos DropBox tenemos varias formas concretas de implementar el sistema:

- En [LiveHacker nos proponen emplear firefox portable](<<a href=>), de modo que ejecutemos un firefox desde dentro del propio DropBox. Esto tiene la ventaja de que si un día estamos en un cibercafé podríamos bajarnos nuestra propia versión del navegador desde la interfaz web y luego borrarla. Es una idea a anotar pero no es lo que buscamos.
- El resto de opciones se basan en ubicar el directorio que contiene nuestro perfil de firefox como un directorio compartido en DropBox. Bien sea [creando un enlace simbólico con el mismo nombre que nuestro perfil que apunte a DropBox](http://jonefox.com/blog/2009/11/16/how-to-sync-firefox-across-multiple-computers-using-dropbox/), usando el[ administrador de perfiles para crear un nuevo perfil](http://robwilkerson.org/2008/09/24/synchronizing-firefox-through-dropbox/) en DropBox, o mi favorita, que consiste simplemente en [editar el archivo profiles.ini para indicar que debe buscar el perfil por defecto en el directorio compartido](http://www.robzand.com/blog/firefox-dropbox-profile-synchronization-across-machines).

La última me parece la mejor porque nos ahorramos el crear un nuevo perfil, simplemente movemos su ubicación y usamos herramientas propias de firefox para colocar el directorio del perfil dentro de DropBox en lugar del truquillo de los enlaces simbólicos.

## Decidido el método, los pasos previos

En todo caso antes de usar uno de estos tres métodos deberías:

1. Hacer una [copia de seguridad de tu perfil](http://support.mozilla.com/en-US/kb/Backing+Up+Your+Information)
2. Modificar donde se guarda la cache del navegador. La cache son un montón de archivitos que se guardan mientras navegas para acceder más rápido a páginas ya visitadas, que no tienen ningún interés para la sincronización y que sólo te harán perder ancho de banda y cpu si intentas sincronizarlos. Para cambiar la ubicación, abre firefox y teclea about:config en la barra de direcciones. A continuación busca la clave browser.cache.disk.parent\_directory. Si no existe créala como de tipo «cadena». El valor que debe contener es el nuevo directorio que usará como cache, asegúrate de que existe en todos los ordenadores que vayas a usar, yo uso /var/tmp. Cierra el navegador , borra el directorio Cache dentro de tu perfil y vuelve a abrir el navegador. Asegúrate de que en /tmp se ha creado un nuevo directorio Cache.

## Mi método casi-preferido

Hecha la preconfiguración podríamos hacer lo que se dice por ejemplo en [robzand](http://www.robzand.com/blog/firefox-dropbox-profile-synchronization-across-machines):

1. Copia el [directorio que contiene tu perfil](http://support.mozilla.com/en-US/kb/Profiles#Where_is_my_profile_stored_) a DropBox
2. Edita el fichero profile.ini (está en la misma carpeta que tu directorio de perfil). Pon un cero en IsRelative, y en Path pon la ruta completa a tu perfil dentro de DropBox, que seguramente será algo como /home/\[tu\_usuario\]/DropBox/4f45s.default
3. Espera a que sincronice, abre el navegador y comprueba que todo funciona correctamente.
4. Ve a otro pc y espera a que sincronice. Edita el fichero profile.ini, pon un cero en IsRelative y pon en Path la ruta al perfil que acaba de ser sincronizado. (Ten en cuenta que a no ser que tengas el mismo nombre de usuario en ambos ordenadores la ruta será distinta)

## Los incovenientes

Al compartir el perfil también se comparten:

- Las extensiones. Si usas diferentes versiones de firefox puede que alguna de las extensiones te de problemas.
- Las cookies y las claves. Las cookies permiten que las páginas web te recuerden de modo que no tengas que escribir tu contraseña cada vez que entras. Si almacenamos tanto las cookies como las claves en un servicio externo como DropBox y alguien lo crackea, toda nuestra vida en la red será vulnerable.
- Cada vez que abras una página el contenido de tu perfil cambia, con lo que dropbox empezará a sincronizar, y habrá un gasto elevado de cpu y ancho de banda.

Estos problemas nos llevan a reflexionar si la comodidad que tiene el perfil compartido compensa el riesgo o a preguntarnos si realmente necesitamos compartir todo el perfil, o nos llega con los marcadores.

## Mi método preferido

Por tanto, si lo único que quieres es compartir los marcadores, que es en general lo mejor desde mi punto de vista, lo único que hay que hacer es:

1. Mover el archivo places.sqlite dentro del perfil de tu ordenador principal a DropBox
2. Crear un enlace simbólico desde el archivo en DropBox a tu perfil. El comando sería algo así:  
    `ln -s [ruta a places.sqlite dentro de dropbox] $HOME/.mozilla/firefox//places.sqlite`
3. Esperar a que sincronice y abrir firefox para comprobar que todo es correcto
4. En el resto de ordenadores borrar el archivo places.sqlite de dentro del perfil y hacer el enlace simbólico desde el que está en Dropbox.