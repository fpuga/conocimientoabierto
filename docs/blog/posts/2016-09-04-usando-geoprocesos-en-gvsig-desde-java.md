---
categories:
- Sin categoría
date: 2016-09-04
permalink: /usando-geoprocesos-en-gvsig-desde-java/878/
slug: usando-geoprocesos-en-gvsig-desde-java
tags:
- como
- desarrollo sofware
- geoprocesos
- gis
- gvsig
- how to
- java
- receta
- tutorial
---

# Usando GeoProcesos en gvSIG desde Java

La semana pasada había [un correo en la lista de desarrollo de gvSIG](https://listserv.gva.es/pipermail/gvsig_desarrolladores/2016-August/007975.html) preguntando como poder lanzar geoprocesos desde tu propio plugin mediante Java. Tras una pequeña investigación he escrito [un código de ejemplo](https://github.com/fpuga/trangalladas/blob/master/gvSIG/GeoProcessExampleExtension.java) que espero que sea útil a quien tenga esta necesidad.

## Descargar el código

A mi particularme me gusta descargar el código fuente de las partes de gvSIG con las que voy a trabajar. Esto simplifica el usar las herramientas del IDE para saber como usarlo, encontrar errores, y revisar los tests, en caso de haberlos, para tener pistas de como escribir mi propio código.

Para ello primero se mira la versión del plugin que se corresponda con la versión de gvSIG que estás usando. Creo que lo más fácil es descargar una versión portable de gvSIG. Entrar a la carpeta que contiene el plugin, en este caso *org.gvsig.geoprocess.app.mainplugin* y abrir el fichero *package.info*. En la property **version** está el tag del repo correspondiente a esa versión. Por ejemplo para la 2.3RC2 sería el 2.266. Por tanto para descargar el repo haremos:

`<br></br>svn checkout http://devel.gvsig.org/svn/gvsig-geoprocess/org.gvsig.geoprocess/tags/org.gvsig.geoprocess-2.2.66/<br></br>`

A continuación,e n caso de usar Eclipse, iremos a import -&gt; Existing maven projects, e importaremos la raíz del nuevo plugin descargado.

## Añadir las dependencias

Al desarrollar en gvSIG debemos tener en cuenta que las dependencias de nuestro plugin, por decirlo de algún modo, serán de dos tipos. En «Tiempo de desarrollo», y en «Tiempo de ejecución». Las dependencias en desarrollo se definen en el pom del proyecto permitiéndonos definir el classpath de desarrollo para trabajar con las clases que nos hagan falta.

En ejecución, cuando estamos probando o ejecutando gvSIG, el classpath se define de manera dinámica por decirlo de algún modo en el fichero de *config.xml*. gvSIG buscará entre las dependencias que hayamos definido en el config las clases que se pueden usar en nuestro plugin.

Para que quede claro, a nuestro pom se añadirán otros proyectos maven. A nuestro config se añadirán plugins de gvSIG.

Por ejemplo para el caso de usar los geoprocesos, añadiremos al pom:

`<br></br><dependency><br></br>	<groupid>org.gvsig</groupid><br></br>	<artifactid>org.gvsig.geoprocess.lib.api</artifactid><br></br>	<version>2.2.66</version><br></br></dependency>`

<dependency>  
 <groupid>org.gvsig</groupid>  
 <artifactid>org.gvsig.geoprocess.lib.sextante</artifactid>  
 <version>2.2.66</version>  
</dependency>

y al config

`<br></br><depends plugin-name="org.gvsig.geoprocess.app.sextante"></depends><br></br>`

## Obtener el algoritmo que queremos

**Esta una de las partes en las que tengo más dudas que esté correcta.**

En general accederemos a las funcionalidades de gvSIG a través de un Locator que nos dará un Manager que nos dará la funcionalidad. En el caso de los geoprocesos sería:

`<br></br>String ALG_NAME = "gvSIG-intersection";<br></br>SextanteGeoProcessManager manager = (SextanteGeoProcessManager) GeoProcessLocator.getGeoProcessManager();<br></br>HashMap<string geoalgorithm=""> algs = manager.getAlgorithms();<br></br>GeoAlgorithm alg = algs.get(ALG_NAME);<br></br></string>`

Debemos castear a la implementación por defecto del manager *SextanteGeoProcessManager* porque la interfaz en sí no proporciona el método *getAlgorithms*. Esto diría que es un bug.

La forma de obtener ALG\_NAME, no estoy seguro de cual es. En principio lo más fácil sería poner un breakpoint y mirar los valores de *algs*. Aunque en mi caso sólo salen los propios de gvSIG y no los de Sextante.

## Seteando valores al algoritmo

Todos los algoritmos definen un método *defineCharacteristics* que nos indican los valores que recibe, tanto de entrada como de salida. Esta definición de valores se obtiene a través del método *getParameters*

En nuestro código debemos obtener cada uno de los parámetros necesarios y setear su valor real para nuestro caso. Por ejemplo:

`<br></br>private void setParams(GeoAlgorithm alg) throws WrongParameterIDException {<br></br>	ParametersSet params = alg.getParameters();`

 FLyrVect interLyr = getLayer("inter");  
 FlyrVectIVectorLayer inter = new FlyrVectIVectorLayer();  
 inter.create(interLyr);

 FLyrVect layerLyr = getLayer("layer");  
 FlyrVectIVectorLayer layer = new FlyrVectIVectorLayer();  
 layer.create(layerLyr);

 params.getParameter(IntersectionAlgorithm.INTER).setParameterValue(  
 inter);  
 params.getParameter(IntersectionAlgorithm.LAYER).setParameterValue(  
 layer);  
 params.getParameter(IntersectionAlgorithm.SELECTGEOM\_INPUT)  
 .setParameterValue(false);  
 params.getParameter(IntersectionAlgorithm.SELECTGEOM\_OVERLAY)  
 .setParameterValue(false);  
}  
  
