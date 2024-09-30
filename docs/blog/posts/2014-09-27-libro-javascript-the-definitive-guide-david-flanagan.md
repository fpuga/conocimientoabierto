---
categories:
- Sin categoría
date: 2014-09-27
permalink: /libro-javascript-the-definitive-guide-david-flanagan/726/
slug: libro-javascript-the-definitive-guide-david-flanagan
---

# Libro: Javascript. The definitive guide. David Flanagan.

Hace poco terminé de leer [JavaScript. The definitive guide, de David Flanagan (la sexta edición)](http://www.amazon.es/gp/product/B00M0NQR34/ref=as_li_ss_tl?ie=UTF8&camp=3626&creative=24822&creativeASIN=B00M0NQR34&linkCode=as2&tag=conociabiert-21)![](http://ir-es.amazon-adsystem.com/e/ir?t=conociabiert-21&l=as2&o=30&a=B00M0NQR34). El libro tiene unas mil página aunque la segunda parte es una guía de referencia (que viene bastante bien para cuando trabajas off-line).

El libro cubre tanto el core del lenguaje como la API de cliente, es decir las funcionalidades que proporcionan los navegadores, y también tiene un capítulo sobre jQuery. A pesar de ser de 2011 está orientado hacia HTML5 y ECMAScript 5, así que cubre cosas como la API de Geolocalización, WebWorkers, WebSockets, Client Side Databases, …

Empecé a leerlo, sin conocer demasiado javascript y con la idea de adquirir buenas prácticas de desarrollo en javascript y en ese sentido me decepcionó un poco. El libro está bien, pero es poco opinativo. Javascript es un lenguaje muy amplió de por sí, y creo que cuando empiezas con él, es necesario que te fijen un par de ideas claras en la cabeza y no que te presenten todas las opciones disponibles. Por ejemplo, presenta muchos ejemplos de código donde enseña a lidiar con las diferencias entre navegadores, o como gestionar eventos, cuando en la práctica la mayoría usamos una librería tipo jQuery que nos abstraiga de esos problemas.

Mi próxima lectura seguramente será [Javascript, the good parts, de Douglas Crockford](http://www.amazon.es/gp/product/B0026OR2ZY/ref=as_li_ss_tl?ie=UTF8&camp=3626&creative=24822&creativeASIN=B0026OR2ZY&linkCode=as2&tag=conociabiert-21)![](http://ir-es.amazon-adsystem.com/e/ir?t=conociabiert-21&l=as2&o=30&a=B0026OR2ZY), que es bastante más corto, y más orientado a promocionar buenas prácticas que a orientarse en el lenguaje. Cuando lo lea podré comparar, pero me da la impresión de que es mejor leer primero el de [Crockford](http://www.crockford.com/) y luego el de [Flanagan](https://twitter.com/__DavidFlanagan).

Supongo que las partes más interesantes variarán según para que tengas que usar javascript, para mi lo mejor del libro seguramente es:

- Que dedica bastante tiempo al Cross Origin y problemas relacionados. Por ejemplo en la sección 13.6.2, 18.1.6. En la 22.3 que explica la API para que un script pueda pasar mensajes a otro objeto Window. Y en la 18.2 explica como gestionar JSONP.
- El capítulo 18 en general, donde habla de Ajax (y algo de Commet) es bastante útil para aclarar conceptos.
- El capítulo 10, es el típico sobre expresiones regulares, pero la verdad es que este merece la pena leerlo. Está bastante bien explicado incluido algunos conceptos avanzados que suelen obviarse.
- Los capítulos del 6 (Objetos), 7 (Arrays), 8 (Funciones) y 9 (Clases), son para mi la parte central del libro. Conviene leerlos con calma y repasarlos para entender como funciona Javascript. En él tratan temas como los [constructores y prototype](http://www.objectplayground.com/), el [hoisting](http://www.etnassoft.com/2010/12/26/hoisting-en-javascript/), [closures](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Closures), o los <a>atributos de las propiedades de los objetos</a> o [sparse arrays](https://www.inkling.com/read/javascript-definitive-guide-david-flanagan-6th/chapter-7/sparse-arrays)

Este libro es una muy buena opción si ya sabes algo de Javascript y quieres adquirir fundamentos más sólidos en el lenguaje. Si buscas un libro de introducción al desarrollo web o a la programación en javascript seguramente haya opciones mejores.

## Otras críticas al libro

- [En el blog de chuidiang](http://blog.chuidiang.com/2013/03/29/he-leido-javascript-the-definitive-guide/).