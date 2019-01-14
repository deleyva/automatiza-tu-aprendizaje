
<li class = "name">
<a aria-label="Index Page" href="//trinket.io/" role="button">
<img alt = "Trinket te ayuda a enseñar con el código" src = "/ cache-prefix-aac84e42 / img / trinket-logo.png" />
</a>
</ li>
- [](#)

- [<i class = "fa fa-star"> </i> Plans] (// trinket.io/plans)
- [<i class = "fa fa-graduation-cap"> </i> Learn] (https://hourofpython.com)
- [<i class = "fa fa-question-circle"> </i> Ayuda] (// trinket.io/help)
- [Registrarse] (// trinket.io/signup)
- [Iniciar sesión <i class = "fa fa-sign-in"> </i>] (// trinket.io/login)

<li class = "name">
<h1> [Python for Everybody] (https://books.trinket.io/pfe/index.html) </h1>
</ li>
- [Menú] (#)

<li>
<a href="https://books.trinket.io">
<i class = "fa fa-angle-left"> </i> Todos los libros de texto
</a>
</ li>

<li class = "has-dropdown">
[Capítulos] (#)
<ul class = "dropdown">
- [Ver todos los capítulos] (https://books.trinket.io/pfe/index.html)
- [Capítulo 1: Introducción] (https://books.trinket.io/pfe/01-intro.html)
- [Capítulo 2: Variables] (https://books.trinket.io/pfe/02-variables.html)
- [Capítulo 3: Condicionales] (https://books.trinket.io/pfe/03-conditional.html)
- [Capítulo 4: Funciones] (https://books.trinket.io/pfe/04-functions.html)
- [Capítulo 5: Iteraciones] (https://books.trinket.io/pfe/05-iterations.html)
- [Capítulo 6: Cadenas] (https://books.trinket.io/pfe/06-strings.html)
- [Capítulo 7: Archivos] (https://books.trinket.io/pfe/07-files.html)
- [Capítulo 8: Listas] (https://books.trinket.io/pfe/08-lists.html)
- [Capítulo 9: Diccionarios] (https://books.trinket.io/pfe/09-dictionaries.html)
- [Capítulo 10: Tuplas] (https://books.trinket.io/pfe/10-tuples.html)
- [Capítulo 11: Regex] (https://books.trinket.io/pfe/11-regex.html)
- [Capítulo 12: Programas en red] (https://books.trinket.io/pfe/12-network.html)
- [Capítulo 13: Python y servicios web] (https://books.trinket.io/pfe/13-web.html)
- [Capítulo 14: Objetos] (https://books.trinket.io/pfe/14-objects.html)
- [Capítulo 15: Python y bases de datos] (https://books.trinket.io/pfe/15-database.html)

<li class = "has-dropdown"> [Programación orientada a objetos] (# # programación orientada a objetos) <ul class = "dropdown">
- [Administración de programas más grandes] (# administrando programas más grandes)
- [Comenzando] (# comenzando)
- [Uso de objetos] (# using-objects)
- [Comenzando con Programas] (# comience con programas)
- [Subdivisión de un problema - Encapsulación] (# subdividing-a-problem --- encapsulation)
- [Nuestro primer objeto de Python] (# our-first-python-object)
- [Clases como tipos] (# clases-como-tipos)
- [Object Lifecycle] (# object-lifecycle)
- [Muchas instancias] (# muchas instancias)
- [Herencia] (# herencia)
- [Resumen] (# resumen)
- [Glosario] (# glosario)

# [Programación orientada a objetos] (# programación orientada a objetos)

## [Administrar programas más grandes] (# administrando programas más grandes)



Al comienzo de este libro, presentamos cuatro patrones de programación básicos que utilizamos para construir programas:

- código secuencial
- Código condicional (si las declaraciones)
- Código repetitivo (bucles)
- Almacenar y reutilizar (funciones)

En capítulos posteriores, exploramos variables simples y estructuras de datos de recopilación como listas, tuplas y diccionarios.

A medida que construimos programas, diseñamos estructuras de datos y escribimos código para manipular esas estructuras de datos. Hay muchas formas de escribir programas y, a estas alturas, es probable que haya escrito algunos programas que "no son tan elegantes" y otros que son "más elegantes". A pesar de que sus programas pueden ser pequeños, está empezando a ver cómo escribir código tiene un poco de "arte" y "estética".

A medida que los programas alcanzan millones de líneas, cada vez es más importante escribir código que sea fácil de entender. Si está trabajando en un programa de un millón de líneas, nunca podrá tener todo el programa en su mente al mismo tiempo. Por lo tanto, necesitamos formas de dividir el programa en múltiples partes más pequeñas para resolver un problema, corregir un error o agregar una nueva función que tenemos menos que ver.

En cierto modo, la programación orientada a objetos es una forma de organizar su código para que pueda ampliar a 500 líneas del código y entenderlo mientras ignora las otras 999,500 líneas de código por el momento.

## [Comenzando] (# comenzando)

Al igual que muchos aspectos de la programación, es necesario aprender los conceptos de programación orientada a objetos antes de poder usarlos de manera efectiva. Así que enfoca este capítulo como una manera de aprender algunos términos y conceptos y trabaja con algunos ejemplos simples para sentar las bases de un aprendizaje futuro. En el resto del libro usaremos objetos en muchos de los programas, pero no construiremos nuestros propios objetos nuevos en los programas.

El resultado clave de este capítulo es tener una comprensión básica de cómo se construyen los objetos y cómo funcionan y, lo que es más importante, cómo hacemos uso de las capacidades de los objetos que nos proporcionan las bibliotecas Python y Python.

## [Uso de objetos] (# using-objects)

Resulta que hemos estado utilizando objetos a lo largo de esta clase. Python nos proporciona muchos objetos incorporados. Aquí hay un código simple donde las primeras líneas deben ser muy simples y naturales para usted.



Pero en lugar de centrarse en lo que logran estas líneas, echemos un vistazo a lo que realmente está sucediendo desde el punto de vista de la programación orientada a objetos. No se preocupe si los siguientes párrafos no tienen ningún sentido la primera vez que los lee porque todavía no hemos definido todos estos términos.

La primera línea es ** construyendo ** un objeto del tipo ** lista **, la segunda y la tercera línea están llamando al método `append ()` ** **, la cuarta línea está llamando al `sort ()` * * método **, y la quinta línea está recuperando el artículo en la posición 0.

La sexta línea está llamando al método `__getitem __ ()` en la lista `stuff` con un parámetro de cero.

```print (stuff.__getitem__(0))
```
La séptima línea es una forma aún más detallada de recuperar el artículo 0 en la lista.

```print (list.__getitem__(stuff,0))
```
En este código, nos importa llamar al método `__getitem__` en la clase` list` y pasar la lista (`stuff`) y el elemento que queremos recuperar de la lista como parámetros.

Las últimas tres líneas del programa son completamente equivalentes, pero es más conveniente simplemente usar la sintaxis del corchete para buscar un elemento en una posición particular en una lista.

Podemos observar las capacidades de un objeto mirando la salida de la función `dir ()`:

```>>> stuff = list()
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__',
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__',
'__setitem__', '__sizeof__', '__str__', '__subclasshook__',
'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
```
La definición precisa de `dir ()` es que enumera los ** métodos ** y ** atributos ** de un objeto Python.

El resto de este capítulo definirá todos los términos anteriores, así que asegúrese de regresar después de terminar el capítulo y volver a leer los párrafos anteriores para verificar su comprensión.

## [Comenzando con programas] (# comenzando con programas)

Un programa en su forma más básica toma algo de entrada, realiza algún procesamiento y produce algo de salida. Nuestro programa de conversión de ascensores muestra un programa muy corto pero completo que muestra estos tres pasos.

Si pensamos un poco más en este programa, existe el "mundo exterior" y el programa. Los aspectos de entrada y salida son donde el programa interactúa con el mundo exterior. Dentro del programa, tenemos código y datos para realizar la tarea que el programa está diseñado para resolver.

A Program

Cuando estamos "en" el programa, tenemos algunas interacciones definidas con el mundo "externo", pero esas interacciones están bien definidas y generalmente no son algo en lo que nos enfocamos. Mientras estamos programando, nos preocupamos solo por los detalles "dentro del programa".

Una forma de pensar acerca de la programación orientada a objetos es que estamos separando nuestro programa en múltiples "zonas". Cada "zona" contiene algunos códigos y datos (como un programa) y tiene interacciones bien definidas con el mundo exterior y las otras zonas dentro del programa.

Si miramos hacia atrás en la aplicación de extracción de enlaces donde usamos la biblioteca BeautifulSoup, podemos ver un programa que se construye conectando diferentes objetos para realizar una tarea:



Leemos la URL en una cadena y luego la pasamos a `urllib` para recuperar los datos de la web. La biblioteca `urllib` usa la biblioteca` socket` para hacer la conexión de red real para recuperar los datos. Tomamos la cadena que recibimos de `urllib` y la entregamos a BeautifulSoup para que la analice. BeautifulSoup utiliza otro objeto llamado `html.parser` [<sup> 1 </sup>] (# fn1) y devuelve un objeto. Llamamos al método `tags ()` en el objeto devuelto y luego obtenemos un diccionario de objetos de etiquetas, hacemos un bucle a través de las etiquetas y llamamos al método `get ()` para que cada etiqueta imprima el atributo 'href'.

Un programa como red de objetos

Podemos dibujar una imagen de este programa y cómo los objetos trabajan juntos.

La clave aquí no es entender completamente cómo funciona este programa, sino ver cómo construimos una red de objetos interactivos y organizamos el movimiento de información entre los objetos para crear un programa. También es importante tener en cuenta que cuando miró ese programa varios capítulos atrás, podía entender completamente lo que estaba sucediendo en el programa sin siquiera darse cuenta de que el programa estaba "orquestando el movimiento de datos entre objetos". En ese entonces solo eran líneas de código las que hacían el trabajo.

## [Subdivisión de un problema: encapsulación] (# subdividing-a-problem --- encapsulation)

Una de las ventajas del enfoque orientado a objetos es que puede ocultar la complejidad. Por ejemplo, aunque necesitamos saber cómo usar el código `urllib` y BeautifulSoup, no necesitamos saber cómo funcionan internamente esas bibliotecas. Nos permite enfocarnos en la parte del problema que necesitamos para resolver e ignorar las otras partes del programa.

Ignorar los detalles al usar un objeto

Esta capacidad de centrarse en una parte de un programa que nos importa e ignorar el resto del programa también es útil para los desarrolladores de los objetos. Por ejemplo, los programadores que desarrollan BeautifulSoup no necesitan saber ni preocuparse sobre cómo recuperamos nuestra página HTML, qué partes queremos leer o qué planeamos hacer con los datos que extraemos de la página web.

Ignorar los detalles al construir un objeto



Otra palabra que usamos para capturar esta idea de que ignoramos los detalles internos de los objetos que usamos es "encapsulación". Esto significa que podemos saber cómo usar un objeto sin saber cómo cumple internamente lo que debemos hacer.

## [Nuestro primer objeto Python] (# our-first-python-object)

En su forma más simple, un objeto es un código más estructuras de datos que es más pequeño que un programa completo. Definir una función nos permite almacenar un poco de código y darle un nombre y luego invocar ese código usando el nombre de la función.

Un objeto puede contener una serie de funciones (que denominamos "métodos"), así como los datos que utilizan esas funciones. Llamamos a los elementos de datos que forman parte de los "atributos" del objeto.



Usamos la palabra clave `class` para definir los datos y el código que conformará cada uno de los objetos. La palabra clave de clase incluye el nombre de la clase y comienza un bloque de código con sangría donde incluimos los atributos (datos) y los métodos (código).

Cada método se parece a una función, comenzando con la palabra clave `def` y consiste en un bloque de código con sangría. Este ejemplo tiene un atributo (x) y un método (parte). Los métodos tienen un primer parámetro especial que nombramos por convención `self`.

Al igual que la palabra clave `def` no hace que se ejecute el código de función, la palabra clave` class` no crea un objeto. En cambio, la palabra clave `class` define una plantilla que indica qué datos y código estarán contenidos en cada objeto de tipo` PartyAnimal`. La clase es como un cortador de galletas y los objetos creados usando la clase son las cookies [<sup> 2 </sup>] (# fn2). No coloque glaseado en el cortador de galletas, coloque glaseado en las galletas y puede colocar glaseado diferente en cada galleta.

Una clase y dos objetos

Si continúa con el código de ejemplo, vemos la primera línea de código ejecutable:

```an = PartyAnimal()
```


Aquí es donde le pedimos a Python que construya (por ejemplo, cree) un ** objeto ** o "instancia de la clase llamada PartyAnimal". Parece una llamada de función a la clase en sí misma y Python construye el objeto con los métodos y datos correctos y devuelve el objeto que luego se asigna a la variable `an`. En cierto modo, esto es bastante similar a la siguiente línea que hemos estado usando todo este tiempo:

```counts = dict()
```
Aquí le estamos indicando a Python que construya un objeto usando la plantilla `dict` (ya presente en Python), devuelva la instancia del diccionario y asigne la variable a` count`.

Cuando la clase PartyAnimal se usa para construir un objeto, la variable `an` se usa para apuntar a ese objeto. Usamos `an` para acceder al código y los datos para esa instancia particular de un objeto PartyAnimal.

Cada objeto / instancia de Partyanimal contiene en su interior una variable `x` y un método / función llamado` party`. Llamamos a ese método `party` en esta línea:

```an.party()
```
Cuando se llama al método `party`, el primer parámetro (al que llamamos por convención` self`) apunta a la instancia particular del objeto PartyAnimal que llama a `party` desde dentro. Dentro del método `party`, vemos la línea:

```self.x = self.x + 1
```
Esta sintaxis que usa el operador 'punto' está diciendo 'la x dentro de uno mismo'. Entonces, cada vez que se llama a `party ()`, el valor interno de `x` se incrementa en 1 y el valor se imprime.

Para ayudar a entender la diferencia entre una función global y un método dentro de una clase / objeto, la siguiente línea es otra forma de llamar al método `party` dentro del objeto` an`:

```PartyAnimal.party(an)
```
En esta variación, accedemos al código desde dentro de la ** clase ** y pasamos explícitamente el puntero del objeto `an` como primer parámetro (es decir,` self` dentro del método). Puede pensar en `an.party ()` como una abreviatura de la línea anterior.

Cuando el programa se ejecuta, produce el siguiente resultado:

```So far 1
So far 2
So far 3
So far 4
```
El objeto se construye y el método `party` se llama cuatro veces, incrementando e imprimiendo el valor de` x` dentro del objeto `an`.

## [Clases como tipos] (# clases-como-tipos)



Como hemos visto, en Python, todas las variables tienen un tipo. Y podemos usar la función `dir` incorporada para examinar las capacidades de una variable. Podemos usar `type` y` dir` con las clases que creamos.

Cuando este programa se ejecuta, produce la siguiente salida:

```Type &lt;class '__main__.PartyAnimal'&gt;
Dir  ['__class__', '__delattr__', ...
'__sizeof__', '__str__', '__subclasshook__',
'__weakref__', 'party', 'x']
Type &lt;class 'int'&gt;
Type &lt;class 'method'&gt;
```
Puedes ver que usando la palabra clave `class`, hemos creado un nuevo tipo. Desde la salida de `dir`, puede ver que tanto el atributo de entero` x` como el método `party` están disponibles en el objeto.

## [Object Lifecycle] (# object-lifeecycle)



En los ejemplos anteriores, estamos definiendo una clase (plantilla) y usando esa clase para crear una instancia de esa clase (objeto) y luego usando la instancia. Cuando el programa termina, todas las variables se descartan. Por lo general, no pensamos mucho en la creación y destrucción de variables, pero a menudo, a medida que nuestros objetos se vuelven más complejos, debemos tomar alguna acción dentro del objeto para configurar las cosas a medida que se está construyendo el objeto y posiblemente limpiar las cosas a medida que objeto está siendo descartado.

Si queremos que nuestro objeto sea consciente de estos momentos de construcción y destrucción, agregamos métodos especialmente nombrados a nuestro objeto:

Cuando este programa se ejecuta, produce la siguiente salida:

```I am constructed
So far 1
So far 2
I am destructed 2
an contains 42
```
Como Python está construyendo nuestro objeto, llama a nuestro método `__init__` para darnos la oportunidad de configurar algunos valores predeterminados o iniciales para el objeto. Cuando Python encuentra la línea:

```an = 42
```
En realidad, "deja a un lado nuestro objeto", por lo que puede reutilizar la variable `an` para almacenar el valor` 42`. Justo en el momento en que nuestro objeto `an` se está 'destruyendo', se llama a nuestro código destructor (` __del__`). No podemos evitar que nuestra variable se destruya, pero podemos hacer cualquier limpieza necesaria justo antes de que nuestro objeto ya no exista.

Cuando se desarrollan objetos, es bastante común agregar un constructor a un objeto para que se establezca en los valores iniciales del objeto, es relativamente raro que se necesite un destructor para un objeto.

## [Muchas instancias] (# muchas instancias)

Hasta ahora, hemos estado definiendo una clase, creando un solo objeto, utilizando ese objeto y luego desechando el objeto. Pero el poder real en la orientación a objetos ocurre cuando hacemos muchos ejemplos de nuestra clase.

Cuando creamos varios objetos de nuestra clase, es posible que deseamos configurar diferentes valores iniciales para cada uno de los objetos. Podemos pasar datos a los constructores para dar a cada objeto un valor inicial diferente:

El constructor tiene un parámetro 'self' que apunta a la instancia del objeto y luego los parámetros adicionales que se pasan al constructor a medida que se construye el objeto:

```s = PartyAnimal('Sally')
```
Dentro del constructor, la línea:

```self.name = nam
```
Copia el parámetro que se pasa (`nam`) en el atributo` name` dentro de la instancia del objeto.

La salida del programa muestra que cada uno de los objetos (`s` y` j`) contienen sus propias copias independientes de `x` y` nam`:

```Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Sally party count 2
```
## [Herencia] (# herencia)

Otra característica poderosa de la programación orientada a objetos es la capacidad de crear una nueva clase al extender una clase existente. Al extender una clase, llamamos a la clase original "clase principal" y a la nueva clase como "clase secundaria".

Para este ejemplo, moveremos nuestra clase `PartyAnimal` a su propio archivo:

Luego, podemos 'importar' la clase `PartyAnimal` en un nuevo archivo y extenderlo de la siguiente manera:

Cuando estamos definiendo el objeto `CricketFan`, indicamos que estamos extendiendo la clase` PartyAnimal`. Esto significa que todas las variables (`x`) y métodos (` party`) de la clase `PartyAnimal` son heredadas por la clase` CricketFan`.

Puedes ver que dentro del método `six` en la clase` CricketFan`, podemos llamar al método `party` desde la clase` PartyAnimal`. Las variables y los métodos de la clase principal se ** fusionan ** en la clase secundaria.

A medida que se ejecuta el programa, podemos ver que `s` y` j` son instancias independientes de `PartyAnimal` y` CricketFan`. El objeto `j` tiene capacidades adicionales más allá del objeto` s`.

```Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Jim party count 2
Jim points 6
['__class__', '__delattr__', ... '__weakref__',
'name', 'party', 'points', 'six', 'x']
```
En la salida de `dir` para el objeto` j` (instancia de la clase `CricketFan`) puede ver que tiene los atributos y métodos de la clase principal, así como los atributos y métodos que se agregaron cuando la clase era ampliado para crear la clase `CricketFan`.

## [Resumen] (# resumen)

Esta es una introducción muy rápida a la programación orientada a objetos que se centra principalmente en la terminología y la sintaxis de definir y utilizar objetos. Revisemos rápidamente el código que vimos al principio del capítulo. En este punto, debe comprender completamente lo que está sucediendo.

La primera línea construye un objeto `list` ** **. Cuando Python crea el objeto `list`, llama al método ** constructor ** (denominado` __init__`) para configurar los atributos de datos internos que se utilizarán para almacenar los datos de la lista. Debido a la ** encapsulación ** no necesitamos saber, ni tenemos que preocuparnos por esto, ya que los atributos de datos internos están ordenados.

No estamos pasando ningún parámetro al ** constructor ** y cuando el constructor regresa, usamos la variable `stuff` para señalar la instancia devuelta de la clase` list`.

Las líneas segunda y tercera están llamando al método `append` con un parámetro para agregar un nuevo elemento al final de la lista al actualizar los atributos dentro de` stuff`. Luego, en la cuarta línea, llamamos al método `sort` sin parámetros para ordenar los datos dentro del objeto` stuff`.

Luego imprimimos el primer elemento de la lista usando los corchetes, que son un atajo para llamar al método `__getitem__` dentro del objeto` stuff` ** **. Y esto es equivalente a llamar al método `__getitem__` en la clase` list` ** ** pasando el objeto `stuff` como primer parámetro y la posición que estamos buscando como segundo parámetro.

Al final del programa, el objeto `stuff` se descarta, pero no antes de llamar al ** destructor ** (llamado` __del__`) para que el objeto pueda limpiar los cabos sueltos según sea necesario.

Esos son los fundamentos y la terminología de la programación orientada a objetos. Hay muchos detalles adicionales sobre cómo usar mejor los enfoques orientados a objetos al desarrollar aplicaciones y bibliotecas grandes que están fuera del alcance de este capítulo. [<sup> 3 </sup>] (# fn3)

## [Glosario] (# glosario)



















---


1. https://docs.python.org/3/library/html.parser.html[↩](#fnref1)
1. La imagen de la cookie está protegida por derechos de autor de CC-BY https://www.flickr.com/photos/dinnerseries/23570475099[#◆(#fnref2)
1. Si tiene curiosidad por saber dónde está definida la clase de la lista, eche un vistazo (esperemos que la URL no cambie) https://github.com/python/cpython/blob/master/Objects/listobject.c - el La lista de clases está escrita en un lenguaje llamado "C". Si echas un vistazo a ese código fuente y te resulta curioso, quizás quieras explorar algunos cursos de informática. [↩] (# fnref3)

Derechos de autor de la imagen de la cookie CC-BY https://www.flickr.com/photos/dinnerseries/23570475099[↩◆(#fnref2)

© 2015-2018 Baratija

#### Sobre nosotros

- [Nuestra historia] (// trinket.io/our-story)
<li> [Blog] (http://blog.trinket.io)
<li> [Asociaciones] (// trinket.io/partners)
</ Li> </ li>
#### Soporte

- [Preguntas frecuentes] (// trinket.io/faq)
- [Ayuda] (// trinket.io/help)
- [Contáctenos] (// trinket.io/contact)

#### Legal

- [Términos de servicio] (// trinket.io/tos)
- [Privacidad] (// trinket.io/privacy)

#### Conectar
