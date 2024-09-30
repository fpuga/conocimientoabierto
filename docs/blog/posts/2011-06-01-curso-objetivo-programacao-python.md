---
id: 328
title: 'Um curso objetivo de programação em Python'
date: '2011-06-01T09:04:09+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=325'
permalink: /curso-objetivo-programacao-python/328/
categories:
    - General
tags:
    - 'desarrollo sofware'
    - python
    - tutorial
---

Gracias al blog de [Anderson Medeiros](http://andersonmedeiros.wordpress.com/2010/06/13/curso-online-de-python/trackback/) encuentro un [interesante tutorial de python escrito en Portugués](http://www.async.com.br/projects/python/pnp/node20.html) pero muy facilito de seguir.

Es un tutorial de introducción, rápido de leer y que me ha ayudado a recordar algunos de esos conceptos que por estar más habituado a otros lenguajes tipo Java no empleas a menudo.

Algunas cosillas que he recordado, aprendido o me han gustado.

### Listas, tupas y strings

Explica bien que son [listas, tuplas, diccionarios y strings](http://www.async.com.br/projects/python/pnp/node13.html). A listas y tuplas se las llama en ocasiones secuencias puesto que sus propiedades son muy parecidas. Una tupla es en realidad una lista inmutable.

Conviene tener en la cabeza lo fácil que es hacer slices (subconjuntos de secuencias) y substrings en python, incluso empleando índices negativos para empezar a contar por el final. LLega con escribir:  
`<br></br>>>> lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']<br></br>>>> lista[2:5]<br></br>['c', 'd', 'e']<br></br>>>>  lista[2:]<br></br>['c', 'd', 'e', 'f', 'g']<br></br>>>> lista[:5]<br></br>['a', 'b', 'c', 'd', 'e']<br></br>>>> lista[:-2]<br></br>['a', 'b', 'c', 'd', 'e']<br></br>>>> lista[-2:]<br></br>['f', 'g']<br></br>`

Los operadores \* y + se pueden usar sobre listas, tuplas y strings. \* replica n veces el elemento y + concatena.

Ejemplo para strings:  
`<br></br>>>> a = "exato"<br></br>>>> print a * 2<br></br>exatoexato<br></br>>>> print "quase " + a<br></br>quase exato<br></br>`  
Ejemplo para listas:  
`<br></br>>>> a = [-1, 0]<br></br>>>> b = [1, 2, 3]<br></br>>>> print b * 3<br></br>[1, 2, 3, 1, 2, 3, 1, 2, 3]<br></br>>>> print a + b<br></br>[-1, 0, 1, 2, 3]<br></br>`

Para chequear si un elemento está contenido en una secuencia o diccionario se usa el operador in  
`<br></br>>>> "x" in "cha"<br></br>False<br></br>>>> 1 in [1,2,3]<br></br>True<br></br>`

### Combinar de forma implícita operaciones lógicas

Además de los operadores lógicos not, or, and python permite [combinar ciertas operaciones lógicas de forma implícita](http://www.async.com.br/projects/python/pnp/op-logical.html#SECTION000345100000000000000):

Por ejemplo podemos comprobar un número está en un determinado rango de esta forma:  
`<br></br>a = 5<br></br>if 3 < a < 9:<br></br>     print "Entre 3 y 9"`

a = 3; b = 3; c = 2;  
if a == b &lt;= c:  
 print "a igual a b y b menor o igual que c"

### Clausula else en bloques for y while

En los for y los while [se puede emplear una claúsula else](http://www.async.com.br/projects/python/pnp/node28.html#SECTION000352200000000000000) que se ejecutará cuando se salga del bloque de iteración por haber acabado la secuencia (en lugar de salir por un break)  
`<br></br>valores = [2, 4, 5, 2, -1]<br></br>for i in valores:<br></br>        if i < 0:<br></br>                print "Negativo encontrado: %d" %i<br></br>                break<br></br>else:<br></br>        print "Nenhum negativo encontrado"<br></br>`

### Valores booleanos

No está de más recordar que [en python se considera falso](http://www.async.com.br/projects/python/pnp/node29.html#SECTION000353100000000000000) a:

- el booleano False
- el valor 0 (zero)
- una lista, diccionario, tupla o string vacios (de tamaño cero)
- el valor especial None

Así por ejemplo para comprobar si una lista no está vacía mejor que emplear  
`<br></br>lista = ['a']<br></br>if (len(lista)) != 0:<br></br>      print "forma poco apropiada de comprobar si una lista no está vacia"<br></br>`  
usaremos directamente  
`<br></br>if lista:<br></br>      print "Lista no vacia"<br></br>`

### Argumentos de funciones

Existen [dos formas de pasar un número variable de argumentos a una función](http://www.async.com.br/projects/python/pnp/node33.html#SECTION000362300000000000000):  
`<br></br>def desculpa(alvo, *motivos):<br></br>        d = "Desculpas %s, mas estou doente" % alvo<br></br>        for motivo in motivos:<br></br>            d = d + " e %s" % motivo<br></br>        return d + "."`

 &gt;&gt;&gt; desculpa("senhor", "meu gato fugiu",  
 ... "minha tia veio visitar")  
  
o bien  
`<br></br> def equipe(diretor, produtor, **atores):<br></br>        for personagem in atores.keys():<br></br>            print "%s: %s" % (personagem, atores[personagem])<br></br>        print "-" * 20<br></br>        print "Diretor:  %s" % diretor<br></br>        print "Produtor: %s" % produtor`

 &gt;&gt;&gt; equipe(diretor="Paul Anderson",  
 ... produtor="Paul Anderson",  
 ... Frank="Tom Cruise", Edmund="Pat Healy",  
 ... Linda="Julianne Moore")

 Frank: Tom Cruise  
 Edmund: Pat Healy  
 Linda: Julianne Moore  
\--------------------  
 Diretor: Paul Anderson  
 Produtor: Paul Anderson

Si tienes algún tutoirial de python que te haya gustado o algún truquillo que quieres compartir deja un comentario.