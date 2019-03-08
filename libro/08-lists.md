Simplemente podríamos recordar cada número a medida que el usuario lo ingresó y usar funciones integradas para calcular la suma y el conteo al final.

Hacemos una lista vacía antes de que comience el ciclo, y luego cada vez que tenemos un número, lo agregamos a la lista. Al final del programa, simplemente calculamos la suma de los números en la lista y la dividimos por el recuento de los números en la lista para obtener el promedio.

## [Listas y cadenas] (# listas y cadenas)



Una cadena es una secuencia de caracteres y una lista es una secuencia de valores, pero una lista de caracteres no es lo mismo que una cadena. Para convertir de una cadena a una lista de caracteres, puedes usar `list`:



Como `list` es el nombre de una función incorporada, debes evitar usarla como nombre de variable. También evito la letra `l` porque se parece demasiado al número` 1`. Por eso uso `t`.

La función `list` rompe una cadena en letras individuales. Si desea dividir una cadena en palabras, puede usar el método `split`:



Una vez que haya usado `split` para dividir la cadena en una lista de palabras, puede usar el operador de índice (corchete) para mirar una palabra en particular en la lista.

Puede llamar a `split` con un argumento opcional llamado ** delimitador ** que especifica qué caracteres usar como límites de palabras. El siguiente ejemplo usa un guión como delimitador:



`join` es el inverso de` split`. Toma una lista de cadenas y concatena los elementos. `join` es un método de cadena, por lo que debes invocarlo en el delimitador y pasar la lista como parámetro:



En este caso, el delimitador es un carácter de espacio, por lo que `join` pone un espacio entre las palabras. Para concatenar cadenas sin espacios, puede usar la cadena vacía "" como un delimitador.



## [Líneas de análisis] (# líneas de análisis)

Por lo general, cuando estamos leyendo un archivo queremos hacer algo en las líneas que no sea simplemente imprimir toda la línea. A menudo queremos encontrar las "líneas interesantes" y luego ** analizar ** la línea para encontrar algunas ** partes ** interesantes de la línea. ¿Qué pasaría si quisiéramos imprimir el día de la semana desde esas líneas que comienzan con "De"?

`From stephen.marquard@uct.ac.za`**`Sat`**`Jan 5 09:14:16 2008`

El método de "división" es muy efectivo cuando se enfrenta a este tipo de problema. Podemos escribir un pequeño programa que busque líneas donde la línea comience con "De", `dividir 'esas líneas, y luego imprimir la tercera palabra en la línea:

Aquí también usamos la forma contraída de la declaración `if` donde colocamos el` continue` en la misma línea que el `if`. Esta forma contraída de `if` funciona de la misma manera que si` continue` estuviera en la siguiente línea y con sangría.

El programa produce la siguiente salida:

```Sat
Fri
Fri
Fri
    ...
