---
categories:
- Sin categoría
date: 2014-03-30
permalink: /organizar-ficheros-routes-nodejs-expressjs/685/
slug: organizar-ficheros-routes-nodejs-expressjs
tags:
- cartolab
- como
- desarrollo sofware
- desarrollo web
- expressjs
- how to
- javascript
- mvc
- nodejs
- web
---

# Organizar los ficheros de routes en nodejs &#8211; expressjs

Una de las tecnologías que estamos probando en [Cartolab](http://cartolab.udc.es) para aplicaciones web es [nodejs](http://nodejs.org/) con [express](http://expressjs.com/) como framework. Hay un montón de tutoriales de como empezar a usarlos, pero a poco que escribas empiezas a preguntarte como organizar el código, y ahí empiezan los problemas. *express* es un framework *no opinativo*, es decir proporciona un montón de utilidades pero da liberar total al usuario sobre como mezclarlas, así que se van desarrollando distintos modos de hacerlo.

La primera pregunta en mi casa sobre organizar el código fue acerca de los ficheros bajo el [directorio routes](http://stackoverflow.com/questions/4602212/organize-routes-in-node-js). Podemos entender las *routes* de *express* como el equivalente al controlador en [ese patrón llamado MVC](http://blog.codinghorror.com/understanding-model-view-controller/) que cada framework implementa como quiere, o viéndolo de otro modo como el mapeo entre una url y una función.

Vamos a ver cuatro estrategias distintas, cada una con sus ventajas e incovenientes.

## Todo en app.js

La versión que se suele emplear en los tutoriales de iniciación. Escribimos en un único fichero todo el código de la aplicación.

- Poco código [boilerplate](http://en.wikipedia.org/wiki/Boilerplate_code)
- Añadir una nueva url implica tocar un sólo fichero
- Nada reusable
- Sólo válido para proyectos pequeños

Es tan sencillo como escribir el mapeo antes de crear el servidor y usar funciones anónimas para la lógica

`<br></br>app.get('/', function(){res.send('root page'});<br></br>`

## Mapear en app y la lógica en ficheros distintos

Este es el segundo ejemplo más habitual. Las url se definen en el fichero principal y las funcionalidades se agrupan en distintos ficheros bajo el directorio *routes*.

- Añadir una nueva url implica tocar como mínimo dos ficheros
- Favorece la reutilización, pero siempre debemos colocar las url a mano
- Implica escribir más código que en el anterior y perder legibilidad

A pesar de que es muy habitual ver esto no me gusta porque no ganamos demasiado, y tener que hacer cambios en dos ficheros acaba introduciendo errores.

`<br></br>// app.js<br></br>var routes = require('./routes');  // Coje el fichero ./routes/index.js por defecto<br></br>var user = require('./routes/user');`

app.get('/', routes.index);  
app.get('/users', user.list);

`<br></br>// routes/user.js<br></br>exports.list = function(req, res){<br></br>res.send("respond with a resource");<br></br>};<br></br>`

`<br></br>// routes/index.js<br></br>exports.index = function(req, res){<br></br>res.send("root page");<br></br>};<br></br>`

## Hacer el objeto app global y derivar todo hacia los ficheros de routes

Evitamos declarar app como variable local, para poder usarla en el resto de ficheros sin tener que preocuparnos de pasar parámetros. El código queda muy limpio pero se dificulta el testing y se pueden introducir bugs difíciles de detectar.

A mi me gusta esta aproximación cuando tenemos poco código y queremos hacer algo rápido, pero hay que ser consciente de los problemas que tiene.

- No es una muy buena práctica hacer app global, en el siguiente punto vemos una mejora. Pero al hacerlo así obtenemos código más legible
- Es bastante modular (excepto por hacer app global)
- Es bastante legible
- Hay separación de conceptos, cada fichero se encarga de unas determinadas url y funcionalidades

**Referencias**

- [Effective node modules](http://dailyjs.com/2012/01/26/effective-node-modules/)
- [Global variable accesible in routes](http://stackoverflow.com/questions/9765215/global-variable-in-app-js-accessible-in-routes)

Veamos como quedaría la implementación

`<br></br>// app.js<br></br>app = express(); //IMPORTANT! define the global app variable prior to requiring routes!<br></br>require('./routes');<br></br>`

`<br></br>// routes/index.js<br></br>require('./main');<br></br>require('./users');<br></br>`

`<br></br>// routes/main.js<br></br>app.get('/', function(req, res) {<br></br>res.send("root page");<br></br>});<br></br>`

`<br></br>// routes/users.js. list() could be an anonymous function, this is only for showing it in another way.`

function list(req, res) {  
res.send("user list");  
};

app.get("/users", list);

## Inyectar app en los ficheros de routes

Es similar al ejemplo anterior, pero el objeto principal es inyectado en los controladores en lugar de usarlo como una variable global. Sacrificamos un poco de legibilidad (hay que meter bastante código «inútil») pero a cambio ganamos en modularidad y testabilidad.

Veamos una posible implementación, teniendo en cuenta que este código no lo he visto en ningún sitio, lo he escrito a partir del artículo de [dailyjs](http://dailyjs.com/2012/01/26/effective-node-modules/) y podría tener algún otro problema.

A mi esta es la aproximación que más me gusta, cuando el código aumenta y no nos queremos ir a soluciones más complicadas.

`<br></br>// app.js<br></br>var app = express();<br></br>// ...<br></br>app.use(express.json());<br></br>require('./routes')(app); // Must be called after app.use(express.json()) and urlencoded;<br></br>`

`<br></br>// routes/index.js<br></br>module.exports = function(app) {<br></br>require('./main')(app);<br></br>require('./users')(app);<br></br>};<br></br>`

`<br></br>// routes/main.js<br></br>module.exports = function(app) {<br></br>function index(req, res) {<br></br>res.send("root page");<br></br>};<br></br>app.get('/', index);<br></br>};<br></br>`

## Otras estrategias

Hay estrategias más complejas, que por ahora no me ha hecho falta probar.

- [Modular web applications with Node.js and Express](https://vimeo.com/56166857)
- [Organize routes in Node.js](http://stackoverflow.com/questions/4602212/organize-routes-in-node-js)
- [Understanding express routes](http://www.packtpub.com/article/understanding-express-routes "Understanding express routes")
- [How to estructure an expressjs application](http://stackoverflow.com/questions/5778245/expressjs-how-to-structure-an-application)