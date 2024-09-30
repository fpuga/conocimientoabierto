---
categories:
- General
date: 2009-12-26
permalink: /plugin-wordpress-blogroll-dinamico/186/
slug: plugin-wordpress-blogroll-dinamico
tags:
- blogroll
- bug
- patch
- rss
- wordpress
---

# Plugin de WordPress para tener un blogroll dinámico

Estoy probando en [marinerosbouzas.com](http://conocimientoabierto.es) un plugin para wordpress llamado [SBS Blogroll](http://wordpress.org/extend/plugins/sbs-blogroll/) bastante chulo que te permite incluir en tu blog un blogroll dinámico. Es decir en lugar de tener en la barra lateral una lista de enlaces estática a los blogs que te gustan pasarás a tener una lista con el título de las últimas entradas que haya habido en esos blogs. El plugin tiene la opción además de

- Añadir el [favicon](http://es.wikipedia.org/wiki/Favicon) a cada entrada enlazada que aparezca en tu blog
- Seleccionar el número total máximo de entradas que habrá y el número máximo de entradas que pueden provenir de cada blog en tu lista
- Desplegar la fecha de cuando fue escrita la entrada
- Personalizar el estilo de como se muestran las entradas mediante css

Es un plugin sencillito pero potente que nos permite evitar el uso de servicios externos como [feevy](http://www.feevy.com/).

La única pega que le veo, es que por lo que he entendido revisando el código del plugin, lo que hace es cada vez que se muestra nuestro blog a un usuario se itera a través de toda la lista de blogs que tengamos, si se ha cumplido un tiempo de cache fijado por nosotros «va» al blog de destino a buscar la información, si no la extrae directamente de la cache, [*parsea*](http://www.alegsa.com.ar/Dic/parseo.php) la información recibida (esté en cache o no) para extraer el título, fecha, favicon, … y una vez tiene los datos de cada entrada los muestra. Todo este proceso puede consumir bastantes recursos y ralentizar nuestra página. Lo mínimo para optimizar el plugin es fijar un tiempo de cache en las opciones de 43200 segundos (12 horas) dado que poca gente actualiza en realidad más de 2 veces al día. Es decir, lo que hacemos con esto es indicar al plugin que sólo compruebe actualizaciones en los blogs que tenemos en la lista cada 12h en lugar de los 10′ que pone el plugin por defecto.

Como siempre, si tenemos muchas visitas o muchos plugins es conveniente que instalemos [algún plugin específico](http://ayudawordpress.com/gua-para-instalar-wp-cache/) para realizar el cacheado.

Otro pequeño pero de este plugin es que la versión actual tiene un pequeño bug que hace que el favicon sólo se muestre cuando indicamos que se muestre también la fecha. Ya lo he corregido y he mandando un [patch](http://conocimientoabierto.es/sw/sbs-blogroll_solved_missing_check_for_show_icon.patch) (bastante sencillito) al autor por lo que espero que salga pronto una nueva versión.

Si no podéis esperar a la nueva versión, instalar el plugin de la forma habitual y luego [sobreescribir con este archivo](http://conocimientoabierto.es/sw/sbs-blogroll.php) el que que haya en la carpeta wp-content/plugins/sbs-blogroll/ de vuestra instalación de wordpress. (para poder bajar el archivo hay que hacer click con el botón derecho sobre el enlace y darle a guardar como)

**Actualización 28/12**: La versión 0.3 del plugin ya funciona correctamente. Thanks to the [author](http://www.someblogsite.com/) for the quick fix.