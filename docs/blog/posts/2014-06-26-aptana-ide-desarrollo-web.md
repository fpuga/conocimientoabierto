---
id: 719
title: 'Aptana. Un IDE para desarrollo web'
date: '2014-06-26T21:14:57+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=719'
permalink: /aptana-ide-desarrollo-web/719/
categories:
    - 'Sin categoría'
tags:
    - 'desarrollo sofware'
    - 'desarrollo web'
    - 'Escoger IDE web'
    - IDE
---

Hace unos meses escribía en el blog que estaba [buscando un IDE para desarrollo web el cliente](http://conocimientoabierto.es/ide-desarrollo-web-cliente/604/). Al final no me he dedicado tanto a web-cliente como pensaba y he estado jugando más en la parte de backend sobre todo con nodejs.

Dado que es el primer IDE (para web) que pruebo y tampoco tengo gran experiencia en desarrollo web me resulta difícil hacer una buena revisión, pero aquí van algunos pros y contras de programar Javascript en [Aptana](http://aptana.com/) desde el punto de vista de alguien que viene de Java+Eclipse.

## Contras

\* El debugger de Apata es [incompatible con la última versión de firebug](< http://stackoverflow.com/questions/11532388/socket-connection-error-when-debugging-php-js-on-aptana-3>) por lo que debes instalar una más antigua. Tuve unos cuantos problemas intentando instalarlo y no he sido capaz de hacer un cambio en el código y recargar la página sin tener que relanzar todo firefox a través del debugger. En resumen el debugger no he sido capaz de hacerlo funcionar de una forma cómoda y he vuelto a firebug.  
\* El preview de la página cuando está puesto el código del google analytics hace que se cierre aptana.  
\* Para que el [Code Assist](https://wiki.appcelerator.org/display/guides2/About+Content+Assist) funcione correctamente, hay que tener unos ficheros de documentación en un formato especial (ScriptDoc), y practicamente ninguna librería los tiene.  
\* En el «Save Action» sólo se pueden quitar los trailing spaces, estaría bien que permitiera al menos reformatear el código  
\* No es capaz de navegar por ocurrencias correctamente. Si marco una variable no soy capaz de moverme entre las apariciones de esa variable (Ctrl + .) como en java. Tampoco es capaz de encontrar desde donde se llama a una función (aunque este es un problema genérico de los lenguajes dinámicos). Aquí hay un [listado de funcionalidades](https://wiki.appcelerator.org/display/tis/Editor+Feature+Matrix) aunque no está del todo actualizado. No he probado a documentar las funciones con ScriptDoc, tal vez así el editor sea más inteligente.  
\* La documentación es escasa  
\* Así como cuando programo en Java todo el equipo usa Eclipse, con web no pasa lo mismo. Así que la idea de tener que crear workspaces y proyectos dentro del workspace llenos de directorios de configuración ocultos me resulta conceptualmente incómodo.

## Pros

\* Me gusta la consola interactiva. Puedo probar código sin tener que abrir la consola javascript del navegador.  
\* Me gusta el Content Assist de html, creo que funciona bastante bien.  
\* Al margen del problema con el debugger, me gusta la funcionalidad de preview ( https://wiki.appcelerator.org/display/tis/Side-by-Side+Previewing ). Me permite poner en dos pestañas paralelas mi código (html, css, js) y el navegador empotrado de aptana, al salvar uno de los ficheros la previsualización se recarga automáticamente. Está bien para ir viendo como queda. Una pena que no haya encontrado forma de debuguear desde el preview.  
\* Me gusta el «Go To Declaration (F3)», aunque se equivoca de vez en cuando, si por ejemplo has estado haciendo pruebas en otro fichero, poniéndolo a las funciones el mismo nombre puede saltar a la que no es.  
\* Me gusta la buena integración (heredada de eclipse) con el escritorio. Poder copiar un fichero en el explorador de archivos y pegarlo en una vista de aptana, o copiar un snippet de código de una página web y pegarlo en Aptana creando automáticamente un nuevo fichero  
\* El sistema de [templates](https://wiki.appcelerator.org/display/guides2/Templates) para no arrancar proyectos como una página en blanco funciona bien.  
\* Es relativamente fácil, extender la funcionalidad a través de [Snippets y ](https://wiki.appcelerator.org/display/guides2/Snippets)[Rubles](https://wiki.appcelerator.org/display/tis/Rubles). Aunque los Rubles hay que escribirlos en Ruby

## Enlaces de interés sobre aptana

\* Una [revisión genérica de Aptana](< http://www.htmlgoodies.com/beyond/webmaster/toolbox/review-of-aptana-studio-3.html#fbid=dy5qeBG2S9b>).  
\* Documentación sobre [html](https://wiki.appcelerator.org/display/guides2/HTML+Development), [css](https://wiki.appcelerator.org/display/guides2/CSS+Development), y [javascript](https://wiki.appcelerator.org/display/tis/JavaScript+Development)

## Conclusiones

Me da la impresión de que la mayoría de opiniones favorables vienen de gente que lo uso en su día cuando no había opciones libres/gratuitas mejores. Además da la impresión de que el proyecto está muerto desde que lo compró Appcelerator.

Creo que el caso de uso más favorable para Aptana es que ya estés usando el IDE en el backend (ruby, php, python) y sólo toques ocasionalmente el cliente por lo que no te merece cambiar de entorno.