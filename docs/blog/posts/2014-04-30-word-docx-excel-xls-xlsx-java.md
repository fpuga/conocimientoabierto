---
id: 699
title: 'Trabajar con Word (docx) y Excel (xls y xlsx) desde Java'
date: '2014-04-30T16:49:23+02:00'
author: fpuga
layout: post
guid: 'http://conocimientoabierto.es/?p=699'
permalink: /word-docx-excel-xls-xlsx-java/699/
categories:
    - 'Sin categoría'
tags:
    - cartolab
    - 'desarrollo sofware'
    - docx
    - excel
    - java
    - programación
    - word
    - xls
    - xlsx
---

![Iconos Word y Excel de MS Office](http://conocimientoabierto.es/wp-content/blogs.dir/16/files/galerias/enelblog/Word-y-Excel-de-Office.jpg)En [Cartolab](http://cartolab.udc.es/) hemos trabajado ultimamente en procesar y generar documentos de Excel (xls y xlsx) y de Word (docx) desde Java. Tras probar algunas librerías open source las que estamos usando son:

[Apache POI Spreadsheet](http://poi.apache.org/spreadsheet/index.html) para hojas de cálculo de Excel. Es fácil de usar y funciona bien tanto para los formatos binarios antiguos de xls (Excel 97-2007) como para xlsx (Excel 2007 OOXML). El [How-To](http://poi.apache.org/spreadsheet/how-to.html) y la [Quick Guide](http://poi.apache.org/spreadsheet/quick-guide.html) de la web son suficientes para empezar a escribir código.

[Docx4j](http://www.docx4java.org/trac/docx4j) para documentos docx (OpenXML de Word 2007). La mejor forma de usarla es crear un documento vacio o con las cabeceras y pies de página desde Word o LibreOffice y definir en él los estilos. Desde nuestro código abrimos el documento y vamos añadiendo nuevos párrafos u otros elementos asignándole los estilos que hemos definido mediante el método *addStyledParagraphOfText(styleID, text);*. El styleID lo obtendremos consultado el fichero *styles.xml* que está comprimido dentro del docx. Si tenemos que hacer cosas más elaboradas el código se complica bastante pero al menos permite hacerlas. Para arrancar puedes leer como [substituir placeholders por tu propio contenido](http://www.smartjava.org/content/create-complex-word-docx-documents-programatically-docx4j), este [otro artículo un poco más general](http://blog.iprofs.nl/2012/09/06/creating-word-documents-with-docx4j/) y los [ejemplos de código que vienen con la librería](https://github.com/plutext/docx4j/tree/master/src/samples/docx4j/org/docx4j/samples).

Para trabajar con documentos .doc de Word también probamos con [Apache POI](http://poi.apache.org/document/index.html) pero es complicado de usar y el resultado no es demasiado bueno. Así que por ahora no tenemos una alternativa válida para este formato.

En algún otro momento también hicimos pruebas con:

- [JasperReports](http://community.jaspersoft.com/project/jasperreports-library) que está muy bien para generar pdf pero el odt y el word lo saca maquetado en forma de tablas por lo que no nos valía.
- [iText](http://itextpdf.com/). Que en versiones antiguas de la librería permitía sacar los resultados en rtf y era sencilla de emplear. Pero las últimas versiones [se ha creado una nueva librería](http://sourceforge.net/projects/itextrtf/) que no hemos probado todavía.

En esta [pregunta de StackOverflow](http://stackoverflow.com/questions/203174/whats-a-good-java-api-for-creating-word-documents) dan más alternativas. ¿Alguien usa otras librerías, preferiblemente open source y gratuitas, distintas a estas?