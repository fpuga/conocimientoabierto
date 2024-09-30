---
categories:
- Sin categoría
date: 2012-12-06
permalink: /borrar-automaticamente-comentarios-pendientes-en-wordpress/502/
slug: borrar-automaticamente-comentarios-pendientes-en-wordpress
tags:
- how to
- odiseus
- spam
- web
- wordpress
---

# Borrar automáticamente comentarios pendientes en WordPress

Esta mañana me he puesto a actualizar [odiseus](http://odiseus.org) y he visto que la base de datos ocupaba cerca de giga y medio, siendo la mayoría consumido por los 300.000 comentarios de spam que se nos escaparon en un blog que hace tiempo que no tiene supervisión y no tenía [Akismet](http://akismet.com/) instalado.

Por algún extraño motivo WordPress todavía no tiene un forma por defecto que permite marcar y eliminar todos los comentarios pendientes, tienes que hacerlo de 20 en 20. Las [soluciones](http://gnoted.com/how-to-delete-all-pending-comments-in-one-click-wordpress/) que vi no me convencían demasiado. Plugins anticuados, borrar cosas directamente en la base de datos sin saber las relaciones que puede haber en un multisite o entre tablas, … Y Akismet tampoco era capaz de lidiar con tantos comentarios.

Finalmente me decidí por el plugin [WP-Optimize](http://wordpress.org/extend/plugins/wp-optimize/) capaz de borrar los comentarios pendientes y hacer alguna otra cosilla mas

Por desgracia más de 50.000 comentarios ya estaban aprobados y no quería borrarlos todos sin más. La solución:

1. Buscar la fecha del último post
2. Marcar como no aprobados todos los comentarios hechos con posterioridad a un mes desde el último post

`UPDATE `wp_4_comments` SET `comment_approved` = 0 WHERE `comment_date` > '20110601';`

A continuación podemos borrar los comentarios no aprobados con wp-optimize.