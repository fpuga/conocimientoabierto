---
categories:
- General
date: 2010-01-10
permalink: /cifrar-particion-disco-duro-externo-linux/197/
slug: cifrar-particion-disco-duro-externo-linux
tags:
- cifrado
- como
- how to
- receta
- seguridad
---

# Cifrar una partición o disco duro externo en GNU/Linux

A pesar de que soy un firme defensor de los asistentes gráficos, creo que ciertas cosillas, sobre todo las relativas a la seguridad y que llega con hacer una vez en la vida es conveniente aprender a hacerlas «de verdad». Una de esas cosas para las que merece la pena remangarse es aprender a cifrar o encriptar ([sic](http://es.wikipedia.org/wiki/Sic)) particiones o discos duros completos. Las instrucciones que voy a dar a continuación están pensadas para cifrar una partición en dispositivo externo pero también valdrían para una interna. Si lo que queremos es cifrar /home quedarían algunas cosas más por hacer que lo que aquí se describe. Por poner las cosas un poco en contexto, la idea de fondo de esta receta es que tengo un disco duro externo con varias particiones. En dos de ellas, cifradas ambas, hago copia de seguridad de un portátil y un sobremesa. La tercera es un almacen de archivos multimedia, música y vídeos obtenidos de gente que los[ compartía de forma no delictiva a través de internet](http://www.filmica.com/david_bravo/archivos/009353.html).

## Comprobaciones previas

- Saber el nombre del dispositivo que equivale a la partición que queremos cifrar, este nombre acostumbra ser del tipo /dev/sdb1 si se trata de una partición o /dev/sdb si es todo el disco. A partir de ahora me referiré a este nombre como $PARTICION. El contenido de esa partición lo perderemos por completo. Podemos identicarlo ejecutando en una consola `fdisk -l`
- Desmontar la partición sobre la que vayamos a trabajar `umount $PARTICION`
- Instalar (en el raro caso de que todavía no lo esté) el paquete *cryptsetup*.

## Comprobar que no hay errores en el disco

A continuación comprobaremos que la partición que vamos a cifrar no tiene errores físicos. Esta operación y la siguiente de rellenar con valores aleatorios el disco pueden tardar varias horas y no son estrictamente necesarias, pero yo recomiendo ejecutarlas.  
`badblocks -s -w $PARTICION -b $TAMAÑO_BLOQUE`

Para saber cual es el tamaño de bloque en nuestra partición podemos usar el comando:  
`tune2fs -l /dev/sda5 | grep -i 'Block size'`

Una forma de acelerar el proceso de chequeo de errores es usar el parámetro `-t random`. Por defecto lo que hace badblocks es llenar todos los bytes del disco duro con aa, 55, ff, 00. Primero escribe el primer patrón (aa) y luego comprueba que todos los bytes valen aa, a continuación hace lo mismo con el segundo patrón,… Con `-t random` da una sóla pasada donde el patrón usado es aleatorio. Es menos fiable pero más rápido. Tampoco es mala idea hacerlo si estamos más o menos seguros de que el disco está bien y nos vamos a saltar el paso de llenar el disco con valores aleatorios.

## Aleatorizar el disco

Si somos un poco paranoicos lo que debemos hacer a continuación es llenar la partición con valores aleatorios, lo que nos protegerá de ciertos ataques criptográficos. Hay varias formas de hacer esto, a mayor nivel de paranoia más lento será. Yo lo hago con este comando:  
`shred -n 1 -v $PARTICION`

El parámetro `-n $numero` define el número de pasadas que haremos, el valor por defecto es 3, pero con 1 es suficiente. Hay quien sugiere usar mejor el comando:  
`dd if=/dev/random of=$PARTICIÓN bs=$TAMAÑO_BLOQUE`

Mientras que shred trabaja con datos pseudo-aleatorios (tomados de */dev/urandom*) los que se usan con esta otra opción son realmente aleatorios, pero el tiempo que tarda en finalizar se multiplica.

Por otro lado prefiero usar *shred* a `dd if=/dev/urandom of=%PARTICION bs=$TAMAÑO_BLOQUE` (que es otra instrucción que se ve habitualmente por ahí en los *how-to*) porque con shred nos va informando del progreso del proceso y es una herramienta específica para este tipo de tareas.

## Cifrar la partición

El siguiente paso consiste en indicar al sistema operativo el tipo de cifrado y contraseña queremos emplear para ese dispositivo.  
`cryptsetup -c aes -h sha256 -y -s 256 luksFormat $PARTICION`

- -c aes indica que vamos a usar como algoritmo de cifrado AES que es el más extendido. Otra buena opción sería Twofish.
- -s 256: que el tamaño de la clave sean 256 bits que es más que suficiente. A mayor tamaño más seguridad pero mayor perdida de rendimiento
- -h sha256: que use como [algoritmo de hash](http://es.wikipedia.org/wiki/Hash) SHA-256.

Si este comando nos da un error del tipo

> Check kernel for support for the aes-cbc-plain cipher spec and verify that /dev/sdb6 contains at least 258 sectors

es seguramente porque no tenemos cargado el módulo dm-crypt. Para cargarlo ahora mismo ejecutamos  
`modprobe dm-crypt `

Para hacer que se cargue automáticamente cada vez que arrancamos el ordenador añadimos al archivo */etc/modules* una línea que contenga unicamente el módulo a cargar, en este caso  
`dm-crypt`

Ahora debemos comprobar si podemos acceder al volumen cifrado  
`cryptsetup luksOpen $PARTICION $NOMBRE`

Este comando es algo así como decirle al kernel que el volumen virtual descifrado, correspondiente al volumen físico cifrado $PARTICION va a ser */dev/mapper/$NOMBRE*. Este comando no es equivalente a montar la partición, es más bien inventarnos una especie de interfaz hardware para acceder a nuestros datos descifrados.

## Creamos un nuevo sistema de archivos en la partición

Si todo ha ido bien ahora debemos formatear la partición, yo uso el sistema de archivos ext4.  
`mkfs.ext4 [-L $ETIQUETA] -m 1 /dev/mapper/$NOMBRE`

- -L $ETIQUETA: Asigna a esa partición un determinado nombre. Yo uso esta opción sobre todo cuando se trata de dispositivos externos, ya que cuando conectemos el dispositivo este se montará automáticamente como */media/$ETIQUETA*, si no tiene etiqueta será simplemente */media/disk*. Hay que tratar de usar un identificador que sea difícil que se repita, para poder asegurarnos que no hay otro dispositivo montado con el mismo nombre yo por ejemplo uso el estilo *fpuga\_backup*
- -m 1: Es para reservar un 1% del disco duro para el superusuario en lugar del 5% por defecto. Es útil dejar siempre algo pero 5 es demasiado

Para cerrar el volumen descifrado y que no se puede acceder a él con la clave haremos  
`cryptsetup luksClose /dev/mapper/$NOMBRE`

## Trabajar con el disco cifrado

Con los pasos dados hasta aquí ya tenemos listo nuestro volumen cifrado, la cuestión ahora es ¿como empezar a meter datos en él?. Primero descifraremos el disco (metiendo la clave), creándose automáticamente un volumen virtual descifrado y luego montaremos el volumen, esto lo hacemos con los comandos:  
`cryptsetup luksOpen $PARTICION $NOMBRE<br></br>mount /dev/mapper/$NOMBRE $PTO_MONTAJE`

En el caso de que sea un partición interna es conveniente que definamos sus propiedades de montaje en */etc/fstab*. En el caso de ser una externa es bastante sencillo, ya que al conectar el dispositivo automáticamente nos saldrá una ventana de diálogo preguntándonos la clave. Al introducirla, si hemos definido una etiqueta para la partición está se montará en */media/$ETIQUETA.*

Para desmontar la partición y cerrar el volumen descifrado podemos hacer click con el botón derecho sobre la partición y darle a desmontar o bien ejecutar los comandos:  
`umount $PTO_MONTAJE && cryptsetup luksClose /dev/mapper/$NOMBRE`

## Referencias

- [7 Steps To An Encrypted Partition (local or removable disk)](http://ubuntu-tutorials.com/2007/08/17/7-steps-to-an-encrypted-partition-local-or-removable-disk/)
- [EncryptedFilesystems – Mandriva Wiki](http://wiki.mandriva.com/en/Docs/SysAdmin/Security/EncryptedFilesystems)
- [Cómo encriptar una partición de disco duro con dm-crypt](http://www.jeanette.es/archives/325)
- [DM-Crypt with LUKS](http://en.gentoo-wiki.com/wiki/SECURITY_System_Encryption_DM-Crypt_with_LUKS)