---
id: 19
title: 'Driver para modem adsl usb en linux mandriva 2007'
date: '2007-08-16T12:52:00+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/driver-para-modem-adsl-usb-en-linux-mandriva-2007/19/'
permalink: /driver-para-modem-adsl-usb-en-linux-mandriva-2007/19/
blogger_blog:
    - conocimientoabierto.blogspot.com
blogger_permalink:
    - /2007/08/driver-para-modem-adsl-usb-en-linux.html
categories:
    - General
---

En mi anterior entrada comenté que había conseguido conectar a internet usando el [driver eciadsl](http://eciadsl.flashtux.org/) para un modem adsl por usb d-link dsl-200 b1 desde Ubuntu Feisty (v 7.04). Pués bien, a pesar de que si que conseguí conectar no lograba una conexión estable y además en muchas ocasiones no lograba conectar al primer intento. Esto, sumado a que no me adaptaba a Gnome y Ubuntu, acostumbrado desde hace unos 6 años a Mandrake/Mandriva y KDE hicieron que volviera a mi distro de toda la vida.

Así que para completar la guía anterior voy a describir alguna de las particularidades para poder instalar el driver en la Mandriva (y alguna otra cosilla que se quedó en el tintero). Que conste que es mucho más fácil que con Ubuntu, lo único de lo que debemos preocuparnos si usamos la Mandriva 2007.0 es de instalar el kernel adecuado (no se cual trae de serie la 2007.1 o 2007 Spring). Mandriva 2007.0 viene por defecto con el kernel 2.6.17-5 que no funciona correctamente con el driver eciadsl. Debemos pasar a uno superior. (Preferiblemente de 2.6.17.8 a 2.6.17.14, porque a partir de 2.6.18 hace falta parchear el driver). Yo he instalado los paquetes [kernel-2.6.17.14mdv-1-1mdv2007.0.i586.rpm](http://rpm.pbone.net/index.php3/stat/4/idpl/4340893/com/kernel-2.6.17.14mdv-1-1mdv2007.0.i586.rpm.html) y [kernel-source-2.6.17.14mdv-1-1mdv2007.0.i586.rpm](http://rpm.pbone.net/index.php3/stat/4/idpl/4340915/com/kernel-source-2.6.17.14mdv-1-1mdv2007.0.i586.rpm.html). Con este kernel la versión eciadsl-usermode-0.11.tar.gz del driver sin ningún parche me funciona de fábula. Atención a bajarse los paquetes que pongan mdv2007.0 o mdv2007.1 según si tenemos la Mandriva 2007 normal o la Mandriva 2007 Spring. Para buscar paquetes en rpm yo suelo usar la página es http://rpm.pbone.net (en concreto para este caso podemos usar la opción 3 y buscar por kernel-2.6.17\*mdv\* o algo parecido)

Una vez hayamos descargado el kernel y el kernel-source con hacer doble clik sobre ellos y darle siempre a aceptar deberían instalarse correctamente. Después añadimos la línea <span style="font-style: italic">dabusb</span> a <span style="font-style: italic">/etc/hotplug/blacklist</span> y reiniciamos. Descomprimimos el driver en una carpeta, lo compilamos y lo instalamos como root (<span style="font-style: italic">./configure &amp;&amp; make &amp;&amp; make install)</span>. A continuación descomprimimos el archivo con los ficheros .bin en <span style="font-style: italic">/etc/eciadsl</span>. Para configurar el driver (siempre como root) usamos el comando <span style="font-style: italic">eciadsl-config-tk</span>.

Las opciones que yo uso usando como proveedor ONO son las siguientes:  
<span style="font-weight: bold"></span>

> <span style="font-size:85%"><span style="font-weight: bold">Fichero de Sincronización:</span> gs7470\_synch04.bin  
> <span style="font-weight: bold">PPP Mode:</span> VCM\_RFC2364  
> <span style="font-weight: bold">VPI:</span>8 <span style="font-weight: bold">VCI:</span>35  
> <span style="font-weight: bold">Provider DNS:</span> ES.Auna</span>

A continuación voy a comentar algunas dudas sueltas que he visto que salen en los foros sobre estos temas.

- A pesar de que en la herramienta para configurar el hardware de Mandriva aparezca una entrada que identifique el dispositivo USB como un modem no significa que pueda configurarse desde allí.
- En la documentación de la página de eciadsl da la impresión de que al encender el ordenador no debe haber ninguna luz encendida en el modem. En mi modem siempre hay una luz encendida y conecto sin problemas.
- Otros ficheros de sincronización que creo que van bien para mi son: gs7470\_synch06.bin, gs7470\_synch01a.bin y gs7470\_synch18.bin
- Si notas que las páginas web cargan muy despacio aunque luego las descargas van a velocidad normal es probable que sea un problema con los servidores DNS. Puedes copiar la dirección ip primaria y secundaria de la configuración que uses en windows o tomarlas por ejemplo de la página [OpenDNS.](http://www.opendns.com/)  
    Una vez anotadas esas dos ips, puedes ejecutar de nuevo el comando <span style="font-style: italic">eciadsl-config-tk</span> e introducirlas a mano seleccionando <span style="font-style: italic">other</span> en <span style="font-style: italic">provider dns</span>. Aunque yo creo que es mejor editar el fichero <span style="font-style: italic">/etc/resolv.conf</span> comentar todas las lineas que aparezcan (poniendo el síbolo # al principio de cada línea) y añadir dos lineas al estilo  
    > nameserver ip1  
    > nameserver ip2
- Si aparece un error como <span style="font-style: italic">nice: pppd: No existe el fichero o el directorio</span> en el 4 punto <span style="font-style: italic">\[EciAdsl 4/5\] Connecting to provider…</span> es que no tenemos instalado el paquete ppp. Para ello vamos <span style="font-style: italic">Sistema -&gt; Confiración -&gt; Configurar su computadora -&gt; Instalar sofware.</span>Buscamos «ppp» en la casilla de busca e instalamos los paquetes <span style="font-style: italic">ppp, ppp-pppoatm</span>. (Según que proveedor tengamos puede ser necesario instalar también los paquetes <span style="font-style: italic">ppp-pppoe</span> y <span style="font-style: italic">rp-pppoe</span>). En algún momento del proceso nos pedirán que introducizcamos el DVD de instalación de Mandriva.
- Si todo parece ir bien pero cuando ejecutamos eciadsl-start se queda colgado en el punto 4 \[EciAdsl 4/5\] Connecting to provider, podemos pulsar Ctrl+Z y después teclear el comando bg (o killall -9 eciadsl-start si bg no funciona) Con esto debería conectar. Tener en cuenta que esto generará ficheros basura de nombre core en el directorio /root que debemos borrar periodicamente.
<div style="text-align: justify">Hay un [hilo del foro](http://eciadsl.flashtux.org/forum/viewtopic.php?t=3152) en el que hablan de ello. A mi me ha funcionado el editar el archivo /usr/local/bin/eciadsl-start, buscar la línea que pone <span style="font-style: italic">nice –20 pppd call adsl updetach</span> (es la línea 546), borrarla y añadir estas dos: > pppd unit 1 call adsl  
> pppd unit 0 call adsl updetach

7. Algunos comando útiles para saber los módulos que tenemos cargados y los dispositivos usb conectados: lsmod, dmesg | grep usb, lsusb
A continuación algunos enlaces que pueden resultar útiles:

</div>- [Soporte D-link DSL-200](http://www.dlink.com.au/tech/#d)
- FTP con cosas del DSL-200: ftp://ftp.dlink.it/Adsl/Dsl-200-B1/
- Página de otro [eagle-usb](http://atm.eagle-usb.org/wakka.php)
- [Como Elegir las DNS](http://wiki.bandaancha.st/C%C3%B3mo_elegir_las_DNS)
- [Drivers y tutoriales para modems ADSL con conexión USB](http://www.bandaancha.st/foros.php?temid=360314) Es bastante antiguo pero igual se saco algo en claro.
- [Datos de conexión de distintos proveedores](http://www.adslayuda.com/Generico-datosdeconexion.html)  
    Este [enlace](http://www.patriziobassi.it/blight/index.php?showtopic=94&hl=) y las preguntas [5.0](http://eciadsl.flashtux.org/faq.php?faq_lang=es#q5.0) y [5.12](http://eciadsl.flashtux.org/faq.php?faq_lang=es#q5.12) del FAQ hablan de como conectar al inicio o sin tener que introducir la clave de root.