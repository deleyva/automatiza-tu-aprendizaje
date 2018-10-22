
# Listas



## [Una lista es una secuencia] (# a-list-is-a-sequence)

Como una cadena, una ** lista ** es una secuencia de valores. En una cadena, los valores son caracteres; En una lista, pueden ser de cualquier tipo. Los valores en la lista se denominan ** elementos ** o, a veces, ** elementos **.



Hay varias formas de crear una nueva lista; lo más simple es encerrar los elementos entre corchetes (`[` y `]`):

```pythonpython
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
```

El primer ejemplo es una lista de cuatro enteros. El segundo es una lista de tres cuerdas. Los elementos de una lista no tienen que ser del mismo tipo. La siguiente lista contiene una cadena, un flotador, un entero y (¡lo!) Otra lista:

```python
['spam', 2.0, 5, [10, 20]]
```

Una lista dentro de otra lista está ** anidada **.



Una lista que no contiene elementos se llama una lista vacía; puede crear uno con corchetes vacíos, `[]`.



Como es de esperar, puede asignar valores de lista a variables:

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
>>> 
```

## [Las listas son mutables] (# lists-are-mutable)



La sintaxis para acceder a los elementos de una lista es la misma que para acceder a los caracteres de una cadena: el operador de corchete. La expresión dentro de los paréntesis especifica el índice. Recuerda que los índices comienzan en 0:

```python
>>> print(cheeses[0])
Cheddar
```

A diferencia de las cadenas, las listas son mutables porque puede cambiar el orden de los elementos en una lista o reasignar un elemento en una lista. Cuando el operador de corchetes aparece en el lado izquierdo de una asignación, identifica el elemento de la lista que se asignará.

```python
>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]
>>> 
```

El elemento one-eth de `numbers`, que solía ser 123, ahora es 5.


Puede pensar en una lista como una relación entre índices y elementos. Esta relación se llama ** mapeo **; cada índice "mapea" a uno de los elementos.



Los índices de lista funcionan de la misma manera que los índices de cadena:

- Cualquier expresión entera puede ser usada como un índice.
- Si intentas leer o escribir un elemento que no existe, obtienes un 'IndexError'.



- Si un índice tiene un valor negativo, cuenta hacia atrás desde el final de la lista.



El operador `in` también funciona en listas.

## [Atravesando una lista] (# traversing-a-list)



La forma más común de recorrer los elementos de una lista es con un bucle `for`. La sintaxis es la misma que para las cadenas:

```python
for cheese in cheeses:
    print(cheese)
```

Esto funciona bien si solo necesita leer los elementos de la lista. Pero si desea escribir o actualizar los elementos, necesita los índices. Una forma común de hacerlo es combinar las funciones `range` y` len`:



```python
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```

Este bucle atraviesa la lista y actualiza cada elemento. `len` devuelve el número de elementos en la lista. `range` devuelve una lista de índices de 0 a ** n ** - 1, donde ** n ** es la longitud de la lista. Cada vez que pasa por el bucle, `i` obtiene el índice del siguiente elemento. La declaración de asignación en el cuerpo usa `i` para leer el valor antiguo del elemento y para asignar el nuevo valor.



Un bucle `for` sobre una lista vacía nunca ejecuta el cuerpo:

```python
for x in empty:
    print('This never happens.')
