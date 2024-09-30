---
id: 300
title: 'Como usar GIT tras no haber seguido el flujo de trabajo idóneo'
date: '2011-05-15T17:17:23+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=300'
permalink: /como-usar-git-tras-no-haber-seguido-flujo-trabajo-idoneo/300/
categories:
    - General
tags:
    - como
    - 'desarrollo sofware'
    - git
    - 'how to'
---

GIT es una herramienta genial cuando eres un desarrollador disciplinado y sigues el flujo de trabajo recomendado:

`<br></br>$ git checkout -b nuevaFuncionalidad<br></br>... programar<br></br>$ git add -u # añadimos automaticamente todos los ficheros indexados que han sido modificados<br></br>$ git add fichero # añadimos los no indexados<br></br>$ git commit -m "Mensaje del commit"<br></br>... más commits<br></br>$ git checkout master<br></br>$ git pull --rebase<br></br>$ git checkout nuevaFuncionalidad<br></br>$ git rebase master<br></br>... (solucionar posibles conflictos)<br></br>$ git checkout master<br></br>$ git rebase nuevaFuncionalidad<br></br>$ git push<br></br>`  
Pero si hay algo que me gusta, y aquí se nota que es una herramienta hecha por desarrolladores para desarrolladores, es lo bien que se comporta cuando no eres tan disciplinado o has metido la pata. Vayamos con un ejemplo (casi) real que se inicia con un viaje en tren Coruña – Vigo.

El estado del repositorio al empezar era este:

`<br></br># On branch master<br></br># Your branch is ahead of 'origin/master' by 1 commit.<br></br>#<br></br># Changes to be committed:<br></br>#   (use "git reset HEAD ..." to unstage)<br></br>#<br></br>#	modified:   config/text_en.properties<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   config/text_gl.properties<br></br>#	new file:   src/es/udc/cartolab/gvsig/tocextra/ReloadVectorialDBLayerTocMenuEntry.java<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>`

