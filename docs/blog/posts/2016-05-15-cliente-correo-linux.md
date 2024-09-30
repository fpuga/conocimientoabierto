---
id: 871
title: 'Cliente de correo para Linux'
date: '2016-05-15T12:57:17+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=871'
permalink: /cliente-correo-linux/871/
categories:
    - 'Sin categoría'
tags:
    - correo-e
    - linux
    - recomendaciones
---

Llevo usando aplicaciones web para usar el correo desde que abrí mi primera cuenta de mail. Gmail tiene tiene una interfaz genial, funciona en cualquier dispositivo y es rápido. El único problema es que tus correos no son tuyos. Estos días he tenido que cerrar una vieja cuenta de correo en gmail y para descargar los mails a modo de copia de seguridad he estado revisando clientes de correo de escritorio:

- Que se lleven bien con gmail/imap, respetando etiquetas, …
- Que permitan agrupar conversaciones al modo en que lo hace gmail
- Que tenga buenas funcionalidades de búsqueda
- Que no use Qt

En las [recomendaciones](https://opensource.com/business/15/10/top-open-source-desktop-email-clients) y [quejas](http://www.techrepublic.com/article/the-lamentable-state-of-linux-and-email-clients/) de clientes sobresalen un par de ellos:

- **Claws Mail**. Que no parece tener el «modo conversación»
- **N1**. Que tiene una pintaza, algo así como el [Atom](https://atom.io/) de los clientes de correo, el problema es que todo el correo pasa a través de sus servidores o tienes que instalar uno en local.
- **Evolution**. Que parece pesado, poco documentado y con demasiada gente quejándose de bugs.
- **Thunderbird**.
- **Geary**.

Tanto Thunderbird ([con plugins](http://techtinkering.com/2014/06/22/how-to-make-thunderbird-feel-like-geary/)) como Geary (por diseño) cumplen todos los requisitos, pero la búsqueda de Thunderbird parece mejor, y la mayor base de usuarios y documentación hace que sea el que vaya a probar.

Siguiendo la [documentación de thunderbird](https://support.mozilla.org/en-US/kb/thunderbird-and-gmail), la documentación sobre [IMAP de Google](https://support.google.com/mail/topic/3397500?hl=en&ref_topic=3398031) es fácil de configurar. Si hay problemas de conexión se puede [deshabilitar el acceso seguro en google](https://www.pcsteps.com/2300-use-gmail-with-thunderbird-offline-access-backup/) o habilitar [OAuth2 en thunderbird](http://kb.mozillazine.org/Using_Gmail_with_Thunderbird_and_Mozilla_Suite) como método de autenticación.

Para configurarlo bien hay que revisar un poco la configuración pero en general funciona todo sin problemas.