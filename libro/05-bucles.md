
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

<li class = "has-dropdown"> [Iteración] (# iteración) <ul class = "dropdown">
- [Actualizando variables] (# actualización-variables)
- [La instrucción 'while'] (# la declaración while-while)
- [Bucles infinitos] (# bucles infinitos)
- ["Infinite loops" y `break`] (# infinite-loops-and-break)
- [Finalización de iteraciones con `continue`] (# finish-iterations-with-continue)
- [Bucles definidos utilizando `for`] (# definite-loops-using-for)
<li> [Patrones de bucle] (# patrones de bucle) <ul>
- [Contando y sumando bucles] (# contando y sumando bucles)
- [Bucles máximos y mínimos] (# bucles máximos y mínimos)
# [Iteración] (# iteración)



## [Actualizando variables] (# actualizando variables)



Un patrón común en las declaraciones de asignación es una instrucción de asignación que actualiza una variable, donde el nuevo valor de la variable depende de la antigua.

```x = x + 1
```
Esto significa que "obtenga el valor actual de` x`, agregue 1 y luego actualice `x` con el nuevo valor".

Si intentas actualizar una variable que no existe, obtienes un error, porque Python evalúa el lado derecho antes de asignar un valor a `x`:

```>>> x = x + 1
NameError: name 'x' is not defined
```
Antes de poder actualizar una variable, debe ** inicializarla **, generalmente con una tarea simple:



```>>> x = 0
>>> x = x + 1
```
Actualizar una variable agregando 1 se llama ** incremento **; restar 1 se llama un ** decremento **.



## [La declaración 'while'] (# la declaración while-while)


Las computadoras se utilizan a menudo para automatizar tareas repetitivas. Repetir tareas idénticas o similares sin cometer errores es algo que a las computadoras les va bien y a las personas les va mal. Debido a que la iteración es tan común, Python proporciona varias características de lenguaje para que sea más fácil.

Una forma de iteración en Python es la instrucción `while`. Aquí hay un programa simple que cuenta a partir de cinco y luego dice "¡Explosión!".

```n = 5
while n &gt; 0:
    print(n)
    n = n - 1
print('Blastoff!')
```
Casi se puede leer la instrucción `while` como si fuera inglés. Significa que "Mientras` n` es mayor que 0, muestra el valor de `n` y luego reduce el valor de` n` en 1. Cuando llegues a 0, sal de la instrucción `while` y muestra la palabra` Blastoff ! `"



Más formalmente, aquí está el flujo de ejecución para una instrucción `while ':

1. Evalúe la condición, obteniendo "Verdadero" o "Falso".
1. Si la condición es falsa, salga de la instrucción `while` y continúe con la ejecución en la siguiente instrucción.
1. Si la condición es verdadera, ejecute el cuerpo y luego vuelva al paso 1.

Si la condición es falsa, salga de la instrucción `while` y continúe con la ejecución en la siguiente instrucción.

Este tipo de flujo se llama un bucle ** porque el tercer paso vuelve a la parte superior. Cada vez que ejecutamos el cuerpo del bucle llamamos una ** iteración **. Para el bucle anterior, diríamos "tenía cinco iteraciones", lo que significa que el cuerpo del bucle se ejecutó cinco veces.



El cuerpo del bucle debe cambiar el valor de una o más variables para que finalmente la condición se vuelva falsa y el bucle finalice. Llamamos a la variable que cambia cada vez que el bucle se ejecuta y controla cuando el bucle termina la ** variable de iteración **. Si no hay una variable de iteración, el bucle se repetirá para siempre, dando como resultado un ** bucle infinito **.

## [Bucles infinitos] (# bucles infinitos)
Una fuente inagotable de diversión para los programadores es la observación de que las instrucciones en el champú, "Enjabonar, enjuagar, repetir", son un bucle infinito porque no hay una ** variable de iteración ** que indique cuántas veces se debe ejecutar el bucle.



En el caso de `countdown`, podemos probar que el bucle termina porque sabemos que el valor de` n` es finito, y podemos ver que el valor de `n` se reduce cada vez que pasa por el bucle, por lo que eventualmente tiene que llegar a 0. Otras veces, un bucle es obviamente infinito porque no tiene ninguna variable de iteración.

## ["Infinite loops" y `break`] (# infinite-loops-and-break)



A veces no sabes que es hora de terminar un ciclo hasta que llegues a la mitad del cuerpo. En ese caso, puede escribir un bucle infinito a propósito y luego usar la instrucción `break` para saltar fuera del bucle.

Este bucle es obviamente un ** bucle infinito ** porque la expresión lógica en la instrucción `while` es simplemente la constante lógica` True`:

```n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')
```
Si comete el error y ejecuta este código, aprenderá rápidamente cómo detener un proceso de Python fuera de control en su sistema o dónde encontrará el botón de apagado en su computadora. Este programa se ejecutará para siempre o hasta que la batería se agote porque la expresión lógica en la parte superior del bucle siempre es verdadera en virtud del hecho de que la expresión es el valor constante "Verdadero".

Si bien este es un bucle infinito disfuncional, aún podemos usar este patrón para crear bucles útiles siempre y cuando agreguemos cuidadosamente el código del cuerpo del bucle para salir explícitamente del bucle usando `break` cuando hayamos alcanzado la condición de salida.

Por ejemplo, supongamos que desea recibir información del usuario hasta que escriban `done`. Podrías escribir:

La condición del bucle es `True`, que siempre es verdadera, por lo que el bucle se ejecuta repetidamente hasta que llega a la instrucción break.

Cada vez que pasa, le pide al usuario un corchete angular. Si el usuario escribe `done`, la instrucción` break` sale del bucle. De lo contrario, el programa hace eco de lo que sea que el usuario escriba y vuelve a la parte superior del bucle. Aquí hay una muestra de ejecución:

```&gt; hello there
hello there
&gt; finished
finished
&gt; done
Done!
```
Esta forma de escribir bucles 'while` es común porque puede verificar la condición en cualquier parte del bucle (no solo en la parte superior) y puede expresar la condición de detención afirmativamente ("detenerse cuando esto sucede") en lugar de negativamente ("seguir adelante hasta que eso suceda.

## [Finalización de iteraciones con `continue`] (# finish-iterations-with-continue)



A veces se encuentra en una iteración de un bucle y desea finalizar la iteración actual y pasar de inmediato a la siguiente iteración. En ese caso, puede usar la instrucción `continue` para saltar a la siguiente iteración sin terminar el cuerpo del bucle para la iteración actual.

Aquí hay un ejemplo de un bucle que copia su entrada hasta que el usuario escribe "hecho", pero trata las líneas que comienzan con el carácter de hash como líneas que no se imprimen (como los comentarios de Python).

Aquí hay una muestra de ejecución de este nuevo programa con `continue` agregado.

```&gt; hello there
hello there
&gt; # don't print this
&gt; print this!
print this!
&gt; done
Done!
```
Todas las líneas se imprimen, excepto la que comienza con el signo hash porque cuando se ejecuta `continue`, finaliza la iteración actual y vuelve a la instrucción` while` para iniciar la siguiente iteración, omitiendo la instrucción `print` .

## [Bucles definidos usando `for`] (# definite-loops-using-for)



A veces queremos recorrer un ** conjunto ** de cosas como una lista de palabras, las líneas de un archivo o una lista de números. Cuando tenemos una lista de cosas para recorrer, podemos construir un bucle ** definido ** usando una instrucción `for`. Llamamos a la frase `while` un bucle ** indefinido ** porque simplemente se repite hasta que alguna condición se convierte en` Falsa`, mientras que el bucle `for` se repite en un conjunto conocido de elementos, por lo que se ejecuta a través de tantas iteraciones como Elementos del conjunto.

La sintaxis de un bucle `for` es similar al bucle` while` en que hay una sentencia `for` y un cuerpo de bucle:

```friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```
En términos de Python, la variable `friends` es una lista [<sup> 1 </sup>] (# fn1) de tres cadenas y el bucle` for` recorre la lista y ejecuta el cuerpo una vez para cada una de las tres cadenas en la lista que da como resultado esta salida:

```Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```La traducción de este bucle `for` al inglés no es tan directa como el` while`, pero si piensa en los amigos como un ** conjunto **, esto es así: "Ejecute las declaraciones en el cuerpo del bucle for una vez para cada amigo ** en ** el conjunto llamado amigos ".

Mirando el bucle `for`, ** for ** y ** in ** son palabras clave reservadas de Python, y` friend` y `friends` son variables.

```for friend in friends:
    print('Happy New Year:', friend)
```
En particular, `friend` es la ** variable de iteración ** para el bucle for. La variable `friend` cambia para cada iteración del bucle y se controla cuando se completa el bucle` for`. La ** variable de iteración ** pasa sucesivamente por las tres cadenas almacenadas en la variable `friends`.

## [Patrones de bucle] (# patrones de bucle)


Estos bucles son generalmente construidos por:

- Inicializando una o más variables antes de que comience el ciclo.
- Realizar algunos cálculos en cada elemento del cuerpo del bucle, posiblemente cambiando las variables en el cuerpo del bucle
- Observando las variables resultantes cuando se completa el bucle.

Usaremos una lista de números para demostrar los conceptos y la construcción de estos patrones de bucle.

### [Recuento y suma de bucles] (# contando y sumando bucles)

Por ejemplo, para contar el número de elementos en una lista, escribiríamos el siguiente bucle `for`:

```count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)
```
Establecemos la variable `count` en cero antes de que comience el bucle, luego escribimos un bucle` for` para ejecutar la lista de números. Nuestra variable ** iteration ** se llama `itervar` y aunque no usamos` itervar` en el bucle, controla el bucle y hace que el cuerpo del bucle se ejecute una vez para cada uno de los valores de la lista.

En el cuerpo del bucle, agregamos 1 al valor actual de `count` para cada uno de los valores en la lista. Mientras el bucle se está ejecutando, el valor de `count` es el número de valores que hemos visto" hasta ahora ".

Una vez que el bucle se completa, el valor de `count` es el número total de elementos. El número total "cae en nuestra vuelta" al final del bucle. Construimos el bucle para que tengamos lo que queremos cuando el bucle finalice.

Otro bucle similar que calcula el total de un conjunto de números es el siguiente:

```total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
```
En este bucle nosotros ** hacemos ** usamos la ** variable de iteración **. En lugar de simplemente agregar uno al `recuento` como en el bucle anterior, agregamos el número real (3, 41, 12, etc.) al total acumulado durante cada iteración de bucle. Si piensa en la variable `total`, contiene el" total acumulado de los valores hasta ahora ". Entonces, antes de que el bucle comience, `total` es cero porque aún no hemos visto ningún valor, durante el bucle` total` es el total acumulado, y al final del bucle `total` es el total general de todos los valores en el lista.

A medida que se ejecuta el bucle, 'total' acumula la suma de los elementos; una variable utilizada de esta manera a veces se llama un ** acumulador **.



Ni el bucle de conteo ni el bucle de suma son particularmente útiles en la práctica porque hay funciones incorporadas `len ()` y `sum ()` que computan el número de elementos en una lista y el total de los elementos en la lista respectivamente .

### [Bucles máximos y mínimos] (# bucles máximos y mínimos)



Para encontrar el valor más grande en una lista o secuencia, construimos el siguiente bucle:

```largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar &gt; largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
```
Cuando el programa se ejecuta, la salida es la siguiente:

```Before: None
Loop: 3 3
Loop: 41 41
Loop: 12 41
Loop: 9 41
Loop: 74 74
Loop: 15 74
Largest: 74
```
La variable 'más grande' se considera mejor como el "valor más grande que hemos visto hasta ahora". Antes del bucle, establecemos `más grande` en la constante` Ninguno`. `Ninguna` es un valor constante especial que podemos almacenar en una variable para marcar la variable como" vacía ".

Antes de que comience el bucle, el valor más grande que hemos visto hasta ahora es 'Ninguno', ya que todavía no hemos visto ningún valor. Mientras el bucle se está ejecutando, si `más grande` es` Ninguno` entonces tomamos el primer valor que vemos como el más grande hasta ahora. Se puede ver en la primera iteración cuando el valor de `itervar` es 3, ya que` más grande` es `Ninguno`, inmediatamente establecemos que 'más grande` es 3.

Después de la primera iteración, `más grande` ya no es` Ninguno`, así que la segunda parte de la expresión lógica compuesta que comprueba `itervar & gt; El mayor 'se dispara solo cuando vemos un valor que es más grande que el "más grande hasta ahora". Cuando vemos un nuevo valor "aún más grande", tomamos ese nuevo valor para "más grande". Puede ver en la salida del programa que "más grande" progresa de 3 a 41 a 74.

Al final del ciclo, hemos escaneado todos los valores y la variable "más grande" ahora contiene el valor más grande en la lista.

Para calcular el número más pequeño, el código es muy similar con un pequeño cambio:

```smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar &lt; smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
```
Nuevamente, 'más pequeño' es el "más pequeño hasta ahora" antes, durante y después de que se ejecute el bucle. Cuando el bucle se ha completado, `más pequeño` contiene el valor mínimo en la lista.

De nuevo, al contar y sumar, las funciones incorporadas `max ()` y `min ()` hacen que la escritura de estos bucles exactos sea innecesaria.

La siguiente es una versión simple de la función `min ()` incorporada en Python:

```def min(values):
    smallest = None
    for value in values:
        if smallest is None or value &lt; smallest:
            smallest = value
    return smallest
```En la versión de la función del código más pequeño, eliminamos todas las declaraciones `print` para que sean equivalentes a la función` min` que ya está incorporada en Python.

## [depuración] (# depuración)

A medida que comienzas a escribir programas más grandes, puedes pasar más tiempo depurando. Más código significa más posibilidades de cometer un error y más lugares para que los errores se oculten.



Una forma de reducir el tiempo de depuración es "depuración por bisección". Por ejemplo, si hay 100 líneas en su programa y las verifica una a la vez, tomaría 100 pasos.

En su lugar, intenta romper el problema por la mitad. Mire en la mitad del programa, o cerca de él, para un valor intermedio que pueda verificar. Agregue una declaración `print` (o algo más que tenga un efecto verificable) y ejecute el programa.

Si la verificación del punto medio es incorrecta, el problema debe estar en la primera mitad del programa. Si es correcto, el problema está en la segunda mitad.

Cada vez que realiza una verificación como esta, reduce a la mitad el número de líneas que tiene que buscar. Después de seis pasos (que es mucho menos que 100), se reduciría a una o dos líneas de código, al menos en teoría.

En la práctica, no siempre está claro qué es lo "medio del programa" y no siempre es posible verificarlo. No tiene sentido contar líneas y encontrar el punto medio exacto. En su lugar, piense en los lugares del programa en los que podría haber errores y en los lugares donde es fácil poner un cheque. Luego, elija un lugar donde piense que las probabilidades son casi las mismas de que el error esté antes o después de la comprobación.

## [Glosario] (# glosario)







Una asignación que da un valor inicial a una variable que se actualizará.







## [Ejercicios] (# ejercicios)

Ejercicio 1: escriba un programa que lea números repetidamente hasta que el usuario ingrese "listo". Una vez que se ingrese "listo", imprima el total, el recuento y el promedio de los números. Si el usuario ingresa algo que no sea un número, detecte su error usando `try` y` except` e imprima un mensaje de error y salte al siguiente número.

```Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
```
Ejercicio 2: escriba otro programa que solicite una lista de números como arriba y al final imprima el máximo y el mínimo de los números en lugar del promedio.

---


1. Examinaremos las listas con más detalle en un capítulo posterior. [↩] (# fnref1)

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