```
Más adelante, aprenderemos técnicas cada vez más sofisticadas para elegir las líneas en las que trabajar y cómo separamos esas líneas para encontrar la información exacta que estamos buscando.

## [Objetos y valores] (# objetos y valores)



Si ejecutamos estas sentencias de asignación:

```a = 'banana'
b = 'banana'
```
sabemos que `a` y` b` se refieren a una cadena, pero no sabemos si se refieren a la cadena ** same **. Hay dos estados posibles:



Variables y objetos

En un caso, `a` y` b` se refieren a dos objetos diferentes que tienen el mismo valor. En el segundo caso, se refieren al mismo objeto.



Para verificar si dos variables se refieren al mismo objeto, puede usar el operador `is`.

En este ejemplo, Python solo creó un objeto de cadena, y tanto `a` como` b` se refieren a él.

Pero cuando creas dos listas, obtienes dos objetos:

En este caso, diríamos que las dos listas son ** equivalentes **, porque tienen los mismos elementos, pero no ** idénticas **, porque no son el mismo objeto. Si dos objetos son idénticos, también son equivalentes, pero si son equivalentes, no son necesariamente idénticos.



Hasta ahora, hemos estado utilizando indistintamente "objeto" y "valor", pero es más preciso decir que un objeto tiene un valor. Si ejecuta `a = [1,2,3]`, `a` se refiere a un objeto de lista cuyo valor es una secuencia particular de elementos. Si otra lista tiene los mismos elementos, diríamos que tiene el mismo valor.



## [Aliasing] (# aliasing)



Si `a` se refiere a un objeto y usted asigna` b = a`, entonces ambas variables se refieren al mismo objeto:

La asociación de una variable con un objeto se denomina ** referencia **. En este ejemplo, hay dos referencias al mismo objeto.



Un objeto con más de una referencia tiene más de un nombre, por lo que decimos que el objeto tiene ** un alias **.



Si el objeto con alias es mutable, los cambios realizados con un alias afectan al otro:

```>>> b[0] = 17
>>> print(a)
[17, 2, 3]
```
Aunque este comportamiento puede ser útil, es propenso a errores. En general, es más seguro evitar los alias cuando trabaja con objetos mutables.



Para objetos inmutables como cadenas, el aliasing no es tanto un problema. En este ejemplo:

```a = 'banana'
b = 'banana'
```
casi nunca hace una diferencia si `a` y` b` se refieren a la misma cadena o no.

## [Lista de argumentos] (# lista-argumentos)



Cuando pasa una lista a una función, la función obtiene una referencia a la lista. Si la función modifica un parámetro de lista, la persona que llama ve el cambio. Por ejemplo, `delete_head` elimina el primer elemento de una lista:

```def delete_head(t):
    del t[0]
```
Así es como se usa:

El parámetro `t` y la variable` letras` son alias para el mismo objeto.

Es importante distinguir entre operaciones que modifican listas y operaciones que crean nuevas listas. Por ejemplo, el método `append` modifica una lista, pero el operador` + `crea una nueva lista:



Esta diferencia es importante cuando escribes funciones que se supone que modifican las listas. Por ejemplo, esta función ** no ** elimina el encabezado de una lista:

```def bad_delete_head(t):
    t = t[1:]              # WRONG!
```
El operador de sector crea una nueva lista y la asignación hace que `t` se refiera a ella, pero nada de eso tiene ningún efecto en la lista que se pasó como argumento.



Una alternativa es escribir una función que crea y devuelve una nueva lista. Por ejemplo, `tail` devuelve todos menos el primer elemento de una lista:

```def tail(t):
    return t[1:]
