---
categories:
  - Sin categoría
date: 2026-02-08
permalink: /bash-debug-mode
slug: bash-debug-mode
tags:
  - bash
  - programming
---

# Bash debug mode

Depurar un script de bash suele consistir en insertar un montón de `echo` que luego hay que borrar.

Un método mejor es usar `set -x`, que activa lo que podríamos llamar _bash debug mode_.

!!! quote "de la documentación [bash](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)"

    -x. Print a trace of simple commands, for commands, case commands, select commands, and arithmetic for commands and their arguments or associated word lists to the standard error after they are expanded and before they are executed. The shell prints the expanded value of the PS4 variable before the command and its expanded arguments.

Esta opción hace un print de cada comando del script a stderr antes de ejecutarlo.

Los parámetros (_parameters_) se expanden antes del print por lo que veremos los valores reales (_arguments_).

Podemos simplemente añadirlo al script cuando estemos depurando, y eliminarlo después. O, incluir la lógica en el propio script mediante parámetros y variables de entorno. Lo bueno de la variable de entorno es que podríamos tener varios scripts que la compartan de modo que activemos el modo debug para todos los scripts a la vez

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
$ GLOBAL_DEBUG_MODE=true ./my-script.sh

+ a=5
+ echo 5
5
+ echo bar
bar
```

Dos trucos adicionales en los que fijarse que nos permiten un poco de magia extra

- El `+` es el [valor de `PS4`](https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html)
- Los prints van a stderr

```text
# Use '2$>' instead of '2>' to combine stderr and stdout
$ PS4='\D{%F:%T} >> ' ./my-script.sh --debug 2> debug.log

5
bar

$ cat debug.log

2026-02-08:19:30:51 >> a=5
2026-02-08:19:30:51 >> echo 5
2026-02-08:19:30:51 >> echo bar
```
