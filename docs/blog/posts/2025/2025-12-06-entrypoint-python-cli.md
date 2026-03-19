---
categories:
  - Sin categoría
date: 2025-12-06
permalink: /entrypoint-python-cli
slug: entrypoint-python-cli
tags:
  - python
  - cli
  - desarrollo
  - herramientas
---

# Entry Point para una CLI Python

La flexibilidad del ecosistema Python le ha permitido convertirse en uno de los lenguajes más utilizados. El coste de esa flexibilidad es que en contra del [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)

> There should be one, and preferably only one, obvious way to do it.

incluso la gente con experiencia encuentra confusión y falta de _ejemplos canónicos_ en aspectos que deberían ser obvios cómo [el empaquetado](https://xkcd.com/1987/).

En este artículo tocamos uno de esos aspectos, el _entry point_ para herramientas de consola (ClI).

## Breve descripción de las "piezas" que entran en juego

### `__main__.py`

Cuando en un _python package_ (directorio que tiene dentro ficheros python), hay un fichero con el nombre `__main__.py` y _ejecutamos_ el módulo desde la línea de comandos (`python -m my_cli`), es ese fichero el que se ejecuta. De la documentación oficial:

> The `__main__.py` file is used to provide a command-line interface for a package.

Si bien en este _module_ no es necesario usar el idiom de `__name__ == "__main__":` es recomendable usarlo para evitar errores absurdos.

### `[proyect.scripts]`

La sección `[proyect.scripts]` de `pyproject.toml` indica a la herramienta de instalación (pip, uv, ...) que debe crear un ejecutable con el nombre que se le indique apuntando (_wrapper script_, _shim_, ...) a un determinado módulo y función.

Es decir, es un mecanismo para la distribución de nuestra herramienta. Los _usuarios_ no necesitarán ejecutar `python -m my-cli`, si no simplemente `my-cli`.

```toml
# El ejecutable `my-cli` apunta a la función `main()` de `my_cli/cli.py`
[project.scripts]
my-cli = "my_cli.cli:main"
```

Si instalamos en un entorno virtual el ejemplo anterior (`python -m pip install -e .[all]`, `uv sync`, ...) se creará un fichero `.venv/bin/my-cli` con este contenido:

```bash
#!/tmp/example/my-cli/.venv/bin/python3
# -*- coding: utf-8 -*-
import sys
from my_cli.cli import main
if __name__ == "__main__":
    if sys.argv[0].endswith("-script.pyw"):
        sys.argv[0] = sys.argv[0][:-11]
    elif sys.argv[0].endswith(".exe"):
        sys.argv[0] = sys.argv[0][:-4]
    sys.exit(main())
```

Si se instala a nivel global sería parecido.

Fijémonos en que:

- Apunta a una ruta de python absoluta. De modo que si lo ejecutamos fuera de un virtualenv `/tmp/example/my-cli/.venv/bin/my-cli` estará apuntando al python correcto.
- Al activar un virtualenv se modifica `"${PATH}"` incluyendo cómo primera entrada `/tmp/example/my-cli/.venv/bin/`, así que el ejecutable estará directamente disponibel cómo `my-cli`
- Importa el módulo y función que hemos indicado
- Es multiplataforma. En linux podremos usar `my-cli`, en windows `my-cli.exe`

### `__init__.py`

Es un fichero que marca un directorio cómo un _python package_. Su contenido se ejecuta siempre que se hace un import del paquete. No debería ser usado para escribir lógica, ni cómo entry point para un ejecutable.

## Mi forma preferida

Las piezas se pueden combinar de muchas formas. Algunas combinaciones serán más correctas que otras, según que criterios o necesidades se tengan en cuenta.

Mis criterios son:

- [src-layout](https://franciscopuga.es/blog/2025/06/30/python-project-layout/)
- Siempre instalar el paquete, sea para usarlo o desarrollarlo
- Asumir que el paquete puede ser distribuido
- Minimizar tiros-en-el-pie, errores absurdos y _subtle bugs_

Con lo que llegamos a la siguiente estructura:

```python
# my-cli/src/my_cli/__init__.py
__version__ = "1.0.0"

# my-cli/src/my_cli/lib.py
def do_things():
    print("do things")

# my-cli/src/my_cli/cli.py
from my_cli.lib import do_things

def main():
    print("Argument parsing logic goes here")
    do_things()

# my-cli/src/my_cli/__main__.py
from my_cli.cli import main

if __name__ == "__main__":
    main()
```

```toml
# my-cli/pyproject.toml
[project.scripts]
my-cli = "my_cli.cli:main"
```

## Algunas dudas

Tengo algunas dudas con esta aproximación que modifico según el caso:

- `cli.main` o `cli.cli`. El mejor nombre para esta función también me causa dudas. Depende del _naming_ del resto código, y de si la herramienta es fundamentalmente una cli, una librería o ambas.
- Cuando se usan librerías cómo Typer o Click y subcomandos la estructura de directorios debería ser algo distinta pero la idea base es la misma.
- Es realmente necesario proporcionar un `__main__.py`. Significa duplicar lógica para un uso muy concreto sólo necesario durante el desarrollo.

## Prácticas "incorrectas"

### Usar `__init__.py`

Al importar nuestro paquete (`import my_tool`) estaremos:

- Polucionando el espacio de nombres con el `cli.main`. Podríamos usar `__all__`, pero eso queda para otro día.
- Fomentando antipatrones
- Corriendo el riesgo de _side effects_ indeseados.

```python
# WRONG
# src/my_cli/__init__.py

from my_cli.cli import main

__version__ = "1.0.0"

if __name__ == "__main__":
    main()
```

### Jugar con el nombre del ejecutable

En `pyproject.toml` se puede asignar un nombre al ejecutable. Salvo que haya un motivo realmente bueno, cómo tener más de un ejecutable, debe tener el mismo nombre que el paquete [para evitar confusiones](https://docs.astral.sh/uv/guides/tools/#commands-with-different-package-names).

```toml
# WRONG
# pyproject.toml
[project.scripts]
# Asignamos el nombre my-tool al ejecutable
my-tool = "my_cli.cli:main"
```

### Ejecutar directamente `cli.py`

Salvo scripts muy pequeños, ejecutar directamente un módulo Python debería ser considerado un antipatrón. Obligar a instalar el paquete y ejecutar los módulos ahorra problemas, sobre todo con los imports. Por ello no permitiremos la ejecución directa del módulo.

```python
# WRONG
# src/my_cli/cli.py
from my_cli.lib import do_things

def main():
    print("Argument parsing logic goes here")
    do_things()

# Permitimos ejecutar directamente este módulo con `python src/my_cli/cli.py`
if __name__ == "__main__":
    main()
```

### Apuntar a `__main__.py` desde `project.scripts`

```python
# src/my_cli/__main__.py
from my_cli.cli import main

if __name__ == "__main__":
    main()
```

```toml
[project.scripts]
my-tool = "my_cli.__main__:main"

```

Parece una buena idea, porqué un cambio grande en la herramienta, que toque `cli.py`, puede obligar a cambiar tanto el fichero `__main__.py` cómo el `pyproject.toml`. Si `pyproject.toml` apunta directamente a `__main__.py` sólo hay que hacer el cambio en un sitio.

Pero no lo es.

- `__main__.py` debería estar reservado para ejecutar con `python -m my_tool` por _Separation of Concerns_.
- El stack trace al usar `my-tool` irá directamente a `cli.py` sin pasar con `__main__.py` que es sólo un wrapper.
- Los imports se vuelven confusos, y podemos acabar con dependencias circulares. En este ejemplo concreto, aunque podría ser escrito de otra forma, "main" es en realidad `cli.main`, no `__main__.main`.
- `__main__` tiene dos significados distintos en python, lo que lleva a confusión.
- Evitamos indirecciones. Con leer `pyproject.toml` podemos saltar al código real, y el _shim_ también queda más limpio.
- Es una práctica más habitual (black, pytest, pip).
- Si el proyecto crece y proporcionamos más ejecutables, el resultado es más limpio.

```toml
[project.scripts]
my-tool = "my_cli.cli:main"
my-tool-db = "my_cli.commands.database:main"
my-tool-serve = "my_cli.commands.server:main"
```

## Referencias

- [Top-level code environment](https://docs.python.org/3/library/__main__.html) en la documentación oficial de Python
- [Entry Point](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) en la documentación de setuptools
- [Why do script entrypoints require a function be specified?](https://discuss.python.org/t/why-do-script-entrypoints-require-a-function-be-specified/14090/18)
