---
categories:
  - General
date: 2011-09-02
permalink: /como-carga-gvsig-las-extensiones/385/
slug: como-carga-gvsig-las-extensiones
tags:
  - cartolab
  - como
  - desarrollo sofware
  - gvsig
---

# Como carga gvSIG las extensiones

En la línea abierta por [Andrés de «Como gvSIG hace xxx»](http://nosolosoftware.com/how-gvsig-manages-the-snappers/) os presento un artículo que explica como se gestiona la carga de las extensiones en gvSIG. Antes de nada debo agradecer a [Cartolab](http://cartolab.udc.es/) cederme tiempo para poder escribirlo.

Lo que sucede cuando lanzamos gvSIG es que la máquina virtual de java ejecuta el método main() de [la clase Launcher de andami](http://forge.osor.eu/plugins/scmsvn/viewcvs.php/*checkout*/trunk/frameworks/_fwAndami/src/com/iver/andami/Launcher.java?content-type=text%2Fplain&root=gvsig-desktop), el framework que sostiene el sistema de ventanas y plugins de gvSIG.

A efectos de este artículo sobre la carga de extensiones podemos decir que ese método main() es el responsable de lo siguiente:

1. Procesar los parámetros que se le pasan por línea de comandos
2. Cargar los plugins
3. Cargar las clases de los plugins
4. Recuperar la configuración persistida de los plugins
5. Inicializar las extensiones
6. Cargar menus y toolbars
7. Hacer la postinicialización de las extensiones

### 1.- Procesar los parámetros que se le pasan por línea de comandos

Lo más habitual es que la orden que ejecute el sistema operativo (quitando los parametros que se pasan a la jvm) sea algo parecido a:

$ java com.iver.andami.Launcher **gvSIG gvSIG/extensiones «$@»**

donde la parte en negrita serían los parámetros que pasamos al main(). En concreto ese segundo parámetro gvSIG/extensiones es el que está definiendo donde está la carpeta de plugins de gvSIG, como ruta relativa desde donde se encuentra el fichero andami.jar.

Es decir, que si bien el directorio de extensiones suele estar en un punto predefinido nosotros podriamos escoger otra ubicación.

### 2.- Carga de los plugins

Procesados los parámetros de entrada la aplicación recorre todos los directorios contenidos en la carpeta de plugins. Si dentro del directorio existe un fichero de nombre _«config.xml»_ lo parsea y en caso de ser correcto añade el par \[«nombre del directorio», objeto PluginConfig\] al campo de la clase _Launcher_

`<br></br>private static HashMap pluginsConfig = new HashMap();<br></br>`  
Donde _PluginConfig_ es una clase que se encarga de mantener toda la información que aportan los ficheros _config.xml_.

Lo más interesante de esta fase es entender que el orden en que se recorren los directorios, y por tanto el orden en que luego se inicializarán las extensiones, es aleatorio, o en realidad es el orden que devuelve el método [lisFiles() de la clase File de Java](<http://download.oracle.com/javase/1.4.2/docs/api/java/io/File.html#listFiles()>), que especifica en su documentación que el orden en se devuelven los ficheros no está asegurado y supongo, dependerá de la implementación concreta de la máquina virtual y del sistema operativo que se emplee.

Hay que aclarar que en este contexto, un plugin, es igual a un directorio contenido dentro del directorio de extensiones/plugins definido como parámetro.

### 3.- Carga de las clases de los plugins

Lo siguiente que intenta hacer es indexar todas las clases de todos los plugins. Para ello recorre _pluginsConfig_, solicitando el valor de la etiqueta del config &lt;libraries library-dir=»VALOR» /&gt;. Lo más habitual es que ese VALOR sea _«./»_, es decir el propio directorio del plugin. Para cada plugin mantiene un objeto _PluginClassLoader_ que basicamente contiene un índice de todos ficheros .class que están dentro de los ficheros .zip o .jar que están en ese _library-dir_.

Para cada plugin se crea un objeto _PluginServices_ que a su vez mantiene la instancia del _PluginClassLoader_ que le corresponde. Esos _PluginServices_ se almacenan en el campo  
`<br></br>private static HashMap pluginsServices= new HashMap();<br></br>`  
de la clase _Launcher_.

Hay que tener en cuenta que a la hora de cargar las clases de un plugin, si en el config se ha definido que depende de otro mediante una etiquetacarga la clases de la dependencia (de forma recursiva) antes que el nuestro. Por tanto, en _pluginsServices_ los plugins se reordenan respecto a _pluginsConfig_ poniendo los plugins de los que se depende antes. Se mantiene también una variable _pluginsOrdered_ con el nombre de los plugins en el mismo orden que _pluginsServices_

### 4.- Persistencia de los plugins

Se actualiza el andamiConfig que contiene una lista (el fichero andami-config.xml habitualmente) que persiste con todos los plugins presentes el directorio de plugins.

Luego se recupera de disco la configuración persistida de los plugins en el fichero plugins-persistance.xml, y se _setea_ esa configuración en el PluginServices asociado a cada plugin.

### 5.- Inicialización de las Extensiones

Es en esta fase cuando salen por consola los mensajes de:

> Initializing extensions from «Nombre_del_plugin» (para cada plugin)

y

> Initializing «Nombre_de_la_Extension» … (para cada extensión)

Se recorre _pluginsOrdered_, y para cada plugin se crea una instancia de cada extensión (en el orden que se define en el config del plugin) y se llama a su método _initialize()_. Además se almacena esas instancia en el campo de _Launcher_:  
`<br></br>private static ArrayList extensions=new ArrayList();<br></br>`  
Por el medio crea también un objeto _ExtensionDecorator_ que nos da un control adicional sobre las extensiones pero esto no nos interesa a los efectos de este artículo.

### 6.- Menus y Toolbars

Se cargarn los menus y los toolbars definidos por los plugins a través de los métodos _installPluginsMenus()_ y _installPluginsControls()_.

### 7.- Post-inicialización de las extensiones

Se va llamando al método postInitialize de cada extensión en el orden en que aparecen en el array extensions. Con este paso finalizaría el proceso de carga.

Una cosa que no he investigado a fondo pero que intuyo que es así, es que en algún momento de este proceso se asocian las instancias del array _extensions_ a los menús y botones del toolbar. De este modo las extensiones (clases que heredan de extension y aparecen en los config) se comportan como una especie de singleton, porque gvSIG siempre la recupera de ese array de extensiones, y cuando el desarrollador externo llama a _PluginServices.getExtension(Class)_ la está recuperando de ahí también (del _ExtensionDecorator_ del que hablamos antes en realidad, pero la idea es la misma)

Esto explica también porque cuando recompilamos nuestro código, si cambiamos algo en la clase de la extensión debemos cerrar y abrir gvSIG. La instancia de la extensión se crea durante la carga de gvSIG y se mantiene hasta que cerramos gvSIG, y por tanto no es «recargada» de los nuevos .class

Me quedan un par de dudas que quedan para estudiar para próximos posts o para quien se anime a escribir más artículos de la serie de «Como hace gvSIG XXX»:

- Al parecer existe una extension del tipo ExclusiveUIExtension a la que se hace referencia en Launcher.initializeExclusiveUIExtension() que no tengo muy claro como funciona
- Estaría bien explicar en detalle el comportamiento de los ExtensionDecorator
- Estaría bien explicar detalladamente el proceso de creación y ubicación de los menús y toolbars
- Algunas partes del código son un poco liosas. Tengo algunas ideas de como refactorizarlo así que si alguien se anima que pregunte
