---
categories:
- General
date: 2011-11-28
permalink: /taller-gvsig-eiel-valencia-metodo-1/420/
slug: taller-gvsig-eiel-valencia-metodo-1
tags:
- cartolab
- gis
- gvsig
- how to
- workshop
---

# Taller de gvSIG-EIEL en Valencia. Método 1.

El jueves por la tarde en las [Jornadas de gvSIG](jornadas.gvsig.org), [Gonzalo](http://cartohistorias.blogspot.com/) y yo estaremos por parte de [Cartolab](cartolab.udc.es) impartiendo el taller sobre [gvSIG-EIEL](http://cartolab.udc.es/cartoweb/gvsig-eiel/).

El taller está pensado para que los que acudan puedan seguir los ejemplos con su portátil. Dado que gvSIG-EIEL hace uso de una base de datos PostGIS para funcionar vamos a explicar dos formas distintas de poder seguir el taller.

La primera de ellas es que instaleis directamente en vuestro portátil la base de datos. Desde Ubuntu es tan sencillo como hacer:

`<br></br>sudo apt-get install postgresql-8.4-postgis pgadmin3<br></br>`  
Y luego crear un template para postgis.  
`<br></br>su postgres<br></br>createdb postgistemplate<br></br>createlang plpgsql postgistemplate<br></br>psql -d postgistemplate -f /usr/share/postgis/lwpostgis.sql<br></br>psql -d postgistemplate -f /usr/share/postgis/spatial_ref_sys.sql<br></br>`

Y en windows [bajándose este pack](http://www.enterprisedb.com/products-services-training/products/postgres-plus-solution-pack/downloads) y acordándose de seleccionar en el momento adecuado que también instale postgis.

Con motivo del taller vamos a proporcionar un nuevo set de datos que os podéis [descargar desde este enlace](http://dl.dropbox.com/u/2131623/gvsig-eiel.sql.zip). Aunque con los publicados en la página web es suficiente para hacer la mayoría de los ejemplos.

Desde la interfaz de pgAdmin3 [se crea una nueva base de datos](http://www.youtube.com/watch?v=1wvDVBjNDys) usando como template «*template\_postgis*» y luego se emplea el set de datos que proporcionamos sobre la base de datos que acabamos de crear. En caso de que hayamos llamado *gvsig-eiel* a la base de datos hariamos:  
`<br></br>psql -U postgres -p 5432 -h localhost -f gvsig-eiel.sql -d gvsig-eiel<br></br>`

En caso de duda [este artículo](http://www.bostongis.com/PrinterFriendly.aspx?content_name=postgis_tut01) puede ayudaros. Si tenéis alguna duda dejad un comentario en el blog o escribidme a fpuga ARROBA cartolab.es. Es importante que si vais a seguir el taller de forma activa traigais todo configurado.

gvSIG-EIEL [podéis descargarlo de la propia página](http://cartolab.udc.es/cartoweb/gvsig-eiel/menu/descarga/usuarios/). Con motivo del taller hemos dispuesto un servidor alternativo por si hubiera problemas.

Mañana publicaré el segundo método. Vamos a distribuir un fichero que podreis volcar a un USB (mínimo 4GB y se perderán los datos que tuvierais en ellos) que actuará como sistema operativo completo con todo instalado que podéis ejecutar directamente desde el USB sin necesidad de tocar nada en el ordenador (aunque funciona considerablemente más lento)