Se trata de la extensión para [gvSIG](http://www.gvsig.org/web/), [extTOCextra](http://gitorious.org/exttocextra) desarrollada inicialmente por [Javi](http://valdaris.com/) y liberada por [Cartolab](http://cartolab.udc.es) como parte del proyecto [gvSIG-EIEL](http://cartolab.udc.es/cartoweb/gvsig-eiel/). Como vemos en algún momento del pasado se hizo un commit directamente sobre master que no se subió al repositorio y tenemos cuatro ficheros preparados para hacer un commit que todavía no se ha hecho.

En el viaje de vuelta Vigo – Coruña, nuestro desarrollador se pone a acabar lo que había empezado a la ida, hace un git status y se encuentra que el estado del repositorio es este:  
`<br></br># On branch master<br></br># Your branch is ahead of 'origin/master' by 1 commit.<br></br>#<br></br># Changes to be committed:<br></br>#   (use "git reset HEAD ..." to unstage)<br></br>#<br></br>#	modified:   config/text_en.properties<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   config/text_gl.properties<br></br>#	new file:   src/es/udc/cartolab/gvsig/tocextra/ReloadVectorialDBLayerTocMenuEntry.java<br></br>#<br></br># Changed but not updated:<br></br>#   (use "git add ..." to update what will be committed)<br></br>#   (use "git checkout -- ..." to discard changes in working directory)<br></br>#<br></br>#	modified:   .classpath<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>#	src/es/udc/cartolab/gvsig/tocextra/preferences/<br></br>`  
A base de memoria y git diff sabemos que:

- El commit ya realizado y los archivos preparados para hacer commit constituyen una nueva funcionalidad (funcionalidad 1) que no nos interesa subir al repo por ahora
- La modificación del .classpath y parte de lo modificado en TocExtraExtension son una pequeña refactorización que tiene sentido en si misma y que nos interesa subir como un commit separado del resto
- El nuevo paqueta es.udc.cartolab.gvsig.tocextra.preferences, y los cambios ShowActivesTocMenuEntry, text\_es.properties, y parte de los de TocExtraExtension son parte de una nueva funcionalidad (funcionalidad 2) que se empezó a programar y que todavía no está terminada. Así que nos interesa tenerla en una rama disinta de master para poder seguir trabajando sobre ella.

A la vista de esto nuestro objetivo será:

- Tener una nueva rama con la funcionalidad 1 conservando la diferencia entre el commit ya realizado y el que tenemos preparado.
- Una rama nueva con la refactorización en un sólo commit para luego traérnosla a master (tras haber sincronizado master con el repo) y subirla
- Una rama nueva con la funcionalidad 2 en tantos commits como queramos para seguir trabajando.

Para conseguirlo tenemos muchos caminos alternativos, provemos uno en el que usemos distintos comandos que nos permitan ver la potencialidad de git.

#### Acabamos el commit que tenemos preparado

`$ git commit -m "i18n for ReloadVectorialDBLayerTocMenuEntry"`

#### Ocultamos temporalmente los cambios que nos quedan para que no nos molesten, creamos una nueva rama para la funcionalidad 1, y limpiamos el master.

`<br></br>$ git status<br></br># On branch master<br></br># Your branch is ahead of 'origin/master' by 2 commits.<br></br>#<br></br># Changed but not updated:<br></br>#   (use "git add ..." to update what will be committed)<br></br>#   (use "git checkout -- ..." to discard changes in working directory)<br></br>#<br></br>#	modified:   .classpath<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>#	src/es/udc/cartolab/gvsig/tocextra/preferences/<br></br>$ git stash<br></br># On branch master<br></br># Your branch is ahead of 'origin/master' by 2 commits.<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>#	src/es/udc/cartolab/gvsig/tocextra/preferences/`

$ git checkout -b reloadDBLayers  
$ git checkout master  
$ git reset -hard HEAD^^ # Devolvemos la rama master al estado que tenía hace dos commits, es decir, eliminamos los cambios en local

#### Creamos una nueva rama para la refactorización y deshacemos la ocultación

`<br></br>$ git checkout -b refactor<br></br>Switched to a new branch 'refactor'<br></br>$ git stash apply<br></br>Auto-merging .classpath<br></br>CONFLICT (content): Merge conflict in .classpath<br></br>Auto-merging config/text_es.properties<br></br>CONFLICT (content): Merge conflict in config/text_es.properties<br></br>$ git st<br></br># On branch refactor<br></br># Changes to be committed:<br></br>#   (use "git reset HEAD ..." to unstage)<br></br>#<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#<br></br># Unmerged paths:<br></br>#   (use "git reset HEAD ..." to unstage)<br></br>#   (use "git add/rm ..." as appropriate to mark resolution)<br></br>#<br></br>#	both modified:      config/text_es.properties<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>#	src/es/udc/cartolab/gvsig/tocextra/preferences/<br></br>`  
Ups, el stash apply nos ha provocado un conflicto. ¿Por qué?. Tómate 15 sg para pensarlo y luego sigue leyendo…

En el commit que teniamos sin hacer había modificaciones sobre text\_es.properties, cuando lo comiteamos dejamos algunas modificaciones sobre ese archivo que estaban basadas en los cambios comiteados. Como la rama «refactor» la creamos a partir de un master limpio, sin esas modificaciones cuando ejecutamos stash apply ese fichero se encuentra en un estado distinto al esperado y se produce un conflicto que no es capaz de resolver automáticamente. Si hubieramos creado la rama refactor a partir de la rama reloadDBLayers el conflicto no se hubiera producido, pero en esa rama hay cambios que no nos interesan por lo que no podemos hacer esto.

Tras la solución del conflicto el estado de repo es este:  
`<br></br># On branch refactor<br></br># Changed but not updated:<br></br>#   (use "git add ..." to update what will be committed)<br></br>#   (use "git checkout -- ..." to discard changes in working directory)<br></br>#<br></br>#	modified:   .classpath<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>#	src/es/udc/cartolab/gvsig/tocextra/preferences/<br></br># no changes added to commit (use "git add" and/or "git commit -a")<br></br>`

#### Separar los cambios realizados sobre TocExtraExtension.java

Como los cambios de la refactorización para el archivo TocExtraExtension.java están mezclados con los de la funcionalidad 2, usaremos la opción [–patch de git add](http://nuclearsquid.com/writings/git-add.html) para separarlos separarlos. Esto nos permitirá escoger que cambios (hunks) de un archivo queremos preparar para comitear en lugar de añadir todo el archivo.  
`<br></br>$ git add -i src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>$ git status<br></br># On branch refactor<br></br># Changes to be committed:<br></br>#   (use "git reset HEAD ..." to unstage)<br></br>#<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#<br></br># Changed but not updated:<br></br>#   (use "git add ..." to update what will be committed)<br></br>#   (use "git checkout -- ..." to discard changes in working directory)<br></br>#<br></br>#	modified:   .classpath<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>#	src/es/udc/cartolab/gvsig/tocextra/preferences/<br></br>$ git add .classpath<br></br>$ git commit -m "Small refactor"<br></br>[refactor 715b4da] Small refactor<br></br> 1 files changed, 18 insertions(+), 14 deletions(-)<br></br>`  
Como se puede ver, hemos hecho commit de sólo una parte de los cambios realizados en TocExtraExtension. Los cambios que quedan son todos los de la funcionalidad 2, así que los comiteamos a una nueva rama  
`<br></br>$ git checkout -b newFeature<br></br>M	config/text_es.properties<br></br>M	src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>M	src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>Switched to a new branch 'newFeature'<br></br>$ git add -u<br></br>$ git add src/es/udc/cartolab/gvsig/tocextra/preferences/<br></br>$ git status<br></br># On branch newFeature<br></br># Changes to be committed:<br></br>#   (use "git reset HEAD ..." to unstage)<br></br>#<br></br>#	modified:   config/text_es.properties<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/ShowActivesTocMenuEntry.java<br></br>#	modified:   src/es/udc/cartolab/gvsig/tocextra/TocExtraExtension.java<br></br>#	new file:   src/es/udc/cartolab/gvsig/tocextra/preferences/TOCExtraPreferencesPage.java<br></br>#<br></br># Untracked files:<br></br>#   (use "git add ..." to include in what will be committed)<br></br>#<br></br>#	bin/<br></br>$ git commit -m "WIP. new feature"<br></br>[newFeature eea0ced] WIP. new feature<br></br> 4 files changed, 137 insertions(+), 13 deletions(-)<br></br> create mode 100644 src/es/udc/cartolab/gvsig/tocextra/preferences/TOCExtraPreferencesPage.java<br></br>`

#### Subimos al repositorio la refactorización

`<br></br>$ git checkout master<br></br>$ git pull --rebase<br></br>$ git checkout refactor<br></br>$ git rebase master<br></br>$ git checkout master<br></br>$ git merge refactor<br></br>$ git push<br></br>$ git branch -D refactor<br></br>$ git checkout newFeature # para seguir trabajando<br></br>`  
Parece complicado, pero en realidad es más difícil de leer que de escribir una vez coges un poco de costumbre.