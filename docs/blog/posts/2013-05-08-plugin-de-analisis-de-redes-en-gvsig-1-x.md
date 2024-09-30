---
categories:
- Sin categoría
date: 2013-05-08
permalink: /plugin-de-analisis-de-redes-en-gvsig-1-x/559/
slug: plugin-de-analisis-de-redes-en-gvsig-1-x
tags:
- análisis de redes
- cartolab
- gis
- gvsig
- scolab
---

# Plugin de análisis de redes en gvSIG 1.x

Una pregunta habitual en las [listas de correo de gvSIG](http://www.gvsig.org/web/home/community/mailing-lists) es si hay alguna herramienta para realizar análisis de redes. En [Cartolab](http://cartolab.udc.es/) hemos estado buscando enlaces a algunos recursos del plugin llamado «*piloto de redes*» que es el más empleado para estos análisis para poder compartirlos.

El plugin de piloto de redes (a veces también se lo llama «*network extension*«, «*análisis de redes*» o «*extGraph*«) es mantenido por [Scolab](http://www.scolab.es/magnoliaPublic/Scolab-project/Proyectos-realizados/Soluciones-escritorio/Redes-gvSIG.html) y dispone de una [página web](https://joinup.ec.europa.eu/software/gvsig-network/home) en la forja de join-up, pero parece desactualizada.

## Instalación

La última versión de este plugin es compatible con la versión 1.12 de gvSIG, y se puede instalar desde el administrador de complementos.

> Herramientas -&gt; Administrador de complementos -&gt; Seleccionamos org.gvsig.graph y seguimos las instrucciones.

## Resumen de uso

1. Se carga una capa de líneas con los líneas conectadas, sin repetir y digitalizadas en el sentido de la circulación.
2. Si queremos un análisis mas acertado deberíamos como mínimo un atributo donde esté definido el coste y otro en el que esté definido el sentido. El **coste** representa cuanto cuesta recorrer ese tramo en las unidades que nosotros queramos, distancia, tiempo,… En el campo **sentido** Asignamos un valor al sentido que se puede seguir por esa línea (el de la digitalización, ambos sentidos, contrario a la digitalización)
3. A continuación vamos a *Red-&gt;calcular topología de red* que nos generará un fichero .net en el mismo direcotorio que la capa original con esa red. Aquí podemos decidir asignar cierta tolerancia a nuestra capa, por si los nodos no están perfectamente conectados,…
4. En la siguiente pantalla, emparejamos los campos que nos solicitan. No es necesario rellenarlos todos. Si escogemos sentido le diremos que valor corresponde a de cada sentido posible.
5. Cuando se carga la red nos preguntará por el campo que tiene un identificador para las geometrías, por ejemplo los nombres de las calles.
6. Con la red cargada tenemos las opciones de introducir paradas, barreras o realizar los análisis. Las **paradas** se pueden administrar desde *Red-&gt;Gestión de paradas*. Son puntos de inicio, fin o de paso intermedio obligatorio de un cálculo de rutas. También se comportan como puntos a partir del cual determinar el equipamiento más cercano,… Las **barreras** son puntos por los que se impide el paso.
7. Entre cálculo y cálculo recordar *Red -&gt; Borrar -&gt; «Eliminar lo que nos interese»*

## Videotutoriales

- Una [serie de cuatro vídeos](http://edugvsig.blogspot.com.es/p/redes.html) (unos 10, 15 minutos en total) con lo más básico del la extensión de redes para calcular rutas óptimas. Emplea la versión 1.1.2 de gvSIG pero permite ver lo más importante.
- [Vídeo de 6 minutos](https://www.youtube.com/watch?v=f95VhFYXMG0), demostrativo de varias de las funcionalidades de la extensión. . Cálculo de rutas. Matriz de distanticas y tiempos. Punto más cercano. Árbol de recubrimiento mínimo. Área de servicio. Está bien para de un vistazo saber todo lo que hace.

## Manuales

- [Versión html en la página de gvSIG](http://www.gvsig.org/web/projects/gvsig-desktop/docs/user/ext/redes/network-analisys-0-1-0/) de la versión 0.1.
- Una versión algo más antigua del manual pero [en formato pdf](https://joinup.ec.europa.eu/software/gvsig-network/document/gvsig_11-manualpilotoderedes-v2-espdf) se puede descargar desde la antigua página del proyecto en la forja join-up.

## Otros recursos

- [Vídeo](https://www.youtube.com/watch?v=ddtOBs8M-ao) de 5 minutos que demuestra como calcular la red y obtener una ruta óptima entre paradas.
- [Vídeo de 5 minutos](https://www.youtube.com/watch?v=qEqG3W8bSWs) para el cálculo de puntos más cercanos.
- [Proyecto del Google Summer Of Code](http://www.google-melange.com/gsoc/proposal/review/google/gsoc2012/davidpinheiro/1) para hacer un[ plugin sobre la extensión de redes para hacer cálculo vrp](https://code.google.com/p/vrp-for-gvsig-network-extension/).
- Hay otro plugin para realizar análisis de redes hecho como [proyecto fin de carrera](https://forxa.mancomun.org/projects/pfcmau/), para la versión 1.1. Parece algo desactualizado.
- En las 2 jornadas de latinoamérica y el caribe de gvSIG se hizo una presentación de la herramienta. [Buscar por la palabra «redes» en esta página](http://www.gvsig.org/web/community/events/jornadas-lac/2010/ponencias).