```

Aunque una lista puede contener otra lista, la lista anidada todavía cuenta como un elemento único. La longitud de esta lista es cuatro:



```python
['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
```

## [Operaciones de lista] (# lista-operaciones)



El operador `+` concatena las listas:

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
>>> 
```

Del mismo modo, el operador repite una lista un número determinado de veces:

```python
>>> [0] * 4
[0, 0, 0, 0]
```

El primer ejemplo se repite cuatro veces. El segundo ejemplo repite la lista tres veces.

## [Listar segmentos] (# list-slices)



El operador de corte también funciona en listas:

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
>>> 
```

Si omite el primer índice, la división comienza al principio. Si omites el segundo, la rebanada va al final. Entonces, si omite ambos, la porción es una copia de toda la lista.



```python
t[:]
['a', 'b', 'c', 'd', 'e', 'f']
```

Dado que las listas son mutables, a menudo es útil hacer una copia antes de realizar operaciones de plegado, huso o mutilación de listas.



Un operador de sector en el lado izquierdo de una asignación puede actualizar varios elementos:

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']
>>> 
```

## [Métodos de lista] (# métodos de lista)



Python proporciona métodos que operan en listas. Por ejemplo, `append` agrega un nuevo elemento al final de una lista:

```python
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print(t)
['a', 'b', 'c', 'd']
>>> 
```

`extend` toma una lista como argumento y agrega todos los elementos:

```python
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
>>> 
```

Este ejemplo deja `t2` sin modificar.

`sort` organiza los elementos de la lista de bajo a alto:

```python
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']
>>> 
```

La mayoría de los métodos de lista son nulos; modifican la lista y devuelven `Ninguno`. Si accidentalmente escribe `t = t.sort ()`, quedará decepcionado con el resultado.



## [Eliminando elementos] (# eliminando elementos)



Hay varias formas de eliminar elementos de una lista. Si conoce el índice del elemento que desea, puede usar `pop`:

```python
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b
>>>
```

`pop` modifica la lista y devuelve el elemento que fue eliminado. Si no proporciona un índice, elimina y devuelve el último elemento.

Si no necesita el valor eliminado, puede usar el operador `del`:

```python
>>> t = ['a', 'b', 'c']
```

Si conoce el elemento que desea eliminar (pero no el índice), puede usar `remove`:

```python
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print(t)
['a', 'c']
```

El valor de retorno de `remove` es` None`.



Para eliminar más de un elemento, puedes usar `del` con un índice de división:

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> print(t)
['a', 'f']
>>> 
```

Como es habitual, la división selecciona todos los elementos hasta el segundo índice, pero sin incluirlo.

## [Listas y funciones] (# listas y funciones)

Hay una serie de funciones integradas que se pueden usar en listas que le permiten mirar rápidamente una lista sin escribir sus propios bucles:

```python
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums))
6
>>> print(max(nums))
74
>>> print(min(nums))
3
>>> print(sum(nums))
154
>>> print(sum(nums)/len(nums))
25.666666666666668
>>> 
```

La función `sum ()` solo funciona cuando los elementos de la lista son números. Las otras funciones (`max ()`, `len ()`, etc.) funcionan con listas de cadenas y otros tipos que pueden ser comparables.

Podríamos reescribir un programa anterior que calculó el promedio de una lista de números ingresados ​​por el usuario usando una lista.

Primero, el programa para calcular un promedio sin una lista:

<iframe src="https://trinket.io/embed/python3/aa04e80e9c" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

En este programa, tenemos las variables `count` y` total` para mantener el número y el total acumulado de los números del usuario, ya que repetidamente pedimos al usuario un número.

Simplemente podríamos recordar cada número a medida que el usuario lo ingresó y usar las funciones integradas para calcular la suma y el conteo al final.

<iframe src="https://trinket.io/embed/python3/f8549505f1" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Hacemos una lista vacía antes de que comience el ciclo, y luego cada vez que tenemos un número, lo agregamos a la lista. Al final del programa, simplemente calculamos la suma de los números en la lista y la dividimos por el recuento de los números en la lista para obtener el promedio.

## [Listas y cadenas] (# listas y cadenas)



Una cadena es una secuencia de caracteres y una lista es una secuencia de valores, pero una lista de caracteres no es lo mismo que una cadena. Para convertir de una cadena a una lista de caracteres, puedes usar `list`:

```python
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
```

Como `list` es el nombre de una función incorporada, debes evitar usarla como nombre de variable. También evito la letra `l` porque se parece demasiado al número` 1`. Así que por eso uso `t`.

La función `list` rompe una cadena en letras individuales. Si desea dividir una cadena en palabras, puede usar el método `split`:



Una vez que haya usado `split` para dividir la cadena en una lista de palabras, puede usar el operador de índice (corchete) para mirar una palabra en particular en la lista.

Puede llamar a `split` con un argumento opcional llamado ** delimitador ** que especifica qué caracteres usar como límites de palabras. El siguiente ejemplo usa un guión como delimitador:

```python
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
```

`join` es el inverso de` split`. Toma una lista de cadenas y concatena los elementos. `join` es un método de cadena, por lo que debe invocarlo en el delimitador y pasar la lista como parámetro:

```python
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
>>> 
```

En este caso, el delimitador es un carácter de espacio, por lo que `join` pone un espacio entre las palabras. Para concatenar cadenas sin espacios, puede usar la cadena vacía "" como un delimitador.



## [Líneas de análisis] (# líneas de análisis)

Por lo general, cuando estamos leyendo un archivo, queremos hacer algo en las líneas que no sea simplemente imprimir toda la línea. A menudo queremos encontrar las "líneas interesantes" y luego ** analizar ** la línea para encontrar alguna ** parte ** interesante de la línea. ¿Qué pasaría si quisiéramos imprimir el día de la semana desde esas líneas que comienzan con "De"?

`From stephen.marquard@uct.ac.za`**`Sat`**`Jan 5 09:14:16 2008`

El método 'split' es muy efectivo cuando se enfrenta con este tipo de problema. Podemos escribir un pequeño programa que busque líneas donde la línea comience con "De", `dividir 'esas líneas, y luego imprimir la tercera palabra en la línea:

