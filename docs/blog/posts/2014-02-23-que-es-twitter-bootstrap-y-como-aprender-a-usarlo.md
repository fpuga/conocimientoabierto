---
id: 657
title: 'Qué es Twitter Bootstrap y cómo aprender a usarlo'
date: '2014-02-23T09:30:10+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=657'
permalink: /que-es-twitter-bootstrap-y-como-aprender-a-usarlo/657/
categories:
    - 'Sin categoría'
tags:
    - bootstrap
    - como
    - 'desarrollo sofware'
    - 'desarrollo web'
    - 'how to'
    - web
---

Generar una plantilla básica sobre la que empezar un proyecto web que tenga en cuenta los distintos navegadores y tamaños de dispositivos consume mucho más tiempo del que debería. Para minimizar este problema durante los últimos dos o tres años [han surgido varios frameworks](http://www.sitepoint.com/best-web-designing-frameworks-2014/) de diseño web. Si te dedicas a esto y no has estado debajo de una piedra este tiempo, sin duda habrás oído hablar de [twitter-bootstrap](http://getbootstrap.com/), que es el que se ha hecho más popular.

## ¿Qué es bootstrap?

Bootstrap o twitter-bootstrap es un framework [creado originalmente por dos desarrolladores/diseñadores de twitter](http://alistapart.com/article/building-twitter-bootstrap) para acelerar el diseño de nuevas aplicaciones web.

El framework proporciona clases css y código javascript para definir el layout de la página, crear componentes que respondan a eventos y estilizar los elementos html más habituales. [Estos ejemplos están hechos con la versión 2](http://www.adobe.com/devnet/html5/articles/twitter-bootstrap.html), pero valen para hacerse una idea.

Podemos decir que los principios en los que se basa la última versión (la 3) son:

- **Responsive Design**: Que según mi definición particular consiste en que la página trata de «hacer lo correcto» al ser visualizada independientemente del dispositivo y tamaño de la pantalla. El término fue acuñado por [Ethan Marcotte en 2010](http://alistapart.com/article/responsive-web-design).
- **Mobile first**: Al contrario que en la versión 2, en la 3, el diseño *responsivo* es la opción por defecto al trabajar con bootstrap
- **Cross Browser**: Trata de ser compatible con la mayoría de navegadores.
- **Integración con jQuery**: Está muy integrado con jquery para el que define nuevos plugins
- **Buenas prácticas**: Trata de emplear algunas de las prácticas más extendidas en cuanto a usabilidad, uso de css3/html5, organización del código, …

## ¿Qué me aporta bootstrap?

Si eres desarrollador con poca experiencia en diseño te proporciona una forma muy rápida de crear un layout responsivo básico de la página en la que empezar a meter tu código.

Si eres diseñador, obtienes una enorme cantidad de clases CSS que personalizar a tu gusto, sin tener que partir de cero.

Si quieres aprender a hacer las cosas mejor, es un compendio de buenas prácticas.

## Aprendiendo a usar bootstrap

La documentación de la [página de bootstrap](http://getbootstrap.com/getting-started) debería ser tu principal fuente de información, sobre todo porque el resto de documentación tiende a quedar más desactualizada, aún así, hay una serie de tutoriales que a mi me han resultado más útiles para empezar, sobre todo porque te permiten coger ideas más generales de lo que permite hacer.

Los enlazo en el orden que creo que merece la pena seguirlos:

1. [Tutorial de w3resource](http://www.w3resource.com/twitter-bootstrap/tutorial.php): Hay partes del tutorial que están con la versión 2, pero cubre muchos aspectos
2. [Understanding twitter bootstrap 3](http://www.sitepoint.com/understanding-twitter-bootstrap-3/). También se le escapa alguna etiqueta de la v2 como el container-fluid, pero en general te permite aprender a diseñar un ejemplo básico.
3. Una [introducción a los componentes](http://www.sitepoint.com/twitter-bootstrap-3-javascript-components/) que proporciona bootstrap como el scrollspy o las ventanas modales
4. Actualizado 31/Agosto/2015. En [Udemy acaban de publicar un post con una muy buena introducción a boostrap](https://blog.udemy.com/bootstrap-tutorial-a-guide-for-beginners/).
5. [Bootstrap 3 Tutorial – An Introductory Course | Udemy](https://www.udemy.com/introduction-to-bootstrap-3/). Una serie de videotutoriales muy chulos donde emplean unas cuantas clases que no he visto en otros sitios. Es de pago pero barato. Con los recursos anteriores seguramente ya no te será necesario este curso, así que mira alguno de los vídeos de muestra antes de comprarlo

## Otros recursos

Desde que nació bootstrap han ido apareciendo un montón de recursos que sacan partido a este framework

- Herramientas tipo wireframe que sacan el código en bootstrap, como por ejemplo [layoutit](http://www.layoutit.com/).
- Una [plantilla de ESRI](http://esri.github.io/bootstrap-map-js/doc/index.html) que usa bootstrap con su API, y otra para [integrarlo con leaflet](https://github.com/bmcbride/bootleaf).
- [Bootstrap sí, pero no](http://bruno.garciaechegaray.com/Bootstrap.The.Melee/presentation/) y sobre todo [please stop using twitter bootstrap](http://css.dzone.com/articles/please-stop-using-twitter), de la que no hay que perderse los comentarios. Dos artículos un poco más críticos con la *moda bootstrap*.
- Los [puntos 4 y 6](http://m5designstudio.com/2013/orlando-web-design/bootstrap-responsive-layout/) sobre *responsivididad* y como *wrapear* texto alrededor de una imagen están bien.
- Un [artículo](http://www.sitepoint.com/foundation-compelling-alternative-bootstrap/) y un [vídeo sobre si usar bootstrap o usar Zurb Foundation](#) (otro framework parecido a bootstrap)
- [Hay un montón de páginas que ofrecen temas hechos a partir de bootstrap, ](#)[startbootstrap](http://startbootstrap.com/) es simplemente una de ellas con por ejemplo [sb admin](http://startbootstrap.com/sb-admin) para hacer *dashboards*

## Conclusiones

En un par de días puedes revisar los enlaces que se proporcionan en este artículo, y refactorizar alguna web sencilla que tengas para que use bootstrap. Será un tiempo bien empleado que recuperarás con creces.

No he probado otros frameworks del estilo, pero supongo que serán parecidos, cada uno con sus fortalezas y debilidades. Si le tienes manía a bootstrap, escoge otro, pero desde luego es una herramienta a meter en tu caja si eres desarrollador web.