```
Esta función deja la lista original sin modificar. Así es como se usa:

Ejercicio 1:

Escriba una función llamada `chop` que tome una lista y la modifique, eliminando el primer y último elemento y devuelva` Ninguno`.

Luego escribe una función llamada `middle` que toma una lista y devuelve una nueva lista que contiene todos los elementos, excepto el primero y el último.

## [depuración] (# depuración)



El uso descuidado de listas (y otros objetos mutables) puede llevar a largas horas de depuración. Aquí hay algunos escollos comunes y maneras de evitarlos:

<li> No olvide que la mayoría de los métodos de lista modifican el argumento y devuelven `Ninguno`. Esto es lo contrario de los métodos de cadena, que devuelven una cadena nueva y dejan el original solo.
Si estás acostumbrado a escribir un código de cadena como este:
<pre class = "sourceCode python"> `word = word.strip ()` </pre>
Es tentador escribir un código de lista como este: ~ <sub> ~ </sub> {.python} t = t.sort () # WRONG! ~ <sub> ~ </sub>

Debido a que `sort` devuelve` None`, la siguiente operación que realice con `t` es probable que falle.
Antes de utilizar los métodos de lista y los operadores, debe leer la documentación detenidamente y luego probarlos en modo interactivo. Los métodos y operadores que las listas comparten con otras secuencias (como cadenas) se documentan en [https://docs.python.org/2/library/stdtypes.html#string-methods◆(https://docs.python.org /2/library/stdtypes.html#string-methods). Los métodos y operadores que solo se aplican a secuencias mutables están documentados en [https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types◆(https://docs.python.org/2 /library/stdtypes.html#mutable-sequence-types). </li>
<li> Escoge un idioma y quédate con él.

Parte del problema con las listas es que hay demasiadas formas de hacer las cosas. Por ejemplo, para eliminar un elemento de una lista, puede usar `pop`,` remove`, `del`, o incluso una asignación de sector.
Para agregar un elemento, puede usar el método `append` o el operador` + `. Pero no olvides que estos son correctos:
<pre class = "sourceCode python"> <code class = "sourceCode python"> t.append (x)
t = t + [x] </code> </pre>
Y estos son incorrectos:
<pre class = "sourceCode python"> <code class = "sourceCode python"> t.append ([x]) # WRONG!
t = t.append (x) # WRONG!
t + [x] # ¡INCORRECTO!
t = t + x # WRONG! </code> </pre>
Pruebe cada uno de estos ejemplos en modo interactivo para asegurarse de que comprende lo que hacen. Observe que solo el último causa un error de tiempo de ejecución; los otros tres son legales, pero hacen lo incorrecto. </li>
<li> Haga copias para evitar el aliasing.

Si desea utilizar un método como `sort` que modifica el argumento, pero también necesita conservar la lista original, puede hacer una copia.
<pre class = "sourceCode python"> <code class = "sourceCode python"> orig = t [:]
t.sort () </code> </pre>
En este ejemplo, también podría usar la función incorporada `ordenada`, que devuelve una nueva lista ordenada y deja el original solo. ¡Pero en ese caso, debes evitar usar `ordenados` como nombre de variable! </li>
<li> Listas, `split` y archivos
Cuando leemos y analizamos archivos, hay muchas oportunidades de encontrar información que puede bloquear nuestro programa, por lo que es una buena idea revisar el patrón ** guardian ** cuando se trata de escribir programas que leen un archivo y buscar una "aguja". en el pajar ".
Revisemos nuestro programa que busca el día de la semana en las líneas de nuestro archivo:
`From stephen.marquard@uct.ac.za`**`Sat`**`Jan 5 09:14:16 2008`
Ya que estamos dividiendo esta línea en palabras, podríamos prescindir del uso de `startswith` y simplemente mirar la primera palabra de la línea para determinar si estamos interesados ​​en la línea. Podemos usar `continue` para omitir las líneas que no tienen" De "como la primera palabra de la siguiente manera:
<pre class = "sourceCode python"> <code class = "sourceCode python"> fhand = open ('mbox-short.txt')
para linea en mano
palabras = línea.split ()
si las palabras [0]! = 'De': continuar
imprimir (palabras [2]) </code> </pre>
Esto parece mucho más simple y ni siquiera necesitamos hacer el `rstrip` para eliminar la nueva línea al final del archivo. Pero es mejor?
<pre> <code> python search8.py
Sab
Rastreo (llamadas recientes más última):
Archivo "search8.py", línea 5, en & lt; module & gt;
si las palabras [0]! = 'De': continuar
IndexError: índice de lista fuera de rango </code> </pre>
Funciona y vemos el día desde la primera línea (Sat), pero luego el programa falla con un error de rastreo. ¿Qué salió mal? ¿Qué datos desordenados hicieron que nuestro programa elegante, inteligente y muy Pythonic fallara?
Puedes mirarlo fijamente durante un largo tiempo y resolverlo o pedirle ayuda a alguien, pero el enfoque más rápido e inteligente es agregar una declaración de "impresión". El mejor lugar para agregar la declaración de impresión es justo antes de la línea donde falló el programa e imprimir los datos que parecen estar causando la falla.
Ahora este enfoque puede generar una gran cantidad de líneas de salida, pero al menos tendrá inmediatamente alguna pista sobre el problema en cuestión. Así que agregamos una impresión de la variable `palabras` justo antes de la línea cinco. Incluso agregamos un prefijo "Debug:" a la línea para que podamos mantener nuestra salida regular separada de nuestra salida de depuración.
<pre class = "sourceCode python"> <code class = "sourceCode python"> para la línea de la mano:
palabras = línea.split ()
imprimir ('Depurar:', palabras)
si las palabras [0]! = 'De': continuar
imprimir (palabras [2]) </code> </pre>
Cuando ejecutamos el programa, una gran cantidad de salida se desplaza fuera de la pantalla, pero al final, vemos nuestra salida de depuración y el rastreo, por lo que sabemos lo que sucedió justo antes del rastreo.
<pre> <code> Debug: ['X-DSPAM-Confidence:', '0.8475']
Depuración: ['X-DSPAM-Probability:', '0.0000']
Depurar: []
Rastreo (llamadas recientes más última):
Archivo "search9.py", línea 6, en & lt; module & gt;
si las palabras [0]! = 'De': continuar
IndexError: índice de lista fuera de rango </code> </pre>
Cada línea de depuración está imprimiendo la lista de palabras que obtenemos cuando "dividimos" la línea en palabras. Cuando el programa falla, la lista de palabras está vacía `[]`. Si abrimos el archivo en un editor de texto y miramos el archivo, en ese punto se ve como sigue:
<pre> <code> X-DSPAM-Resultado: Inocente
Procesado X-DSPAM: sábado 5 de enero 09:14:16 2008
X-DSPAM-Confianza: 0.8475
X-DSPAM-Probabilidad: 0.0000

Detalles: http://source.sakaiproject.org/viewsvn/?view=rev&amp;rev=39772 </code> </pre>
¡El error ocurre cuando nuestro programa encuentra una línea en blanco! Por supuesto, hay "cero palabras" en una línea en blanco. ¿Por qué no pensamos en eso cuando estábamos escribiendo el código? Cuando el código busca la primera palabra (`palabra [0]`) para verificar si coincide con "De", obtenemos un error de "índice fuera de rango".
Por supuesto, este es el lugar perfecto para agregar un código ** guardian ** para evitar marcar la primera palabra si la primera palabra no está allí. Hay muchas maneras de proteger este código; Elegiremos verificar el número de palabras que tenemos antes de mirar la primera palabra:
<pre class = "sourceCode python"> <code class = "sourceCode python"> fhand = open ('mbox-short.txt')
cuenta = 0
para linea en mano
palabras = línea.split ()
# imprimir 'Depurar:', palabras
si len (palabras) == 0: continuar
si las palabras [0]! = 'De': continuar
imprimir (palabras [2]) </code> </pre>
Primero comentamos la declaración de impresión de depuración en lugar de eliminarla, en caso de que nuestra modificación falle y tengamos que volver a depurar. Luego agregamos una declaración del tutor que verifica si tenemos cero palabras, y si es así, usamos `continue` para saltar a la siguiente línea del archivo.
Podemos pensar que las dos afirmaciones "continuar" nos ayudan a refinar el conjunto de líneas que son "interesantes" para nosotros y que queremos procesar un poco más. Una línea que no tiene palabras es "poco interesante" para nosotros, así que saltamos a la siguiente línea. Una línea que no tiene "De" como su primera palabra no nos interesa, así que la omitimos.
El programa modificado se ejecuta con éxito, así que quizás sea correcto. Nuestra declaración de tutores asegura que las `palabras [0]` nunca fallarán, pero tal vez no sea suficiente. Cuando estamos programando, siempre debemos pensar: "¿Qué podría salir mal?" </li>

Si estás acostumbrado a escribir un código de cadena como este:



Antes de utilizar los métodos de lista y los operadores, debe leer la documentación detenidamente y luego probarlos en modo interactivo. Los métodos y operadores que las listas comparten con otras secuencias (como cadenas) se documentan en [https://docs.python.org/2/library/stdtypes.html#string-methods◆(https://docs.python.org /2/library/stdtypes.html#string-methods). Los métodos y operadores que solo se aplican a secuencias mutables están documentados en [https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types◆(https://docs.python.org/2 /library/stdtypes.html#mutable-sequence-types).



Para agregar un elemento, puede usar el método `append` o el operador` + `. Pero no olvides que estos son correctos:

Pruebe cada uno de estos ejemplos en modo interactivo para asegurarse de que comprende lo que hacen. Observe que solo el último causa un error de tiempo de ejecución; Los otros tres son legales, pero hacen lo incorrecto.



En este ejemplo, también podría usar la función incorporada `ordenada`, que devuelve una nueva lista ordenada y deja el original solo. ¡Pero en ese caso debes evitar usar `ordenados` como nombre de variable!

Cuando leemos y analizamos archivos, hay muchas oportunidades de encontrar información que puede bloquear nuestro programa, por lo que es una buena idea revisar el patrón ** guardian ** cuando se trata de escribir programas que leen un archivo y buscar una "aguja". en el pajar ".

`From stephen.marquard@uct.ac.za`**`Sat`**`Jan 5 09:14:16 2008`

Esto parece mucho más simple y ni siquiera necesitamos hacer el `rstrip` para eliminar la nueva línea al final del archivo. Pero es mejor?

Puedes mirarlo fijamente durante un largo tiempo y resolverlo o pedirle ayuda a alguien, pero el enfoque más rápido e inteligente es agregar una declaración de "impresión". El mejor lugar para agregar la declaración de impresión es justo antes de la línea donde falló el programa e imprimir los datos que parecen estar causando la falla.

Cuando ejecutamos el programa, una gran cantidad de salida se desplaza fuera de la pantalla, pero al final, vemos nuestra salida de depuración y el rastreo, por lo que sabemos lo que sucedió justo antes del rastreo.

¡El error ocurre cuando nuestro programa encuentra una línea en blanco! Por supuesto, hay "cero palabras" en una línea en blanco. ¿Por qué no pensamos en eso cuando estábamos escribiendo el código? Cuando el código busca la primera palabra (`palabra [0]`) para verificar si coincide con "De", obtenemos un error de "índice fuera de rango".

Primero comentamos la declaración de impresión de depuración en lugar de eliminarla, en caso de que nuestra modificación falle y tengamos que volver a depurar. Luego agregamos una declaración del tutor que verifica si tenemos cero palabras, y si es así, usamos `continue` para saltar a la siguiente línea del archivo.

El programa modificado se ejecuta con éxito, así que quizás sea correcto. Nuestra declaración de tutores asegura que las `palabras [0]` nunca fallarán, pero tal vez no sea suficiente. Cuando estamos programando, siempre debemos pensar: "¿Qué podría salir mal?"

Ejercicio 2: Averigüe qué línea del programa anterior aún no está correctamente protegida. Vea si puede construir un archivo de texto que haga que el programa falle y luego modifíquelo para que la línea esté bien protegida y pruébelo para asegurarse de que maneja su nuevo archivo de texto.

Ejercicio 3: reescriba el código guardián en el ejemplo anterior sin dos declaraciones 'if'. En su lugar, use una expresión lógica compuesta utilizando el operador lógico `and` con una sola instrucción` if`.

## [Glosario] (# glosario)























## [Ejercicios] (# ejercicios)

Ejercicio 4: descargue una copia del archivo desde [www.py4e.com/code3/romeo.txt◆(hpyp://www.py4e.com/code3/romeo.txt)



Escriba un programa para abrir el archivo `romeo.txt` y léalo línea por línea. Para cada línea, divida la línea en una lista de palabras usando la función `split`.

Para cada palabra, verifique si la palabra ya está en una lista. Si la palabra no está en la lista, agréguela a la lista.

Cuando se complete el programa, ordene e imprima las palabras resultantes en orden alfabético.

```Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
```
** Ejercicio 5: ** Escriba un programa para leer los datos del buzón de correo y cuando encuentre la línea que comienza con "De", dividirá la línea en palabras usando la función `split`. Estamos interesados ​​en quién envió el mensaje, que es la segunda palabra en la línea Desde.

`De stephen.marquard@uct.ac.za sábado 5 de enero 09:14:16 2008`

Analizará la línea Desde e imprimirá la segunda palabra para cada línea Desde, también contará el número de líneas Desde (no Desde :) e imprimirá un recuento al final.

Esta es una buena salida de muestra con algunas líneas eliminadas:

```python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
```
** Ejercicio 6: ** Reescriba el programa que solicita al usuario una lista de números e imprime el máximo y el mínimo de los números al final cuando el usuario ingresa "listo". Escriba el programa para almacenar los números que el usuario ingresa en una lista y use las funciones `max ()` y `min ()` para calcular los números máximo y mínimo después de que se complete el ciclo.

```Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
```
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
