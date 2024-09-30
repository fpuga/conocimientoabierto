---
categories:
- General
date: 2009-06-28
permalink: /trasladar-dominio-telefonica/96/
slug: trasladar-dominio-telefonica
---

# Trasladar un dominio desde telefonica

Si alguna vez contraste un dominio con telefónica, seguramente vinculado a alguna de sus soluciones de ADSL para empresas y ahora quieres trasladarlo puede que tengas algún problema. Hace un par de días explicaba el [procedimiento más general para trasladar un dominio](http://conocimientoabierto.es/hosting-dominio-traslado-dns/89/), pero mi experiencia con telefónica para trasladar el dominio [marinerosbouzas.com](http://marinerosbouzas.com) no fue tan sencilla. Explico lo que yo tuve que hacer por si alguien se encuentra en la misma tesitura.

Lo primero es identificar si estamos en esta situación, para ello hacemos un [whois a nuestro dominio](http://dinahosting.com/whois.php). Si el resultado es parecido a este en el que sale como **Registrar** *Interdomain* y como **Name Server** *Terra* es que lo estamos.

> Domain names in the .com and .net domains can now be registered  
> with many different competing registrars. Go to http://www.internic.net  
> for detailed information.
> 
> Domain Name: MARINEROSBOUZAS.COM  
> Registrar: INTERDOMAIN, S.A.  
> Whois Server: whois.interdomain.net  
> Referral URL: http://www.interdomain.es  
> Name Server: DNS3.TERRA.ES  
> Name Server: DNS4.TERRA.ES  
> Status: ok  
> Updated Date: 19-jun-2009  
> Creation Date: 28-may-2004  
> Expiration Date: 28-may-2010

Para gestionar nuestro dominio podemos entrar en el (bastante limitado) [panel de control](http://telefonica.terra.es/paneldecontrol/) que nos proporciona telefónica. Vamos a *«Modificación de Datos»* y nos aseguramos que los datos del *«Propietario»* o *«Registrante»* sean los nuestros, especialmente el nombre y el correo-e. Aunque el dominio perteneza a una empresa para simplificar los trámites es mejor ponerlo temporalmente a nuestro nombre.

Lo lógico sería que desde este panel pudieramos obtener el [auth code](http://www.wdbc.com/domain/transfer-authcode.cfm) pero no se da la opción, además en mi caso, tras llamar a telefónica me informaron de que ese dominio no constaba. Lo que debió suceder es que es que en el lio de filiales (terra) que tiene telefonica durante fusiones o fisiones se perdió la información. Además actualmente telefónica no se dedica a la gestión de dominios si no que es otra filial, [interdomain](http://www.interdomain.es), quien lo hace y es con interdomain con quien debemos contactar.

Podemos probar a escribir al soporte de interdomain info (arroba) interdomain.org , pero nos responderán algo como:

> Actualmente su dominio se encuentra gestionado directamente por Telefónica Net. Usted tiene habilitado un panel de control en Telefónica Net desde el cual puede gestionar el dominio y son ellos quienes tienen que facilitarle las claves de acceso. Pero desde ese panel no podrá modificar las DNS ya que Telefónica tiene las suyas propias.
> 
> Si quiere salir de la gestión de Telefónica Net tiene que remitirnos [el archivo que le adjuntamos](http://www.interdomain.es/publica/faqs/Formulario_Solicitud_Login_Passoword.pdf) (LEER DETENIDAMENTE). Una vez recibamos el formulario, sacaremos el dominio de la gestión de Telefónica Net y le enviaremos las claves. Desde nuestro Panel de Gestión si que puede realizar las modificaciones previas al traslado de las DNS y redireccionar su dominio hacia su futuro proveedor de servicios sin perder días de trabajo, mientras se tramita el traslado y obtener el Auth Code (o password de transferencia).
> 
> Si ni el titular del dominio ni el contacto administrativo del dominio pueden firmar la solicitud de claves, ésta puede ser firmada por una persona con poderes dentro de la empresa, adjuntando copia de poderes de la empresa donde aparezca su nombre.

Debemos por tanto descargarnos ese pdf, imprimirlo, cubrirlo con nuestros datos y enviarlo por fax al número que allí se indica junto a una copia de nuestro dni. Tras el envio del fax nos enviarán un correo-e donde consta una clave de usuario y una clave de dominio. Vamos al [Panel de Gestión de interdomain](http://www.interdomain.es/PortalServlet?pagina=/privado/alta_usuario_final.jsp?presentar_login=1) e introducimos nuestro nombre de usuario (el mismo que el dominio) y la clave de usuario.

Volvemos a pinchar en *«Panel de Gestión» -&gt; Gestión y modificación de domnios -&gt; Se introduce el nombre del dominio y le damos a buscar -&gt; Introducimos la clave de gestión de dominio -&gt; Editar -&gt; Y copiamos el Password de Transferencia*. En principio este password es el mismo que la clave de gestión de dominio que te mandan por transferencia, que es a lo que la mayoría de la gente llama *Auth Code*

Ahora que ya tenemos nuestro *auth code* ya podemos ir a la página web de otro registrador para iniciar los trámites para el traslado del dominio.