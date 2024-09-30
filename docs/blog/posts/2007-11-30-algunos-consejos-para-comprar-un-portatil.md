---
id: 30
title: 'Algunos consejos para comprar un portátil'
date: '2007-11-30T00:25:00+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/algunos-consejos-para-comprar-un-portatil/30/'
permalink: /algunos-consejos-para-comprar-un-portatil/30/
blogger_blog:
    - conocimientoabierto.blogspot.com
blogger_permalink:
    - /2007/11/algunos-consejos-para-comprar-un.html
categories:
    - drivers
    - linux
    - migracion
    - portatil
tags:
    - 'comprar portátil'
    - hardware
    - recomendaciones
---

Como comenté voy a tratar de dar una serie de consejos a la hora de comprar un portátil e [instalarle linux](http://www.linux-on-laptops.com/). La primera decisión a tomar a la hora de comprar un ordenador debe ser en que horquilla de precios vamos a movernos. Particularmente considero que cualquier portátil de entre 700 y 1000€ debería satisfacer las necesidades de la mayoría de la gente por un período de unos 4 años. Invertir más dinero no significa necesariamente que el portátil nos vaya a durar mucho más tiempo, sino que obtendremos algunas características adicionales o servicios de valor añadido proporcionados por el fabricante.

La segunda decisión es si vetamos alguna marca. Particularmente considero que existen una serie de marcas como [Sony](http://vaio.sony.es/view/ShowProductCategory.action?referer=http%3A%2F%2Fwww.sony.es%2Fview%2FShowProductCategory.action%3Fsite%3Dodw_es_ES&site=voe_es_ES_cons&category=VAIO+Notebooks) o [Toshiba](http://es.computers.toshiba-europe.com/cgi-bin/ToshibaCSG/jsp/notebookHomepage.do?service=ES) que ofrecen una confianza adicional, pero por el precio de una de estas marcas podemos comprar un portátil mucho más potente de otra. No me gusta hacer recomendaciones negativas porque no suelen ser muy objetivas pero por lo que he estado leyendo la única marca que en principio me desagrada es [Asus](http://www.asus.es/products.aspx?l1=5). Es conveniente además considerar el comprarse un ordenador clónico. Franquicias como [PCBOX](http://www.pcbox.com/) ofrecen este servicio y suelen ser de buena calidad.

El siguiente punto a considerar es si queremos un portátil [<span style="font-style: italic;">linux friendly</span>](http://www.linux.org/hardware/). A día de hoy no suelen existir muchos problemas para conseguir drivers para cualquier hardware que funcionen en linux, pero algunos funcionan mejor que otros. Personalmente he optado por aquello fabricantes que sacan por si mismos drivers funcionales como una forma de premio por tratar de forma adecuada el software libre.

El último punto general es que uso le vamos a dar al portátil. Y este está muy relacionado con la pantalla. Si lo vamos a usar como un remplazo del de escritorio porque no tenemos sitio en casa y apenas lo vamos a mover podemos optar por uno con pantalla de 17». Si tenemos ordenador en casa y el trabajo y necesitamos algo muy movible para consultar el correo y trabajar durante viajes etc… podemos plantearnos uno con pantalla de entre 12» y 14». Para otros usos, moverlo a menudo pero tampoco estar cargando con él todavía lo mejor suele ser optar por una panorámica de 15.4». Es muy conveniente que antes de comprarlo pidamos ver el portátil encendido y juguemos con el brillo de la pantalla para comprobar lo buena que es.

Pasemos a considerar los aspectos más técnicos del asunto. Téngase en cuenta que mis comentarios son generalizaciones, seguro que los expertos en la materia se pondrían por las nubes, pero a la hora de la verdad poca gente encuentra diferencia entre un ordenador u otro.

<span style="font-weight: bold;">Procesador: </span>Es el cerebro del ordenador, pero no nos dejemos engañar por número extraños o vendedores desinformados. A día de hoy cualquier procesador que no ponga Celeron o Semprom será más que suficiente para nuestras necesidades. Es en general preferible gastar algo de dinero en más RAM que en un procesador mejor. Optar por un procesador de intel o por uno de AMD es en principio indiferente. Lo único que resaltaría es que todos los procesadores AMD Athlon permiten la virtualización por hardware mientras que sólo los intel con un número igual o superior a T5600 lo hacen. Si no vais a virtualizar esto os dará igual. Para comparar entre distintos procesadores podeis ver las características de los [amd en esta página](http://products.amd.com/en-us/NotebookCPUFilter.aspx) (usar la parte que pone «model number») o los [intel en esta otra](http://processorfinder.intel.com/List.aspx?ProcFam=2643&sSpec=&OrdCode=) (usar la parte que pone «processor number»).

<span style="font-weight: bold;">RAM:</span> Es fácil, cuanta más mejor. A día de hoy 1GB obligatorio y 2GB recomendable. El rendimiento también mejora si es a 667MHz en lugar de a 533MHz

<span style="font-weight: bold;">Disco Duro: </span>A partir de 100GB es en general más que suficiente si no vamos bajar películas o música de forma compulsiva. Tengamos siempre presente cual es el uso que le vamos a dar al portátil y que los discos duros externos están baratos.

<span style="font-weight: bold;">Peso:</span> Si vamos a moverlo yo no cogería nada que en sus especificaciones pusiese más de 3kg (aunque fuese (3.01kg). 2.7kg más o menos puede ser una buena opción.

[Wifi: ](http://es.wikipedia.org/wiki/Wifi)A día de hoy todos los portátiles traen wifi, pero debemos ver que especificaciones cumplen. En principio todos cumplen la norma b/g (que es el wifi absolutamente mayoritario que hay en cafeterías, universidades, …) pero algunos cumplen también la norma a (suelen nombrarse como a/b/g). Que cumpla la 802.11a (nombre oficial) no lo consideraría como algo limitante pero si interesante. Por otro lado podemos preguntar al vendedor que tarjeta wireless lleva para comprobar si existen drivers nativos para linux, podemos emularlos con [ndiswrapper](http://www.bdw.es/2005/08/22/ndiswrapper-wifi-facil-en-linux/) o no va. Si es una intel funcionará perfectamente.

<span style="font-weight: bold;">Tarjeta Gráfica:</span> A no ser que seamos muy jugones cualquiera vale. A día de hoy tanto las gráficas intel como las nvidia funcionan correctamente en linux (incluida la aceleración 3d). Las ati aún no están al nivel apropiado pero están haciendo esfuerzos en el camino correcto, tal vez en 6 meses si sean una opción a considerar. De todas formas cuidado con las nvidia porque no todas tienen soporte en linux, aquí está la [lista de tarjetas soportadas](http://www.nvidia.es/object/linux_supported_es.html) por el último driver. Con la tarjeta más sencilla de intel la GMA 950 yo no he tenido ningún problema y l[os efectos gráficos en 3d en linux](http://es.youtube.com/watch?v=xYZUKDa1AMs) han funcionado sin que haya hecho nada.

<span style="font-weight: bold;">Puertos, conectividad y otras cosillas.</span>

- Todos los portátiles traen puertos USB y tarjeta de red. La mayoría incluyen también modem (aunque yo no me preocuparía si no lo trajera).
- Algunos traen Firewire (IEEE1394) pero tampoco es muy habitual que lo vayamos a necesitar, podemos pasar de ello.
- Todos traen también salida para un monitor externo (para conectar un proyector por ejemplo). A mi particularmente me gusta que traigan salida de s-video porque de este modo se puede enchufar el ordenador a la televisión muy fácilmente y usarlo a modo de dvd portátil por ejemplo.
- La nueva moda es incluir lectores de tarjetas pero yo no lo veo mucha utilidad.
- Cuidado si necesitáis disquetera porque la mayoría ya no trae dentro del portátil (aunque si existen dispositivos externos)
- Bluetooth/Infrarojos. Puede ser útil si tienes un móvil que lo tenga para descargar imágenes y otras cosillas del móvil. En caso contrario tampoco le veo mucha utilidad (ratones y teclados inalámbricos suelen traer su propio adaptador. En todo caso tampoco debería ser un factor limitante a la hora de la compra puesto que hay dispositivos USB que dan conectividad bluetooth por alrededor de 20€.
- Webcam. Si no somos fanáticos de las videoconferencias no es necesario, generalmente no haremos una videoconferencia desde un lugar público por lo que tampoco nos importará mucho comprar una externa. ([También alrededor de 25€](http://www.pcbox.com/catalogo/catalogo/default.asp?lan=es&cnt=es&familia=26))
- Si vamos a usar el ordenador de forma más o menos fija, podría ser muy útil que tuviera puertos PS2 para conectarles un teclado y un ratón externo (Si va a ser ocasional con los USB es suficiente)

<span style="font-weight: bold;">Batería: </span>No comento nada, porque es difícil dar un criterio sobre esto, y lo cierto es que hoy en día hay enchufes en prácticamente cualquier sitio donde necesitemos usar un portátil.

Si llegado el momento final tenéis dudas entre varios podéis inclinaros [por los fabricantes más responsables en temas medio ambientales](http://notime-towaste.blogspot.com/2007/11/ranking-verde-de-electronicos.html).Otras recomendaciones, opiniones, críticas y preguntas en los comentarios :)

**Actualización**: 14 de Mayo de 2016. Si tienes dudas de cuando comprarlo dicen que [la mejor fecha es verano](http://www.gciencia.com/tecno/queres-mercar-un-ordenador-espera-o-veran/).