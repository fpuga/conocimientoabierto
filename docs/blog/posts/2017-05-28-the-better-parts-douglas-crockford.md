---
id: 901
title: 'Charlas «The better Parts» por Douglas Crockford'
date: '2017-05-28T19:07:48+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=901'
permalink: /the-better-parts-douglas-crockford/901/
categories:
    - 'Sin categoría'
tags:
    - charlas
    - Crockford
    - 'desarrollo sofware'
    - javascript
    - recomendaciones
    - vídeo
---

Seguramente las charlas más conocidas de Crockford son las basadas en su libro [The good parts](http://conocimientoabierto.es/libro-javascript-the-good-parts-de-douglas-crockford/858/) y o algunas más modernas a las que llama de «The better parts» donde revisa alguna de sus anteriores prácticas y comenta features de ES6.

Dentro de esta serie de *The Better Parts* se pueden encontrar varias dadas en distintas momentos, entre ellas.

- [The Better Parts | .concat() 2015](https://www.youtube.com/watch?v=_EF-FO63MXs). El problema de esta charla es que no se ven las transparencias (y a pesar de ser similares) a las slides que usa en otras se hace un poco complicado seguir el hilo. Creo que una de las novedades de esta charla respecto a otra es cuando habla de los [Template Literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).
- [The Better Parts. Infoq. Agosto/2014](https://www.infoq.com/presentations/efficient-programming-language-es6). Las transparencias de esta charla, que también valen de guía para el resto [están aquí](https://drive.google.com/file/d/0B9h_EQ82pIpuUi02S1dYNmRfZlk/edit). La de la JSConfUY me pareció un poco más fluída que esta. Pero hay al menos dos secciones que en esta están mejor explicadas o ampliadas la que llama en las transaprecias *New Good Parts in ES6* que empieza en el minuto 12 y acaba en el 25. Y cuando explica su *constructor pattern* (slide 46) a partir del minuto 34. El constructor también lo explica en la JSConfUY pero aquí se entienda mejor.
- [The Better Parts – JSConfUY Septiembre/2014](https://www.youtube.com/watch?v=bo36MrBfTk4). En apareciencia esta tiene un poco más de carga filosófica que la de Infoq.

Yo ví la charla de JSConfUY, ojee la de concat, y fuí a algunas partes concretas de la de InfoQ. Mi recomendación es que veas la de InfoQ. O si no que veas de la JSConfUY y las partes concretas que mencionó de la de InfoQ.

A nivel contenidos las charlas son similares.

Arranca con una cita de Saint-Exupéry, «It seems that perfection is attained not when there is nothing more to add, but when there is nothing more to subtract.» y de como los programadores deben buscar la perfección. Por ello hace incapié en uno de sus habituales, que un lenguaje nos dé un montón de características no significa que tengamos que usarlas todas si no sólo las «buenas».

Luego habla de jslint y de su libro de «The good parts». Combate algunas de las criticas que se hacen de jslint y defiende porqué el estilo de desarrollo no es simplemente un «acuerdo», si no que hay estilos mejores que otros, y que escribir de una determinada forma elimina bugs y por tanto te acerca a la perfección.

Continúa con una mini revisión de esas buenas partes de JavaScript en general mezclándolo con como debería ser el lenguaje del futuro (tiene otra charla sobre esto llamada [The Post JavaScript Apocalypse](https://www.youtube.com/watch?v=NPB34lDZj3E)), centrándose en su propuesta para un nuevo tipo de datos numérico llamado [DEC64](http://dec64.com/).

Y termina hablando un poco de JSON.

## The better parts

Entre las prácticas que menciona como mejores están.

\* No usar *for*. Sólo *array.forEach* y derivados  
\* No dice nada de *for..of*, supongo que en el momento todavía no habría una propuesta al respecto, pero si habla de evitar *for..in* y emplear unicamente *Object.keys(object).forEach*  
\* Y dice que tampoco usa ya while si no que usa una construcción de este tipo  
`<br></br>function repeat(func) {<br></br>  if (func() !== undefined) {<br></br>    return repeat(func);<br></br>  }<br></br>}<br></br>`

Como vemos, y como el mismo dice, estás Better Parts van en la línea de usar JavaScript como un lenguaje funcional.

Especial atención merece su nuevo patrón para la construcción de objetos. Hace tiempo que aboga por no usar *new* pero también ha dejado de usar *Object.create*, de hecho ha dejado de usar *this* para evitar problemas de seguridad. También defiende que la herencia basada en prototipos es una mejor idea que las jerarquías clásicas. Porqué, las jerarquías son en general erróneas, y además suelen establecerse al principio del proyecto, cuando menos información se tiene de como debe ser.

Su patrón para la construcción de objetos tendría este aspecto

`<br></br>function constructor(spec) {<br></br>  let {member} = spec,<br></br>      {other} = other_constructor(spec),<br></br>      method = function () {<br></br>        // member, other, method<br></br>      };`

 return Object.freeze({  
 method,  
 other  
 });  
}

Donde

- *spec* será generalmente un object literal, que permite inicializar el objeto
- *member* será un miembro privado de la clase, no accesible desde el exterior
- Esta construcción permite que se pueden llamar tantas veces como se quiera a otros constructores (*other\_constructor*), de ese modo se obtiene herencia múltiple, y se pueden copiar, las funciones de interés de esos otros objetos en nuestro objetos
- También puedo crear nuevos métodos (*method*), que tendrán acceso a los miembros privados, a otros métodos, a lo que proporcione *other*. En este caso *method* es público porque se devuelve al llamante pero con el mismo diseño podría ser un método privado
- Se devuelve un nuevo objeto (el literal dentro de freeze, con todos los métodos de interés)
- Lo congela para hacerlo inmutable, con todas las implicaciones que eso trae. Seguridad, comparaciones más sencillas, …
- Comenta que este sistema tiene un costo en memoria. Al contrario que otras estrategias que reaprovechan los métodos, en esta *method* sería creado cada vez. Pero a cambio es muy rápido, porque no hay que recorrer el prototype chain para encontrar las claves si no que están directamente en el propio objeto

En otro momento, me gustaría hacer un artículo con los distintos patrones de creación de objetos de Javascript, pero debo decir que este me convence mucho, porque debe ser de las pocas veces que veo algo de este tema en JS que parece tener sentido a la primera. Lo que no comprendo es porque llama «constructor» a su función de ejemplo cuando en realidad es una «factory».