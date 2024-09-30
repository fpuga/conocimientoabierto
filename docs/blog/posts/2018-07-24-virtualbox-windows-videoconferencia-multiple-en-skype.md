---
categories:
- Sin categoría
date: 2018-07-24
permalink: /virtualbox-windows-videoconferencia-multiple-en-skype/965/
slug: virtualbox-windows-videoconferencia-multiple-en-skype
tags:
- como
- how to
- linux
- receta
- skype
- virtualbox
- windows
---

# Virtualbox + Windows + VideoConferencia Múltiple en Skype

Si usas linux no sería extraño que alguna vez te hayas encontrado con una **ineludible** videoconferencia de grupo por Skype y hayas tenido que hacer números para poder participar.

Quien dice Skype, dice alguno de esas extrañas aplicaciones privativas de videoconferencia que alguna gente (clientes) insisten en usar.

Si tienes una licencia de Windows que puedas reusar para una máquina virtual, a mi estas instrucciones me funcionan en Ubuntu 18.04 para poder usar webcam y micro.

`<br></br># Substituir por el usuario deseado<br></br>USER=$(whoami)`

sudo apt install virtualbox virtualbox-ext-pack virtualbox-guest-additions-iso virtualbox-guest-x11 virtualbox-dkms  
sudo usermod -a -G vboxusers $USER  
sudo usermod -a -G video,audio,pulse-access $USER  
sudo usermod -a -G audio pulse

Tras crear la máquina guest con Windows:

- Encender la máquina virtual
- `Dispositivos ópticos` -&gt; `montar una nueva iso` -&gt; En `/usr/share/virtualbox` seleccionr VBoxGuestAdditions.iso.
- En caso de que no se ejecute automáticamente el cd/iso, ejecutaremos el .exe desde el explorador de archivos.

Con estas instrucciones tendremos una máquina virtual que soporte webcam, audio, usbs, portapapeles bidireccional (a activar en la configuración de cada máquina), …