---
categories:
- Sin categoría
date: 2012-07-22
permalink: /emacs-analisis-estatico-codigo-python/478/
slug: emacs-analisis-estatico-codigo-python
tags:
- análisis estático de código
- desarrollo sofware
- emacs
- python
---

# Emacs y análisis estático de código en python

Gracias a [Cartolab](http://cartolab.udc.es/) he podido seguir dándole una vuelta al análisis de código estático en python. La idea era reducir los incómodos errores que se producen porque te equivocas al escribir el nombre de una variable o cosas parecidas de las que no te das cuenta has que ejecutas el código. Tratar de detectar estos errores [de la forma en que lo veíamos en el artículo anterior](http://conocimientoabierto.es/herramientas-analisis-codigo-estatico-python/468/) sigue sin ser demasiado productivo y aquí es donde entra en juego la [extensión para emacs Flymake](http://flymake.sourceforge.net/).

Lo que hace Flymake es «pedirle» a emacs que esté continuamente realizando ciertos análisis sobre el código o tratando de compilarlo y/o ejecutarlo. En realidad flymake es un plugin bastante genérico que funciona del siguiente modo:

1. Si al abrir un nuevo buffer está marcado como «a chequear», flymake programa un temporizador para el buffer. La forma de marcar buffers suele ser en función de la extensión del archivo que abramos
2. Crea una copia temporal de los buffers abiertos cada cierto tiempo
3. Ejecuta un programa externo sobre la copia del buffer. Este programa puede ser gcc, make u otra cosa como una herramienta de análisis estático de código.
4. Parsea la salida que produce el programa externo y da una salida visual en el buffer actual para representar los posibles errores.

## Activar flymake

Activar flymake junto a alguna de las herramientas que veíamos en el post anterior es bastante fácil. Flymake viene instalado por defecto, así que sólo tenemos que tener en el path los ejecutables a las herramientas de análisis, y añadir a nuestro .emacs las instrucciones para que se activen con los ficheros python.

**flymake con pyflakes**:  
`<br></br>(when (load "flymake" t)<br></br>(defun flymake-pyflakes-init ()<br></br>(let* ((temp-file (flymake-init-create-temp-buffer-copy<br></br>'flymake-create-temp-inplace))<br></br>(local-file (file-relative-name<br></br>temp-file<br></br>(file-name-directory buffer-file-name))))<br></br>(list "pyflakes" (list local-file))))<br></br>(add-to-list 'flymake-allowed-file-name-masks'("\\.py\\'" flymake-pyflakes-init)))<br></br>`

**flymake con pylint** (el comando epylint es un modo especial de pylint para trabajar con emacs)  
`<br></br>(when (load "flymake" t)<br></br>(defun flymake-pylint-init ()<br></br>(let* ((temp-file (flymake-init-create-temp-buffer-copy<br></br>'flymake-create-temp-inplace))<br></br>(local-file (file-relative-name<br></br>temp-file<br></br>(file-name-directory buffer-file-name))))<br></br>(list "epylint" (list local-file))))<br></br>(add-to-list 'flymake-allowed-file-name-masks'("\\.py\\'" flymake-pylint-init)))<br></br>`  
**flymake con pep8**  
`(when (load "flymake" t)<br></br>(defun flymake-pylint-init ()<br></br>(let* ((temp-file (flymake-init-create-temp-buffer-copy<br></br>'flymake-create-temp-inplace))<br></br>(local-file (file-relative-name<br></br>temp-file<br></br>(file-name-directory buffer-file-name))))<br></br>(list "pep8.py" (list "--repeat" local-file))))<br></br>(add-to-list 'flymake-allowed-file-name-masks'("\\.py\\'" flymake-pylint-init)))<br></br>`

Por otro lado también podriamos configurar flymake para hacer que se pasarán [las tres herramientas de forma automática](http://stackoverflow.com/questions/1259873/how-can-i-use-emacs-flymake-mode-for-python-with-pyflakes-and-pylint-checking-co) pero yo lo veo innecesario dado que la información que proporcionan es en muchos casos redudante y estamos disminuyendo el rendimiento del ordenador.

Además de indicarle a flymake con que herramienta queremos trabajar, tenemos que activarlo para los buffers que nos interesen. Esto podemos hacerlo de varios modos:

- Manual. Activando el modo menor de flymake. ` M-x flymake-mode`
- Que active el modo menor flymake cuando estemos en el modo python. Añadiendo al .emacs  
    `(add-hook 'python-mode-hook 'flymake-mode)`
- O que active el modo flymake en base a las extensiones de fichero que le hemos pasado anteriorme (flymake-allowed-file-name-masks)  
    `(add-hook 'find-file-hook 'flymake-find-file-hook)`

## Configurar flymake

Por defecto flymake ilumina (*highlight*) la línea de código donde se produce el error, empleando un color u otro en función de si es un error o un warning. Al dejar el ratón encima de la línea con el error (*hover*) nos muestra la descripción del error.

Para cambiar los colores que se emplean por defecto podemos emplear algo parecido a esto:  
`<br></br>'(flymake-errline ((((class color)) (:background "LightPink" :foreground "black"))))<br></br>'(flymake-warnline ((((class color)) (:background "LightBlue2" :foreground "black"))))<br></br>`  
Para que subraye en lugar de hacer highlight de la línea con el error:  
`<br></br>'(flymake-errline ((((class color)) (:underline "red"))))<br></br>'(flymake-warnline ((((class color)) (:underline "yellow")))))<br></br>`

Para hacer que **el fringe derecho se muestre un indicador de en que líneas hay errores** podemos usar [rfringe](http://www.emacswiki.org/emacs/RFringe). Aunque yo no he sido capaz de hacerlo funcionar.

**Mostrar la descripción del error en el minibuffer**. Esto es imprescindible cuando se trabaja en modo -nw.  
`<br></br>(defun my-flymake-show-help ()<br></br>(when (get-char-property (point) 'flymake-overlay)<br></br>(let ((help (get-char-property (point) 'help-echo)))<br></br>(if help (message "%s" help)))))<br></br>(add-hook 'post-command-hook 'my-flymake-show-help)<br></br>`  
Aunque el código anterior a mi me funciona, para mostrar el error en el minibuffer se suele emplear el plugin [flymake-cursor](http://www.emacswiki.org/emacs/FlymakeCursor).

**Moverse a través de los errores**. Podemos emplear los comandos M-x flymake-goto-prev-error para ir al error anterior, o M-x flymake-goto-next-error para ir al siguiente. También podemos vincularlos a determinadas teclas:  
`<br></br>(global-set-key [TECLA] 'flymake-goto-prev-error)<br></br>(global-set-key [TECLA] 'flymake-goto-next-error)<br></br>`  
**Links relacionados**

- [Manual adicional sobre flymake](http://www.gnu.org/software/emacs/manual/html_mono/flymake.html)