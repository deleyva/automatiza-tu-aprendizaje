# Llamadas a funciones

Siempre acompañadas de paréntesis. Dentro podemos pasarle parámetros.

```python
type(32)
int
```

### Built-in functions

```python
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('Hello world')
```

### Funciones de conversiones de tipos o casting

```python
>>> int(3.99999)
3
>>> int(-2.3)
-2
```

### Funciones matemáticas

```python
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio)

>>> radians = 0.7
>>> height = math.sin(radians)

>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865476

>>> math.sqrt(2) / 2.0
0.7071067811865476
```

### Poniendo en práctica

<iframe src="https://trinket.io/embed/python3/6c4060f81d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Parámetros y argumentos

Algunas de las funciones incorporadas que hemos visto requieren argumentos. Por ejemplo, cuando llamas math.sin pasas un número como argumento. Algunas funciones toman más de un argumento: math.pow toma dos, la base y el exponente.

Dentro de la función, los argumentos se asignan a variables llamadas parámetros. Aquí hay un ejemplo de una función definida por el usuario que toma un argumento:

```python
def print_twice(bruce):
    print(bruce)
    print(bruce)
```

### Funciones fructíferas y funciones 'nulas' (void)

Algunas de las funciones que utilizamos, como las funciones matemáticas, producen resultados, a falta de un nombre mejor, las llamaremos funciones fructíferas. Otras funciones, como print_twice, realizan una acción pero no devuelven un valor. Se llaman funciones nulas. Cuando llama a una función fructífera, casi siempre quiere hacer algo con el resultado; por ejemplo, puede asignarlo a una variable o usarlo como parte de una expresión:

```python
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
```

Cuando llamas a una función en el modo interactivo, Python muestra el resultado.

```python
>>> math.sqrt(5)
2.23606797749979
```

En un script, si llamas a una función fructífera y no almacena el resultado de la función en una variable, el valor de retorno desaparece.

```python
math.sqrt(5)
```

Para devolver un resultado de una función, usamos la instrucción return en nuestra función. Por ejemplo, podríamos hacer una función muy simple llamada addtwo que sume dos números y devuelva un resultado.

<iframe src="https://trinket.io/embed/python3/4bfd83e7d0" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



<!--
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

