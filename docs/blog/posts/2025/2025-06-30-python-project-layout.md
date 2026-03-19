---
categories:
  - Sin categoría
date: 2025-06-30
permalink: /python-project-layout
slug: python-project-layout
tags:
  - desarrollo
  - python
---

# Estructura de directorios de una librería Python

En Python hay fundamentalmente dos recomendaciones distintas de cómo estructurar los directorios (_project layout_) de una librería o herramienta, que queramos distribuir.

No incluyo en este artículo estructuras para _proyectos_. Por ejemplo una aplicación web monorepo con el _backend_ y el _front_ en el mismo repositorio. Proyectos que quieren desarrollar distintas herramientas bajo el mismo namespace. U otros casos particulares.

## Sin directorio raíz

Es la estructura más sencilla, especialmente para proyectos pequeños o scripts individuales.

En algunos artículos llaman a esta estructura _flat layout_. Esto induce a error, porqué _flat layout_ es el nombre más usado para la siguiente estructura que veremos. El artículo es antiguo pero en realpython llaman a esto [one-off-script](https://realpython.com/python-application-layouts/#one-off-script)

```text
my_project/
├── __init__.py
├── my_project.py
├── requirements.txt
├── tests/
│   └── test_my_project.py
└── README.md
```

Tiene a favor que es simple, no requiere subdirectorios, ni siquiera el fichero `__init__.py`, y todo está a la vista.

Pero nunca deberíamos usarlo. El _boilerplate_ de generar una estructura mejor tiene un coste cero si usamos un cookiecutter, y con esta estructura enseguida aparecen problemas de cómo organizar el código, empaquetar el proyecto y a la mínima tendremos problemas con los `import`.

## Módulo en la raíz (flat layout)

También llamado _adhoc layout_.

Es probablemente la más usada. El paquete (directorio) principal del proyecto [está directamente en la raíz](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#flat-layout).

```text
my-project/
├── my_project/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├───.github
│   └───workflows
├───docs
│   └───mkdocs.yml
├── pyproject.toml
└── README.md
```

**Pros:**

- Más directa que `src layout` al eliminar un nivel de anidación.
- No es necesario instalar (`pip install`) para ejecutar el código.
- Muchos proyectos siguen este patrón.

**Contras:**

- **Riesgo de _import_ locales:** Existe mayor riesgo de que Python importe el módulo en desarrollo (en el _source tree_ digamos) en lugar del módulo instalado. Esto puede llevar a errores difíciles de detectar a la hora de ejecutar los tests, empaquetar e instalar el proyecto.
- No es tan explícito como `src layout` sobre lo que se empaqueta y lo que no.

## Subdirectorio `src/` (src layout)

Es una de [las más recomendadas](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).

```text
my-project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├───.github
│   └───workflows
├───docs
│   └───mkdocs.yml
├── pyproject.toml
└── README.md
```

**Pros:**

- Al colocar el código en `src/my_project/`, el intérprete de Python siempre importará la versión instalada del paquete, no la versión en desarrollo en el directorio raíz. Esto ayuda a asegurar que el comportamiento en desarrollo sea el mismo que en producción.
- **Claridad de empaquetado:** Deja claro qué partes del proyecto son el código fuente que se va a empaquetar y distribuir. Otros archivos (tests, documentación, configuración de desarrollo) se mantienen fuera del paquete.
- **Fomenta buenas prácticas:** Al requerir una "instalación" (aunque sea editable) para que el código funcione correctamente en desarrollo.
- **Mejor aislamiento de pruebas:** Los tests se colocan fuera del directorio `src/`, lo que significa que no se incluyen en el paquete distribuido y evita dependencias de prueba en el código de producción.
- [Es el que prefiere uv](https://docs.astral.sh/uv/concepts/projects/init/#libraries)

**Contras:**

- Requiere más boilerplate. Para ejecutar el código se requiere una instalación editable o ajustar el `PYTHONPATH`.
- La carpeta `src/` adicional puede ser redundante.

## Variantes y Comentarios

- [Alguna gente prefiere introducir un nivel extra](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html) de indirección donde por ejemplo incluir _venv_
- Cuando escojamos un nombre para el proyecto, si vamos a publicarlo deberíamos comprobar que el nombre no está cogido en PyPy.
- [Separadores de nombre](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/#creating-a-package-in-src-layout). Los módulos y paquetes de Python no admiten _hyphens_, `-`, sólo _underscore_, `_`. Es habitual usar `kebab-case` (_hyphenated_) para el nombre del repositorio (carpeta raíz) y `snake_case` (_underscored_) para los paquetes y módulos.
- Alguna gente considera que lo correcto es empaquetar los tests dentro del _distributable package_. Yo no.

## Mi preferida

Mi preferida es _src layout_.

Las funcionalidades de los editores (_compact folders_, _quick open_) y herramientas cómo `uv` o `cookiecutter` reducen las incomodidades que introduce esta estructura.

Visual y organizativamente me gusta cómo queda la raíz del proyecto.

Me molesta mucho perder tiempo en los "esto no puede estar pasando", y esta estructura minimiza esos _subtle bugs_

Creo que el simple hecho de preocuparse de entenderla ayuda a que la gente no se líe a tocar `sys.path`, o probar con `python -m` a ver si sus `import` funcionan de esa forma. Aunque de "los scripts dentro de proyectos" hablaremos en otro artículo.

## Referencias

- [Testing & Packaging](https://hynek.me/articles/testing-packaging/). **Muy buena** explicación del problema del import local frente al import del código instalado al testear y distribuir.
- [Ticket de uv en el que se discute la estructura por defecto de los proyectos](https://github.com/astral-sh/uv/issues/8178).
- [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) en Python Packaging User Guide
- [Packaging a python library](https://blog.ionelmc.ro/2014/05/25/python-packaging/)
