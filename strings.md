Del capítulo [Strings](https://books.trinket.io/pfe/06-strings.html)

Una cadena es una secuencia Una cadena es una secuencia de caracteres. Puede acceder a los caracteres uno a la vez con el operador de corchete:

```python
>>> fruit = 'banana'
>>> letter = fruit[1]
```

Para la mayoría de las personas, la primera letra de "banana" es b, no a. Pero en Python, el índice es un desplazamiento desde el principio de la cadena, y el desplazamiento de la primera letra es cero.

### Obteniendo la longitud de una cadena

```python
>>> fruit = 'banana'
>>> len(fruit)
6
>>> last = fruit[length-1] # Esto es algo muy chulo que no tienen otros lenguajes de programación
>>> print(last)
a
```

### Atravesar un string con un loop

```python
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

```

Otra forma más sencilla:

```python
for char in fruit:
    print(char)
```

### Trocear cadenas

```python
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
# Y si omito un dígito antes o después
# de los dos puntos
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
```

### Las cadenas de texto son inmutables

```python
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
```

Se pueden cambiar creando un nuevo string:

```python
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
```

O con la función replace():

```python
cadena = 'Hola'
cadena = cadena.replace('H', 'h')
print(cadena)
hola
```

### El operador _in_

```python
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False

```

### Comparación de cadenas

Los operadores de comparación trabajan en cadenas. Para ver si dos cuerdas son iguales:

```python
if word == 'banana':
    print('All right, bananas.')
```

Otras operaciones de comparación son útiles para poner las palabras en orden alfabético:

```python
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
```

Python no maneja las letras mayúsculas y minúsculas de la misma manera que las personas. Todas las letras mayúsculas vienen antes de todas las letras minúsculas, así que:

```bash
Your word, Pineapple, comes before banana.
```

### Metodos de cadenas (String methods)

>**info**
>
>¿Qué son los métodos? Funciones pertenecientes a objetos, en este caso a una cadena de texto. 

```python
>>> stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str

    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.
>>>
>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA
```

Obteniendo el índice de una letra:

```python
>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1
```

El método de búsqueda puede encontrar subcadenas y caracteres:

```python
>>> word.find('na')
2
```

Puede tomar como segundo argumento el índice donde debe comenzar:

```python
>>> word.find('na', 3)
4
```

### Método strip()

```python
>>> line = '  Here we go  '
>>> line.strip()
'Here we go'
```

### Método startswith()

```python
>>> line = 'Have a nice day'
>>> line.startswith('Have')
True
>>> line.startswith('h')
False   # ¿Qué podríamos hacer para que coincidiera?
```

### Parseando cadenas

```python
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ',atpos)
>>> print(sppos)
31
>>> host = data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>>
```

### Formateando cadenas

```python
num1 = 2
num2 = 3
print('La suma de {} y {} es {}'.format(num1, num2, num1+num2))
print('{:>10}'.format('test'))
```

... y mucho más [aquí](https://pyformat.info/).

