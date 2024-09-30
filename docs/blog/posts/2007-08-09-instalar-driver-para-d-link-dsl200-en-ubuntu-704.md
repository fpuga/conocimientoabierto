---
id: 327
title: 'Instalar driver para D-Link DSL200 en Ubuntu 7.04'
date: '2007-08-09T12:25:00+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/instalar-driver-para-d-link-dsl200-en-ubuntu-704/18/'
permalink: /instalar-driver-para-d-link-dsl200-en-ubuntu-704/327/
blogger_blog:
    - conocimientoabierto.blogspot.com
blogger_permalink:
    - /2007/08/instalar-driver-para-d-link-dsl200-en.html
categories:
    - 'd-link dsl-200'
    - drivers
    - linux
    - migracion
    - receta
---

<div style="text-align: justify">El principal problema que puedes encontrarte en un sistema operativo es tener algún dispositivo hardware para el que no existan drivers, es decir que los programas de tu ordenador no puedan usar el cacharro que te has comprado. Yo soy un <span style="font-weight: bold">insatisfecho</span> cliente de ONO, para conectarme por ADSL uso el [modem usb d-link dsl 200 b1](http://www.dlink.es/?go=jN7uAYLx/oIJaWVUDLYZU93ygJVYLelXSNvhLPG3yV3oWI9pxu5vbMYjOadh5itsRWm5kCVP+J0IBN7m3qPkLE4S), que sólo viene con drivers para sistemas privativos. Por suerte en el activo mundo del software libre alguien se ha preocupado de programar un [driver llamado eciadsl](http://eciadsl.flashtux.org/) válido para una gran cantidad de modem adsl por usb. Como la instalación del citado driver puede dar algún que otro quebradero de cabeza, voy a tratar de hacer una pequeña guia de los pasos que he seguido yo para poder conectarme a internet, particularizando para mi modem con ONO desde una Ubuntu Feisty (v 7.04)

</div>1. Comprobar que nuestro modem está soportado por el driver en esta [página](http://eciadsl.flashtux.org/modems.php)
2. Comprobar que cumplimos los prerequisitos en cuanto a los paquetes que tenemos instalados. No voy a comentar nada de este paso porque deberían cumplirse para cualquier distribución moderna.
3. En la sección de [downloads](http://eciadsl.flashtux.org/download.php) de la página podemos ver que archivo descargar en función de nuestro kernel y si tendremos que parchearlo. En general para distros seminuevas nos bajaremos el archivo [eciadsl-usermode-0.11.tar.gz](http://eciadsl.flashtux.org/download/eciadsl-usermode-0.11.tar.gz) sin más. <div style="text-align: center">| Si nuestro kernel es superior a la versión 2.6.18 (como sucede con Ubuntu Feisty el driver por defecto no funciona. Debemos parchearlo con el [synch.patch](http://eciadsl.flashtux.org/download/beta/synch.patch) o bajarnos esta versión del driver ya parcheada:[eciadsl-usermode-0.11-synch.patch.tar.bz2](http://eciadsl.flashtux.org/download/beta/eciadsl-usermode-0.11-synch-patch.tar.bz2) (descargable desde el [hilo 2.6.18 kernel problem del foro de eciadsl](http://eciadsl.flashtux.org/forum/viewtopic.php?t=3247)   Para conocer la versión de nuestro kernel empleamos el comando <span style="font-style: italic">uname -r</span> |
    |---|
    
    </div>
4. El resto de pasos deben hacerse desde un terminal e identificados como root. Podemos hacer esto anteponiendo la orden <span style="font-style: italic">sudo</span> a cada uno de los comandos que aparecen aquí o directamente escribiendo <span style="font-style: italic">su root</span> en el terminal (a partir de ese momento se ejecutan todos los comandos como root. <div style="text-align: center">| En Ubuntu no funciona automaticamente lo de hacer <span style="font-style: italic">su root</span> para solucionarlo: Sistema -&gt; Administración -&gt; Gestión de Usuarios y Grupos -&gt; y cambiar la clave de root (que por defecto es la de nuestro usuario habitual)   Con esto ya deberia funcionar. |
    |---|
    
    </div>
5. Descomprimimos el archivo y en el directorio donde lo hayamos hecho tecleamos las siguientes instrucciones (Doy por hecho que estamos usando el archivo ya parcheado):  
    <span style="font-style: italic">./configure  
    make  
    make install</span><div style="text-align: center">| Si tenemos el ubuntu de serie es probable que el configure falle con el siguiente error <span style="font-style: italic">C compiler cannot create executables</span>. Esto puede ser debido a varias cosas pero seguramente lo solucionaremos instalando algunos paquetes. Para ello introducimos el CD de Ubuntu. Después vamos a Sistema -&gt; Administración -&gt; Gestor de paquetes Synaptic.   Buscamos el paquete build-essential. Tras unos instantes nos dirá que se necesitan instalar varios paquetes más, aceptamos y después le damos a <span style="font-style: italic">Aplicar</span>   Con esto ya deberiamos poder crear los ejecutables tecleando los comandos anteriores. |
    |---|
    
    </div>
6. A continuación debemos descargar el fichero [eciadsl-synch\_bin.tar.bz2](http://eciadsl.flashtux.org/download/eciadsl-synch_bin.tar.bz2) también disponible en la sección de [downloads](http://eciadsl.flashtux.org/download) y descomprimirlo en el directorio <span style="font-style: italic">/etc/eciadsl</span>. Este archivo contiene los archivos de sincronización .bin (son las información que necesita el modem para conectarse con el proveedor en la etapa en que uno de los leds parpadea)
7. El siguiente paso es comprobar que tenemos el módulo dabusb deshabilitado. Para curarnos en salud lo que debemos hacer es (tras arrancar el ordenador con el modem desconectado) 
    - Si existe el fichero <span style="font-style: italic">/etc/hotplug/blacklist</span> editarlo y añadir una línea con la palabra <span style="font-style: italic">dabusb</span>
    - Si no existe el fichero mencionado teclearemos en un terminal <span style="font-style: italic">eciadsl-remove-dabusb</span>
    
     A continuación podremos volver a conectar el modem.
8. Toca configurar el driver. Para ello podemos emplear el comando <span style="font-style: italic">eciadsl-config-tk</span>(en modo gráfico) o <span style="font-style: italic">eciadsl-config-text</span>(en modo texto). Si tenemos el ubuntu de serie es poco probable que venga instalado tcl/tk necesario para usar el modo de configuración gráfico de modo que tendremos que emplear el modo texto. <div style="text-align: center">| Si nos toca usar el modo texto y usamos ubuntu es probable que nos encontremos con más problemas. Si aparece algún error a la hora de introducir los datos (especialmente con la clave de conexión) puede ser porque la shell que usemos sea distinta a la que enlaza <span style="font-style: italic">/bin/sh</span>. En la configuración por defecto de mi Ubuntu 7.04 usa una shell bash pero <span style="font-style: italic">/bin/sh</span> apunta a una shell dash. Podemos ver cual es nuestra shell mediante <span style="font-style: italic">echo $SHELL</span> y este valor debería coincidir con el que haya en <span style="font-style: italic">ls -l /bin/sh</span>. Si no es así debemos cambiarlo. Esto podría variar de unos sistemas a otros pero en general será algo así como: <span style="font-style: italic">ln -fs /bin/bash /bin/sh</span>.  Tras configurar el driver si queremos podemos volver <span style="font-style: italic">/bin/sh</span> a su estado original o dejarlo así. Para deshacer el cambio. Si cuando hicimos ls -l /bin/sh apuntaba a una shell que no fuera dash esa es la que debemos emplear en lugar de /bin/dash: <span style="font-style: italic">ln -fs /bin/dash /bin/sh</span> |
    |---|
    
    </div>Cuando ejecutemos <span style="font-style: italic">eciadsl-config-text</span> tendremos que seguir (aproximadamente) los siguientes pasos.  
    1\. Configure all your settings  
    2\. Introducir el nombre de usuario que nos haya dado nuestro proveedor de acceso a internet  
    La clave que nos hayan dado. (si no sabemos alguno de estos tendremos que llamar al servicio de atención al cliente)  
    3\. Seleccionamos nuestro proveedor. Si no aparece en la lista podemos seleccionar el 5<span style="font-style: italic">8</span> que es <span style="font-style: italic">other</span> con lo cual después tendremos que introducir a mano nuestro servidor DNS o bien seleccionar uno cualquiera de nuestro propio país que en general debería funcionar correctamente.  
    4\. Damos intro dos veces para aceptar los DNS por defecto (o escribimos los que queramos)  
    5.VPI suele ser 8. VCI suele ser 35 (al menos estos son valores correctos para ONO en Pontevedra.  
    6\. A continuación seleccionamos nuestro modem.  
    7\. Después 5 intros aceptando los valores por defecto.  
    8\. A continuación vienen varias opciones que son dependientes del proveedor. En mi caso funciona escogiendo todas las opciones por defecto hasta que pregunta si nuestro proveedor usa DHCP que en mi caso es No y si usas IP estática que en general también será No. El fichero de sincronización que uso es gs7470\_synch04.bin
    
    <div style="text-align: center">| Aunque es probable que nos valgan varios ficheros de sincronización .bin distintos si cuando estemos conectando pone <span style="font-style: italic">Synchronization successful</span> y luego <span style="font-style: italic">Couldn’t get channel number: Input/output error</span> debemos probar otros ficheros. También podemos probar otros ficheros si notamos problemas de desconexiones o la sincronización es lenta. En el propio foro de soporte de eciadsl uno de los desarrolladores comenta que no conocen exactamente el protocolo de sincronización y que en caso de errores es conveniente probar otros ficheros. Para ello, debemos ejecutar <span style="font-style: italic">eciadsl-config-text</span> y seleccionar la opción 3 para escoger un nuevo fichero de la lista. A continuación podemos volver a ejecutar <span style="font-style: italic">eciadsl-start</span> para comprobar si hay mejoras.   A la hora de probar un nuevo fichero lo mejor es apagar y encender el ordenador (no reiniciar) aunque desconectando y conectando el modem unos instantes después debería ser suficiente. |
    |---|
    
    </div>
9. Si todo ha ido bien ya deberíamos poder conectarnos a internet para ello tecleamos <span style="font-style: italic">eciadsl-start</span> y cruzamos los dedos.

<div style="text-align: justify">Actualización: El proceso para escribir este post no fue lineal ya que no conseguí hacer funcionar el driver a la primera. Una de las cosas que probé fue a desinstalar el paquete *restricted-manager* pero no creo que sea necesario, aunque si estas desesperado quítalo. También deberías probar la versión vcs del driver, distintos ficheros .bin, a cambiar el kernel… En todo caso no desesperes en el [foro de eciadsl](http://eciadsl.flashtux.org/forum) hay multitud de mensajes y seguro que alguno se ajusta a tu problema. ¡Suerte!</div>