---
id: 898
title: 'Recargar el navegador desde Emacs'
date: '2017-05-21T12:41:45+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=898'
permalink: /recargar-el-navegador-desde-emacs/898/
categories:
    - 'Sin categoría'
tags:
    - como
    - css
    - 'desarrollo web'
    - emacs
    - herramientas
    - html
    - IDE
    - javascript
    - tutorial
---

Aunque Emacs no suele aparecer entre los editores preferidos para desarrollo web sigue teniendo opciones que lo hacen interesante.

En este artículo vamos a comentar algunos «plugins» que nos ayudan a recargar el navegador automáticamente cuando hacemos cambios en el código. No todos funcionan en las últimas versiones de Emacs, pero los dejo en el artículo para saber lo que hay disponible, o al menos lo que no merece la pena probar.

## Conclusiones

Para quien quiera ir directo al grano el que me parece más recomendable en este momento es [Mini Kite Mode](https://github.com/tungd/kite-mini.el), que se comenta al final de listado y que descubrí a través de [esta pregunta de stackoverlow](https://stackoverflow.com/questions/22192164/remote-controlling-chrome-chromium-browser-from-emacs). En las respuestas se mencionan algunos complementos para emacs para trabajar con desarrollo web que no he probado y que también podrían ser interesantes pero están todos desactualizados.

## Listado de plugins

### Impatient Mode

Uno de los limitantes de [Impatient Mode](https://github.com/netguy204/imp.el) es que hay que habilitar el *impatient-mode* por cada uno de los buffers que se quieran observar. Aunque supongo que se puede configurar de algún modo algún hook para que automáticamente habilite la observación en los buffers abiertos con determinadas extensiones.

Tras habilitar el modo `M-x impatient-mode` y lanzar el servidor `M-x httpd-start` tendremos en localhost un navegador que escuche los cambios `http://localhost:8080/imp/`

Otro de sus problemas es que lo que parece hacer, es cargar dentro de un iframe la web que estamos editando en emacs, y desde el código html/js en el que está empotrado el frame se hace un pooling cada cierto tiempo para ver si el contenido cambia y recargar. Empotrar tu código dentro de un iframe al final excepto para casos sencillos puede ser problemático y el sistema de pooling tampoco es muy efectivo en la práctica, porque cada pocas pulsaciones de teclas se hace un refresco de la página.

### Skewer Mode

Para hacer funcionar [Skewer Mode](https://github.com/skeeto/skewer-mode) seguramente haya que hacer un par de pruebas, pero hay un [vídeo](https://www.youtube.com/watch?v=VEcobuYr5wg) y una [pregunta de stackexchange](https://emacs.stackexchange.com/questions/2376/how-to-use-skewer-mode) que pueden ayudar.

La parte interesante de este modo es que permite abrir un buffer en modo REPL para javascript. De modo que podemos evaluar el código js directamente en emacs como si estuvieramos usando la consola del navegador. O podemos editar nuestra fuente javascript y relanzar una función o porciones de código al navegador.

Uno de los mayores limitante es que la recarga no es automática, y en el modo html funciona tag a tag. Es decir, no podemos reenviar el buffer entero al navegador, si no sólo los tags que nos interesen. Lo que hace es modificar el dom, para actulizar el contenido de los tags. No lo he encontrado especialmente cómodo, pero tiene algunas extensiones que podrían simplificar el trabajo como [skewer-less](https://github.com/purcell/skewer-less) o [skewer-reload-stylesheets](https://github.com/NateEag/skewer-reload-stylesheets).

### Emacs browser refresh

[Browser refresh](https://github.com/syohex/emacs-browser-refresh) es una idea sencilla e interesante. Basicamente usa [xdotool](http://semicomplete.com/projects/xdotool), una herramienta que permite scriptear movimiento de ratón y pulsaciones de teclas, para poner la ventana del navegador en foco y pulsar «F5», cuando le damos a salvar. El script original no funciona del todo bien, y aunque es fácil de arreglar es una solución «error prone». Si tenemos varias ventanas del navegador abiertas, o hemos cambiado de pestaña puede funcionar incorrectamente.

### GC Refresh Mode

De nuevo una buena idea pero el código de [GC Refresh Mode](https://github.com/Unitech/gc-refresh-mode) está desactualizado y no funciona. Al activar el modo `M-x gc-refresh-mode` pregunta la url a recargar, que puede ser un http://localhost o un file:///, abre esa uri en chrome en modo remote-debugging y sobreescribe *C-x C-s* para que al recargar se ejecute un script en python. El script en python es una implementación muy sencilla del Chrome Debugging Protocol que conecta a un socket con el que comunicarse con la instancia del navegador que abrió antes, busca la pestaña donde está la uri de interés y la recarga.

El problema es que Chrome ya no usa exactamente este sistema y el script no funciona. Este plugin está inspirado en la página de [Save And Reload Browser](https://www.emacswiki.org/emacs/SaveAndReloadBrowser) del Emacs Wiki.

### chrome-reload-page

Basándose en la idea de GC Refresh Mode hace algún tiempo escribí [un ejemplo de código](https://github.com/fpuga/trangalladas/tree/master/emacs/chrome-reload-page) (funcional) que acabó de subir a github.

Este script usa el [Chrome debugging protocol](https://developer.chrome.com/devtools/docs/integrating) para recargar la pestaña. El script lleva empotrado el código de python del fork de max-weller de [chrome\_remote\_shell](https://github.com/max-weller/chrome_remote_shell) para ahorrar trabajo.

### Mini Kite Mode

[Mini Kite Mode](https://github.com/tungd/kite-mini.el) es la más funcional de las opciones de este artículo.

Se puede instalar directamente desde MELPA. Para usarlo añadiremos a nuestro .emacs, las siguientes líneas.

`(require 'kite-mini)<br></br>(require 'kite-mini-console)<br></br># Automatically Turn on the mode for your buffer of choice.<br></br>(add-hook 'js-mode-hook (lambda () (kite-mini-mode t)))<br></br>(add-hook 'css-mode-hook (lambda () (kite-mini-mode t)))<br></br>(add-hook 'html-mode-hook (lambda () (kite-mini-mode t)))`

El segundo *require* sólo es necesario si queremos abrir un buffer de Emacs como una consola js en modo REPL (similar a la consola de DevTools). Y los hooks permiten activar el modo para los buffers de interés en tener que activarlo a mano `M-x kite-mini-mode`

Una vez en un buffer (y través a ver lanzado chrome / chromium en modo remote debug) simplemente conectamos con

`M-x kite-mini-connect`

Si la pestaña que tenemos abierta es con la que queremos interactual podemos simplemente pulsar intro. A partir de ese momento podemos lanzar la consola de js, enviar una región al navegador para que sea evaluada, o recargar la pestaña.

El mayor problema, de esta herramienta, y en realidad de todas las que usen el Remote Debug, es que sóla una herramienta puede estar conectada mediante el protocolo a la vez, y las DevTools hace uso de este sistema también. De modo que si kite está conectado y se abren las DevTools kite se desconectará. Y si son las DevTools las que estan activadas cuando hacemos kite-mini-connect, kite no llegará a conectar.

Para simplificar un poco el flujo he editado el fichero de *~/.emacs.d/elpa/kite-mini-20160508.406/kite-mini-el* para que antes de hacer el reload salve el buffer, quedando así  
`<br></br>(defun kite-mini-reload ()<br></br>  (interactive)<br></br>  (save-buffer)<br></br>  (kite-mini-call-rpc<br></br>   "Page.reload"<br></br>   (list :ignoreCache t)))`

De este modo al pulsar *C-c C-r*, primero salva y luego recarga. El siguiente paso, sería que mientras esté conectado, pulsar *C-x C-s* salve el buffer y recargue, pero por ahora con esto me llega.