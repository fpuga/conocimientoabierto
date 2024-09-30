---
categories:
- General
date: 2010-07-03
permalink: /copia-seguridad-blog-wordpress/229/
slug: copia-seguridad-blog-wordpress
tags:
- backup
- bash
- como
- how to
- receta
- script
- wordpress
---

# Copia de seguridad de un blog en WordPress

Resulta conveniente realizar con regularidad una copia de seguridad de la información que tengamos en nuestro blog. Este backup deberíamos hacerlo como mínimo antes de una actualización importante del blog, por ejemplo antes de [migrar de WordPress 2.x a la versión 3](http://wordpress3-es.com/como-actualizar-wordpress-3-por-ftp/).

[Hacer un backup de wordpress](http://codex.wordpress.org/WordPress_Backups) consiste en dos cosas:

- Copiar los ficheros (imágenes, temas, …)
- Copiar los artículos y configuraciones (la base de datos)

Existen algunos plugins que pueden ayudarnos en estas tareas, pero si no tienes tirria a la línea de comandos en este artículo se describe un método rápido y eficiente para hacer la copia. El único requisito es que nuestro proveedor de hosting nos proporcione acceso por ssh, que es lo más habitual. Para ahorrarnos meter la clave ssh cada vez que hagamos la copia podemos subirla al servidor [en este artículo se explica como crearla y subirla](http://www.vicente-navarro.com/blog/2008/01/13/autentificacion-trasparente-por-clave-publicaprivada-con-openssh/) pero en resumen consiste en ejecutar estos dos comandos (o sólo el segundo si ya tenemos una clave creada)  
`ssh-keygen -b 4096 -t rsa<br></br>ssh-copy-id usuario@servidor`

El primer paso será hacer un volcado de la base de datos a un fichero en el servidor:

`ssh usuario@servidor "mysqldump --opt --user=USUARIO_BD -p --host=URL_BD NOMBRE_BD > /ruta/fichero_a_guardar"`

Por ejemplo  
`ssh fpuga@dreamhost.com "mysqldump --opt --user=fpuga_bd -p --host=localhost conocimientoabierto_bd_wordpress > conocimientoabierto/base_datos.sql"`

La opción -p significa que nos preguntará cual es la clave de la base de datos por consola. Podemos indicarla directamente haciendo –pasword=CLAVE. Esto puede ser útil si metemos estas sentencias en un script pero deberiamos tener el script a buen recaudo para que no puedan ver nuestra clave.

El fichero sql donde se volcará la base de datos podríamos comprimirlo, pero con la estrategia que vamos a usar es mejor dejarlo en texto plano. El proceso de comprimir tiene un consumo elevado de cpu (algunos hosting limitan la cpu que se consume) y en el siguiente paso nos bajaremos el fichero por rsync.

rsync lo que hace es buscar las diferencias entre lo que tengamos en el servidor y lo que tengamos en nuestro disco duro, y sólo se baja lo que varíe. Si hubiéramos comprimido en el paso anterior la base de datos tendría que bajarse el fichero entero pero al estar en formato texto se bajará sólo la diferencia lo que resulta óptimo tanto en gasto de cpu como en ancho de banda consumida. La copia de los ficheros del servidor a nuestro disco duro, consistirá entonces en ejecutar:

` rsync -av --delete usuario@servidor:ruta_remota $RUTA_LOCAL`

por ejemplo:

`rsync -av --delete fpuga@dreamhost.com:conocimientoabierto/ /home/fpuga/backup/conocimientoabierto`

La opción delete hace que se borren los archivos locales que ya han sido borrados del servidor remoto. [Puede ser peligrosa así que cuidado](http://www.vicente-navarro.com/blog/2008/01/13/backups-con-rsync/). La ruta local donde se copien los archivos debe existir previamente. Fijaos en que cuando se pone la ruta remota después de los dos puntos no se inicia con / porque sólo queremos indicar una ruta relativa.

Por último borraremos del servidor el fichero de volcado de la base de datos  
`ssh usuario@servidor "rm /ruta/fichero_a_guardar"`

Y para no teclear tanto [podemos crearnos un script muy sencillito](http://repo.or.cz/w/fpuga.git/blob/48c3183cc56216117181dd069e7f27d7fe1c5623:/foo/web_backup.sh). Llega con que cambies los valores de las variables por los de tu servidor.

Antes de escribir el script estuve leyendo sobre algunos plugins pero ninguno se adaptaba a mis necesidades, de todas formas estas referencias puede venirte bien si prefieres usar otro sistema:

- [Choosing a WordPress backup plugin that is right for you](http://www.bloggingtips.com/2010/01/08/choosing-a-wordpress-backup-plugin-that-is-right-for-you/).
- [Backing Up Your Database](http://codex.wordpress.org/Backing_Up_Your_Database).
- [IDrive for WordPress](http://wordpress.org/extend/plugins/idrive-for-wordpress/).
- Plugin [Updraft](http://wordpress.org/extend/plugins/updraft/).
- Plugin [myEASYbackup](http://wordpress.org/extend/plugins/myeasybackup/).
- Plugin [BackWPup](http://wordpress.org/extend/plugins/myeasybackup/).