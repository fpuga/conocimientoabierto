---
categories:
  - Sin categoría
date: 2026-01-02
permalink: /bash-unset-vs-empty-variables
slug: bash-unset-vs-empty-variables
tags:
  - bash
  - programming
---

# Bash: Variables indefinidas (_unset_) vs vacías (_empty_)

Bash es un lenguaje particular respecto a las variables que no han sido definidas previamente.

En Python, por ejemplo, las reglas son claras: una variable debe estar declarada antes de usarse. Si esa variable no existe, el intérprete lanzará un error.

```python
>>> print (my_var)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    print (my_var)
           ^^^^^^
NameError: name 'my_var' is not defined

>>> my_var="foo"
>>> print (my_var)
foo
```

En bash, **por defecto**, no se distingue entre una variable vacía y una indefinida. Al acceder a una variable no definida, bash no lanza errores y no detiene el script. Simplemente asume la asume cómo un _empty string_.

Esto, que parece cómodo para pequeños scripts, es también causa de muchos desastres: `rm -rf "${build_dir}/"`.

## Empty vs Null

En este artículo usaremos exclusivamente el termino _empty variable_ o _variable vacía_.

Pero para bash no hay diferencia práctica entre _null_ y _empty_. A veces también se habla de ese valor cómo _empty string_ o _null string_

En la práctica el valor de estas dos variables es el mismo:

```bash
explicit_empty_or_null_string=""
implicit_empty_or_null_string=
```

## Empty vs Unset

Pero, aunque bash intente disimularlo, si hay diferencias entre _empty o null_ y _unset_:

- **empty**: La variable existe, tiene un espacio asignado en memoria, pero su contenido es una cadena de longitud cero.
- **unset**: La variable no existe en el entorno actual. No tiene un espacio de memoria asignado.

Sin "protecciones", ambos tipos se comportan igual al expandirse:

```bash
#!/usr/bin/env bash
# Sin 'set -u'

unset explicit_not_existent_var # variable indefinida
explicit_empty_string=""  # variable vacía
implicit_empty_string=    # variable vacía

# En los cuatro casos se imprimirán líneas vacías
echo "A: ${implicit_no_existent_var}"
echo "B: ${explicit_not_existent_var}"
echo "C: ${explicit_empty_string}"
echo "D: ${implicit_empty_string}"
```

## Unbound variables

La cosa cambia cuando activamos el modo de bash de protección ante _unbound variables_

!!! note "unset vs unbound"

    No hay diferencias a nivel práctico entre el término `unset` y el término `unbound` en bash y se pueden usar cómo sinónimos. Lo que sucede es que al usar una variable no definida bajo `set -u` el mensaje de error (`bash: foo: unbound variable`) hace referencia a `unbound`,mientras que los comandos en sí hacen referencia a `unset`

Cuando usamos `set -u` (o `set -o nounset`) cambiamos "al modo protección". Una práctica que forma parte del llamado bash strict mode y que debería usarse en el 95% de los casos.

!!! quote "de la documentación [bash](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)"

    Treat unset variables and parameters other than the special parameters '@' or '_', or array variables subscripted with '@' or '_', as an error when performing parameter expansion. An error message will be written to the standard error, and a non-interactive shell will exit.

Siguiendo el ejemplo anterior:

```bash
#!/usr/bin/env bash

set -u

unset explicit_not_existent_var # variable indefinida
explicit_empty_string=""  # variable vacía
implicit_empty_string=    # variable vacía

echo "A: ${implicit_not_existent_var}" # bash: implicit_no_existent_var: unbound variable
echo "B: ${explicit_not_existent_var}" # bash: explicit_no_existent_var: unbound variable
echo "C: ${explicit_empty_string}" # imprime una cadena vacía
echo "D: ${implicit_empty_string}" # imprime una cadena vacía
```

## Operaciones útiles

Hay varias "operaciones" que es útil conocer para validar estas variables.

La primera es:

