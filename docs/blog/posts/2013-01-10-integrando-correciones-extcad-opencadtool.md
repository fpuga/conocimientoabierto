---
id: 525
title: 'Integrando las correcciones de extCAD en OpenCADTools'
date: '2013-01-10T18:18:35+01:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=525'
permalink: /integrando-correciones-extcad-opencadtool/525/
categories:
    - 'Sin categoría'
tags:
    - cad
    - cartolab
    - gis
    - git
    - gvsig
    - opencadtools
---

He estado trabajando en integrar todas las correcciones que se hicieron en la extensión oficial de CAD para gvSIG, desde el nacimiento de [OpenCADTools](https://github.com/opencadtools/opencadtools) en las propias opencadtools. Este artículo describe:

- Como se realizó el proceso de integración para ver de donde pueden venir errores futuros y la *extraña apariencia* que tiene el repositorio actual.
- Contar el método seguido en sí por si resulta útil a gente que tenga que hacer algo parecido.

Debo agradecer al [Cartolab](http://cartolab.udc.es) el que me haya cedido horas de mi trabajo diario para poder escribir este artículo y realizar la integración en si misma. Además, debo agradecer a los organizadores del [codesprint de Münich](http://gvsigce.blogspot.de/2012/10/gvsig-ce-code-sprint-summary.html) por financiar mi estancia allí y a los participantes por las aportaciones recibidas.

## El problema

Tenemos tres repositorios svn con código parecido pero no igual:

- [gvSIG](http://www.gvsig.org/web/). Contiene entre otras muchas cosas el proyecto extCAD. Se trata del código base con commits desde 2005 hasta la actualidad
- [gisEIEL](http://webeiel.dicoruna.es/giseiel). A partir del año 2006 la Universidade da Coruña, a través de un convenio con la Diputación de A Coruña, realizó un fork de las herramientas de CAD de la versión 0.x de gvSIG. Este desarrollo fue asignado al Laboratorio de Bases de Datos de dicha universidad. En su repositorio actual sólo está el resultado final del fork, no los commits intermedios, porque lo que no se pueden comparar los logs para hacer una integración de código más ordenada.
- OpenCADTools. A partir de 2009, con financiación de la Diputación de Pontevedra y en el marco de los trabajos de desarollo de [gvSIG-EIEL](http://cartolab.udc.es/cartoweb/gvsig-eiel/) Cartolab hizo una integración del código de gisEIEL con el de gvSIG adaptando todo ello primero a la versión 1.1.2 de gvSIG y luego a la 1.9. Se dispone de todo el historial desde el principio hasta la actualidad. Posteriormente Cartolab continuo el desarrollo de las OpenCADTools como un proyecto propio.

Lo que queremos ahora es:

1. Obtener las mejoras realizadas en los tres proyectos desde que evolucionaron por separado para obtener una extensión de CAD mucho más potente. Nos concentraremos en el código de gvSIG y el de OpenCADTools por ser los que más desarrollo han tenido y estar ambos adaptados a la rama 1.9 de gvSIG, mientras que gisEIEL continua en versiones más antiguas. Emplearemos el proyecto de gisEIEL sólo para consultar dudas de autoría o Copyright.
2. Es fundamental respetar lo máximo posible la historia de commits. Debemos saber cuando se integró un cambio, por qué, y quien lo hizo. Esto nos permitirá prevenir errores futuros.
3. Es fundamental respetar lo máximo posible la autoría y el copyright de todas las modificaciones.
4. Nuestra meta final es además que el código resultante pueda ser integrado en el proyecto gvSIG, por tanto nuestra base debe ser el código de extCAD, y las mejoras de OpenCADTools deben poder ser introducidas en forma de parches sobre extCAD.

Para ello necesitamos poder comparar de forma sencilla estos tres repositorios. Dada la cantidad de commits que ha habido y la divergencia existente resulta muy complicado comparar los logs o encontrar un punto común. Haremos por tanto un análisis inicial clase a clase que nos permita ver el grueso de las diferencias y tomar decisiones.

## Análisis clase a clase

- Montamos un repositorio local de git que contenga en ramas separadas el código de cada proyecto.
- Obtenemos un fichero de texto *all\_files.txt* con todas los ficheros que hay (sin repetir) estén en una rama u otra. Haremos el listado de ficheros de cada rama mediante tree, y compararemos los ficheros con [meld](http://meldmerge.org/) para incluír rapidamente los ficheros que están en una y no en otra en el fichero all\_files.txt  
    `<br></br>git checkout heads/extcad<br></br>tree -fi --noreport > extcad_files.txt<br></br>git checkout heads/opencadtools<br></br>tree -fi --noreport > opencadtools_files.txt<br></br>cp opencadtools_files.txt all_files.txt`
- Hacemos un [script muy sencillo](https://github.com/fpuga/trangalladas/blob/master/scm_tools/getNoDiffsFiles.sh) que mete un carácter **=** antes de cada línea de un fichero *checked\_files.txt* para todos aquellos ficheros que no hayan variado.
- Sobre el fichero *checked\_files.txt* marcamos con una **x** aquellos ficheros que sabemos que no es necesario que comprobemos, por ejemplo el directorio install de OpenCADTools que con el nuevo sistema de paquetes de gvSIG está obsoleta. Algunos de estos ficheros serán eliminados a posteriori
- Los ficheros distintos los revisaremos uno a uno con algo como esto:  
    `<br></br>fileToCheck=./src/com/iver/cit/gvsig/CADExtension.java<br></br>git diff master:$fileToCheck refs/heads/opencadtools:$fileToCheck<br></br>`  
    La variable fileToCheck la rellenamos con un copy&amp;paste desde *checked\_files.txt*. Y vamos marcando en el fichero de *checked\_files.txt* con una **m** aquellos en las que la «versión más correcta» sea la del trunk de gvSIG. A veces el cambio es simplemente una cabecera, indentado, …

Este proceso aunque algo tedioso nos permite hacernos una imagen mental del estado de los repositorios lo que aumentará nuestra capacidad para tomar decisiones.

## Primera fase de la de integración

En el caso de OpenCADTools fue sencillo encontrar el punto en que se completo la migración de las herramientas desde la versión 1.1.2 de gvSIG a la 1.9. Perder el histórico de la migración no era grave y nos permitía simplificar el proceso, así que lo que se decidió fue escoger el commit en que esa migración se consideraba finalizaday volcar todo el repo de OpenCADTools en ese punto sobre el de extCAD.

`<br></br># En un repo con sólo OpenCADTools, hacemos<br></br>$ git checkout -b ultimoMigracion<br></br># 0f517d66 = commit de interés, del 14 de Septiembre con mensaje "Updated StartEditing from gvSIG 1.9"<br></br>$ git reset --hard 0f517d66<br></br># y sobre nuestro repo de trabajo:<br></br>cp -r $repoOpenCadTools .<br></br>`

A continuación vamos descartando todos los ficheros en los que sepamos que el contenido del master es más válido, los marcados como **m** en la fase anterior:

`git checkout -- los_ficheros_donde_prefiramos_el_master<br></br>`

Nuestros lectores más hábiles en el uso de git se habrán dado cuenta, de que podríamos hacer el análisis de los ficheros tipo **m** directamente en este paso, pero como ya comentamos, hacerlo del otro modo nos permite afianzar nuestro conocimiento de los repositorios.

## Segunda fase de la integración

Ahora tendremos en nuestro repo ficheros nuevos y ficheros modificados.

Los ficheros nuevos son todos ellos nuevas herramientas cuyas clases pueden ser agrupadas. Así que vamos comiteándolos aprovechando para revisar las cabeceras y las autorías. Resulta sencillo identificar si una de estas nuevas clases fue desarrollada inicialmente por el Laboratorio de Bases de Datos y adaptada con posterioridad por Cartolab, o fue creada directamente por Cartolab. Basta comprobar si existe o no en el repositorio de gisEIEL. En general los autores concretos de cada clase o quienes la adaptaron están también idendificados en el código fuente, cuando esto no es así lo que se ha hecho ha sido poner de forma genérica «Laboratorio de Bases de Datos» y/o «Cartolab». La autoría se ha reflejado mediante anotaciones @author en el código fuente de las clases

De este modo vamos haciendo commits para las herramientas y dado que es git empleamos la opción –author para reflejar quien hizo el commit original en el repo de OpenCADTools (al menos de forma aproximada)

Los ficheros modificados en este caso son pocos, por lo que permite tomar decisiones de forma individual.

## Tercera fase de la integración

Probablemete la fase más complicada. Nos toca integrar los 143 commits que hubo en OpenCADTools desde el que tomamos como referencia hasta el último commit previo a la integración.

Tras varias pruebas y sin encontrar una forma rápida y segura de integrar esos commits se optó por generar parches e ir integrándolos uno. En algunos casos hubo que retocar los parches o los ficheros a mano puesto que no se integraban correctamente.

## Cuarta fase de la integración

Toca limar algunas aspectos, por ejemplo:

- El nombre de los commiters, para lo que se emplea este [script](http://stackoverflow.com/a/392427/930271)
- Comprobar que podemos exportar lo que tenemos a un repositorio vacio de git ([pasos 7 a 9](http://www.mabishu.com/blog/2011/01/13/migrate-subversion-repository-to-git-without-loosing-data/))

Además se hace testeo funcional de las herramientas de CAD para encontrar posibles problemas en la integración y resolver los bugs que se deriven de ella.

## Conclusiones

Dada la disparidad de la evolución de los repositorios el proceso fue tedioso. Pero ahora tenemos un repositorio git actualizado a los últimos cambios de las herramientas por defecto de gvSIG y de las opencadtools. Esto nos permite trazar el origen de algunos bugs, y realizar integración de parches en ambos sentidos, así que merece la pena.