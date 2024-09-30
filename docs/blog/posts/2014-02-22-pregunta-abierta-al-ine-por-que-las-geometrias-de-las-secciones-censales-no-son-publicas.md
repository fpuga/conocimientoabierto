---
id: 659
title: 'Pregunta abierta al INE. ¿Por qué las geometrías de las secciones censales no son públicas?'
date: '2014-02-22T17:34:06+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=659'
permalink: /pregunta-abierta-al-ine-por-que-las-geometrias-de-las-secciones-censales-no-son-publicas/659/
categories:
    - 'Sin categoría'
tags:
    - gis
    - ine
    - 'open data'
---

Con motivo del [Open Data Day](http://opendataday.org/), [hemos intentado](http://vigodd2014.wordpress.com/) hacer una visualización para la que necesitábamos las geometrías de las secciones censales.

Al parecer por la política del [INE](http://www.ine.es/infoine/) respecto a estos datos no es posible obtenerlos así que les he escrito un correo. Actualizaré este artículo con lo que respondan.

> Con motivo del Open Data Day \[1\] estamos intentando hacer una visualización para la que necesitamos las geometrías de los distritos censales.
> 
> He visto que es posible obtener información de las secciones censales a través de WMS \[2\] pero se especifica que no es posible obtener las geometrías a través de WFS \[3\].
> 
> Parece ser que esto es debido a la política del INE, que es el propietario de esta información \[4\].
> 
> Me gustaría que me informaran si esto es correcto y en caso de no serlo de donde puedo obtener dicha información.
> 
> En caso de que efectivamente exista una política de no publicación acerca de esos datos, me gustaría saber cual es el motivo de que la ciudadadanía no tenga acceso a ellos.
> 
> Les hago saber que he reproducido este mensaje en mi blog \[5\] y que con su permiso reproduciré también la respuesta que me den.
> 
> Muchas Gracias.
> 
> \[1\] http://opendataday.org/  
> \[2\] http://www.idee.es/wms/IDEE-Limite/IDEE-Limite  
> \[3\] http://www.cartociudad.es/portal/web/guest/directorio-de-servicios  
> \[4\] http://listserv.gva.es/pipermail/gvsig\_usuarios/2012-February/021286.html  
> \[5\] http://conocimientoabierto.es/pregunta-abierta-al-ine-por-que-las-geometrias-de-las-secciones-censales-no-son-publicas/659/

## Actualización 25/02/2014

El lunes por la mañana me llegó este correo de respuesta del INE:

> Estimado Sr.Sra.: En relación con su consulta le informamos lo siguiente :
> 
> el INE facilita como petición a medida los Ficheros de Cartografía Digital, estos ficheros contienen la digitalización de los contornos georeferenciados de todos los municipios y de gran parte de las secciones censales, según coordenadas UTM, huso 28, 29, 30 y 31. Los ficheros tienen formato EXPORT de Arclnfo (e009) y SHAPE.
> 
> en la siguiente dirección puede consultar las secciones disponibles
> 
> http://www.ine.es
> 
> -productos y servicios
> 
> -información estadística
> 
> -información a medida y ficheros especiales
> 
> http://www.ine.es/ss/Satellite?L=es\_ES&amp;c=Page&amp;cid=1254735550786&amp;p=1254735550786&amp;pagename=ProductosYServicios%2FPYSLayout
> 
> -estos ficheros tienen un coste dependiendo de si solo quiere uno o todos.
> 
> hay que solicitarlos como petición a medida
> 
> las peticiones a medida se pueden realizar mediante este medio o bien directamente al Area de Atención a Usuarios. Fax 91-5839158
> 
> en las peticiones de información a medida se indicará los datos de la persona de contacto (nombre, dirección postal, teléfono, fax y correo electrónico si dispone de él) y detallando lo mejor posible la información que se desea
> 
> -Atentamente
> 
> -Área de Difusión por Internet.
> 
> — CALIDAD DE LA INFORMACIÓN —  
> La presente información se ha obtenido siguiendo estrictos procedimientos de control de calidad; no obstante, pueden producirse errores involuntarios o de interpretación, por lo que las cifras ofrecidas pueden, en algún caso, no ser correctas o adecuadas a su petición.
> 
> NOTA: Por favor, no responda a este correo ya que los correos electrónicos recibidos en esta dirección se borran automáticamente. Si necesita volver a contactar con nosotros utilice un nuevo formulario de consulta http://www.ine.es/infoine indicando su número de referencia.

En resumen, que hay que pagar por los datos. La verdad es que les escribí inicialmente por curiosidad, no porque tenga ninguna necesidad de los datos y no querría alargar esto de forma indefinida, por lo que si alguien se anima a colaborar con una respuesta o dar alguna idea se lo agradecería. Estaba pensando en enviarles como respuesta un correo parecido al que escribo a continuación. **¿Qué opináis?**. Para facilitar la colaboración he pegado este documento en [un etherpad de libre modificación](https://pad.riseup.net/p/carta_al_ine).

> Hola,
> 
> Les escribo de nuevo con relación a la cuestión con número de referencia <del>XXXX</del>. Esta cuestión era relativo al acceso pública a las geometrías de las secciones censales.
> 
> Lo primero darles las gracias por su pronta respuesta y la claridad de la misma y notificarles de nuevo que estoy copianda mis preguntas y sus respuestas de forma abierta en esta dirección de internet \[1\].
> 
> El motivo de solicitarles esta información en primer lugar, era para demostrar el poder que tiene el disponer de datos abiertos a la hora de la toma de decisiones y la participación ciudadana en un trabajo que estaba realizando junto a otra gente de forma voluntaria como motivo del Open Data Day.
> 
> No quiero alargar esto de forma indefinida, pero a la vista de su respuesta me surgen una serie de dudas que les manifiesto:
> 
> \* ¿Por qué los costes de acceso a esta información no son claramente enunciados? A pesar de ser el INE un «organismo autónomo» entiendo que en el fondo tiene un carácter (¿y financiación?) público y por tanto sería interesante hacer un esfuerzo en detallarlos.
> 
> \* Si bien creo que ni la LISIGE ni la Ley de Reutilización de la Información Pública obligan a la publicación gratuita de la información, el espíritu de estas normativas es el facilitar lo máximo posible el acceso. Si bien es difícil cuantificar \[2\] las ventajas de disponer de la mayoría de información geográfica de forma gratuita, si que parece existir un consenso general de que ello favorece el desarrollo económico y social de un país. Con esto en cuenta, mi pregunta sería si los ingresos obtenidos por el instituto por la comercialización de esta información son lo suficientemente significativos como para que compense limitar el acceso a los mismos a las empresas y ciudadanía.
> 
> \* Mi última cuestión de índole más práctica sería bajo que terminos o licencia de uso se distribuyen las geometrías de las secciones censales. En concreto, en caso de adquirirlas podría luego revenderlas o publicarlas de forma abierta en internet.
> 
> Por último, felicitarles por el trabajo que realizan, dado que somos muchos los que podemos realizar una labor comercial o investigadora gracias a los datos que publican.
> 
> Atentamente
> 
> \[1\] http://conocimientoabierto.es/pregunta-abierta-al-ine-por-que-las-geometrias-de-las-secciones-censales-no-son-publicas/659/
> 
> \[2\] http://blog-idee.blogspot.com.es/2011/11/que-valor-tiene-la-informacion.html