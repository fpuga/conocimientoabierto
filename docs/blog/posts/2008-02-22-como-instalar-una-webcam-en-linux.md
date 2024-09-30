---
categories:
- General
date: 2008-02-22
permalink: /como-instalar-una-webcam-en-linux/38/
slug: como-instalar-una-webcam-en-linux
---

# Como instalar una webcam en linux

Hace tiempo que comenté en este blog un modo de [instalar los drivers para una webcam en linux](http://conocimientoabierto.blogspot.com/2007/04/instalar-los-drivers-para-una-webcam.html). La cosa ha avanzado y es un poco más fácil que entonces, pero por desgracia sigue habiendo truquillos que si no los conoces te hacen invertir una horita de busqueda por internet, así que hay va una miniguia, centrada sobre todo en mandriva 2008 pero válida para la mayoría de distros actuales.

1. Enchufar la webcam al ordenador
2. Averiguar cual es el kernel que tienes instalado en tu distribución. Para ello puedes abrir una consola y teclear <span style="font-style: italic">uname -r</span>
3. Instalar las fuentes del kernel que tengas instalado. Para ello debes buscar desde el gestor de software de tu distribución el paquete <span style="font-style: italic">kernel-source-tu\_numero\_de\_kernel.</span> En mandriva en ocasiones llegará con ejecutar el comando <span style="font-style: italic">urpmi kernel-source-&amp;(uname -r)</span>
4. Buscar en el gestor de software de tu distribución el paquete <span style="font-style: italic">dkms-gspcav1</span>. (Si no lo encuentras prueba buscando simplemente spca). Por cierto que ya le podían cambiar el nombre y llamarlo driver-webcam o algo un poquito reconocible. En mandriva: <span style="font-style: italic">urpmi dkms-gspacv1</span>
5. Reiniciar el ordenador, o si no quieres reiniciar teclear <span style="font-style: italic">modprobe gspca</span>.

Recuerda todos estos comandos deben ejecutarse como root, aunque por lo general es más sencillo (pero no más rápido) hacerlo desde la interfaz gráfica.

Con eso ya debería estar instalada, puedes comprobarlo a través de programas como amsn o kopete.