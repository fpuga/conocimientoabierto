---
categories:
- Sin categoría
date: 2012-02-04
permalink: /si-el-liferea-tarda-mucho-en-arrancar/451/
slug: si-el-liferea-tarda-mucho-en-arrancar
tags:
- liferea
- receta
- rss
- sistema operativo
---

# Si el liferea tarda mucho en arrancar&#8230;

`<br></br>$ eatmydata liferea<br></br>`  
[Liferea](http://liferea.sourceforge.net/) es un lector de feeds (como google reader, pero en aplicación de escritorio) libre que cumple su cometido. La verdad es que no me parece la *aplicación definitiva* para leer rss pero funciona.

Eso si, tiene [un error enormemente molesto](https://bugs.launchpad.net/ubuntu/+source/liferea/+bug/290666) y es lo lento que es cuando arranca, sincroniza feeds o marcas toda una carpeta como leída.

Simplificando un poco, lo que está pasando es que el objetivo principal de los sistemas de ficheros modernos es evitar la pérdida accidental de información, de modo que se sacrifica rendimiento (y la duración del disco duro) ante problemas hipotéticos como el de que se vaya la corriente y el ordenador se apague de manera brusca. Por defecto, sqlite, que es la base de datos que emplea Liferea, pide muy a menudo al sistema operativo que se asegure de que la información que gestiona el programa está guardada en el disco duro. Es decir, cuando un programa quiere guardar algo en el disco duro, pide al sistema operativo que lo guarde, pero esto no tiene porque suceder de manera inmediata (se dice que la escritura es asíncrona). El sistema operativo puede mantenerlo en la RAM hasta que considera que es el momento idóneo de escribirlo en disco. Pero las aplicaciones también tienen la opción de forzar al sistema operativo a que los datos sean escritos (sincronizar), y está opción de forzar es lo que usa liferea tan a menudo.

Como este problema no es exclusivo de liferea si no que sucede en muchas aplicaciones, un desarrollador de debian, ha escrito un programa llamado [eatmydata](http://www.makelinux.net/man/1/E/eatmydata) que permite desactivar las funciones de sincronización del sistema operativo para aquellos programas que nos interesen. De modo que si un programa ejecutado bajo el paraguas de eatmydata pide forzar el sincronizado, no sucederá nada, esa orden será ignorada. En general esto no es peligroso, pero hay que tener cuidado de cuando se usa y no hacerlo nunca con aplicaciones críticas. Con liferea haciendo copias de seguridad de vez en cuando no hay problema. Para instalar eatmydata llega con:  
`<br></br>sudo apt-get install eatmydata<br></br>`  
y para ejecutar un programa bajo eatmydata  
`<br></br>eatmydata nombre_del_programa<br></br>`