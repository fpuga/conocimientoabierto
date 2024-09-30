---
id: 851
title: 'Eventos en backbonejs'
date: '2016-01-02T14:02:19+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=851'
permalink: /eventos-backbonejs/851/
categories:
    - 'Sin categoría'
tags:
    - backbonejs
    - 'desarrollo sofware'
    - 'desarrollo web'
    - patrones
---

Una de las formas más interesantes de desacoplar código, vistas fundamentalmente, usando un framework MV\* tipo backbone es aprender a usar correctamente los eventos y patrones asociados. Observer (pub/sub), Event Aggregator, Mediator, …

La mejor lectura al respecto que he encontrado es este [post de Derick Bailey](https://lostechies.com/derickbailey/2011/07/19/references-routing-and-the-event-aggregator-coordinating-views-in-backbone-js/) (creador de MarionetteJS), donde de forma muy ilustrativa examina distintas opciones finalizando con como hacerlo con eventos. Es recomendable también leer los comentarios, donde Derick responde a varias dudas de los lectores.

La sección sobre [Eventos de Developing Backbone Applications](http://addyosmani.com/backbone-fundamentals/#events) explica bien como usar los eventos en general en backbone y esta otra sección revisita el post de Derick exponiendo la [diferencia entre Event Aggregator y Mediator](http://addyosmani.com/backbone-fundamentals/#event-aggregators-and-mediators).

Pero para trabajar con Eventos de forma correcta además de los patrones y las especifidades de backbone es necesario conocer algunas técnicas y características de javascript relacionadas con el [contexto](http://ryanmorr.com/understanding-scope-and-context-in-javascript/). La siguiente selección de artículos puede ahorrarte un par de horas de quebraderos de cabeza:

- Primero es importante conocer [a que hace referencia this en cada caso](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
- Y en este algo algo viejo (anterior a que *bind* fuera un estándar) pero todavía ilustrativo artículo [explican los problemas del *binding loss*](http://alistapart.com/article/getoutbindingsituations)
- La [documentación del método bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) y algún [ejemplo de uso](http://www.smashingmagazine.com/2014/01/understanding-javascript-function-prototype-bind/), también son de interés.
- Y trabajando con underscore / backbone es fundamental conocer y saber usar [\_.bind y \_.bindAll](http://blog.bigbinary.com/2011/08/18/understanding-bind-and-bindall-in-backbone.html)
- Y ya como extra, un artículo sobre [partial application](<partial application http://benalman.com/news/2012/09/partial-application-in-javascript/>)