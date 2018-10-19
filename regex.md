## Regex

### Intro

Ya hemos trabajado con archivos de texto tratando de encontrar, modificar o extraer datos del mismo. Sabemos que teníamos que seguir los siguientes pasos:

* Abrir el archivo en modo lectura
* Recorrer todas las líneas del archivo
	* Si la linea empieza por x hacer lo siguiente:
		* Buscar la posición del caracter donde comienza el texto que queremos extraer.
		* Trocear la cadena de texto usando la posición anterior como punto de partida y almacenarla en una variable o añadirla a una lista.

El programa quedó así:

```python
fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From '):
	    tokens = line.split()
    	print(tokens[1])
    	count += 1

print("There were", count, "lines in the file with From as the first word")
```

Trabajar con regex nos va a ahorrar mucho trabajo. Simplemente definiremos un patrón y con una sola línea de código nos lo buscará y extraerá del texto objeto de trabajo. Los pasos necesarios serán:

* Importar la librería re (```import re```)
* Abrir el archivo en modo lectura.
* Encontrar el patrón que queremos buscar y almacenar todas las ocurrencias en una lista.

¿Has visto? No se requiere ningún bucle. El anterior script quedaría así:

```python
import re
fh = open("mbox-short.txt")
lista = re.findall('[0-9]+', fh.read())
```

### Clases de caracter

|
Shorthand character class
|
Represents
|
|--- |--- |
|\d|Any numeric digit from 0 to 9.|
|\D|Any character that is not a numeric digit from 0 to 9.|
|\w|Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)|
|\W|Any character that is not a letter, numeric digit, or the underscore character.|
|\s|Any space, tab, or newline character. (Think of this as matching “space” characters.)|
|\S|Any character that is not a space, tab, or newline.|


### Recetas

Imagina que quieres encontrar un número de teléfono en una cadena. Sabes el patrón: tres números, un guión, tres números, un guión y cuatro números. Aquí tienes un ejemplo: '415-555-4242'

El caracter que usamos en las regex para encontrar números es '\d'. Pues bien, el patrón que queremos encontrar sería: r'\d\d\d-\d\d\d-\d\d\d'.

>**info**
>
>¿Qué significa la 'r' en r'\d\d\d-\d\d\d-\d\d\d'?
>
>%accordion%Solución%accordion%
>
>r significa 'raw', es decir, crudo. Cogerá la cadena de texto tal cual, sin tomar el caracter contrabarra '\' como caracter de escape.
>
>%/accordion%

Bues bien, para extraer el número quedaría:

```python
import re
texto = 'Mi número de teléfono es 415-555-4242'
numero = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', texto)
print(numero)
```

La salida sería una lista con un elemento = ['415-555-4242']

Imagina que quieres sacar sólo el segundo elemento, es decir, los segundos tres números números. Agruparemos los grupos que queramos hacer usando paréntesis.

```python
import re
texto = 'Mi número de teléfono es 415-555-4242'
numero = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', texto)
print(numero) # Saldrá una lista con un tuple [('415', '555-4242')]
print(numero[0][1]) # Saldrá '555-4242'
```
#### Más recetas

Usando re.compile y accediendo a los datos con la función group():

```python
>>> heroRegex = re.compile (r'Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'
```

```python
>>> mo2 = heroRegex.search('Tina Fey and Batman.')
>>> mo2.group()
'Tina Fey'
```

Especificando caracteres opcionales '()?':

```python
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
```

```python
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'

>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-4242'
```

Encontrando cero o más '*':

```python
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'

>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
```

Encontrando uno o más con '+':

```python
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo3 == None
True
```

Encontrando repeticiones con las llaves '{}':

```python
>>> haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'

>>> mo2 = haRegex.search('Ha')
>>> mo2 == None
True
```

Greedy and Nongreedy Matching

Las expresiones de python son greedy por defecto

```python
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```

>**danger**

>#### ¡Atención!
>
>El símbolo '?' tiene dos usos en las expresiones regulares: declarar nongreedy matchings (patrones no codiciosos) o marcar un grupo opcional.




>**tip**
>
>### Ahora en vídeo
>
>{% youtube %}https://www.youtube.com/watch?v=m4cOCrageIU{% endyoutube %}


