
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

<li class = "has-dropdown"> [Tuplas] (# tuplas) <ul class = "dropdown">
- [Las tuplas son inmutables] (# tuplas son inmutables)
- [Comparando tuplas] (# comparando tuplas)
- [Asignación de tupla] (# asignación de tupla)
- [Diccionarios y tuplas] (# diccionarios-y-tuplas)
- [Asignación múltiple con diccionarios] (# asignación múltiple con diccionarios)
- [Las palabras más comunes] (# las palabras más comunes)
- [Usando tuples como claves en los diccionarios] (# using-tuples-as-keys-in-dictionary)
- [Secuencias: cadenas, listas y tuplas - ¡Oh My!] (# Secuencias-listas-listas-y-tuplas --- oh-my)
- [Depuración] (# depuración)
- [Glosario] (# glosario)
- [Ejercicios] (# ejercicios)

# [Tuplas] (# tuplas)

## [Las tuplas son inmutables] (# tuplas son inmutables)



Una tupla [<sup> 1 </sup>] (# fn1) es una secuencia de valores muy parecida a una lista. Los valores almacenados en una tupla pueden ser de cualquier tipo, y están indexados por enteros. La diferencia importante es que las tuplas son ** inmutables **. Las tuplas también son ** comparables ** y ** hashable **, por lo que podemos clasificar las listas y usar tuplas como valores clave en los diccionarios de Python.



Sintácticamente, una tupla es una lista de valores separados por comas:

```>>> t = 'a', 'b', 'c', 'd', 'e'
```
Aunque no es necesario, es común incluir tuplas entre paréntesis para ayudarnos a identificar tuplas rápidamente cuando observamos el código de Python:



```>>> t = ('a', 'b', 'c', 'd', 'e')
```
Para crear una tupla con un solo elemento, debe incluir la coma final:



Sin la coma, Python trata `('a')` como una expresión con una cadena entre paréntesis que se evalúa como una cadena:

```>>> t2 = ('a')
>>> type(t2)
&lt;type 'str'&gt;
```
Otra forma de construir una tupla es la función incorporada `tupla`. Sin argumento, crea una tupla vacía:



Si el argumento es una secuencia (cadena, lista o tupla), el resultado de la llamada a `tuple` es una tupla con los elementos de la secuencia:

Como `tuple` es el nombre de un constructor, debes evitar usarlo como nombre de variable.

La mayoría de los operadores de listas también trabajan en tuplas. El operador de corchete indexa un elemento:



Y el operador de corte selecciona un rango de elementos.



```>>> print(t[1:3])
('b', 'c')
```
Pero si intentas modificar uno de los elementos de la tupla, obtendrás un error:



```>>> t[0] = 'A'
TypeError: object doesn't support item assignment
```
No puede modificar los elementos de una tupla, pero puede reemplazar una tupla por otra:

## [Comparando tuplas] (# comparando tuplas)



Los operadores de comparación trabajan con tuplas y otras secuencias. Python comienza comparando el primer elemento de cada secuencia. Si son iguales, continúa con el siguiente elemento, y así sucesivamente, hasta que encuentre elementos que difieran. Los elementos subsiguientes no se consideran (incluso si son realmente grandes).

La función `sort` funciona de la misma manera. Se ordena principalmente por el primer elemento, pero en el caso de un empate, se ordena por el segundo elemento, y así sucesivamente.

Esta característica se presta a un patrón llamado ** DSU ** para

una secuencia mediante la creación de una lista de tuplas con una o más claves de clasificación que preceden a los elementos de la secuencia,

la lista de tuplas usando el `sort` incorporado de Python, y

Extrayendo los elementos ordenados de la secuencia.

[DSU]

Por ejemplo, suponga que tiene una lista de palabras y desea clasificarlas de la más larga a la más corta:

El primer bucle crea una lista de tuplas, donde cada tupla es una palabra precedida por su longitud.

`sort` compara el primer elemento, la longitud, el primero y solo considera el segundo elemento para romper lazos. El argumento de palabra clave `reverse = True` le dice a` sort` que vaya en orden decreciente.



El segundo bucle atraviesa la lista de tuplas y crea una lista de palabras en orden descendente de longitud. Las palabras de cuatro caracteres están ordenadas en orden ** alfabético inverso **, por lo que "qué" aparece antes de "suave" en la siguiente lista.

La salida del programa es la siguiente:

```['yonder', 'window', 'breaks', 'light', 'what',
'soft', 'but', 'in']
```
Por supuesto, la línea pierde gran parte de su impacto poético cuando se convierte en una lista de Python y se clasifica en orden de longitud de palabra descendente.

## [Asignación de tupla] (# asignación de tupla)



Una de las características sintácticas únicas del lenguaje Python es la capacidad de tener una tupla en el lado izquierdo de una declaración de asignación. Esto le permite asignar más de una variable a la vez cuando el lado izquierdo es una secuencia.

En este ejemplo tenemos una lista de dos elementos (que es una secuencia) y asignamos el primer y segundo elementos de la secuencia a las variables `x` y` y` en una sola declaración.

No es mágico, Python ** aproximadamente ** traduce la sintaxis de asignación de tupla para que sea la siguiente: [<sup> 2 </sup>] (# fn2)

Estilísticamente, cuando usamos una tupla en el lado izquierdo de la declaración de asignación, omitimos los paréntesis, pero la siguiente es una sintaxis igualmente válida:

```>>> m = [ 'have', 'fun' ]
>>> (x, y) = m
>>> x
'have'
>>> y
'fun'
>>>
```
Una aplicación especialmente inteligente de la asignación de tuplas nos permite ** intercambiar ** los valores de dos variables en una sola declaración:

```>>> a, b = b, a
```
Ambos lados de esta declaración son tuplas, pero el lado izquierdo es una tupla de variables; El lado derecho es una tupla de expresiones. Cada valor en el lado derecho se asigna a su variable respectiva en el lado izquierdo. Todas las expresiones en el lado derecho son evaluadas antes de cualquiera de las asignaciones.

El número de variables a la izquierda y el número de valores a la derecha deben ser iguales:



```>>> a, b = 1, 2, 3
ValueError: too many values to unpack
```
Más generalmente, el lado derecho puede ser cualquier tipo de secuencia (cadena, lista o tupla). Por ejemplo, para dividir una dirección de correo electrónico en un nombre de usuario y un dominio, podría escribir:



```>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
```
El valor de retorno de `split` es una lista con dos elementos; el primer elemento se asigna a `uname`, el segundo a` domain`.

```>>> print(uname)
monty
>>> print(domain)
python.org
```
## [Diccionarios y tuplas] (# diccionarios-y-tuplas)



Los diccionarios tienen un método llamado `items` que devuelve una lista de tuplas, donde cada tupla es un par clave-valor:

Como debe esperar de un diccionario, los elementos no están en ningún orden en particular.

Sin embargo, como la lista de tuplas es una lista y las tuplas son comparables, ahora podemos ordenar la lista de tuplas. Convertir un diccionario en una lista de tuplas es una forma de generar el contenido de un diccionario ordenado por clave:

```>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> t
[('b', 1), ('a', 10), ('c', 22)]
>>> t.sort()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
```
La nueva lista se clasifica en orden alfabético ascendente por el valor clave.

## [Asignación múltiple con diccionarios] (# asignación múltiple con diccionarios)



Combinando `items`, tupla asignación y` for`, puedes ver un bonito patrón de código para recorrer las claves y los valores de un diccionario en un solo bucle:

```for key, val in list(d.items()):
    print(val, key)
```
Este bucle tiene dos ** variables de iteración ** porque `items` devuelve una lista de tuplas y` key, val` es una asignación de tuplas que se repite sucesivamente a través de cada uno de los pares clave-valor en el diccionario.

Para cada iteración a través del bucle, tanto `clave` como` valor` avanzan al siguiente par clave-valor en el diccionario (aún en orden hash).

La salida de este bucle es:

```10 a
22 c
1 b
```
Nuevamente, está en orden de clave hash (es decir, no hay un orden particular).

Si combinamos estas dos técnicas, podemos imprimir el contenido de un diccionario ordenado por el ** valor ** almacenado en cada par clave-valor.

Para hacer esto, primero hacemos una lista de tuplas donde cada tupla es `(valor, clave)`. El método `items` nos daría una lista de tuplas` (clave, valor) `, pero esta vez queremos ordenar por valor, no por clave. Una vez que hemos construido la lista con las tuplas de clave de valor, es una cuestión simple ordenar la lista en orden inverso e imprimir la nueva lista ordenada.

```>>> d = {'a':10, 'b':1, 'c':22}
>>> l = list()
>>> for key, val in d.items() :
...     l.append( (val, key) )
...
>>> l
[(10, 'a'), (22, 'c'), (1, 'b')]
>>> l.sort(reverse=True)
>>> l
[(22, 'c'), (10, 'a'), (1, 'b')]
>>>
```
Al construir cuidadosamente la lista de tuplas para que tenga el valor como primer elemento de cada tupla, podemos ordenar la lista de tuplas y obtener el contenido de nuestro diccionario ordenado por valor.

## [Las palabras más comunes] (# las palabras más comunes)



Volviendo a nuestro ejemplo de ejecución del texto de ** Romeo y Julieta ** Act 2, Scene 2, podemos aumentar nuestro programa para usar esta técnica para imprimir las diez palabras más comunes en el texto de la siguiente manera:

La primera parte del programa que lee el archivo y calcula el diccionario que asigna cada palabra al conteo de palabras en el documento no se modifica. Pero en lugar de simplemente imprimir `count` y finalizar el programa, construimos una lista de` (val, key) `tuplas y luego ordenamos la lista en orden inverso.

Como el valor es primero, se utilizará para las comparaciones. Si hay más de una tupla con el mismo valor, se verá el segundo elemento (la clave), por lo que las tuplas en las que el valor es el mismo se ordenarán según el orden alfabético de la clave.

Al final, escribimos un bonito bucle `for` que realiza una iteración de asignación múltiple e imprime las diez palabras más comunes al recorrer una parte de la lista (` lst [: 10] `).

Así que ahora la salida finalmente se parece a lo que queremos para nuestro análisis de frecuencia de palabras.

```61 i
42 and
40 romeo
34 to
34 the
32 thou
32 juliet
30 that
29 my
24 thee
```
El hecho de que este análisis y análisis de datos complejos se puede realizar con un programa Python de 19 líneas fácil de entender es una de las razones por las que Python es una buena opción como lenguaje para explorar información.

## [Uso de tuplas como claves en los diccionarios] (# using-tuples-as-keys-in-dictionary)



Debido a que las tuplas son ** hashable ** y las listas no, si queremos crear una clave ** compuesta ** para usar en un diccionario, debemos usar una tupla como clave.

Nos encontraríamos con una clave compuesta si quisiéramos crear un directorio telefónico que se asigne desde los pares de apellidos y apellidos a los números de teléfono. Suponiendo que hayamos definido las variables `last`,` first` y `number`, podríamos escribir una declaración de asignación de diccionario de la siguiente manera:

```directory[last,first] = number
```
La expresión entre paréntesis es una tupla. Podríamos usar la asignación de tuplas en un bucle `for` para atravesar este diccionario.



```for last, first in directory:
    print(first, last, directory[last,first])
```
Este bucle atraviesa las claves en `directorio`, que son tuplas. Asigna los elementos de cada tupla a `last` y` first`, luego imprime el nombre y el número de teléfono correspondiente.

## [Secuencias: cadenas, listas y tuplas - ¡Oh My!] (# Secuencias-listas-y-tuplas --- oh-my)



Me he centrado en las listas de tuplas, pero casi todos los ejemplos de este capítulo también funcionan con listas de listas, tuplas de tuplas y tuplas de listas. Para evitar enumerar las posibles combinaciones, a veces es más fácil hablar de secuencias de secuencias.

En muchos contextos, los diferentes tipos de secuencias (cadenas, listas y tuplas) se pueden usar indistintamente. Entonces, ¿cómo y por qué eliges uno sobre los otros?



Para comenzar con lo obvio, las cadenas son más limitadas que otras secuencias porque los elementos deben ser caracteres. También son inmutables. Si necesita la capacidad de cambiar los caracteres en una cadena (en lugar de crear una nueva cadena), es posible que desee utilizar una lista de caracteres en su lugar.

Las listas son más comunes que las tuplas, principalmente porque son mutables. Pero hay algunos casos en los que quizás prefieras las tuplas:

1. En algunos contextos, como una declaración `return ', es sintácticamente más simple crear una tupla que una lista. En otros contextos, es posible que prefiera una lista.
1. Si desea usar una secuencia como clave de diccionario, debe usar un tipo inmutable como una tupla o cadena.
1. Si está pasando una secuencia como un argumento a una función, el uso de tuplas reduce el potencial de comportamiento inesperado debido al aliasing.

Si desea usar una secuencia como clave de diccionario, debe usar un tipo inmutable como una tupla o cadena.

Debido a que las tuplas son inmutables, no proporcionan métodos como `sort` y` reverse`, que modifican las listas existentes. Sin embargo, Python proporciona las funciones integradas `sorted` y` reverseed`, que toman cualquier secuencia como parámetro y devuelven una nueva secuencia con los mismos elementos en un orden diferente.



## [depuración] (# depuración)



Las listas, los diccionarios y las tuplas se conocen genéricamente como ** estructuras de datos **; en este capítulo estamos empezando a ver estructuras de datos compuestas, como listas de tuplas y diccionarios que contienen tuplas como claves y listas como valores. Las estructuras de datos compuestos son útiles, pero son propensas a lo que yo llamo ** errores de forma **; es decir, los errores causados ​​cuando una estructura de datos tiene el tipo, tamaño o composición incorrectos, o tal vez usted escribe un código y olvida la forma de sus datos e introduce un error.

Por ejemplo, si está esperando una lista con un entero y le doy un entero antiguo simple (no en una lista), no funcionará.

Cuando está depurando un programa, y ​​especialmente si está trabajando en un error, hay cuatro cosas que puede intentar:

Examine su código, léalo de nuevo y verifique que diga lo que quería decir.

Experimente haciendo cambios y ejecutando diferentes versiones. A menudo, si muestra lo correcto en el lugar correcto en el programa, el problema se vuelve obvio, pero a veces debe dedicar algo de tiempo a construir andamios.

¡Tómate un tiempo para pensar! ¿Qué tipo de error es: sintaxis, tiempo de ejecución, semántico? ¿Qué información puede obtener de los mensajes de error o de la salida del programa? ¿Qué tipo de error podría causar el problema que estás viendo? ¿Qué fue lo último que cambió, antes de que apareciera el problema?

En algún momento, lo mejor que puede hacer es retirarse, deshacer los cambios recientes, hasta que vuelva a un programa que funcione y que comprenda. Entonces puedes empezar a reconstruir.

Los programadores principiantes a veces se atascan en una de estas actividades y se olvidan de las demás. Cada actividad viene con su propio modo de falla.

Por ejemplo, leer su código puede ayudar si el problema es un error tipográfico, pero no si el problema es un malentendido conceptual. Si no entiende lo que hace su programa, puede leerlo 100 veces y nunca ver el error, porque el error está en su cabeza.



Realizar experimentos puede ayudar, especialmente si ejecuta pruebas pequeñas y simples. Pero si ejecuta experimentos sin pensar o leer su código, podría caer en un patrón que yo llamo "programación aleatoria", que es el proceso de hacer cambios aleatorios hasta que el programa haga lo correcto. No hace falta decir que la programación aleatoria puede llevar mucho tiempo.



Tienes que tomarte tiempo para pensar. La depuración es como una ciencia experimental. Debe tener al menos una hipótesis sobre cuál es el problema. Si hay dos o más posibilidades, trate de pensar en una prueba que elimine una de ellas.

Tomar un descanso ayuda con el pensamiento. También lo hace hablar. Si explica el problema a otra persona (o incluso a usted mismo), a veces encontrará la respuesta antes de terminar de formular la pregunta.

Pero incluso las mejores técnicas de depuración fallarán si hay demasiados errores, o si el código que intenta corregir es demasiado grande y complicado. A veces, la mejor opción es retirarse, simplificando el programa hasta que llegue a algo que funcione y que comprenda.

Los programadores principiantes a menudo son reacios a retirarse porque no pueden soportar eliminar una línea de código (incluso si está mal). Si te hace sentir mejor, copia tu programa en otro archivo antes de comenzar a borrarlo. Luego puedes pegar las piezas de nuevo poco a poco.

Encontrar un error difícil requiere leer, correr, rumiar y, a veces, retirarse. Si te quedas estancado en una de estas actividades, prueba las otras.

## [Glosario] (# glosario)





















## [Ejercicios] (# ejercicios)

** Ejercicio 1: ** Revisa un programa anterior de la siguiente manera: Lee y analiza las líneas "De" y saca las direcciones de la línea. Cuente el número de mensajes de cada persona usando un diccionario.

Después de haber leído todos los datos, imprima a la persona con el mayor número de confirmaciones creando una lista de tuplas (conteo, correo electrónico) del diccionario. Luego, ordene la lista en orden inverso e imprima a la persona que tenga más compromisos.

```Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
```
** Ejercicio 2: ** Este programa cuenta la distribución de la hora del día para cada uno de los mensajes. Puedes sacar la hora de la línea "De" encontrando la cadena de tiempo y luego dividiendo esa cadena en partes usando el carácter de dos puntos. Una vez que haya acumulado los conteos para cada hora, imprima los conteos, uno por línea, ordenados por hora como se muestra a continuación.

Ejecución de la muestra:

```python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
```
** Ejercicio 3: ** Escriba un programa que lea un archivo e imprima las ** letras ** en orden decreciente de frecuencia. Su programa debe convertir todas las entradas a minúsculas y solo contar las letras a-z. Su programa no debe contar espacios, dígitos, puntuación o cualquier otra cosa que no sean las letras a-z. Encuentre muestras de texto de varios idiomas diferentes y vea cómo la frecuencia de las letras varía según el idioma. Compare sus resultados con las tablas en [wikipedia.org/wiki/Letter_frequencies◆ (wikipedia.org/wiki/Letter_frequencies).



---


1. Dato curioso: la palabra "tupla" proviene de los nombres que se dan a las secuencias de números de diferentes longitudes: simple, doble, triple, cuádruple, quituple, sextuple, septuple, etc. [↩] (# fnref1)
1. Python no traduce la sintaxis literalmente. Por ejemplo, si intenta esto con un diccionario, no funcionará como podría esperarse. [↩] (# fnref2)

Python no traduce la sintaxis literalmente. Por ejemplo, si intenta esto con un diccionario, no funcionará como podría esperarse. [↩] (# fnref2)

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
