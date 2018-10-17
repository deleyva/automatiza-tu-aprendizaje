## [Las tuplas son inmutables] (# tuplas son inmutables)



Una tupla [<sup> 1 </sup>] (# fn1) es una secuencia de valores muy parecida a una lista. Los valores almacenados en una tupla pueden ser de cualquier tipo, y están indexados por enteros. La diferencia importante es que las tuplas son ** inmutables **. Las tuplas también son ** comparables ** y ** hashable **, por lo que podemos clasificar las listas y usar tuplas como valores clave en los diccionarios de Python.



Sintácticamente, una tupla es una lista de valores separados por comas:

```
& gt; & gt; & gt; t = 'a', 'b', 'c', 'd', 'e'
```

Aunque no es necesario, es común incluir tuplas entre paréntesis para ayudarnos a identificar tuplas rápidamente cuando observamos el código de Python:



```
& gt; & gt; & gt; t = ('a', 'b', 'c', 'd', 'e')
```

Para crear una tupla con un solo elemento, debe incluir la coma final:



Sin la coma, Python trata `('a')` como una expresión con una cadena entre paréntesis que se evalúa como una cadena:

```
& gt; & gt; & gt; t2 = ('a')
& gt; & gt; & gt; tipo (t2)
& lt; escribe 'str' & gt;
```

Otra forma de construir una tupla es la función incorporada `tupla`. Sin argumento, crea una tupla vacía:



Si el argumento es una secuencia (cadena, lista o tupla), el resultado de la llamada a `tuple` es una tupla con los elementos de la secuencia:

Como `tuple` es el nombre de un constructor, debes evitar usarlo como nombre de variable.

La mayoría de los operadores de listas también trabajan en tuplas. El operador de corchete indexa un elemento:



Y el operador de corte selecciona un rango de elementos.



```
& gt; & gt; & gt; imprimir (t [1: 3])
('antes de Cristo')
```

Pero si intentas modificar uno de los elementos de la tupla, obtendrás un error:



```
& gt; & gt; & gt; t [0] = 'A'
TypeError: el objeto no admite la asignación de elementos
```

No puede modificar los elementos de una tupla, pero puede reemplazar una tupla con otra:

## [Comparando tuplas] (# comparando tuplas)



Los operadores de comparación trabajan con tuplas y otras secuencias. Python comienza comparando el primer elemento de cada secuencia. Si son iguales, pasa al siguiente elemento, y así sucesivamente, hasta que encuentra elementos que difieren. Los elementos subsiguientes no se consideran (incluso si son realmente grandes).

La función `sort` funciona de la misma manera. Se ordena principalmente por el primer elemento, pero en el caso de un empate, se ordena por el segundo elemento, y así sucesivamente.

Esta característica se presta a un patrón llamado ** DSU ** para

una secuencia mediante la creación de una lista de tuplas con una o más claves de clasificación que preceden a los elementos de la secuencia,

la lista de tuplas usando el `sort` incorporado de Python, y

Extrayendo los elementos ordenados de la secuencia.

[DSU]

Por ejemplo, suponga que tiene una lista de palabras y desea clasificarlas de la más larga a la más corta:

El primer bucle crea una lista de tuplas, donde cada tupla es una palabra precedida por su longitud.

`sort` compara el primer elemento, la longitud, el primero y solo considera el segundo elemento para romper lazos. El argumento de la palabra clave `reverse = True` le dice a` sort` que vaya en orden decreciente.



El segundo bucle atraviesa la lista de tuplas y crea una lista de palabras en orden descendente de longitud. Las palabras de cuatro caracteres están ordenadas en orden ** alfabético inverso **, por lo que "qué" aparece antes de "suave" en la siguiente lista.

La salida del programa es la siguiente:

```
['Yonder', 'window', 'breaks', 'light', 'what',
'suave', 'pero', 'en']
```

Por supuesto, la línea pierde gran parte de su impacto poético cuando se convierte en una lista de Python y se clasifica en orden de longitud de palabra descendente.

## [Asignación de tupla] (# asignación de tupla)



Una de las características sintácticas únicas del lenguaje Python es la capacidad de tener una tupla en el lado izquierdo de una declaración de asignación. Esto le permite asignar más de una variable a la vez cuando el lado izquierdo es una secuencia.

En este ejemplo, tenemos una lista de dos elementos (que es una secuencia) y asignamos los elementos primero y segundo de la secuencia a las variables `x` y` y` en una sola declaración.

No es mágico, Python ** aproximadamente ** traduce la sintaxis de asignación de tupla para que sea la siguiente: [<sup> 2 </sup>] (# fn2)

Estilísticamente, cuando usamos una tupla en el lado izquierdo de la declaración de asignación, omitimos los paréntesis, pero la siguiente es una sintaxis igualmente válida:

```
& gt; & gt; & gt; m = ['tener', 'diversión']
& gt; & gt; & gt; (x, y) = m
& gt; & gt; & gt; X
'tener'
& gt; & gt; & gt; y
'divertido'
& gt; & gt; & gt;
```

Una aplicación especialmente inteligente de la asignación de tuplas nos permite ** intercambiar ** los valores de dos variables en una sola declaración:

```
& gt; & gt; & gt; a, b = b, a
```

Ambos lados de esta declaración son tuplas, pero el lado izquierdo es una tupla de variables; El lado derecho es una tupla de expresiones. Cada valor en el lado derecho se asigna a su variable respectiva en el lado izquierdo. Todas las expresiones en el lado derecho son evaluadas antes de cualquiera de las asignaciones.

El número de variables a la izquierda y el número de valores a la derecha deben ser iguales:



```
& gt; & gt; & gt; a, b = 1, 2, 3
ValueError: demasiados valores para descomprimir
```

Más generalmente, el lado derecho puede ser cualquier tipo de secuencia (cadena, lista o tupla). Por ejemplo, para dividir una dirección de correo electrónico en un nombre de usuario y un dominio, podría escribir:


## [Las tuplas son inmutables] (# tuplas son inmutables)



Una tupla [<sup> 1 </sup>] (# fn1) es una secuencia de valores muy parecida a una lista. Los valores almacenados en una tupla pueden ser de cualquier tipo, y están indexados por enteros. La diferencia importante es que las tuplas son ** inmutables **. Las tuplas también son ** comparables ** y ** hashable **, por lo que podemos clasificar las listas y usar tuplas como valores clave en los diccionarios de Python.



Sintácticamente, una tupla es una lista de valores separados por comas:

& gt; & gt; & gt; t = 'a', 'b', 'c', 'd', 'e'

Aunque no es necesario, es común incluir tuplas entre paréntesis para ayudarnos a identificar tuplas rápidamente cuando observamos el código de Python:



& gt; & gt; & gt; t = ('a', 'b', 'c', 'd', 'e')

Para crear una tupla con un solo elemento, debe incluir la coma final:

## [Las tuplas son inmutables] (# tuplas son inmutables)