- **noop** `:`. Llamada a veces [operación null](https://bashcommands.com/bash-noop), permite evaluar las variables si que se ejecute su resultado. Veremos su utilidad en ejemplos posteriores.

### Conditional Expressions

Lo más básico es usar la expresiones condicionales del `[[` _[compound command](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html)_ y los _[builtin commands](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html)_ `test` y `[`

De la documentación de [expresiones condicionales](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html):

- `-v varname`. True if the shell variable _varname_ is set (has been assigned a value). If _varname_ is an indexed array variable name subscripted by `@` or `*`, this returns true if the array has any set elements. If _varname_ is an associative array variable name subscripted by `@` or `*`, this returns true if an element with that key is set.
- `-z string`. True if the length of string is zero.
- `-n string`. True if the length of string is non-zero.

Usaremos estas expresiones dentro de un if o con operadores cómo `&&` o `||`. El que en general debemos usar es `-v` dado que `-z` y `-n` dan error en modo `set -u` con variables indefinidas.

!!! danger

    `-v` espera un nombre de variable, no se debe poner el `$`. Si estamos trabajando con referencias hay que usar -R.

A modo de ejemplo

```bash
set -u
unset foo

if [[ -z "${foo}" ]]; then echo "'foo' is not set"; exit 1; fi # bash: foo: unbound variable
[[ -z "${foo}" ]] && echo "'foo' is not set" && exit 1 # bash: foo: unbound variable

if ! [[ -v foo ]]; then echo "'foo' is not set"; exit 1; fi # 'foo' is not set
[[ -z foo ]] || echo "'foo' is not set" && exit 1 # 'foo' is not set
[[ -z foo ]] || foo='DEFAULT_VALUE' # DEFAULT_VALUE is assigned to foo
```

### Parameter Expansion

Para asignar valores por defecto o "fallar pronto" si una variable está vacía el [parameter expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html) de bash es más elegante que las expresiones condiciones

- **Valor por defecto** (safe fallback) `:-`. Si la variable es `unset` o `empty` aplica un valor por defecto sin modificar la variable original.
- **Asignación por defecto** `:=`. Si la variable es `unset` o `empty` **asigna** un valor por defecto a la variable original.
- **Fallo Temprano** `:?`. Si la variable es `unset` o `empty`, e independientemente de haber usado `set -u` se aborta el script con un mensaje.

```bash
# Si 'nombre' no existe o está vacío, usa "Mundo".
echo "Hola ${nombre:-Mundo}"

# Asigna "rm" a FAVORITE_COMMAND si no estaba definido.
# Usamos noop (:) para que Bash evalúe la expresión sin ejecutar el resultado. Sin `:`, ejecutaría el `rm` o lo que contenga la variable FAVORITE_COMMAND
: ${FAVORITE_COMMAND:=rm}

# Si build_dir no está seteado, aborta imprimiendo el mensaje.
rm -rf "${build_dir:?Error: Directorio no definido}/"
```

## Algunas referencias extras

- StackOverflow. [How to check if a variable is set in Bash](https://stackoverflow.com/q/3601515/930271)
- StackOverflow. [How can I test whether a positional parameter is set in Bash?](https://stackoverflow.com/q/13361658/930271)
- StackOverflow. [Check if a Bash array contains a value](https://stackoverflow.com/q/3685970/930271)

## Conclusiones: Guía de estilo

Los scripts en bash son potentes y flexibles pero es fácil que el código sea difícil de leer o con bugs ocasionales pero catastróficos.

Dentro de mis normas para bash en lo referente a variables vacías y no definidas están:

**Usar `set -u`**. Hay pocas situaciones en que este modo no sea el correcto. Y en partes concretas de un script se puede desactivar y volver a activar.

```bash
#!/usr/bin/env bash

set -u

echo "Start"

set +u
echo "Something weird related to unbound variables"
set -u
echo "Come back to safety"
```

**Usar `:-` para asignar valores por defecto**. No uso el comando de asignación `:=`. Por nada en especial, simplemente me permite reducir la cantidad de formas distinta de hacer lo mismo. No se pueden usar con `$1`.

```bash
#!/usr/bin/env bash

set -u

"${foo:=World}" # error, intentará ejecutar el comando `World`
: "${1:=World}" # error, no se puede asignar a $1
: "${foo:=World}" # No da error, pero "reducimos la API a conocer"

# Me gustan más estas soluciones
foo="${1:-World}"
foo="${foo:-World}"

die(){
  # Call like `die "File not found"` or `die`
  local error=${1:-Undefined error}
  echo "$0: $LINE $error" >&2
  exit 1
}

# Si no queremos que salte unbound pero no nos preocupa que sea empty, podemos dejar el
# valor por defecto vacío
info() {
    # Will print the message `info "this is a message"` or an empty line `info`
    local msg="${1:-}"
    echo "${msg}"
}
```

**Usar `:?` para comprobar cuando una variable es vacía o indefinida**.

Ejemplos:

```bash
#!/usr/bin/env bash

set -u

user="${1:?Mandatory parameter for 'user' is missing}"

build_dir_path=$(find . -type d -iname 'build_dir')
: ${A:?'build_dir' folder is not found}

: ${VIRTUAL_ENV:?"virtualenv should be activated before continue"}

# Prefiero la versión anterior a estas
[[ -v VIRTUAL_ENV ]] && echo "virtualenv should be activated before continue" && exit 1
# No usar -z porqué genera un unbound
if ! [[ -v VIRTUAL_ENV ]] ; then
    echo "virtualenv should be activated before continue"
    exit 1
fi
```

Para entender mejor otras opciones

```bash

# Estamos intentando usar una unbound variable, da el mensaje genérico al respecto.
: ${VIRTUAL_ENV} # bash: VIRTUAL_ENV: unbound variable

# Genera su propio mensaje de error, distinto al habitual
: ${VIRTUAL_ENV:?} # bash: VIRTUAL_ENV: parameter null or not set

# definimos la variable pero en blanco
VIRTUAL_ENV=

# Sigue detectando que está vacía
: ${VIRTUAL_ENV:?} # bash: VIRTUAL_ENV: parameter null or not set
: ${VIRTUAL_ENV} # No da error, simplemente es una cadena vacía que no se ejecuta
```
