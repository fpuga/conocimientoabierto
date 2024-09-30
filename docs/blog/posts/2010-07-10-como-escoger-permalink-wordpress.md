---
categories:
- General
date: 2010-07-10
permalink: /como-escoger-permalink-wordpress/238/
slug: como-escoger-permalink-wordpress
tags:
- como
- how to
- permalinks
- rendimiento
- seo
- wordpress
---

# Como escoger el permalink en WordPress

Escribí este texto en Mayo de 2009, pero tantas vueltas quería darle para que quedara perfecto, que al final nunca llego a ver la luz. He aprovechado la salida de la nueva versión de WordPress para comprobar si aún tenía vigencia, y a pesar de que [parece que se va a solucionar en breve](http://core.trac.wordpress.org/ticket/12935) por ahora este post sigue siendo correcto.. Así que sin darle más vueltas ahí va. Un batiburrillo de conocimientos sobre posicionamiento en buscadores (SEO), rendimiento de wordpress y permalinks.

## Como optimizar las url para el posicionamiento en buscadores

Lo primero que debes saber sobre optimizar las url para el posicionamiento en buscadores es que **no debes obsesionarte con ello**. Los criterios que usan los motores de búsqueda (SE, de sus siglas en inglés) son secretos (y seguramente cambiantes), por tanto la mayor parte de la información se basa en especulaciones. El [valor que los SE asignan a la url](http://www.seomoz.org/article/search-ranking-factors#ranking-factors) se dice que no es demasiado. De todas formas los criterios que desarrollo aquí no están sólo escritos pensando en el SEO (Optimizar el posicionamiento en buscadores) si no en la comodidad para el lector y el CT (click through, que el usuario haga click en un enlace que aparece en una página de búsqueda o anuncio). Dicho esto, las recomendaciones más generales que se suelen dar son:

- Cuanto más corta sea la url sin que se pierda el sentido mejor. Por ello es buena idea [eliminar el www](http://bloggingbits.com/wordpress-permalinks-seo/) del principio de las url.
- [Usa – para separar las palabras](http://www.youtube.com/watch?v=Q3SFVfDIS5k), por ejemplo si tu artículo va sobre «Para La caza de ballenas en el ártico» la url debería ser más o menos así http://midominio.com/parar-caza-ballenas-artico y no parar\_caza\_ballenas\_artico.
- Elimina de la url toda información superflua (artículos, posesivos, …) y deja sólo las palabras clave. Por ejemplo la url de un artículo titulado «Descubre las maravillas del gran continente africano» podría ser «descubrir-africa»
- Pon las páginas más importantes en la raíz del dominio y trata de estructurar el resto de una forma lógica. Por ejemplo: midominio.com/ecologia/caza-ballenas-artico y midominio.com/viajes/descubrir-africa y midominio.com/hazte-socio. O si tus artículos son muy basados en fechas midominio.com/2009/04/caza-ballenas-artico
- Ten cuidado a la hora de repetir títulos. Si haces una serie de artículos «Como Bloguear I», «Como Bloguear II», … y las url son demasiado parecidos los buscadores podrían pensar que estas haciendo spam y penalizarte (no estoy seguro de esto). Así que podrias optar por títulos y url del estilo «Escoger un titulo para el post (como bloguear I)» «escoger-titulo-post-bloguear-i», «El cuerpo del artículo (como bloguear II)» «cuerpo-articulo-bloguear-ii».
- Por supuesto no pueden existir dos url exactamente iguales. Por ejemplo en WordPress si una url (permalink) coincide con otra (aunque hayas editado el permalink a mano) -2 es añadido automaticamente. Otros CMS pueden funcionar de otra forma así que ten cuidado.
- Hay quien dice que las url que terminan en / posicionan mejor pero suponen un mayor gasto de ancho de banda. [Matt Cutts dice que mejor dejar las extensiones](http://www.youtube.com/watch?v=dSG6C33GwsE) (es decir url que acaben en .htm) aunque no por motivos de posicionamiento. Yo prefiero dejarlas sin la extensión y sin la /
- Si quieres que google news te indexe uno de los requisitos es que existan al menos tres digitos al final de cada url, por ejemplo caza-ballenas-456. Aunque hay que valorar la confusión que puede introducir para el lector el que haya números en la url

## Como aplicar estas reglas a WordPress.

Pasar de la teoría a la práctica no siempre es fácil y exige establecer compromisos. Veamos que sucede en wordpres.

En la instalación por defecto de wordpress a los nuevos artículos que escribamos se les asignará una url del tipo midominio.com/?p=123. Pero podemos hacer que esta url, [permalink en la jerga de wp](http://codex.wordpress.org/Using_Permalinks), tenga una forma más bonita y acorde a las reglas que ya hemos descrito.

La estructura de los permalinks se cambia a través del menú de «Opciones» del panel de control de wp. En [este artículo](http://www.homebizpal.com/blogging/wordpress/understanding-wordpress-permalinks/) comentan como se modifican los permalinks y que hacer si ya tenemos artículos escritos con la vieja estructura. Esto es importante, si cambiamos los permalinks en un blog ya en uso, las url de nuestros post cambiarán, de modo que los enlaces a nuestro blog pasarán a apuntar a direcciones inexistentes. Esto es solucionable mediante reglas 301 de redireccionado, pero este tema esta fuera del alcance de este artículo.

En los permalinks de wp generalmente usaremos una estructura a medida. Los códigos más usados son para generar esta estructura son:

- %postname%: Una versión saneada del título del artículo. Si el título es ¿Como cazar ballenas? el permalink será como-cazar-ballenas
- %year%: Los cuatro digitos del año de la fecha de publicación del post.
- %month%: Dos digitos para el mes
- %post\_id%: El identificador único de cada post. A cada post se le asigna un número distinto que jamas se repite.
- %categorie%: La categoría que hemos asignado a la entrada. Si le hemos asignado más de una es la que tenga un ID más bajo.

Para cambiar los permalinks tan sólo debemos combinar los códigos que acabo de explicar y darle a actualizar. Esta es la parte fácil, decidir cual es la mejor estructura para nuestro caso algo más complicado.

Hasta ahora la mayoría de artículos escritos sobre los permalinks de wordpress te recomendaban usar la estructura /%categorie%/%postname%/ o bien directamente /%postname%/. Pero una discusión de enero de 2009 [en las listas de correos de wordpress](http://comox.textdrive.com/pipermail/wp-testers/2009-January/011097.html) muy bien resumida en [este artículo](http://dougal.gunters.org/blog/2009/02/04/efficient-wordpress-permalinks) advierte de que estas dos estructuras puede dar problemas de rendimiento. Los artículos sobre seo escritos con anterioridad a esa fecha están incompletos porque no tienen en cuenta este factor.

## Rendimiento vs Posicionamiento

Este problema de rendimiento lo dividiremos en dos para explicarlo, aunque en el fondo son el mismo:

- Cuando el permalink contiene cadenas de texto (midominio.com/seo/wordpress-permalinks) wordpress tiene que hacer más accesos a la base de datos (querys) y más operaciones que cuando el permalink sólo contiene números (midominio.com/7405). Esto no es muy grave en la mayoría de casos, pero a medida que añadimos plugins, widgets y tenemos más visitas si puede convertirse en un problema. Sobre todo si usamos algún tipo de hosting compartido que limite el uso de cpu, querys por segundo u otro tipo de restricciones. La solución o minimización de este problema está en [instalar algún plugin de cache](http://ayudawordpress.com/%C2%BFcuantas-queries-son-las-adecuadas/).
- La segunda parte del problema, algo más grave se produce cuando la estructura del permalink comienza por una cadena en lugar de por un número. Es decir una estructura tipo midominio.com/seo/wodpress-permalinks sufriría ambos problemas mientras que una del tipo midominio.com/2009/seo-wordpress-permalinks sólo sufriría el primero. Si además de empezar por una cadena tenemos muchas páginas (no posts) y adjuntos (del orden de miles) el número de reglas que wordpress tiene que almacenar en la base de datos crece exponencialmente y con la forma en la que se hace actualmente además de ralentizar mucho la carga de las páginas e incrementar los querys puede acceder que no podamos acceder a la base de datos de forma manual (operaciones de copia de seguridad, …). Este problema podría solucionarse en futuras versiones de wordpress (en el momento de escribir publicar este post estamos en la versión 3.0).

Dicho todo esto, hay que recalcar que no deberíamos preocuparnos en exceso, porque hasta ahora los reportes de este tipo de problemas han sido muy pocos. Pasemos entonces a ver los pros y contras de las estructuras más típicas.

- **/%categorie%/%postname%/**. Una de las favoritas si sólo consideramos aspectos SEO y no de rendimiento. Buena estructura porque añadimos keywords a través de la categoría y resulta más ordenado lo que es bueno para las SE y para el usuario. En el punto negativo antes de ponernos a escribir debemos tratar de pensar bien las categorías y no borrar o modificar categorías que ya hayamos usado. En definitiva nosotros mismos debemos ser ordenados y tener las cosas claras. Hay que tener cuidado si editamos el post en no cambiar las categorías porque podriamos cambiar la url. (Sucederá cuando la nueva categoría que añadamos tenga un id inferior a la actual). Si usamos categorías anidadas ambas se incluyen en la url (/blogging/wp/titulo). Esto genera estructura pero aleja a las páginas de la raíz y disminuye el rendimiento. El uso de esta estructura podría llegar a generar graves problemas de rendimiento
- **/%postname%/ o /%postname% o /%postname%.html**. La otra favorita de los expertos en SEO. Hay quien dice que Google concede más importancia a los archivos que cuelgan de la raíz, pero hay quien dice que tener todo en la raíz es malo porque no da importancia a unas cosas sobre otras y google prefiere el empleo de url más estructuradas. Por otro lado hay quien dice que google concede más importancia cuando las direcciones acaban en /, otros dicen que da más importancia a las páginas estáticas y por tanto conviene usar el .html. Dado que el algoritmo de clasificación es secreto debes optar por lo que crear que resulta menos confuso para los lectores, que en mi opinión es /%postname
- **/%year%/%month%/%postname%**. Esta es la estructura más usada, pero no la más recomendable. Incluír la fecha añade algo de información contextual a la url. Es la mejor opción, tanto en rendimiento como en SEO, si tu página está muy basada en eventos temporales, o públicas a menudo. El problema está, en que si escribes artículos genéricos, que es lo más habitual, puede dar la impresión de quedar desfasados cuando pasa cierto tiempo. Si escribimos mucho es buena idea para aportar información extra al lector. Lo malo es que se suelen crear muchos subdirectorios lo que no gusta a las SE. Aunque se podría usar algo tipo /%year%/%postname%/ solamente. Añade información a los lectores, que de un vistazo ven la época en que se escribió el post. Téngase en cuenta que esto es bueno para los lectores pero malo para el blog, porque muchos no entrarán si ven que la fecha es antigua. Empezar la url con números es lo más eficiente en cuanto a escalabilidad y tiempo de carga de la página.
- **/%postid%/posname%**. Mismas consideraciones que la anterior respecto a rendimiento y SEO. Si escribes poco o artículos muy genéricos posiblemente sea mejor esta.

## En resumen,

1. Cuando creas un nuevo blog lo primero que tienes que hacer es ir a Opciones-&gt;Permalinks y modificar la estructura por defecto.
2. Si tu blog es muy basado en eventos temporales en la casilla de «custom» escribe /%year%/%month%/%postname%
3. Si tu blog va a tener mucho tráfico o muchas páginas (del orden de miles) en la casilla «custom» escribe: /%postid%/%postname%
4. En caso contrario (este es el caso más habitual) escribe /%postname%

## Por que este blog usa otra estructura

Este blog incumple las conclusiones anteriores y usa la estructura /%postname%/%postid% esto es por dos motivos:

- Incluír números como el último punto de la url no limita demasiado el CT, la gente lee el dominio y a continuación las keywords, cuando llega a los números simplemente deja de leer, con lo que no hay una ruptura visual a la hora de asociar las keywords al dominio y se refuerza el branding.
- El segundo motivo es la creencia de que en un futuro cercano salga algún plugin para wordpress que interprete los permalinks de otra forma. Si en lugar de empezar a leer la url por la derecha, se empezara por la izquierda esta estructura sería de las más eficientes en cuanto a rendimiento.