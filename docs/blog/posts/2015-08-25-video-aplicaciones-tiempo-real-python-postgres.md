---
id: 810
title: 'Video: Aplicaciones en tiempo real con python y postgres'
date: '2015-08-25T22:59:21+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=810'
permalink: /video-aplicaciones-tiempo-real-python-postgres/810/
categories:
    - 'Sin categoría'
tags:
    - como
    - 'desarrollo sofware'
    - 'desarrollo web'
    - 'how to'
    - postresql
    - python
    - tutorial
    - vídeo
---

<iframe allowfullscreen="" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/PsorlkAF83s?rel=0" width="420"></iframe>

Una charla de como montar aplicaciones en tiempo real con python y postgres. Tiempo real entendido como notificaciones de un chat, hacer algo cada vez que se actulice una tabla de la bd etc,…

El vídeo se hace un poco largo, seguramente con las transparencias llegaba para hacerse una idea general. Pero aún así se hace interesante por alguna de las técnicas que emplea:

- Aboga por no usar frameworks en python. Con las librerías de hoy en día es sencillo montar una API Rest gestionando las llamadas de bajo nivel directamente
- Usa las funciones de postgres de LISTEN y NOTIFY que combinadas con un trigger permiten que código cliente (psycopg2) sean notificados cuando algo pasa en la base de datos (se modifica una fila o lo que sea) y actuén en consecuencia (provocar un cambio en el navegador mediante websockets)
- Para simplificar la API y el diseño de la bd, los datos se guardan como tipos nativos postgres (varchar, boolean,…), y se usa la función de postgres row\_to\_json para recuperarlos una cadena de texto con formato json.
- Usa [httpie](https://github.com/jkbrzt/httpie) para probar la API Rest. Si alguna vez usaste <a hre="http://www.codingpedia.org/ama/how-to-test-a-rest-api-from-command-line-with-curl/">curl</a> para esto enseguida verás que está bien conocer httpie.
- A pesar de que la idea principal de la charla es montar una aplicación en tiempo real con el mínimo número de dependencias (complejidad) el proceso de build que monta no parece trivial. pip para dependencias en python, nodeenv (una especie de entorno virtual para node que se integra con el virtualenv de python), bower para las dependencias javascript de cliente,… Todo ello orquestrado por un Makefile.
- No muestra como hacer la parte del frontend, pero en todo caso [el código está en su repo](https://bitbucket.org/btubbs/todopy-pg)