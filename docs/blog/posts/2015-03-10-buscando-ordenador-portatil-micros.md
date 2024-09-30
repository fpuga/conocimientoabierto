---
categories:
- Sin categoría
date: 2015-03-10
permalink: /buscando-ordenador-portatil-micros/764/
slug: buscando-ordenador-portatil-micros
tags:
- comprar portátil
- hardware
- portátil
- recomendaciones
---

# Buscando ordenador portátil &#8211; Micros

En el [último artículo](http://conocimientoabierto.es/buscando-portatil-impresiones-foros-reviews/760/) veiamos que para encontrar un ordenador portátil adecuado (en rendimiento y presupuesto) uno los factores más importantes era el micro. Centrándonos en los Intel, la [wikipedia nos da un buen punto de entrada](http://en.wikipedia.org/wiki/Intel_Core). Lo primero a saber es que existen varias generaciones.

- La 5 generación de nombre Broadwell (o Intel Core 5th Gen) salió (aproximadamente) en Enero de 2015 y utiliza tecnología de 14nm
- La 4 generación de nombre Haswell (o Intel Core 4th Gen) salieron en Junio de 2013 y utiliza tecnología de 22nm
- La 3 generación lleva por nombre Ivy Bridge y es de 2012 así que la descartamos en el análisis.
- Por el medio tenemos el Haswell-E (Agosto de 2014) y el Ivi Bridge-E (Septiembre de 2013) de los que sólo hay versiones i7 también en 22nm.

Hasta donde he podido entender a pesar de ser un logro tecnológico importante [hasta finales de año probablemente no tenga mucho sentido comprar un ordenador con micro de 5 generación](http://www.trustedreviews.com/opinions/intel-s-14nm-revolution-everything-you-need-to-know). Tras la generación la forma de clasificarlos es por «familia» o «gama» (o «product line»). Donde las fundamentales para portátiles como el que buscamos serían:

- i3. Los de gama baja.
- i5. Gama media. En versón mobile, tienen 3M de cache, 2 cores y TDP de entre 11.5 y 47 con muy pocos siendo de 47.
- i7. Gama alta. En versión mobile, tienen entre 4 y 8M de cache, los hay de 2 y de 4 cores y TDP de entre 11.5 y 47 siendo la mayoría de 47.

Tanto los i5 como los i7 tienen Hyperthreading, Virtualización por hardware (VT-x) y Turbo Boost. Hay otras tecnologías (menos importantes para nuestro caso) como [VT-d](https://software.intel.com/en-us/blogs/2009/06/25/understanding-vt-d-intel-virtualization-technology-for-directed-io) que dependen del modelo concreto y no de ser i5 o i7. Además hay que tener en cuenta que en algunos portátiles se montan micros de desktop y no de mobile. Por ello al final es necesario consultar las [características concretas de cada micro](http://ark.intel.com/). Para orientarnos con los modelos es bueno saber que suelen tener cuatro números y a continuación 1 o más letras. El primero de los números hace referencia a la generación, y las letras del final depende. Si son:

- [K, X, S o T se refieren a modificaciones concretas sobre el micro](http://www.pugetsystems.com/labs/articles/Introduction-to-Intel-S-series-Processors-617/)
- Una M significa que es versión mobile con dos cores (aunque puede tener otro sufijo en lugar de la M y ser mobile igual)
- MQ o HQ significa que es mobile pero tiene cuatro cores. La [diferencia entre HQ y MQ](http://forum.notebookreview.com/threads/hq-vs-mq-processors.765365/) es que los HQ van soldados a la placa (más difíciles de cambiar por tanto, pero mi impresión es que ligeramente superiores para el mismo modelo) y los MQ no.
- U e Y significa que son pensados para ultrabooks porque tienen un menor consumo. Y menor consumo que U

Por ejemplo un [i7-4600M](http://ark.intel.com/products/76349/Intel-Core-i7-4600M-Processor-4M-Cache-up-to-3_60-GHz), es un i7 de cuarta generación mobile con dos cores mientras que un [i7-4770HQ](http://ark.intel.com/products/83505/Intel-Core-i7-4770HQ-Processor-6M-Cache-up-to-3_40-GHz) es un i7 de cuarta generación mobile con 4 cores. [Otro ejemplo](http://ark.intel.com/compare/76611,81016,81012,78929), un i5-4210Y consumirá menos que un i5-4210U que consumirá menos que un i5-4210M. Pero generalmente a menor consumo también menor velocidad de reloj y peor rendimiento.

## GPU

Los micros actuales llevan «incluida» una tarjeta gráfica en el propio micro, y por tanto sería algo a considerar a la hora de escoger micro pero por ahora vamos a obviarlo.

## Conclusiones

Lo que hemos visto en este artículo nos permite identificar a grandes rasgos las diferencias entre un micro y otro. Pero la pregunta más importante a resolver es al final si escoger un i7 con cuatro cores o un i5 con dos. Entender si para un caso concreto como el de escoger un ordenador para desarrollo es [mejor más cores o más velocidad de reloj](http://create.pro/blog/need-lots-cores-faster-cpu-clock-speed-cores-ghz-multi-threading-hyper-threading-explained/) es algo que resulta difícil de responder. ¿Alguna opinión? Pero teniendo varias aplicaciones, incluidos servidores y máquinar virtuales funcionando a la vez, sin ser ninguno de los procesos muy intensivos, parece lógico pensar que más cores aunque sea reduciendo la velocidad es la decisión acertada. Para tratar de reducir el precio en la [página de intel](http://ark.intel.com/) vemos que los modelos i7 del [470x al 472x](http://ark.intel.com/compare/75116,75117,75118,75119,78930,78931,78932,78933,78934,78935) serían buenas opciones, aunque como siempre al final dependerá de como cada fabricante monte el portátil.

## Referencias

- [Haswell Core i3 vs. i5 vs. i7 – Which is right for you?](http://www.pugetsystems.com/labs/articles/Haswell-Core-i3-vs-i5-vs-i7-Which-is-right-for-you-475/). Los comentarios son interesantes también.
- [Se queda algo viejo pero explica algunos términos como TDP](http://www.pugetsystems.com/labs/articles/Specs-Explained-CPU-137/#SmartCache)
- [Which CPU Should You Buy? Comparing Intel Core i5 vs. i7](http://www.pcmag.com/article2/0,2817,2404674,00.asp)

## Resto de artículos de esta serie

- [Buscando un portátil para programar](http://conocimientoabierto.es/buscando-portatil-programar/752/)
- [Buscando un portátil – Impresiones sacadas de foros y reviews](http://conocimientoabierto.es/buscando-portatil-impresiones-foros-reviews/760/)
- [Buscando ordenador portátil – Micros](http://conocimientoabierto.es/buscando-ordenador-portatil-micros/764/)
- [Buscando un portátil – Listado de candidatos entre 900 y 1150€](http://conocimientoabierto.es/buscando-portatil-listado-de-candidatos-entre-900-y-1150e)