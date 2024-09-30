---
categories:
- Sin categoría
date: 2016-08-07
permalink: /si-el-disco-duro-no-para-al-arrancar-ubuntu-vacia-la-papelera/874/
slug: si-el-disco-duro-no-para-al-arrancar-ubuntu-vacia-la-papelera
tags:
- gvfs
- gvfsd-trash
- how to
- linux
- receta
- sistema operativo
- sistemas
---

# Si el disco duro no para al arrancar ubuntu vacía la papelera

Los discos duros (casi) infinitos actuales han hecho que en un año haya acumulado más de 4000 ficheros y casi 60GB en la papelera de Gnome. Nunca pensé que esto fuera un problema pero ultimamente el ordenador tardaba muchísimo en iniciarse y el disco duro incluso después de arrancar el escritorio estaba funcionando durante uno o dos minutos.

El comando *iotop* nos permite saber que procesos están consumiendo más acceso a disco, y al lanzarlo durante el arranque descubrí que el problema era el servicio [gvfsd-trash](https://en.wikipedia.org/wiki/GVfs), responsable de la gestión de la papelera. Hay un montón de bugs y comentarios en los foros quejándose de este problema \[[1](https://ubuntuforums.org/showthread.php?t=2076379)\], \[[2](https://ubuntuforums.org/showthread.php?t=1654912)\], \[[3](https://bugzilla.gnome.org/show_bug.cgi?id=587221)\].

A falta de una solución mejor [simplemente vaciar la papelera funciona](https://askubuntu.com/questions/87608/ubuntu-10-10-trash-cpu-overload). Así que ya sabes, si la lucecita del disco duro no para durante el arranque vacia la papelera.