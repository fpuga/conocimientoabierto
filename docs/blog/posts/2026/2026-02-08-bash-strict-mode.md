---
categories:
  - Sin categoría
date: 2026-01-02
permalink: /bash-strict-mode
slug: bash-strict-mode
tags:
  - bash
  - programming

draft: true
---

# Bash strict mode

Bash es un lenguaje increíblemente flexible, e increíblemente inseguro. En la mayoría de lenguajes cuando se produce una excepción, salvo que se capture, el programa termina. En bash no es así por defecto:

```bash
cd /path/to/folder-that-not-exists

# This will be executed in the current folder
rm -rf *
```

Mucha gente ha escrito sobre el _bash strict mode_, generalmente descrito cómo `set -euo pipefail`.

En este artículo explico mi versión del modo seguro.

## `set -x`

`-x` no influye en la seguridad del script. Lo podemos llamar _bash debug_mode_. Hace un print de cada comando del script antes de ejecutarlo.

Los parámetros (_parameters_) se expanden antes del print por lo que veremos los valores reales (_arguments_).

Podemos simplemente añadirlo al script cuando estemos depurando, y eliminarlo después. Si es importante proveer esa funcionalidad podemos proporcionar un parámetro o una variable de entorno. Lo bueno de la variable de entorno es que podríamos tener varios scripts que la compartan de modo que se usara en todos:

```bash
#!/usr/bin/env bash


DEBUG="${GLOBAL_DEBUG_MODE:-false}"

while [[ $# -gt 0 ]]; do
    case $1 in
        --debug) DEBUG=true ;;
    esac
    shift
done

"${DEBUG}" && set -x

a=5
echo "${a}"
echo "bar"
```

Salida:

```text
# ./my-script.sh --debug
$ GLOBAL_DEBUG_MODE=true ./my-script.sh

+ a=5
+ echo 5
5
+ echo bar
bar
```

## set -u

En anteriores artículos [hablamos del uso de `set -u`](./2026-01-02-bash-unset-vs-empty-variables.md) pero esto sólo produce un error, no aborta el programa.

## set -u

This option causes the bash shell to treat unset variables as an error and exit immediately. This brings us much closer to the behavior of higher-level languages.

#### Before

```
#!/bin/bash
set -eo pipefail

echo $a
echo "bar"

# output
# ------
#
# bar
```

#### After

```
#!/bin/bash
set -euo pipefail

echo $a
echo "bar"

# output
# ------
# line 5: a: unbound variable
```

## set -e

The `-e` option will cause a bash script to exit immediately when a command fails. This is generally a vast improvement upon the default behavior where the script just ignores the failing command and continues with the next line. This option is also smart enough to not react on failing commands that are part of conditional statements. Moreover, you can append a command with `|| true` for those rare cases where you don't want a failing command to trigger an immediate exit.

#### Before

```
#!/bin/bash

# 'foo' is a non-existing command
foo
echo "bar"

# output
# ------
# line 4: foo: command not found
# bar
```

#### After

```
#!/bin/bash
set -e

# 'foo' is a non-existing command
foo
echo "bar"

# output
# ------
# line 5: foo: command not found
```

#### Prevent immediate exit

```
#!/bin/bash
set -e

# 'foo' is a non-existing command
foo || true
echo "bar"

# output
# ------
# line 5: foo: command not found
# bar
```
