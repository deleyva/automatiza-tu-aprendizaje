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


