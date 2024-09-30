---
id: 9
title: 'Instalar los drivers para una webcam'
date: '2007-04-04T20:11:00+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/instalar-los-drivers-para-una-webcam/6/'
permalink: /instalar-los-drivers-para-una-webcam/9/
blogger_blog:
    - conocimientoabierto.blogspot.com
blogger_permalink:
    - /2007/04/instalar-los-drivers-para-una-webcam.html
categories:
    - drivers
    - 'itrust wb-1200p'
    - linux
    - receta
    - webcam
---

**Actualización 19/06/2009:** Este artículo está desfasado. En la actualidad la mayoría de las webcam funcionan en gnu/linux simplemente con enchufarlas. Lo explico algo mejor [en este artículo](http://conocimientoabierto.es/instalar-drivers-webcam-linux/83/).

Lo primero que debemos hacer es acudir a esta [página](http://mxhaard.free.fr/spca5xx.html) y comprobar si nuestra webcam está soportada. Para ello podemos buscar el nombre de nuestra cámara en la 5 columna, la que pone algo parecido a *based cameras.*

En caso de no encontrarla podemos buscar alguna que use el mismo chip, y usar sus valores. Para averiguar si usa el mismo chip debemos fijarnos en el ID del fabricante y el ID del dispositivo. En Mandriva podemos obtener estos valores del Panel de Control en la sección de Hardware. Una forma un poco más genérica consiste en abrir un terminal de root y teclear *lsusb*. En mi caso saldrían los siguiente valores.  
`<br></br>[root@localhost ~]# lsusb<br></br>Bus 001 Device 003: ID 2001:5100 D-Link Corp. [hex]<br></br>Bus 001 Device 002: ID 093a:2468 Pixart Imaging, Inc. Easy Snap Snake Eye WebCam<br></br>Bus 001 Device 001: ID 0000:0000<br></br>`  
Debemos identificar el correspondiente a la cámara, que en mi caso es el segundo dispositivo. Los primeros número tras ID corresponden al fabricante y los otros al dispositivo.  
`<br></br>ID Fabricante=093a<br></br>ID Dispositov=2468<br></br>`  
Si la cámara está soportada y el driver es del tipo spca5xx, tenemos suerte ya que podemos encontrar el driver que nos hace falta en la sección Download de esa misma web. A pesar de existir versiones precompiladas, si nuestra versión del kernel es superior a la 2.6.11 (lo que es muy probable, *uname -a* para comprobarlo) es mejor que nos descarguemos el archivo *gspcav1-xxxx.tar.gz* y lo compilemos nosotros mismos.

Descomprimimos el fichero en nuestro disco duro y dentro de ese directorio  
`<br></br>#make<br></br>#make install<br></br>`  
Si no se produce ningún error nuestra webcam debería estar casí lista para funcionar. Ahora debemos reiniciar el ordenador (supongo que si ejecutamos *modprobe gspca* no hace falta que reiniciemos pero no aseguro que esto de buen resultado). Para comprobar que ha sido correctamente instalado podemos usar nuestro cliente de mensajería instantanea favorito. En mi caso he tenido problemas con kopete, pero con amsn y el ekiga sin problemas. En amsn he seleccionado webcam de baja calidad porque si no el vídeo iba a demasiados pocos frames por segundo.

Al igual que en el [post anterior](http://conocimientoabierto.blogspot.com/2007/03/sonido-y-mltiples-usuarios.html) en el que hablaba del sonido si deseamos lanzar programas como otro usuario debemos añadir ese usuario al grupo video o dar permisos sobre los dispostivos /dev/video  
`gpasswd -a user2 video`