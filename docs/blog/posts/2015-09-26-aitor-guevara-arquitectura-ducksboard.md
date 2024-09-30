---
id: 825
title: 'Aitor Guevara hablando de la arquitectura de Ducksboard'
date: '2015-09-26T21:32:02+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=825'
permalink: /aitor-guevara-arquitectura-ducksboard/825/
categories:
    - 'Sin categoría'
tags:
    - arquitectura
    - 'desarrollo sofware'
    - 'desarrollo web'
    - ducksboard
    - vídeo
---

Un vídeo algo antiguo (2013) en el que [Aitor Guevara](http://blog.aitorciki.net/) (CTO de Ducksboard) nos habla de cual era la arquitectura de Ducksboard en aquel momento. A pesar de que el vídeo dura más de una hora y media Aitor consigue hacer amena una charla técnica. No entra al mínimo detalle técnico pero si da una buena idea general. Responde sin rubor a preguntas como cual era el costo de la infraestructura que tenían en Linode (400$) o cuantos clientes de pago tienen.

https://www.youtube.com/watch?v=ArpNnabLqZE

Por el medio de la charla caen perlas del estilo de:

- Usamos twisted para hacer aplicaciones asíncronas en python. ¿Conoceis nodejs? pues lo mismo pero tiene 10 años en lugar de 1.
- Usamos backbone, porque tenemos un montón de javascript. Tenemos un montón no porque nos guste si no porque es lo que hay.

Otra de las cosas que más me gustan es la defensa que hace de PostgreSQL, que es el componente central de su infraestructura (especialmente hacia el minuto 50 pero en realidad lo hace en varios momentos). Hacia el minuto 44 explica como usan ellos backbone. La verdad es que aquí no me quedo muy claro desde donde servían el html, o si iba todo en los templates, porque el django del frontend en principio sólo actuaba como API Rest sirviendo JSON al navegador. Eso si, su django usa SQLAlchemy y no django-orm porque tenían cosas en el postgres que django-orm no soporta.

Los últimos minutos de la charla presenta un par de herramientas que «análisis del negocio» que también son de interés.

[En este post además del vídeo están las transparencias](http://blog.aitorciki.net/2013/12/30/de-chachara-arquitectura-de-ducksboard/).