<li class = "has-dropdown"> [Funciones] (# funciones) <ul class = "dropdown">
- [Llamadas de función] (# función-llamadas)
- [Funciones integradas] (# funciones incorporadas)
- [Funciones de conversión de tipo] (# tipo-conversión-funciones)
- [Números aleatorios] (# números aleatorios)
- [Funciones matemáticas] (# math-funciones)
- [Agregar nuevas funciones] (# agregando-nuevas-funciones)
- [Definiciones y usos] (# definiciones y usos)
- [Flujo de ejecución] (# flujo de ejecución)
- [Parámetros y argumentos] (# parámetros-y-argumentos)
- [Funciones fructíferas y funciones nulas] (# funciones fructíferas y funciones nulas)
- [¿Por qué funciona?] (# Por qué-funciones)
- [Depuración] (# depuración)
- [Glosario] (# glosario)
- [Ejercicios] (# ejercicios)

# [Funciones] (# funciones)

## [Llamadas de función] (# función-llamadas)



En el contexto de la programación, una función ** es una secuencia de instrucciones con nombre que realiza un cálculo. Cuando define una función, especifica el nombre y la secuencia de instrucciones. Más tarde, puede "llamar" a la función por su nombre. Ya hemos visto un ejemplo de una función ** llamada **:

```>>> type(32)
&lt;class 'int'&gt;
```
El nombre de la función es `tipo`. La expresión entre paréntesis se llama el ** argumento ** de la función. El argumento es un valor o variable que estamos pasando a la función como entrada a la función. El resultado, para la función `type`, es el tipo del argumento.



Es común decir que una función "toma" un argumento y "devuelve" un resultado. El resultado se llama el ** valor de retorno **.



## [Funciones incorporadas] (# incorporadas en funciones)

Python proporciona una serie de funciones integradas importantes que podemos usar sin necesidad de proporcionar la definición de la función. Los creadores de Python escribieron un conjunto de funciones para resolver problemas comunes y las incluyeron en Python para que las utilicemos.

Las funciones `max` y` min` nos dan los valores más grandes y más pequeños en una lista, respectivamente:

```>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>>
```
La función `max` nos dice el" carácter más grande "en la cadena (que resulta ser la letra" w ") y la función` min` nos muestra el carácter más pequeño (que es un espacio).

Otra función incorporada muy común es la función `len` que nos dice cuántos elementos hay en su argumento. Si el argumento a `len` es una cadena, devuelve el número de caracteres en la cadena.

```>>> len('Hello world')
11
>>>
```
Estas funciones no se limitan a mirar las cadenas. Pueden operar en cualquier conjunto de valores, como veremos en capítulos posteriores.

Debe tratar los nombres de las funciones incorporadas como palabras reservadas (es decir, evitar usar "max" como nombre de variable).

## [Funciones de conversión de tipos] (# funciones de conversión de tipos)



Python también proporciona funciones integradas que convierten valores de un tipo a otro. La función `int` toma cualquier valor y lo convierte en un entero, si puede, o se queja de lo contrario:



```>>> int('32')
32
>>> int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
```
`int` puede convertir valores de coma flotante en enteros, pero no se redondea; corta la parte de la fracción

```>>> int(3.99999)
3
>>> int(-2.3)
-2
```
`float` convierte números enteros y cadenas en números de punto flotante:



```>>> float(32)
32.0
>>> float('3.14159')
3.14159
```
Finalmente, `str` convierte su argumento en una cadena:



```>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
```
## [Números aleatorios] (# números aleatorios)



Dadas las mismas entradas, la mayoría de los programas de computadora generan las mismas salidas cada vez, por lo que se dice que son ** deterministas **. El determinismo suele ser algo bueno, ya que esperamos que el mismo cálculo dé el mismo resultado. Para algunas aplicaciones, sin embargo, queremos que la computadora sea impredecible. Los juegos son un ejemplo obvio, pero hay más.

Hacer que un programa sea realmente no determinista resulta no ser tan fácil, pero hay formas de que al menos parezca no determinista. Uno de ellos es utilizar ** algoritmos ** que generan ** números pseudoaleatorios **. Los números pseudoaleatorios no son realmente aleatorios porque son generados por un cálculo determinista, pero con solo mirar los números es casi imposible distinguirlos de los aleatorios.



El módulo "aleatorio" proporciona funciones que generan números pseudoaleatorios (que a partir de ahora llamaré "aleatorios").



La función `random` devuelve un float aleatorio entre 0.0 y 1.0 (incluyendo 0.0 pero no 1.0). Cada vez que llamas `random`, obtienes el siguiente número en una larga serie. Para ver una muestra, ejecute este bucle:

```import random

for i in range(10):
    x = random.random()
    print(x)
```
Este programa produce la siguiente lista de 10 números aleatorios entre 0.0 y hasta, pero sin incluir 1.0.

```0.11132867921152356
0.5950949227890241
0.04820265884996877
0.841003109276478
0.997914947094958
0.04842330803368111
0.7416295948208405
0.510535245390327
0.27447040171978143
0.028511805472785867
```
Ejercicio 1: Ejecute el programa en su sistema y vea qué números obtiene. Ejecute el programa más de una vez y vea qué números obtiene.

La función `random` es solo una de las muchas funciones que manejan números aleatorios. La función `randint` toma los parámetros` low` y `high`, y devuelve un número entero entre` low` y `high` (incluyendo ambos).



```>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
9
```
Para elegir un elemento de una secuencia al azar, puedes usar `choice`:



```>>> t = [1, 2, 3]
>>> random.choice(t)
2
>>> random.choice(t)
3
```
El módulo `random` también proporciona funciones para generar valores aleatorios a partir de distribuciones continuas que incluyen Gaussian, exponential, gamma y algunas más.

## [Funciones matemáticas] (# funciones matemáticas)



Python tiene un módulo `math` que proporciona la mayoría de las funciones matemáticas conocidas. Antes de que podamos usar el módulo, tenemos que importarlo:

```>>> import math
```
Esta declaración crea un ** objeto de módulo ** llamado math. Si imprime el objeto de módulo, obtiene alguna información al respecto:

```>>> print(math)
&lt;module 'math' (built-in)&gt;
```
El objeto módulo contiene las funciones y variables definidas en el módulo. Para acceder a una de las funciones, debe especificar el nombre del módulo y el nombre de la función, separados por un punto (también conocido como un punto). Este formato se llama ** notación de puntos **.



```>>> ratio = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio)

>>> radians = 0.7
>>> height = math.sin(radians)
```
El primer ejemplo calcula la base logarítmica 10 de la relación señal-ruido. El módulo matemático también proporciona una función llamada `log` que calcula los logaritmos base` e`.



El segundo ejemplo encuentra el seno de 'radianes'. El nombre de la variable es un indicio de que `sin` y las otras funciones trigonométricas (` cos`, `tan`, etc.) toman argumentos en radianes. Para convertir de grados a radianes, divide por 360 y multiplica por 2 ** π **:

```>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865476
```
La expresión `math.pi` obtiene la variable` pi` del módulo matemático. El valor de esta variable es una aproximación de ** π **, con una precisión de aproximadamente 15 dígitos.



Si conoce su trigonometría, puede verificar el resultado anterior comparándolo con la raíz cuadrada de dos dividido por dos:



```>>> math.sqrt(2) / 2.0
0.7071067811865476
```
## [Agregar nuevas funciones] (# agregar nuevas funciones)




Aquí hay un ejemplo:

```def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
```
`def` es una palabra clave que indica que esta es una definición de función. El nombre de la función es `print_lyrics`. Las reglas para los nombres de funciones son las mismas que para los nombres de variables: las letras, los números y algunos signos de puntuación son legales, pero el primer carácter no puede ser un número. No puede usar una palabra clave como el nombre de una función, y debe evitar tener una variable y una función con el mismo nombre.



Los paréntesis vacíos después del nombre indican que esta función no acepta ningún argumento. Más adelante construiremos funciones que toman argumentos como sus entradas.



La primera línea de la definición de la función se llama el ** encabezado **; el resto se llama el ** cuerpo **. El encabezado debe terminar con dos puntos y el cuerpo debe estar sangrado. Por convención, la sangría es siempre de cuatro espacios. El cuerpo puede contener cualquier número de declaraciones.

Las cadenas en las declaraciones impresas están entre comillas. Las comillas simples y las comillas dobles hacen lo mismo; la mayoría de las personas usan comillas simples, excepto en casos como este, donde aparece una comilla simple (que también es un apóstrofe) en la cadena.



Si escribe una definición de función en modo interactivo, el intérprete imprime puntos suspensivos (** ... **) para hacerle saber que la definición no está completa:

```>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.")
...     print('I sleep all night and I work all day.')
...
```
Para finalizar la función, debe ingresar una línea vacía (esto no es necesario en un script).

La definición de una función crea una variable con el mismo nombre.

```>>> print(print_lyrics)
&lt;function print_lyrics at 0xb7e99e9c&gt;
>>> print(type(print_lyrics))
&lt;class 'function'&gt;
```
El valor de `print_lyrics` es un ** objeto de función **, que tiene el tipo" función ".



La sintaxis para llamar a la nueva función es la misma que para las funciones incorporadas:

```>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```
Una vez que haya definido una función, puede usarla dentro de otra función. Por ejemplo, para repetir el refrán anterior, podríamos escribir una función llamada `repeat_lyrics`:

```def repeat_lyrics():
    print_lyrics()
    print_lyrics()
```
Y luego llamar a "repeat_lyrics":

```>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```
Pero eso no es realmente cómo va la canción.

## [Definiciones y usos] (# definiciones-y-usos)



Recopilando los fragmentos de código de la sección anterior, todo el programa se ve así:

Este programa contiene dos definiciones de funciones: `print_lyrics` y` repeat_lyrics`. Las definiciones de funciones se ejecutan igual que otras declaraciones, pero el efecto es crear objetos de funciones. Las sentencias dentro de la función no se ejecutan hasta que se llama a la función, y la definición de la función no genera salida.



Como es de esperar, debe crear una función antes de poder ejecutarla. En otras palabras, la definición de la función debe ejecutarse antes de la primera vez que se llama.

Ejercicio 2: Mueva la última línea de este programa a la parte superior, para que la llamada a la función aparezca antes de las definiciones. Ejecute el programa y vea qué mensaje de error recibe.

Ejercicio 3: Mueva la llamada de la función a la parte inferior y mueva la definición de `print_lyrics` después de la definición de` repeat_lyrics`. ¿Qué pasa cuando ejecutas este programa?

## [Flujo de ejecución] (# flujo de ejecución)



Para garantizar que una función se define antes de su primer uso, debe conocer el orden en que se ejecutan las instrucciones, lo que se denomina ** flujo de ejecución **.

La ejecución siempre comienza en la primera declaración del programa. Las declaraciones se ejecutan de una en una, en orden de arriba a abajo.

Las definiciones de la función ** no alteran el flujo de ejecución del programa, pero recuerde que las sentencias dentro de la función no se ejecutan hasta que se llama a la función.

Una llamada de función es como un desvío en el flujo de ejecución. En lugar de ir a la siguiente instrucción, el flujo salta al cuerpo de la función, ejecuta todas las declaraciones allí y luego vuelve a retomar donde se detuvo.
Eso suena bastante simple, hasta que recuerdas que una función puede llamar a otra. Mientras se encuentra en medio de una función, el programa podría tener que ejecutar las instrucciones en otra función. ¡Pero mientras ejecuta esa nueva función, el programa podría tener que ejecutar otra función!

Afortunadamente, Python es bueno para mantener un registro de dónde está, por lo que cada vez que una función se completa, el programa retoma el lugar donde se quedó en la función que lo llamó. Cuando llega al final del programa, termina.

¿Cuál es la moraleja de este sórdido cuento? Cuando lees un programa, no siempre quieres leer de arriba a abajo. A veces tiene más sentido si sigues el flujo de ejecución.

## [Parámetros y argumentos] (# parámetros-y-argumentos)



Algunas de las funciones incorporadas que hemos visto requieren argumentos. Por ejemplo, cuando llamas `math.sin` pasas un número como argumento. Algunas funciones toman más de un argumento: `math.pow` toma dos, la base y el exponente.

Dentro de la función, los argumentos se asignan a variables llamadas ** parámetros **. Aquí hay un ejemplo de una función definida por el usuario que toma un argumento:



```def print_twice(bruce):
    print(bruce)
    print(bruce)
```
Esta función asigna el argumento a un parámetro llamado `bruce`. Cuando se llama a la función, imprime el valor del parámetro (cualquiera que sea) dos veces.

Esta función funciona con cualquier valor que se pueda imprimir.

```>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
```
Las mismas reglas de composición que se aplican a las funciones integradas también se aplican a las funciones definidas por el usuario, por lo que podemos usar cualquier tipo de expresión como argumento para `print_twice`:



```>>> print_twice('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
```
El argumento se evalúa antes de llamar a la función, por lo que en los ejemplos las expresiones "Spam '* 4`and`math.cos (math.pi)` solo se evalúan una vez.



También puedes usar una variable como argumento:

```>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
```
El nombre de la variable que pasamos como argumento (`michael`) no tiene nada que ver con el nombre del parámetro (` bruce`). No importa cómo se llamó el valor de regreso a casa (en la persona que llama); Aquí en `print_twice`, llamamos a todos` bruce`.

## [Funciones fructíferas y funciones nulas] (# funciones fructíferas y funciones nulas)



Algunas de las funciones que utilizamos, como las funciones matemáticas, producen resultados; A falta de un nombre mejor, los llamo ** funciones fructíferas **. Otras funciones, como `print_twice`, realizan una acción pero no devuelven un valor. Se les llama ** funciones nulas **.

Cuando llama a una función fructífera, casi siempre quiere hacer algo con el resultado; por ejemplo, puede asignarlo a una variable o usarlo como parte de una expresión:

```x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
```
Cuando llamas a una función en modo interactivo, Python muestra el resultado:

```>>> math.sqrt(5)
2.23606797749979
```
Pero en un script, si llama a una función fructífera y no almacena el resultado de la función en una variable, el valor de retorno desaparece en la niebla.

```math.sqrt(5)
```
Este script calcula la raíz cuadrada de 5, pero como no almacena el resultado en una variable ni muestra el resultado, no es muy útil.



Las funciones anuladas pueden mostrar algo en la pantalla o tener algún otro efecto, pero no tienen un valor de retorno. Si intenta asignar el resultado a una variable, obtiene un valor especial llamado `Ninguno`.



```>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
```
El valor `Ninguno` no es el mismo que la cadena" Ninguno ". Es un valor especial que tiene su propio tipo:

```>>> print(type(None))
&lt;class 'NoneType'&gt;
```
Para devolver un resultado de una función, usamos la declaración `return` en nuestra función. Por ejemplo, podríamos hacer una función muy simple llamada `addtwo` que suma dos números y devuelve un resultado.

Cuando este script se ejecute, la instrucción `print` imprimirá" 8 "porque la función` addtwo` fue llamada con 3 y 5 como argumentos. Dentro de la función, los parámetros `a` y` b` fueron 3 y 5 respectivamente. La función calculó la suma de los dos números y la colocó en la variable de función local denominada `added`. Luego usó la declaración `return` para enviar el valor calculado al código de llamada como el resultado de la función, que se asignó a la variable` x` y se imprimió.

## [¿Por qué funciona?] (# Por qué-funciones)



Puede que no esté claro por qué vale la pena dividir un programa en funciones. Hay varias razones:

- La creación de una nueva función le brinda la oportunidad de nombrar un grupo de declaraciones, lo que hace que su programa sea más fácil de leer, comprender y depurar.
- Las funciones pueden hacer que un programa sea más pequeño eliminando el código repetitivo. Más tarde, si realiza un cambio, solo tendrá que hacerlo en un lugar.
- La división de un programa largo en funciones le permite depurar las partes una a la vez y luego ensamblarlas en un todo de trabajo.
- Las funciones bien diseñadas suelen ser útiles para muchos programas. Una vez que escribas y depuras una, puedes reutilizarla.

A lo largo del resto del libro, a menudo usaremos una definición de función para explicar un concepto. Parte de la habilidad de crear y usar funciones es hacer que una función capture adecuadamente una idea como "encontrar el valor más pequeño en una lista de valores". Más adelante, le mostraremos el código que encuentra el más pequeño en una lista de valores y lo presentaremos como una función llamada `min` que toma una lista de valores como su argumento y devuelve el valor más pequeño de la lista.

## [depuración] (# depuración)



Si está utilizando un editor de texto para escribir sus scripts, es posible que tenga problemas con los espacios y las pestañas. La mejor manera de evitar estos problemas es usar espacios exclusivamente (sin pestañas). La mayoría de los editores de texto que conocen Python lo hacen de forma predeterminada, pero algunos no.



Las pestañas y los espacios suelen ser invisibles, lo que los hace difíciles de depurar, así que trata de encontrar un editor que administre la sangría por ti.

Además, no olvide guardar su programa antes de ejecutarlo. Algunos entornos de desarrollo lo hacen automáticamente, pero otros no. En ese caso, el programa que está viendo en el editor de texto no es el mismo que el programa que está ejecutando.

La depuración puede llevar mucho tiempo si continúa ejecutando el mismo programa incorrecto una y otra vez.

Asegúrese de que el código que está viendo es el código que está ejecutando. Si no está seguro, coloque algo como `print (" hola ")` al principio del programa y vuelva a ejecutarlo. ¡Si no ve `hola`, no está ejecutando el programa correcto!

## [Glosario] (# glosario)







































## [Ejercicios] (# ejercicios)

Ejercicio 4: ¿Cuál es el propósito de la palabra clave "def" en Python?

a) Es una jerga que significa "el siguiente código es realmente genial" <br/> b) Indica el inicio de una función <br/> c) Indica que la siguiente sección de código con sangría debe almacenarse para más adelante < br /> d) byc son verdaderas <br/> e) Ninguna de las anteriores

Ejercicio 5: ¿Qué se imprimirá el siguiente programa de Python?

```def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()
```
a) Zap ABC jane fred jane <br/> b) Zap ABC Zap <br/> c) ABC Zap jane <br/> d) ABC Zap ABC <br/> e) Zap Zap Zap

Ejercicio 6: reescriba su cálculo de pago con tiempo y medio para horas extras y cree una función llamada `computepay` que toma dos parámetros (` hours` y `rate`).

```Enter Hours: 45
Enter Rate: 10
Pay: 475.0
```
Ejercicio 7: reescriba el programa de calificación del capítulo anterior utilizando una función llamada `computegrade` que toma una puntuación como parámetro y devuelve una nota como una cadena.

```Score   Grade
&gt; 0.9     A
&gt; 0.8     B
&gt; 0.7     C
&gt; 0.6     D
&lt;= 0.6    F
```
```Program Execution:
```
```Enter score: 0.95
A
```
```Enter score: perfect
Bad score
```
```Enter score: 10.0
Bad score
```
```Enter score: 0.75
C
```
```Enter score: 0.5
F
```
Ejecute el programa repetidamente para probar los diferentes valores de entrada.

© 2015-2018 Baratija

#### Sobre nosotros

- [Nuestra historia] (// trinket.io/our-story)
<li> [Blog] (http://blog.trinket.io)
<li> [Asociaciones] (// trinket.io/partners)
</ Li> </ li>
#### Soporte

- [FAQ] (// trinket.io/faq)
- [Ayuda] (// trinket.io/help)
- [Contáctenos] (// trinket.io/contact)

#### Legal

- [Términos de servicio] (// trinket.io/tos)
- [Privacidad] (// trinket.io/privacy)

#### Conectar
-->