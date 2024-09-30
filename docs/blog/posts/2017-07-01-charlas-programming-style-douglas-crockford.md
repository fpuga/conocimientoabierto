---
id: 909
title: 'Charlas “Programming Style” por Douglas Crockford'
date: '2017-07-01T10:00:29+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=909'
permalink: /charlas-programming-style-douglas-crockford/909/
categories:
    - 'Sin categoría'
tags:
    - charlas
    - 'coding style'
    - Crockford
    - 'desarrollo software'
    - javascript
    - recomendaciones
    - vídeo
---

Otra de las [series](http://conocimientoabierto.es/the-better-parts-douglas-crockford/901/) de charlas más conocidas de [Crockford](http://crockford.com/), son en las que habla de la importancia del estilo de código que empleamos.

> A good style can help produce better programs. Style should not be about personal preferences and self-expression. Douglas Crockford

De esta serie creo que la más interesante es:

- YUIConf 2011. 66′. Douglas Crockford. [Programming Style &amp; Your brain](https://www.youtube.com/watch?v=taaEzHI9xyY). En esta charla Crockford explica lo importante que es usar un estilo de código adecuado, y como hay estilos mejores que otros (según el lenguaje que estemos usando). Al programar no debemos tratar de demostrar lo listos que somos, si no escribir código para que otros puedan entenderlo, y hay estilos que favorecen esto además de reducir los bugs que podamos cometer. La charla se centra en Javascript y la herramienta JSLint, pero el porqué de usar un estilo y herramientas es importante vale para cualquier lenguaje.

Otras charlas similares serían:

- HTML5 Dev Conf 2011. 36′. [JavaScript Programming Style and Your Brain](https://www.youtube.com/watch?v=cIOIyfRoGcM) with Douglas Crockford. Es una versión reducida de la charla, contempla menos casos que en las otras.
- JaxConf 2012. 54′. Douglas Crockford: [Programming Style &amp; Your Brain](https://www.youtube.com/watch?v=_EANG8ZZbRs). Bastante completa, pero un poco más aburrida que la larga.

## Escogiendo un estilo de código

Crockford dice que al escoger un estilo, debemos priorizar (y en ese orden) que:

1. Evite errores (aunque sea errores que raramente sucedan)
2. Sea legible. Comuniqué claramente su intención al resto de programadores. Y se debe preferir esto sobre ahorrar memoria o velocidad.

## Algunos comentarios de estilo de su charla con los que estoy de acuerdo

### La llave va a la derecha

La llave va a la derecha, porqué el siguiente código en js produce un error silencioso:

\[cc lang=»javascript»\]  
return  
{  
ok: false  
};  
\[/cc\]

Mientras que esto funciona correctamente:

\[cc lang=»javascript»\]  
return {  
ok: false  
};  
\[/cc\]

### Usar Strict Equality Comparison

No usar nunca «==» usar siempre «===». Evita resultados indeseados al hacer casting.

### No usar el slash para generar strings multilínea

No usar el slash para generar strings multilínea porqué si hay un espacio después del slash se produce un error  
\[cc lang=»javascript»\]  
«hola \\  
mundo»  
\[/cc\]

### Usar siempre las llaves para los bloques de código

Usar siempre las llaves aunque sea para escribir en la misma linea \[cci lang=»javascript»\]if (flag) { doSomething(); }\[/cci\]

### No usar pre/post incremento

No usar pre/post incremento. En lugar de ++x o x++ usar x+=1; Los primeros casos obligan a pensar más en lo que se está haciendo de que valor va a tener x cuando se ejecute algo, e introduce más errores.

### No usar asignación transitiva

No usar la asignación transitiva var a = b = 0. Porqué no está claro si lo que se quería hacer era  
\[cc lang=»javascript»\]  
var a = 0,  
b = 0;

b = 0;  
var a = b;  
\[/cc\]

### En los switch usar siempre break

En el switch usar siempre break después de cada caso. Es muy fácil usarlo mal, y que se presente un bug difícil de depurar.

### Forma de usar las IIFE

Al usar Immediately Invocable Function Expression, preferir la tercera forma que aparece aquí  
\[cc lang=»javascript»\]  
function () {  
…  
}(); // Syntax error!

(function () {  
…  
})(); // Bien

(function () {  
…  
}()); // Mejor. Queda más claro lo que estamos haciendo según Crockford  
\[/cc\]

### Usar siempre el «;»

Usar siempre el ; para evitar el Automatic Semicolon Insertion que puedo provocar bugs difíciles de depurar.

## Algunos con los que puedo estar de acuerdo, pero debería revisar

### Declaración de variables en el top

Como javascript no tiene (¿tenía?) block scope, si no sólo function scope, hay que declarar todas las variables en la parte de arriba y declarar todos los métodos antes de usarlos. Esto deja claro como funciona el hoisting en javascript que puede introducir errores. Esto incluye el no declarar variables dentro del for – for (var i …) {, para dejar claro que la variable i es válida para toda la función, y tiene valor antes (undefined) y después del for (el último valor que haya tomado en el bucle). Habría que ver como se conjuga esto con let, const, …

### Espacio entre paréntesis y resto de elementos

Una serie de reglas sobre donde y como usar los paréntesis, del tipo:

- No space before ( when used to invoke a function
- No space between a function name and a parameter list
- One space between all other names and (

Uso equivocado según crockford:

- foo (bar);
- function foo (b) {…}
- function(x) {…}
- return(a+b);
- if (a=== 0) {…}