En este caso para no escribir a mano los idenfificadores de los parámetros uso las variables estáticas definidas en el propio algoritmo. Eso hace que haya que añadir al pom el algortimo:

`<br></br><dependency><br></br>	<groupid>org.gvsig</groupid><br></br>	<artifactid>org.gvsig.geoprocess.algorithm.intersection</artifactid><br></br>	<version>2.2.66</version><br></br></dependency><br></br>`

Para las capas de entrada al algoritmo hay que generar una *FlyrVectIVectorLayer*. Como se muestra en el código de ejemplo lo más sencillo es obtener un *FLyrVect* y construirla con el create.

## Ejecutando el algoritmo

Los algoritmos se lanzan mediante el método *execute* que como indica la documentación admite hasta tres parámetros.

- ITaskMonitor task. Que puede ser nulo y permite monitorizar el estado para por ejemplo poner una barra de progreso al usuario
- HashMap<string string=""> outputMap. Que permite modificar los nombres que sextante asigna a los parámetros de salida (en general capas)</string>
- OutputFactory outputFactory. Define como se crearán los objetos de salida. Puede ser nuestra propia implementación o usar la factoría por defecto

Por tanto ejecutarlo sería simplemente:

`<br></br>alg.execute(null, new DefaultOutputFactory(), null);<br></br>`

## Obteniendo los resultados

Con la factoría por defecto las capas se crean en un directorio temporal que en linux es */tmp/tmp-andami* y les asigna nombres aleatorios (creo que basados en el timestamp). Supongo que habrá alguna utilidad que nos permite ejecutar una especie de FinalActions para añdirlos automáticamente a la vista. O implementando nuestra propia *OutputFactory* podríamos definir otras rutas. También diría que podemos prescindir del *OutputFactory* y lanzar el algoritmo mediante *processAlgorithm* si igual que hicimos con los parámetros de entrada seteamos adecuadamente los valores de salida, especialmente el *OutputChannel* de las capas.

En todo caso el método *getOutputObjects* nos devuelve los objetos de salida, así por ejemplo podríamos llegar el *FlyrVectIVectorLayer* de la capa de polígonos de salida con:

`<br></br>OutputObjectsSet outputSet = alg.getOutputObjects();<br></br>OutPut output = outputSet.getOutPut(IntersectionAlgorithm.RESULT_POL)<br></br>FlyrVectIVectorLayer result_pol = (FlyrVectIVectorLayer) output.getOutputObject();<br></br>`