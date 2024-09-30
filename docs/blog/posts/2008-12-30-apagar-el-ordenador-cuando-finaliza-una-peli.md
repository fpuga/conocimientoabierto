---
categories:
- linux
- scripting
date: 2008-12-30
permalink: /apagar-el-ordenador-cuando-finaliza-una-peli/54/
slug: apagar-el-ordenador-cuando-finaliza-una-peli
---

# Apagar el ordenador cuando finaliza una peli

Si eres de los que se llevan el portátil a la habitación para ver una película o el último episodio de tu serie favorita este artículo te interesa. Con la ayuda de la gente de [espaciolinux](http://www.espaciolinux.com/postlite40062-.html) he escrito un script para linux que hace que el ordenador se apague automáticamente unos segundos después de que finaliza la película que estás viendo.

Por ahora sólo funciona con el escritorio KDE 3.5 o inferior, y el reproductor kaffeine, aunque si alguien está interesado que deje un comentario y vemos como arreglarlo. El script es el siguiente:

```
#!/bin/sh<br></br><br></br># apaga_pelis.sh  v0.2. 2008/12/29<br></br># Francisco Puga. http://conocimientoabierto.es<br></br># Author makes devolution of this code to Public Domain<br></br><br></br># Sólo funciona con dcop (KDE 3.5 o inferior) y el reproductor kaffeine<br></br><br></br># Lanza la pelicula deseada, calcula su duración y se duerme a la espera<br></br># de que pase ese tiempo. Cuando se despierta calcula si la película ya ha<br></br># finalizado (por si ha habido pausas) y si no vuelve a dormirse.<br></br><br></br>kaffeine -f $1<br></br><br></br>#Calculamos la duracion y le sumamos 30s para que no apague justo despues<br></br>DURACION=$(expr $(dcop kaffeine KaffeineIface getLength) + 60)<br></br>sleep $DURACION<br></br><br></br>while [ $(dcop kaffeine KaffeineIface isPlaying) == "true" ]; do<br></br><br></br>  RESTA=$(expr $DURACION - $(dcop kaffeine KaffeineIface getTimePos))<br></br>  sleep $RESTA<br></br>done<br></br><br></br>dcop kaffeine KaffeineIface quit<br></br>dcop ksmserver ksmserver logout 0 2 2
```

[![](http://2.bp.blogspot.com/_wrQ7gWEOyz8/SVqaSwdOWFI/AAAAAAAAADY/HaK5jmgAZ6E/s320/abrir_con.jpg)](http://2.bp.blogspot.com/_wrQ7gWEOyz8/SVqaSwdOWFI/AAAAAAAAADY/HaK5jmgAZ6E/s1600-h/abrir_con.jpg)  
Lo único que teneis que hacer es copiar el texto anterior en un archivo de texto y guardarlo en algún sitio de vuestro disco duro. Luego pulsais con el botón derecho sobre él, vais a <span style="font-style: italic">propiedades -&gt; permisos</span> y marcais la casilla «<span style="font-style: italic">es ejecutable</span>«.

A continuación pulsais con el botón derecho sobre algún archivo que querais reproducir, propiedades, y luego pulsamos sobre el icono que se ve en la imagen. En la siguiente pantalla le damos a «añadir» y seleccionamos el archivo que contiene el script.

[![](http://2.bp.blogspot.com/_wrQ7gWEOyz8/SVqd1jVTprI/AAAAAAAAADg/WF6IUrVF4OU/s320/abrir_con2.jpg)](http://2.bp.blogspot.com/_wrQ7gWEOyz8/SVqd1jVTprI/AAAAAAAAADg/WF6IUrVF4OU/s1600-h/abrir_con2.jpg)  
Aceptamos y cuando esté agregado, lo seleccionamos y le damos a «bajar». El primer programa de la lista es con el que se abrirá ese tipo de archivo cuando hagamos doble click sobre él. El resto son accesibles desde el menú abrir con que se despliega cuando pulsamos con el botón derecho sobre el archivo.

Es decir, a partir de este momento cuando queramos que el ordenador se apague tras finalizar la película, debemos pulsar con el botón derecho sobre el archivo, vamos a abrir con y allí seleccionamos nuestro script.