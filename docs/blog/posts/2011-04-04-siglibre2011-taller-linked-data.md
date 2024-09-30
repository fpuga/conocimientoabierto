---
categories:
- General
date: 2011-04-04
permalink: /siglibre2011-taller-linked-data/295/
slug: siglibre2011-taller-linked-data
tags:
- girona
- gis
- linked data
- rdf
- siglibre2011
- web
- web semántica
---

# SigLibre2011: Taller Linked Data

Hace poco CartoLab me dió la oportunidad de asistir a las [V Jornadas de SIG Libre de Girona](http://www.sigte.udg.edu/jornadassiglibre2011/). El primer día, y a pesar de los temores de [Gonzalo](http://cartohistorias.blogspot.com/), llegamos a la sede de los talleres sin perdernos, aunque es de recibo decir que caimos de nuevo en el error del año pasado de intentar aparcar en el campus de la Facultat de Letres, lo que roza lo imposible, por lo que al final aparcamos en la ciudad y subimos andando (en realidad son apenas 10 minutitos de caminata).

El taller al que fuí por la mañana iba sobre [Linked Data](http://en.wikipedia.org/wiki/Linked_Data). Para mi gusto el taller acabo siendo más bien una clase teórica, por lo que por ahora para mi se queda en el cajón de “una esas tecnologías que habría que probar un día”.

LinkedData viene siendo un avance de cara a la [web semántica](http://es.wikipedia.org/wiki/Web_sem%C3%A1ntica), que se podría explicar diciendo algo así como que el objetivo es las webs no tengan datos si no información. Y esta información pueda estar enlazada y ser enlazable, no sólo en un formato entendible por los humanos, si no en un formato apto para que las máquinas puedan relacionarse entre sí. Ese lenguaje común que las máquinas podrían interpretar y en que se asienta el linked data es el [RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework). La [página de preguntas frecuentes de la web de Linked Data](http://linkeddata.org/faq) lo deja más claro de como lo puedo hacer yo.

Un ejemplo de las posibilidades sería por ejemplo que el IGN publicara un nomenclator en RDF. Cada uno de estos ficheritos RDF podría incluir el nombre del lugar y sus coordenadas geográficas. El INE en lugar de permitir bajarte csv podría publicar ficheros en RDF donde las estadísticas estuvieran enlazadas a los RDF que publica el nomeclator, lo que aportaría componente geográfica a los datos del INE sin que el INE se tuviera que preocupar de esta componente, sólo tendrían que enlazar una fuente fiable. Un tercero podría tomar ambos datos y proporcionar un servicio con ellos, por ejemplo rastrear las ofertas de trabajo de infojobs mezcladas con los datos del paro del INE y mostrar en un mapa que tipos de trabajo se ofrecen en los sitios donde hay más paro.

Me quedo con una de las frases del ponente que decía más o menos así:

> Lo bueno o lo malo de LinkedData es que el producir la información es muy costoso pero el consumirla es relativamente sencillo.

La verdad es que es una tecnología con muy buena pinta, por ejemplo [ya existen herramientas](http://www4.wiwiss.fu-berlin.de/bizer/d2r-server/) que permiten servir la información de una base de datos relacional en formato RDF, e interrogar a la BD mediante [SPARQL](http://www.w3.org/TR/rdf-sparql-query/).

Para saber más:

- [Linked Data](http://linkeddata.org/).
- [CKAN. The data hub](http://ckan.net/). Ejemplos de gente usando Linked Data, a los que podríamos enlazar nuestra propia información.
- http://geosparql.appspot.com/