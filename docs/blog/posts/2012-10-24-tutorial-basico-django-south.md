---
categories:
- Sin categoría
date: 2012-10-24
permalink: /tutorial-basico-django-south/493/
slug: tutorial-basico-django-south
tags:
- desarrollo sofware
- django
- south
- tutorial
- web
---

# Tutorial básico de django south

[South](http://south.aeracode.org/) es una app de [django](https://www.djangoproject.com/) que permite modificar la estructura de la base de datos de una aplicación django cuando cambiamos el modelo *(models.py)*.

El comando [syncdb](https://docs.djangoproject.com/en/dev/ref/django-admin/#django-admin-syncdb) sólo crea nuevas tablas, pero no modifica tablas existentes, así que si en el modelo de una aplicación renombramos un campo de una tabla existente syncdb no realizará ese cambio en la base de datos. A este tipo de cambios en la base de datos se les denomina *«migración del esquema»* y es de lo que se encarga South.

# Instalación

1. **pip install south**
2. Agregar «south» a INSTALLED\_APPS
3. Ejecutar syncdb antes de crear nuestros propios modelos. Está será la última (y única) vez, que necesitamos ejecutar este comando  
    `manage.py syncdb`

# Usar south en un una app nueva

1. Crear la aplicación, y empezar a rellenar el models.py
2. Crear el script de migración inicial  
    `python manage.py schemamigration app_name --initial`
3. Hacer los cambios en la bbdd  
    `python manage.py migrate app_name`

# Usar south en una app ya creada

`python manage.py convert_to_south app_name`

En el caso de que haya otros desarrolladores en el equipo y cada cual esté usando su propia instancia de la base de datos, el resto de desarrolladores deberá migrar la primera versión en modo fake,  
`python manage.py migrate app_name 0001 --fake`

el resto normal, así:  
`python manage.py migrate app_name`

De lo contrario [no podrán migrar su versión de la base de datos](http://south.readthedocs.org/en/latest/convertinganapp.html#converting-an-app).

# Migración de modelos

1. Modificamos el models.py de nuestra aplicación
2. Crear un nuevo script de migración  
    `python manage.py schemamigration app_name --auto`
3. Aplicar la migración a la bbdd  
    `python manage.py migrate app_name`

# Como funciona

Se puede decir que South funciona en varios niveles de abstracción disintos.

- Añade una tabla en la base de datos que mantiene el estado actual de la base de datos. Es decir, guarda que migraciones se han aplicado.
- Crea un directorio en la applicación, donde guarda para cada migración un fichero (script) con la información necesaria para realizarla
- Añade varios comandos al manage.py

Los ficheros de migración generados en deben subirse al repositorio para que el resto de los desarrolladores pueda también realizar la migración.

# Referencias

- [Una introducción básica](http://www.djangopro.com/2011/01/django-database-migration-tool-south-explained/).
- [Un ejemplo de funcionamiento algo más completo](http://agiliq.com/blog/2012/01/south/).
- [Documentación oficial](http://south.readthedocs.org/en/latest/index.html).

**Nota**: Editado el 7/Marzo/2015 para añadir el comentario de [Mauricio](http://conocimientoabierto.es/tutorial-basico-django-south/493/#comment-4055).