---
categories:
- Sin categoría
date: 2015-08-09
permalink: /comentarios-articulo-complejidad-reversibilidad-kent-beck/806/
slug: comentarios-articulo-complejidad-reversibilidad-kent-beck
tags:
- buenas prácticas
- desarrollo sofware
- Kent Beck
---

# Comentarios al artículo de Complejidad y Reversibilidad de Kent Beck

[Andrés](http://nosolosoftware.com/) me pincha para que lea y comente [el último post de Kent Beck](http://nosolosoftware.com/complejidad-y-reversibilidad/) en su *muro de facebook*. Como todo lo que escribe Beck hay que leerlo con atención y se pueden sacar lecciones interesantes. Pero este artículo en particular se me hace complicado de leer porque creo que mezcla demasiadas cosas a la vez. Comienza con una teoría general sobre sistemas complejos y luego salta a prácticas concretas de facebook para atajarla en distintos estadios del desarrollo sin pararse a explicar que técnicas tienen sentido en según que contextos. Analicémoslo por tanto atendiendo al artículo como dos partes separadas.

## Complejidad y Software

[Software complexity](https://en.wikipedia.org/wiki/Programming_complexity) es un término con definición propia en el mundo académico. En la práctica todo desarrollador tiene una noción intuitiva de que es complejidad y [debería tener como principio el atajarla](http://nosolosoftware.com/compilaciones/del-software/#principles). Beck explica alguno de los elementos de la complejidad y cuales de ellos se puede intentar mantener bajo control en un producto como facebook. La cuestión es, si en otro tipo de productos software se puede o tiene más sentido atacar otro frente distintos al de la irreversibilidad. Personalmente se escapa de mis conocimientos esta reflexión pero apunto algunos elementos para el debate:

- Estados. Atendiendo al producto como un todo (hardware, acciones del usuario, red,..) seguramente será difícil de atajar. Si nos quedamos con las acciones (interacción) del usuario me recuerda a la diferenciación entre [mapa y camino](http://nosolosoftware.com/glosario/mapa-vs-camino/) de la que se reapropió Andrés [atendidendo a Verplank](http://nosolosoftware.com/bill-verplank/).
- Interdependencias. [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)), KIS, Patrones, Modularidad o cualquier [práctica de buen diseño](http://www.artima.com/weblogs/viewpost.jsp?thread=331531) entiendo que ayuda a disminuirla a no ser que se me escape algo.
- Incertidumbre. Supongo que es el más complicado. Usuarios usando la aplicación en formas no previstas. Requisitos cambiantes,…
- Irreversibilidad. Nada que decir, es en el que se centra Beck.

## Atajar la Irreversibilidad

La segunda parte del artículo habla de algunas de las técnicas que usan en Facebook para combatirla. Algunas pueden ser consideradas de *modernas* como el Frequent Pushes (¿[Continuous Delivery](http://www.thoughtworks.com/continuous-delivery)?) y otras como el Code Review llevan con nosotros mucho tiempo. Beck las enumera todas juntas pero creo que intentar ponerlas bajo una clasificación más o menos habitual en factorías de software tradicionales puede ayudar a decidir cuales pueden ser aplicables en cada caso. Dejo fuera (IRC y Data-informed decisions)

- Desarrollo 
    - Development servers
    - Code review
    - Correlation
- Pre-Producción / Testing 
    - Internal usage
    - Staged rollout
    - Advance countries
    - Shadow production
- Producción 
    - Frequent pushes
    - Soft launches
    - Dynamic configuration
    - Right hand side units
    - Double write/bulk migrate/double read

Sin duda algunas de las técnicas como Staged Rollout es discutible en que fase van y son clasificables bajo esta óptica. La idea de intentar clasificarlas es sólo para poder compararlas con una forma de trabajo que nos resulte más cercana para a partir de ahí ver cuales podemos empezar a aplicar y en que punto de nuestro proceso.

## Qué puedo aplicar y cómo si no soy Facebook

Más que técnicas concretas en realidad lo que Beck plantea es una cultura (o dos). El Desarrollo Ágil y el DevOp. Intentar aplicar alguna de sus estrategias de forma separada sin abrazar la filosofía subyacente creo que sólo produce desgaste. Con esto no quiero decir que tengas que hacer *pair programming* y tener un *devop* en tu equipo, pero sí al menos comprender que hay valor en los principio que proponen.

Para mi los pasos en ese camino son tres: Tests, Automatización y Monitorización.

**Monitorización**. Si no estás midiendo lo que sucede rendimiento, comportamiento de usuarios, … saber lo que está pasando o cuando un cambio no tiene el efecto previsto.

**Automatización**. Si hacer un despliegue es costoso e implica varios pasos, se harán pocos , se tardará más tiempo en tener feedback, se introducen más posibilidades de error y no hablemos de lo que supone revertir un mal cambio. Si no se automatizan los procesos se vuelve más complicado que todos los desarrolladores tengan el mismo entorno y este sea parecido a producción.

**Tests**. Probablemente la piedra angular. Estoy leyendo *Working Effectively with Legacy Code*, y en los primeros capítulos expone algunas cuestiones sobre tests que tienen relevancia para la «reversibilidad». En el libro comparan trabajar sin tests a hacer acrobacias sin red, y expone dos formas de introducir cambios en un sistema.

> Changes in a system can be made in two primary ways. I like to call them Edit and Pray and Cover and Modify. Unfortunately, Edit and Pray is pretty much the industry standard. When you use Edit and Pray, you carefully plan the changes you are going to make, you make sure that you understand the code you are going to modify, and then you start to make the changes. When you’re done, you run the system to see if the change was enabled, and then you poke around further to make sure that you didn’t break anything. The poking around is essential. When you make your changes, you are hoping and praying that you’ll get them right, and you take extra time when you are done to make sure that you did.  
> Superficially, Edit and Pray seems like “working with care,” a very professional thing to do. The “care” that you take is right there at the forefront, and you expend extra care when the changes are very invasive because much more can go wrong. But safety isn’t solely a function of care. I don’t think any of us would choose a surgeon who operated with a butter knife just because he worked with care. Effective software change, like effective surgery, really involves deeper skills. Working with care doesn’t do much for you if you don’t use the right tools and techniques.  
> Cover and Modify is a different way of making changes. The idea behind it is that it is possible to work with a safety net when we change software. The safety net we use isn’t something that we put underneath our tables to catch us if we fall out of our chairs. Instead, it’s kind of like a cloak that we put over code we are working on to make sure that bad changes don’t leak out and infect the rest of our software. Covering software means covering it with tests. When we have a good set of tests around a piece of code, we can make changes and find out very quickly whether the effects were good or bad. We still apply the same care, but with the feedback we get, we are able to make changes more carefully.

En esencia, durante el desarrollo tener tests te permite probar y si no funciona revertir a coste casi cero. En producción el coste de revertir no es cero (al menos sin aplicar otras de las técnicas mencionadas) pero al menos te permite detectar errores de forma temprana.