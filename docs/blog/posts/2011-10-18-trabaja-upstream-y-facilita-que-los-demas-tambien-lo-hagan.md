---
id: 394
title: 'Trabaja upstream y facilita que los demás también lo hagan'
date: '2011-10-18T18:01:10+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=394'
permalink: /trabaja-upstream-y-facilita-que-los-demas-tambien-lo-hagan/394/
categories:
    - General
tags:
    - 'desarrollo sofware'
    - 'software libre'
---

No os perdáis los artículos enlazados por[ Andrés sobre los costes de no trabajar upstream](http://nosolosoftware.com/los-costes-de-no-trabajar-upstream/trackback). En resumen:

La mayoría de desarrollos basados en software libre se mantienen en «local». Para satisfacer las necesidades de un cliente puede llegar un momento en que sea necesario parches una aplicación. Si estos parches no son integrados en la rama principal de un proyecto en la mayoría de las ocasiones nos veremos en la necesidad de actualizar nuestro código con el del repositorio principal. Bien porque hayan corregido errores que nuestro cliente reporta, porque queramos mantener nuestro código actualizado …

Cada vez que actualicemos nuestro código tendremos que comprobar que nuestros parches siguen correctamente integrados, independientemente del tamaño del proyecto esto acaba volviéndose un verdadero quebradero de cabeza. Tendremos que sacar nuestros propios ejecutables de la aplicación …  
Si nuestros parches se encuentran upstream son otros los que se encargan de todo este trabajo.

Trabajar upstream tampoco es gratis. Es probable que otros desarrolladores hagan comentarios a tu código y pidan otra aproximación, el mantenedor exigirá un formato de código determinado etc … Además la realidad es que los mantenedores serán menos propensos a incluir tus cambios cuanta menos participación tengas en el proyecto.

Se debe por tanto trabajar upstream. En general si. Si tu código difiere mucho es importante hacerlo porque te ahorrará horas de mantenimiento que compensarán el integrar tus parches.  
Si tus parches son pequeños a veces lleva más tiempo integrarlos que manterlos en local. Pero subirlos incrementará tu reputación en el proyecto de modo que cuando necesites integrar porciones más grandes de código o incluso ayuda para desarrollar alguna característica el resto de la comunidad estará predispuesto a ayudarte.

Integrar código en upstream es también una forma de decirle a tus (posibles) clientes, ey, yo puedo hacer eso que pedís y mantenerlo.