<iframe src="https://trinket.io/embed/python3/25794fcf19" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Aquí también usamos la forma contraída de la declaración `if` donde colocamos el` continue` en la misma línea que el `if`. Esta forma contraída de `if` funciona de la misma manera que si` continue` estuviera en la siguiente línea y con sangría.

El programa produce la siguiente salida:

```python
Sat
Fri
Fri
Fri
...
```

Más adelante, aprenderemos técnicas cada vez más sofisticadas para elegir las líneas para trabajar y cómo las separamos para encontrar la información exacta que estamos buscando.

## [Objetos y valores] (# objetos y valores)



Si ejecutamos estas sentencias de asignación:

```python
a = 'banana'
b = 'banana'
```

sabemos que `a` y` b` se refieren a una cadena, pero no sabemos si se refieren a la cadena ** same **. Hay dos estados posibles:

![objetos y valores](img/objecrts_values.png)

Variables y objetos

En un caso, `a` y` b` se refieren a dos objetos diferentes que tienen el mismo valor. En el segundo caso, se refieren al mismo objeto.



Para verificar si dos variables se refieren al mismo objeto, puede usar el operador `is`.

```python
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
```

En este ejemplo, Python solo creó un objeto de cadena, y tanto `a` como` b` se refieren a él.

Pero cuando creas dos listas, obtienes dos objetos:

```python
>>> a = [1, 2, 3]
```

En este caso, diríamos que las dos listas son ** equivalentes **, porque tienen los mismos elementos, pero no ** idénticas **, porque no son el mismo objeto. Si dos objetos son idénticos, también son equivalentes, pero si son equivalentes, no son necesariamente idénticos.



Hasta ahora, hemos estado utilizando indistintamente "objeto" y "valor", pero es más preciso decir que un objeto tiene un valor. Si ejecuta `a = [1,2,3]`, `a` se refiere a un objeto de lista cuyo valor es una secuencia particular de elementos. Si otra lista tiene los mismos elementos, diríamos que tiene el mismo valor.



## [Aliasing] (# aliasing)



Si `a` se refiere a un objeto y usted asigna` b = a`, entonces ambas variables se refieren al mismo objeto:

```python
>>> a = [1, 2, 3]
```

La asociación de una variable con un objeto se denomina ** referencia **. En este ejemplo, hay dos referencias al mismo objeto.



Un objeto con más de una referencia tiene más de un nombre, por lo que decimos que el objeto tiene ** un alias **.



Si el objeto con alias es mutable, los cambios realizados con un alias afectan al otro:

```python
>>> b[0] = 17
>>> print(a)
[17, 2, 3]
```

Aunque este comportamiento puede ser útil, es propenso a errores. En general, es más seguro evitar los alias cuando trabaja con objetos mutables.



Para objetos inmutables como cadenas, el aliasing no es tanto un problema. En este ejemplo:

```python
a = 'banana'
b = 'banana'
```

casi nunca hace una diferencia si `a` y` b` se refieren a la misma cadena o no.

## [Lista de argumentos] (# lista-argumentos)



Cuando pasa una lista a una función, la función obtiene una referencia a la lista. Si la función modifica un parámetro de lista, la persona que llama ve el cambio. Por ejemplo, `delete_head` elimina el primer elemento de una lista:

```python
def delete_head(t):
    del t[0]
```

Así es como se usa:

```python
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'delete_head' is not defined
>>> print(letters)
['a', 'b', 'c']
```

El parámetro `t` y la variable` letras` son alias para el mismo objeto.

Es importante distinguir entre las operaciones que modifican las listas y las operaciones que crean nuevas listas. Por ejemplo, el método `append` modifica una lista, pero el operador` + `crea una nueva lista:

```python
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> print(t1)
[1, 2, 3]
>>> print(t2)
None
>>> t3 = t1 + [3]
>>> print(t3)
[1, 2, 3, 3]
>>> t2 is t3
False
>>> 
```

Esta diferencia es importante cuando escribes funciones que se supone que modifican las listas. Por ejemplo, esta función ** no ** elimina el encabezado de una lista:

```python
def bad_delete_head(t):
    t = t[1:]              # WRONG!
```

El operador de sector crea una nueva lista y la asignación hace que `t` se refiera a ella, pero nada de eso tiene ningún efecto en la lista que se pasó como argumento.



Una alternativa es escribir una función que crea y devuelve una nueva lista. Por ejemplo, `tail` devuelve todos menos el primer elemento de una lista:

```python
def tail(t):
    return t[1:]
```

Esta función deja la lista original sin modificar. Así es como se usa:

```python
>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tail' is not defined
>>> print(rest)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rest' is not defined
>>> 
```

