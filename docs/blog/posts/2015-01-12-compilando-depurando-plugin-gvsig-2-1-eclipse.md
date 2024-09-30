---
categories:
- Sin categoría
date: 2015-01-12
permalink: /compilando-depurando-plugin-gvsig-2-1-eclipse/745/
slug: compilando-depurando-plugin-gvsig-2-1-eclipse
tags:
- como
- desarrollo sofware
- eclipse
- gvsig
- how to
- programación
- receta
- tutorial
---

# Compilando y depurando un plugin de ejemplo para gvSIG 2.1 desde Eclipse

Joaquín del Cerro ha publicado un artículo explicando [como compilar y depurar un plugin de ejemplo para gvSIG 2.1 con NeatBeans](http://blog.gvsig.org/2014/12/29/compilando-y-depurando-un-plugin-de-ejemplo-para-gvsig-2-1-0-desde-un-ide-netbeans/). He adaptado sus instrucciones para Eclipse que es mi IDE habitual. Este artículo no es tan detallado como el suyo así que seguramente tendrás que consultar los dos, especialmente los pasos previos que comenta Joaquín para que todo funcione.

Una vez que tenemos los «previos» realizados, creamos un nuevo workspace en eclipse, por ejemplo *workspace-gvsig-landregistry*.

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_1](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_1.png-nggid0225-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_1") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_1.png) </div>Nos aseguramos de que tenemos instalados en eclipse:

- [Subversive como plugin de SVN](http://www.gvsig.org/plone/projects/gvsig-desktop/docs/devel/gvsig-devel-guide/2-1-0/trabajar-con-el-nucleo-de-gvsig/compile_gvsig/configurar-el-cliente-de-svn)
- [El plugin de maven para eclipse](http://www.gvsig.org/plone/projects/gvsig-desktop/docs/devel/gvsig-devel-guide/2-1-0/trabajar-con-el-nucleo-de-gvsig/compile_gvsig/instalar-el-plugin-de-maven-para-eclipse-m2e) y el conector de maven con subversive. Si no tenemos el conector instalado, más adelante cuando descarguemos el plugin del repositorio nos debería dar la opción de instalarlo

Abrimos la perspectiva de eclipse de *SVN Repository Exploring*, desde *Window -&gt; Open perspective -&gt; Other*, o cualquier otro de los sitios desde los que se puede abrir.

Y añadimos el repositorio del plugin desde *File -&gt; New -&gt; Repository Location* o el icono correspondiente. Como URL usaremos:  
`<br></br>http://devel.gvsig.org/svn/gvsig-plugintemplates/org.gvsig.landregistryviewer/trunk/org.gvsig.landregistryviewer/<br></br>`

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_2](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_2.png-nggid0226-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_2") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_2.png) </div>Seleccionamos el repositorio que acabamos de añadir y en el menú contextual escogemos *Check out as maven project*

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_3](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_3.png-nggid0227-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_3") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_3.png) </div>Si no tenemos el conector de maven-svn instalado, nos pedirá instalarlo. En la ventana previa al checkout nos aseguraremos de que la opción «All projects» está activada

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_4](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_4.png-nggid0228-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_4") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_4.png) </div>Puede tardar un ratito en descargar, sobre todo si tiene que descargar muchas dependencias. Cuando acabe, pasamos a la perspectiva Java y ya tendremos los proyectos correspondientes al plugin configurados en el workspace.

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_5](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_5.png-nggid0229-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_5") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_5.png) </div>Si no tienes la opción de *Build automatically* activada, haz un *build all*. A continuación pon un punto de ruptura para comprobar que todo funciona correctamente en el punto que indica Joaquín (método createWindow de la clase LandRegistryViewerExtension).

Tras lanzar gvSIG en modo debug,

`<br></br>./gvSIG --debug --pause<br></br>`

configuramos el debugger. En *Debug Configurations*, añadiremos una nueva configuración del tipo *Remote Java Application*

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_6](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_6.png-nggid0231-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_6") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_6.png) </div>En name pondremos lo que queramos, por ejemplo *org.gvsig.landregistryviewer.app*, en project *org.gvsig.landregistryviewer.app.mainplugin* y en port *8765*. Si antes de crear la configuración de debug seleccionamos el proyecto *org.gvsig.landregistryviewer.app.mainplugin* en el package explorer nos rellenará automáticamente name y project.

<div class="ngg-gallery-singlepic-image ngg-center" style=""> [ ![compile_plugin_gvsig21_7](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/cache/compile_plugin_gvsig21_7.png-nggid0230-ngg0dyn-0x0x100-00f0w010c010r110f110r010t010.png "compile_plugin_gvsig21_7") ](https://conocimientoabierto.es/wp-content/blogs.dir/16/files/compile_plugin_gvsig_21/compile_plugin_gvsig21_7.png) </div>Al darle a debug debería abrirse gvSIG y pararse la ejecución en el punto que hemos marcado.