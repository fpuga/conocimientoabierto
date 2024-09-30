---
categories:
- Sin categoría
date: 2012-03-18
permalink: /actualizar-la-version-de-antroid-de-un-htc-tattoo-ii-parte/461/
slug: actualizar-la-version-de-antroid-de-un-htc-tattoo-ii-parte
tags:
- android
- como
- dispositivos móviles
- hardware
- how to
- software
---

# Actualizar la versión de Antroid de un HTC Tattoo (II parte)

Las consideraciones generales sobre como actualizar las puedes leer en la [primera parte de este artículo](http://conocimientoabierto.es/actualizar-la-version-de-antroid-de-un-htc-tattoo-i-parte/454/).

Las [principales instrucciones que yo he seguido](http://wiki.cyanogenmod.com/wiki/HTC_Tattoo:_Full_Update_Guide) han sido la de los propios desarrolladores de la ROM que he instalado. Lo cuento un poco más detallado. Deberías seguir las instrucciones de esa guía, lo que aquí escribo son más bien posibles problemas y es complementario a lo que allí pone.

## Los pasos a seguir

1. Instalar jdk y [android sdk](http://developer.android.com/sdk/installing.html). El único componente que hace falta es «SDK Platform tools» que es lo que contiene el comando [adb](http://wiki.cyanogenmod.com/wiki/ADB).
2. Enciende el GPS. A veces no lo detecta si lo tienes apagado y deja de funcionar. Y recuerda que las operaciones que hagamos a partir de ahora con el teléfono deben hacerse con la opción «*depuración*» activada (En tu teléfono, *ajustes -&gt; aplicaciones -&gt; desarrollo*)
3. Rootear el dispositivo. Con el sistema proporcionado con Cyanogenmod yo conseguí acceso de Root (es cuando el prompt se convierte en #) pero no conseguí instalar el comando «*su*» para poder convertirse en root de forma sencilla. Así que cada vez que necesitaba acceso de root (cuando en los tutoriales se menciona usar «*su*«, tenía que ejecutar los comandos que se indican en el punto 5 y 6 [de la parte de rooting](http://wiki.cyanogenmod.com/wiki/HTC_Tattoo:_Full_Update_Guide#Rooting_the_HTC_Tattoo)). Un par de avisos:

- Si parece que se queda colgado pulsa intro para ver si aparece el prompt
- Si no consegues hacerlo, habilita la opción de[ instalar software desde fuentes no fiables](http://www.gandroides.com/noticia-como-instalar-aplicaciones-fuera-del-android-market__2.aspx) y prueba a instalar alguna aplicación como [UniversalAndroot](http://forum.xda-developers.com/showthread.php?t=747598). Recuerda que puedes instalar aplicaciones con adb usando *adb install aplicación.apk*

6. Haz copia de seguridad con una aplicación como Titanium Backup o Mybackup … instalables desde el Market.
7. Instala el recovery. A mi la versión de ClockModRecovery que [está enlazada en las instrucciones](http://wiki.cyanogenmod.com/wiki/HTC_Tattoo:_Full_Update_Guide#Installing_the_ClockworkMod_Recovery) me dió problemas. Descargué otra versión distinta de algún sitio que no recuerdo, y al que llegué buscando el error que me daba al intentar instalarlo.
8. Apaga el teléfono y vuelve a encenderlo en modo recovery: botón de encendido + botón teléfono (verde/descolgar) + botón casa (home)
9. Ve a la opción de «backup and restore» y haz un backup. Dejará en un directorio de la SD clockwordmod/backup/fecha una copia de seguridad de tu ROM actual y tus datos. Enciende el teléfono en modo normal y copia esa carpeta al pc.
10. Llegamos al punto de no retorno. Si todavía quieres segir, enciende en modo Recovery y ejecuta las siguientes acciones:
- Wipe de datos
- Wipe de caché
- Wipe de Dalvik Caché (en «Advanced»)
- Format / System (en «mounts and storage)
- Factory Reset

12. Sube al teléfono la ROM y las [google apps](http://forum.cyanogenmod.com/topic/32485-cyanogenmod-7-for-the-htc-tattoo-v7101-10-oct-2011/). Como ROM yo [emplee un nightly build con buenas críticas en los foros](http://forum.xda-developers.com/showpost.php?p=22149109&postcount=155). Recuerda que puedes subirlas a la SD del teléfono con *adb push &lt;nombre\_de\_fichero&gt; /sdcard*.
13. Enciende en modo recovery y en instalar zip escoge primero la rom y luego las google apps. Escoge reboot y cruza los dedos.
La primera vez a mi me tardó en arrancar unos 3 o 4 minutos así que paciencia. Comprueba que todo funciona, GPS, Wifi, llamar etc … y listo. Acuerdate de configurar la red preferida, el punto de acceso, …

## En caso de problemas con la batería

Espera a haber hecho un par de recargas completas. Si tras eso sigue habiendo problemas:

1. Cargala al 100% y déjala todavía un rato más
2. Sin desconectar el teléfono se enciende en modo recovery
3. Se hace un wipe de la batería
4. Apágalo y desconectalo
5. Enciende el teléfono, y no lo apagues ni lo reinicies hasta que la batería se descargue totalmente por si sóla

Por otro lado, la ROM de Cyanogen viene con un launcher llamado ADW Launcher. Alguna gente opina que el que menos batería gasta es «Launcher Pro». Pero esto parece ser más bien para gustos.

Y una cosa que no me ha quedado clara es si la ROM de Cyanogen por defecto hace overclock del procesador, es decir como si hiciera girar más rápido al reloj que marca al ritmo que debe funcionar el procesado (que no tiene nada que ver con la hora). Esto gasta batería y puede controlarse con una aplicación llamada SetUP. Si bajas la frecuencia el teléfono será menos responsivo pero disminuirá el consumo de batería.

## El resultado

<div class="ngg-gallery-singlepic-image " style="max-width: 144px"> [ ![17032012027](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/cache/17032012027.jpg-nggid0216-ngg0dyn-320x240x100-00f0w010c010r110f110r010t010.jpg "17032012027") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/17032012027.jpg) </div>