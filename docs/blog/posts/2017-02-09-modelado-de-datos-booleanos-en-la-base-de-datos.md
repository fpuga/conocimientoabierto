---
categories:
- Sin categoría
date: 2017-02-09
permalink: /modelado-de-datos-booleanos-en-la-base-de-datos/891/
slug: modelado-de-datos-booleanos-en-la-base-de-datos
tags:
- buenas prácticas
- desarrollo sofware
- modelo de datos
- postgresql
- recomendaciones
---

# Modelado de datos booleanos en la base de datos

Cuando definimos la información que un usuario puede visualizar o modificar a través de un formulario nos encontraremos datos aparentemente booleanos. Por ejemplo: ¿Hay un pozo en esta aldea?.

La primera aproximación para implementar esta información es poner un checkbox en el formulario y definir el campo como booleano en la base de datos.

`CREATE TABLE aldea (id serial, pozo boolean);`

Haciéndolo de este modo existen varios posibles problemas:

- A nivel usabilidad. Que pasa si el usuario no sabe si hay un pozo. Lógicamente dejará el checkbox sin marcar, pero cuando se revise esa información no se podrá saber si a conciencia se dejo en blanco indicando que no había pozo, o si se desconocía el dato.
- A nivel implementación. Por defecto, a no ser que la lógica implementada en cliente lo gestione de otra forma, en la base de datos almacenaremos un valor NULL y no un valor FALSE. Al tener valores nulos las queries que hagamos se pueden complicar, por ejemplo un *SELECT \* FROM aldea WHERE pozo IS FALSE;* no nos devolverá los valores nulos. Si empleamos la tabla para hacer un informe o exportarla a una hoja de cálculo tendremos que lidiar con los nulos, …

Por tanto cuando modelemos una información que parezca binaria, preguntémonos (y preguntemos al cliente) si es necesario distinguir entre falso, y desconocer el dato. Si estamos en la segunda situación debemos huír de usar checkboxes y emplear otro tipo de widget, como un combobox donde el usuario pueda escoger «Existe», «No existe» o dejar en blanco si no conoce el dato. A nivel implementación la información del combobox la guardaremos en general como un texto o un tipo enumerado. Y si eres un producto owner que usa algún tipo de documento para definir el modelo de datos a los desarrolladores asegurate siempre de especificar esta información.

Habrá situaciones en las que aún presentando al usuario la información mediante un combo, nos interese modelar el campo como un booleano. En este caso la lógica por encima de la base de datos sería la responsable de traducir el campo en blanco por un nulo, el ‘Existe’ por un true y el ‘No existe’ por un false.

Cuando modelemos un campo en la base de datos que sea verdaderamente binario para evitar confusiones deberíamos implementarlo de esta forma.

`<br></br>CREATE TABLE aldea (<br></br>id serial,<br></br>pozo boolean NOT NULL DEFAULT false<br></br>)<br></br>`

### Addendum

Cuando trabajamos con campos booleanos que admiten el valor nulo nos podemos encontrar un problema adicional al hacer migraciones de la base de datos. Imaginemos que tenemos un campo *contador* de tipo *boolean*, y que en la base de datos tenemos valores a *true*, *false* y *null*. Si a posteriori decidimos cambiar contador por un sistema de medida, con opciones como Contador, Manual, Volumétrico, … hacer la migración hacia adelante será sencillo.

`<br></br>UPDATE myschema.mytable SET sistema_medicion = 'Contador' WHERE contador IS true;<br></br>`

Pero el revert no sería tan sencillo, porque habremos perdido la información de nulos y false.