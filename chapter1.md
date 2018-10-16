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



