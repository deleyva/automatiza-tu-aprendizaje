## Los tuples son inmutables

Contenido extraído de [aquí](https://books.trinket.io/pfe/10-tuples.html).

Tutorial en español [aquí](https://librosweb.es/libro/algoritmos_python/capitulo_7/tuplas.html)

Un tuple es una secuencia de valores muy parecida a una lista. Los valores almacenados en una tupla pueden ser de cualquier tipo, y están indexados por enteros. La diferencia importante es que los tuples son ** inmutables **. Los tuples también son ** comparables ** y ** hashable **, por lo que podemos clasificar las listas y usar tuplas como valores clave en los diccionarios de Python.



Sintácticamente, una tupla es una lista de valores separados por comas.

```
>>>t = 'a', 'b', 'c', 'd', 'e'
```

Aunque no es necesario, es común incluir tuplas entre paréntesis para ayudarnos a identificar tuplas rápidamente cuando observamos el código de Python:



```
>>>t = ('a', 'b', 'c', 'd', 'e')
```

Para crear una tupla con un solo elemento, debe incluir la coma final:



Sin la coma, Python trata `('a')` como una expresión con una cadena entre paréntesis que se evalúa como una cadena:

```python
>>>t2 = ('a')
>>>tipo (t2)
<type 'str'>
```

Otra forma de construir una tupla es la función incorporada `tuple()`. Sin argumento, crea una tupla vacía:

>>> t = tuple()
>>> print(t)
()
>>> 

Si el argumento es una secuencia (cadena, lista o tupla), el resultado de la llamada a `tuple` es una tupla con los elementos de la secuencia:

```python
>>> t = tuple('lupins')
>>> print(t)
('l', 'u', 'p', 'i', 'n', 's')
>>> 
```

Como `tuple` es el nombre de un constructor, debes evitar usarlo como nombre de variable.

La mayoría de los operadores de listas también trabajan en tuplas. El operador de corchete indexa un elemento:

```python
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])
a
>>> 
```

Y el operador de corte selecciona un rango de elementos.



```python
>>>imprimir (t [1: 3])
('b', 'c')
```

Pero si intentas modificar uno de los elementos de el tuple, obtendrás un error:



```python
>>>t [0] = 'A'
TypeError: el objeto no admite la asignación de elementos
```

No puede modificar los elementos de un tuple, pero puede reemplazar un tuple con otra.

## Comparando tuples

Los operadores de comparación trabajan con tuplas y otras secuencias. Python comienza comparando el primer elemento de cada secuencia. Si son iguales, pasa al siguiente elemento, y así sucesivamente, hasta que encuentra elementos que difieren. Los elementos subsiguientes no se consideran (incluso si son realmente grandes).

```python
>>> (0, 1, 2) < (0, 3, 4)
>>> (0, 1, 2000000) < (0, 3, 4)
True
True
>>>  
```

La función `sort` funciona de la misma manera. Se ordena principalmente por el primer elemento, pero en el caso de un empate, se ordena por el segundo elemento, y así sucesivamente.

Esta característica se presta a un patrón llamado **DSU ** para una secuencia mediante la creación de una lista de tuplas con una o más claves de clasificación que preceden a los elementos de la secuencia, la lista de tuplas usando el `sort` incorporado de Python, y extrayendo los elementos ordenados de la secuencia.

[DSU]

Por ejemplo, suponga que tiene una lista de palabras y desea clasificarlas de la más larga a la más corta:

<iframe src="https://trinket.io/embed/python3/a9108b396f" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

El primer bucle crea una lista de tuplas, donde cada tupla es una palabra precedida por su longitud.

`sort` compara el primer elemento, la longitud, el primero y solo considera el segundo elemento para romper lazos. El argumento de la palabra clave `reverse = True` le dice a` sort` que vaya en orden decreciente.

El segundo bucle atraviesa la lista de tuplas y crea una lista de palabras en orden descendente de longitud. Las palabras de cuatro caracteres están ordenadas en orden ** alfabético inverso **, por lo que "qué" aparece antes de "suave" en la siguiente lista.

La salida del programa es la siguiente:

```python
['Yonder', 'window', 'breaks', 'light', 'what',
'suave', 'pero', 'en']
```

Por supuesto, la línea pierde gran parte de su impacto poético cuando se convierte en una lista de Python y se clasifica en orden de longitud de palabra descendente.

## Asignación de tuple



Una de las características sintácticas únicas del lenguaje Python es la capacidad de tener una tupla en el lado izquierdo de una declaración de asignación. Esto le permite asignar más de una variable a la vez cuando el lado izquierdo es una secuencia.

En este ejemplo, tenemos una lista de dos elementos (que es una secuencia) y asignamos los elementos primero y segundo de la secuencia a las variables `x` y` y` en una sola declaración.

```python
>>> m = [ 'have', 'fun' ]
>>> x, y = m
>>> x
'have'
>>> y
'fun'
>>> 
```

No es mágico, Python ** aproximadamente ** traduce la sintaxis de asignación de tupla para que sea la siguiente:

```python
>>> m = [ 'have', 'fun' ]
>>> x = m[0]
>>> y = m[1]
>>> x
'have'
>>> y
'fun'
>>> 
```

Estilísticamente, cuando usamos una tupla en el lado izquierdo de la declaración de asignación, omitimos los paréntesis, pero la siguiente es una sintaxis igualmente válida:

```python
>>>m = ['tener', 'divertido']
>>>(x, y) = m
>>>X
'tener'
>>>y
'divertido'
>>> gt;
```

Una aplicación especialmente inteligente de la asignación de tuples nos permite ** intercambiar ** los valores de dos variables en una sola declaración:

```python
>>>a, b = b, a
```

Ambos lados de esta declaración son tuplas, pero el lado izquierdo es una tupla de variables; El lado derecho es una tupla de expresiones. Cada valor en el lado derecho se asigna a su variable respectiva en el lado izquierdo. Todas las expresiones en el lado derecho son evaluadas antes de cualquiera de las asignaciones.

El número de variables a la izquierda y el número de valores a la derecha deben ser iguales:



```python
>>>a, b = 1, 2, 3
ValueError: too many values to unpack
```

Más generalmente, el lado derecho puede ser cualquier tipo de secuencia (cadena, lista o tupla). Por ejemplo, para dividir una dirección de correo electrónico en un nombre de usuario y un dominio, podría escribir:

```python
>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
```


## Diccionarios y tuples

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> print(t)
[('a', 10), ('b', 1), ('c', 22)]
>>> 
Connection to server timed out. Run trinket again to reconnect.
```
### Diccionarios y tuples

Los diccionarios no se ordenan, los tuples sí:

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> t
[('b', 1), ('a', 10), ('c', 22)]
>>> t.sort()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
```

## Asignación múltiple con diccionarios


Combinando `items`, tupla asignación y` for`, puedes ver un bonito patrón de código para recorrer las claves y los valores de un diccionario en un solo bucle:

```python
for key, val in list(d.items()):
    print(val, key)
```

Este bucle tiene dos ** variables de iteración ** porque `items` devuelve una lista de tuplas y` key, val` es una asignación de tuplas que se repite sucesivamente a través de cada uno de los pares clave-valor en el diccionario.

Para cada iteración a través del bucle, tanto `clave` como` valor` avanzan al siguiente par clave-valor en el diccionario (aún en orden hash).

La salida de este bucle es:

```
10 a
22 c
1 b
```

Nuevamente, está en orden de clave hash (es decir, no hay un orden particular).

Si combinamos estas dos técnicas, podemos imprimir el contenido de un diccionario ordenado por el ** valor ** almacenado en cada par clave-valor.

Para hacer esto, primero hacemos una lista de tuplas donde cada tupla es `(valor, clave)`. El método `items` nos daría una lista de tuplas` (clave, valor) `, pero esta vez queremos ordenar por valor, no por clave. Una vez que hemos construido la lista con las tuplas de clave de valor, es una cuestión simple ordenar la lista en orden inverso e imprimir la nueva lista ordenada.

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> l = list()>>> for key, val in d.items() :...     l.append( (val, key) )...
>>> l[(10, 'a'), (22, 'c'), (1, 'b')]
>>> l.sort(reverse=True)
>>> l[(22, 'c'), (10, 'a'), (1, 'b')]
>>>
```

Al construir cuidadosamente la lista de tuplas para que tenga el valor como primer elemento de cada tupla, podemos ordenar la lista de tuplas y obtener el contenido de nuestro diccionario ordenado por valor.

### Las palabras más comunes

Volviendo a nuestro ejemplo de ejecución del texto de ** Romeo y Julieta ** Act 2, Scene 2, podemos aumentar nuestro programa para usar esta técnica para imprimir las diez palabras más comunes en el texto de la siguiente manera:

<iframe src="https://trinket.io/embed/python3/02d5959f40" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

La primera parte del programa que lee el archivo y calcula el diccionario que asigna cada palabra al conteo de palabras en el documento no se modifica. Pero en lugar de simplemente imprimir `count` y finalizar el programa, construimos una lista de` (val, key) `tuplas y luego ordenamos la lista en orden inverso.

Dado que el valor es primero, se utilizará para las comparaciones. Si hay más de una tupla con el mismo valor, verá el segundo elemento (la clave), por lo que las tuplas en las que el valor es el mismo se ordenarán según el orden alfabético de la clave.

Al final, escribimos un bonito bucle `for` que realiza una iteración de asignación múltiple e imprime las diez palabras más comunes al recorrer una parte de la lista (` lst [: 10] `).

Así que ahora la salida finalmente se parece a lo que queremos para nuestro análisis de frecuencia de palabras.

```python
61 i
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

El hecho de que este complejo parseo y análisis de datos se puede realizar con un programa de Python de 19 líneas fácil de entender es una de las razones por las que Python es una buena opción como lenguaje para explorar información.

## Uso de tuplas como claves en los diccionarios

Debido a que las tuplas son **hashable** y las listas no, si queremos crear una clave **compuesta** para usar en un diccionario, debemos usar una tupla como clave.

Nos gustaría encontrar una clave compuesta si quisiéramos crear un directorio telefónico que se asigne desde los apellidos, los pares de primer nombre a los números de teléfono. Asumiendo que hemos definido las variables `last`,` first` y `number`, podríamos escribir una declaración de asignación de diccionario de la siguiente manera:

```python
directory[last,first] = number
```

La expresión entre paréntesis es una tupla. Podríamos usar la asignación de tuplas en un bucle `for` para atravesar este diccionario.

```python
for last, first in directory:
    print(first, last, directory[last,first])
```

Este bucle atraviesa las claves en `directorio`, que son tuplas. Asigna los elementos de cada tupla a `last` y` first`, luego imprime el nombre y el número de teléfono correspondiente.

>**tip**
>
>### Ahora en vídeo (activa los subtítulos)
>
>{% youtube %}https://www.youtube.com/watch?v=GA8aGIgI-dc&{% endyoutube %}