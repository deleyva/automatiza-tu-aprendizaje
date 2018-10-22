# Leyendo de un CSV

Para leer datos de un archivo CSV con el módulo csv, debe crear un objeto Reader. Un objeto Reader le permite iterar sobre líneas en el archivo CSV. Ingrese lo siguiente en la shell interactiva, con [example.csv](https://raw.githubusercontent.com/deleyva/atuomatiza-tu-aprendizaje/master/example.csv) en el directorio de trabajo actual:

```python
>>> import csv
>>> exampleFile = open('example.csv')
>>> exampleReader = csv.reader(exampleFile)
>>> exampleData = list(exampleReader)
>>> exampleData
```

El módulo csv viene con Python, así que no hay que instalarlo.

Para leer los datos:

```python
>>> exampleData[0][0]
'4/5/2015 13:34'
>>> exampleData[0][1]
'Apples'
>>> exampleData[0][2]
'73'
>>> exampleData[1][1]
'Cherries'
>>> exampleData[6][1]
'Strawberries'
```

## Escribiendo en un .csv

```python
>>> import csv
>>> outputFile = open('output.csv', 'w', newline='')
>>> outputWriter = csv.writer(outputFile)
>>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
   21
>>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
   32
>>> outputWriter.writerow([1, 2, 3.141592, 4])
   16
>>> outputFile.close()
```

## Los argumentos 'delimiter' y 'lineterminator'

```python
>>> import csv
>>> csvFile = open('example.tsv', 'w', newline='')
>>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
>>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
   24
>>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
   17
>>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
   32
>>> csvFile.close()
```

Esto produce un archivo llamado example.tsv con el siguiente contenido:

apples  oranges grapes

eggs    bacon   ham
spam    spam    spam    spam    spam    spam

# JSON y APIs

La notación de objetos de JavaScript (Javascript Object Notation) es una forma popular de formatear datos como una sola cadena legible por humanos. JSON es la forma nativa en que los programas JavaScript escriben sus estructuras de datos y, por lo general, se parece a lo que produciría la función pprint() de Python. No necesitas saber JavaScript para trabajar con datos con formato JSON. Aquí hay un ejemplo de datos formateados como JSON:

```js
{"name": "Zophie", "isCat": true,
 "miceCaught": 0, "napsTaken": 37.5,
 "felineIQ": null}
```

Es útil saber JSON, ya que muchos sitios web ofrecen contenido JSON como una forma para que los programas interactúen con el sitio web. Esto se conoce como proporcionar una interfaz de programación de aplicaciones (API). 

Acceder a una API es lo mismo que acceder a cualquier otra página web a través de una URL. La diferencia es que los datos devueltos por una API están formateados (con JSON, por ejemplo) para las máquinas; Las API no son fáciles de leer para las personas.

Muchos sitios web hacen que sus datos estén disponibles en formato JSON. Facebook, Twitter, Yahoo, Google, Tumblr, Wikipedia, Flickr, Data.gov, Reddit, IMDb, Rotten Tomatoes, LinkedIn y muchos otros sitios populares ofrecen API para que otros programas las utilicen.

Algunos de estos sitios requieren registro, que casi siempre es gratis. Deberá buscar la documentación de las URL que debe solicitar su programa para obtener los datos que desea, así como el formato general de las estructuras de datos JSON que se devuelven. 

Esta documentación debe ser proporcionada por cualquier sitio que ofrezca la API; Si tienen una página de "Desarrolladores", busqua la documentación allí. Con las API, puede escribir programas que hagan lo siguiente: 
* Descarguen los datos sin procesar de los sitios web. (Acceder a las API suele ser más conveniente que descargar páginas web y analizar HTML con Beautiful Soup).
* Descarguen automáticamente las nuevas publicaciones de una de sus cuentas de redes sociales y publíquelas en otra cuenta. Por ejemplo, puedes tomar tus publicaciones de Tumblr y publicarlas en Facebook.
* Cree una "enciclopedia de películas" para su colección de películas personales extrayendo datos de IMDb, Rotten Tomatoes y Wikipedia y colocándolos en un solo archivo de texto en su computadora. Puede ver algunos ejemplos de API de JSON en los recursos en http://nostarch.com/automatestuff/.

## El módulo JSON

El módulo json de Python maneja todos los detalles de la traducción entre una cadena con datos JSON y los valores de Python para las funciones json.loads() y json.dumps(). JSON no puede almacenar todo tipo de valor de Python. Puede contener valores de solo los siguientes tipos de datos: cadenas, enteros, flotantes, booleanos, listas, diccionarios y NoneType. JSON no puede representar objetos específicos de Python, como objetos de archivo, objetos CSV Reader o Writer, objetos Regex u objetos Selenium WebElement.

## Leyendo un json con la función json.load()

```python
>>> stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,
"felineIQ": null}'
>>> import json
>>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
>>> jsonDataAsPythonValue
{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
```

## Escribiendo un json con la función json.dumps()

```python
>>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
>>> import json
>>> stringOfJsonData = json.dumps(pythonValue)
>>> stringOfJsonData
'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
```

