---
categories:
- General
date: 2011-06-17
permalink: /comentario-diseno-bases-de-datos-postgis/360/
slug: comentario-diseno-bases-de-datos-postgis
tags:
- base de datos
- cartolab
- gis
- postgis
- sistemas
---

# Comentario sobre el diseño de bases de datos PostGIS

Un par de comentarios muy rápidso sobre una práctica que considero acertada a la hora del diseño con bases de datos PostGIS.

### No uses el esquema public

PostGIS emplea de forma intensiva el esquema public para crear funciones, tipos de datos etc… Si tu también empleas ese esquema cuando vuelques tu base de datos ese esquema tendrá que ser incluído y no sólo irán tus datos si no también toda la parte de PostGIS lo que incrementará el tamaño del dump y el tiempo de restauración.

Además si el usuario quiere restaurar la bd sobre una ya existente con PostGIS saldrán un montón de errores de que las funciones ya existen, con lo que se hace difícil depurar otros posibles errores. También se pueden producir errores si tu dump corresponde a una versión de PostGIS distinta a la que tiene el usuario.

### Cuando vuelques tu base de datos excluye el esquema public del volcado

Por lo ya explicado en el punto 1. Hacer esto es tan sencillo como:

`<br></br>pg_dump --no-owner -N public -h servidor -U usuario -f /tmp/base_de_datos.sql base_de_datos<br></br>`

### Vuelca también la tabla geometry\_columns

Los únicos datos que estarán en el esquema público que te hacen falta serán los de la tabla geometry\_columns. Vuelca por tanto esos datos (no hace falta la estructura) a otro fichero sql.

`<br></br>pg_dump --no-owner -a -t geometry_columns -h servidor -U usuario -f /tmp/geometry_columns.sql base_de_datos<br></br>`

Teniendo en cuenta estos consejos apenas tendrás trabajo extra y harás la vida mucho más fácil a quien tenga que restaurar la base de datos (que puede que seas tu mismo)

**Actualización 17/Febrero/2013**. Acabo de encontarme por primera vez desde que escribí esto con alguien que también declara en un post [lo importante de no usar el schema public](http://justobjects.org/blog/2013/moving-postgis-tables-from-the-public-schema-to-a-new-schema/trackback) cuando se trabaja con postgis.