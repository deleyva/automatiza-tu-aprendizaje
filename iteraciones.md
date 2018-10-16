## Iteraciones o loops

Del capítulo [Loops and iterations](https://books.trinket.io/pfe/05-iterations.html)

>**info**
>
>Palabras reservadas en Python:
>
>and       del       from      None      True
>as        elif      global    nonlocal  try
>assert    else      if        not       while
>break     except    import    or        with
>class     False     in        pass      yield
>continue  finally   is        raise
>def       for       lambda    

>**info**
>
>¿Qué es un traceback? traceback es una lista de las funciones que se ejecutan, impresa cuando se produce una excepción.

### The while statement

Los ordenadores se utilizan a menudo para automatizar tareas repetitivas. Repetir tareas idénticas o similares sin cometer errores es algo que a las computadoras les va bien y a las personas les va mal. Debido a que la iteración es tan común, Python proporciona varias características de lenguaje para que sea más fácil. Una forma de iteración en Python es la instrucción while. Aquí hay un programa simple que cuenta a partir de cinco y luego dice "¡Blastoff!".

```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```

### Loops infinitos

```python
n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')
```

Para salir, presionar Ctrl + r

Por ejemplo, supongamos que desea recibir información del usuario hasta que escriban listo. Podrías escribir:

<iframe src="https://trinket.io/embed/python3/e180d9bfe9" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Terminando las iteraciones con _Continue_

A veces se encuentra en una iteración de un bucle y desea finalizar la iteración actual y pasar de inmediato a la siguiente iteración. En ese caso, puede usar la instrucción continue para saltar a la siguiente iteración sin terminar el cuerpo del bucle para la iteración actual. 

Aquí hay un ejemplo de un bucle que copia su entrada hasta que el usuario escribe "hecho", pero trata las líneas que comienzan con el carácter de hash como líneas que no se imprimen (como los comentarios de Python).

<iframe src="https://trinket.io/embed/python3/65a108bc2b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Loos definidos usando _for_

A veces queremos recorrer un conjunto de cosas como una lista de palabras, las líneas en un archivo o una lista de números. Cuando tenemos una lista de cosas para recorrer, podemos construir un bucle definido usando una instrucción for. Llamamos a la instrucción while un bucle indefinido porque simplemente se repite hasta que alguna condición se vuelve falsa, mientras que el bucle for se recorre en un conjunto conocido de elementos, por lo que se ejecuta en tantas iteraciones como elementos hay en el conjunto. 

La sintaxis de un bucle for es similar al bucle while ya que hay una sentencia for y un cuerpo de bucle:

```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```

En términos de Python, la variable friends es una lista de tres cadenas y el bucle for recorre la lista y ejecuta el cuerpo una vez para cada una de las tres cadenas en la lista que da como resultado esta salida:

```bash
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```

### Contando y sumando

```python
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1 # También se puede hacer count += 1
print('Count: ', count)
```

```python
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
```

### Loops para buscar el máximo y el mínimo

```python
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
```

```python
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
```

```python
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
```