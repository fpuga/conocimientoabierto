---
categories:
- General
date: 2009-09-10
permalink: /como-usar-feedburner-servir-feed/144/
slug: como-usar-feedburner-servir-feed
tags:
- como
- estadísticas
- feed
- feedburner
- how to
- permalinks
- wordpress
---

# Como usar FeedBurner para servir nuestro feed

<div class="ngg-gallery-singlepic-image ngg-left" style="max-width: 300px"> [ ![feedburner](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/cache/mybrand0.jpg-nggid011-ngg0dyn-300x225x100-00f0w010c010r110f110r010t010.jpg "feedburner") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/mybrand0.jpg "usar nuestro propio feed o el de feedburner") </div> [Feedburner](http://www.feedburner.com/) es un servicio web propiedad de Google que se encarga de redistribuir nuestros feeds. Es algo así como si feedburner se subscribiera al feed que proporcionamos desde nuestro blog, luego volviera a distribuirlo y nosotros indicamos a nuestros lectores que se conecten a través de esa segunda versión de nuestro feed y no a través del que proporcionamos directamente en el blog. La ventaja de esto es que ahorramos ancho de banda y que Feedburner puede proporcionarnos [estadísticas](http://conocimientoabierto.es/estadisticas-wordpress/66/) interesantes de los lectores. La parte mala es que pasamos a tener cierta dependencia de un servicio externo y una disminución de la privacidad puesto que google pasa a poder recolectar información sobre nuestros lectores. Feedburner estuvo de modo hace un par de años cuando el ancho de banda era un bien escaso y las empresas de hosting eran caras, en la actualidad no resulta en general necesario. Desde mi punto de vista el único motivo para usarlo sería por el de las estadísticas, tu debes valorar si la información que proporciona compensa el ceder datos a google.

Si te decides a usarlo, una forma de minimizar el impacto de la dependencia externa es activar la característica [My Brand](http://www.google.com/support/feedburner/bin/answer.py?hl=en&answer=79590), en este artículo se explica como activar FeedBurner con My Brand para nuestro blog.

Antes de continuar, debes tener presente dos cosas

- Para poder usar My Brand tienes que añadir un registro CNAME a las dns de tus dominios, mira en las páginas de ayuda de tu hosting como hacerlo. Generalmente se encuentra en el apartado Dominios o «Gestión de DNS» y es fácil, pero es bueno que mires como hacerlo antes de meterte en faena
- Las direcciones que se indican aquí para los [feeds por defecto de wordpress](http://codex.wordpress.org/WordPress_Feeds) del tipo dominio.com/feed y dominio.com/comments/feed son sólo válidas si tenemos activados los permalinks de wordpress. Si no los tienes activados deberás usar la dirección dominio.com?feed=rss2 y dominio.com/wp-commentsrss2.php. Si los permalinks están customizados también puedes usar el otro tipo de dirección pero es mejor usar la *customizada*.

#### Pasos para servir nuestro feed a través de Feedburner

Entramos en feedburner.com con nuestra cuenta de gmail. Si no tenemos una podemos crear una cuenta de google allí mismo.

<div class="ngg-gallery-singlepic-image ngg-center" style="max-width: 320px"> [ ![feedburner - my brand - Imagen 1](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/cache/mybrand1.jpg-nggid012-ngg0dyn-320x240x100-00f0w010c010r110f110r010t010.jpg "feedburner - my brand - Imagen 1") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/mybrand1.jpg "como configurar my brand y feedburner para nuestro blog") </div>En el formulario que aparece en mitad de la página escribimos la dirección de nuestro blog (en el ejemplo usamos la página [www.marinerosbouzas.com](http://www.marinerosbouzas.com), y pulsamos en siguiente \[Imagen 1, puedes pinchar sobre las imágenes para ampliarlas\]. Dejamos seleccionado el usar rss en lugar de atom (esto no importa) y pulsamos siguiente.

<div class="ngg-gallery-singlepic-image ngg-center" style="max-width: 230px"> [ ![feedburner - my brand - Imagen 2](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/cache/mybrand2.jpg-nggid013-ngg0dyn-320x240x100-00f0w010c010r110f110r010t010.jpg "feedburner - my brand - Imagen 2") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/mybrand2.jpg "como configurar my brand y feedburner para nuestro blog") </div>En esta pantalla \[Imagen 2\] escogemos un título para el feed, generalmente el nombre del blog. Feed address es la dirección desde la que serviremos nuestro rss a partir de ahora así que es bueno que escojamos algo fácil y significativo, por ejemplo *feeds.feedburner.com/tudominio*.

Por defecto feedburner contabiliza la cantidad de usuarios subscritos a nuestros feeds. En las siguientes pantallas tenemos la opción de activar el clickthrougs, es decir contabilizar el número de veces que los lectores acceden a nuestra web por pinchar en el feed. Yo no lo activo por que significa que feedburner añadirá un código html algo intrusivo en nuestros feeds para poder trazar lo que hacen nuestros lectores. Hay más opciones pero las que están por defecto suelen ser adecuadas para la mayoría

<div class="ngg-gallery-singlepic-image ngg-center" style="max-width: 226px"> [ ![feedburner - my brand - Imagen 3](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/cache/mybrand3.jpg-nggid014-ngg0dyn-320x240x100-00f0w010c010r110f110r010t010.jpg "feedburner - my brand - Imagen 3") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/mybrand3.jpg "como configurar my brand y feedburner para nuestro blog") </div>Si además del feed de los posts, queremos que el de los comentarios se sirva también a través de feedburner volveremos [ al inicio](http://feedburner.com) e introduciremos la dirección http://tudominio.com/comments/feed, en este caso http://marinerosbouzas.com/comments/feed, y en la siguiente pantalla escogemos como *feed address* feeds2.feedburner.com/comentarios\_tudominio (en este caso feeds2.feedburner.com/comentarios\_marinerosbouzas) y como *feed title* «Comentarios para tudominio» por ejemplo \[Imagen 3\].

A partir de ahora nuestros lectores podrán acceder a nuestro feed a través de *http://feeds.feedburner.com/tudominio* y a través de *http://tudominio.com/feed*. Esta última dirección es, por ahora, el valor por defecto que obtendrá alguien que introduzca en su lector de feeds la dirección de nuestro blog. Para hacer que por defecto se sirva el feed a través de feedburner debemos hacer algunos cambios en la plantilla del blog o instalar un plugin. Pero antes de entrar en esto activaremos la característica My brand.

#### Pasos para activar My Brand

La opción de My Brand permite que la dirección del feed que servimos a través de feedburner sea del estilo *http://feed.tudominio.com/tudominio* en lugar de *http://feeds.feedburner.com/tudominio*. Lo bueno de esto es que si alguna vez feedburner quiebra, se vuelve de pago o deja de satisfacernos nuestros lectores estarán subscritos a una dirección sobre la que tenemos el control y no a una externa.

Para activar My Brand pulsamos en *My account* y después en My brand. Debemos localizar una línea que pone algo parecido a \[Imagen 4\]

> feeds CNAME XXXXX.feedproxy.ghs.google.com

Crearemos un registro CNANE en nuestro hosting que apunte a esa dirección: XXXXX.feedproxy.ghs.google.com (el valor de las XXX dependerán de cada caso)

<div class="ngg-gallery-singlepic-image ngg-center" style="max-width: 198px"> [ ![feedburner - my brand - Imagen 4](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/cache/mybrand4.jpg-nggid015-ngg0dyn-320x240x100-00f0w010c010r110f110r010t010.jpg "feedburner - my brand - Imagen 4") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/mybrand/mybrand4.jpg "como configurar my brand y feedburner para nuestro blog") </div>De vuelta en [ la página de configuración de my brand](http://feedburner.google.com/fb/a/mybrand) introducimos el valor *feeds.tudominio.com* (en nuestro caso feeds.marinerosbouzas.com, nótese que no hay que poner el http:// delante) en el campo que aparece en el punto 2 de la imagen 4 y le damos a activar. Por supuesto en lugar de *feeds* podemos usar el subdominio que queramos.

Con esto hemos activado la dirección *feeds.tudominio.com/tudominio* para servir el feed de nuestro blog a través de feedburner pero manteniendo la dirección de subscripción bajo nuestro control. Si también servimos los comentarios a través de feedburner estos estarán, sin necesidad de tocar nada más en *feeds.tudominio.com/tudominio\_comentarios*

#### Modificar nuestro tema para servir por defecto los nuevos feeds

El último paso, es indicar a la gente que accede a tu blog que no quieres que se subscriban a través del feed propio de wordpress si no a través del proporcionado por feedburner. Es posible hacer esto a través de un plugin como [FeedSmith](http://www.google.com/support/feedburner/bin/answer.py?hl=en&answer=78483), pero si quieres hacerlo a mano tampoco es muy complicado, tan sólo tienes que editar el tema que usas y modificar un par de líneas para hacer referencia a las nuevas direcciones de los feeds. En general tendrás que hacer las modificaciones en dos lugares distintos:

- Entre las etiquetas &lt; header &gt; que suelen estar en el archivo header.php debes localizar las etiquetas &lt; link &gt; que hagan referencia a los feed y cambiar el valor de *href* por las nuevas direcciones. Esto es lo que hace que cuando un lector de feeds intente descubrir por si mismo el feed de tu blog lo resuelva correctamente
- El segundo cambio será necesario cuando en algún sitio del tema indiquemos la dirección directa para subscribirse.

#### Pasos para el tema default de wordpress

En concreto, particularizando para el tema por defecto que viene con wordpress lo que habría que hacer es:

- Abrir con un editor de textos el archivo wp-content/themes/default/header.php y buscar las líneas:  
    > &lt;link rel=»alternate» type=»application/rss+xml» title=»&lt;?php printf(\_\_(‘%s RSS Feed’, ‘kubrick’), get\_bloginfo(‘name’)); ?&gt;» href=»<span style="color:red">&lt;?php bloginfo(‘rss2\_url’); ?&gt;</span>» /&gt;  
    > &lt;link rel=»alternate» type=»application/atom+xml» title=»&lt;?php printf(\_\_(‘%s Atom Feed’, ‘kubrick’), get\_bloginfo(‘name’)); ?&gt;» href=»&lt;?php bloginfo(‘atom\_url’); ?&gt;» /&gt;
- Borrar la segunda, la que pone algo de atom y substituir el texto que está en rojo en la primera por http://feeds.tudominio.com/tudominio
- En el archivo wp-content/themes/default/footer.php buscar la línea  
    > &lt;a href=»<span style="color: #ff0000">&lt;?php bloginfo(‘rss2\_url’); ?&gt;</span>«&gt;RSS das Entradas&lt;/a&gt; &amp;amp; &lt;a href=»<span style="color: #ff0000">&lt;?php bloginfo(‘comments\_rss2\_url’); ?&gt;</span>«&gt;RSS dos Comentarios&lt;/a&gt;.
- Substituir lo que está en rojo en la primera por http://feeds.tudominio.com/tudominio. Si también estas haciéndolo para los comentarios substituye también lo que está en rojo en la segunda línea por http://feeds.tudominio.com/tudominio\_comentarios.