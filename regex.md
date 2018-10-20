## Regex (regular expressions)

Información extraida de [_Automate the boring stuff_](https://automatetheboringstuff.com/chapter7/) de Al Sweigart.

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

| Shorthand character class | Represents |
|:---: |:---: |
|\d|Cualquier dígito numérico de 0 a 9.|
|\D|Cualquier caracter que NO sea un dígito numérico de 0 a 9.|
|\w|Cualquier letra, dígito numérico, o el guión bajo. (Piensa en este atajo como el caracter de palabra.)|
|\W|Cualquier caracter que NO sea una letra, dígito numérico, o el guión bajo. .|
|\s|Cualquier espacio, tabulador, o caracter de nueva línea. (Think of this as matching “space” characters.)|
|\S|Cualquier caracter que NO sea espacio, tabulador, o caracter de nueva línea.|




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
>>> heroRegex = re.compile (r'Batman|Tina Fey') # Crea un objeto regex
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

___

#### Utilizando atajos de caracter

```python
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6
geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

#### Compila tus propias clases de caracteres

```python
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

#### Inicio y final de cadena

```python
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello world!')
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> beginsWithHello.search('He said hello.') == None
True
```

```python
>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
<_sre.SRE_Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two.') == None
True
```

```python
>>> wholeStringIsNum = re.compile(r'^\d+$')
>>> wholeStringIsNum.search('1234567890')
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
>>> wholeStringIsNum.search('12345xyz67890') == None
True
>>> wholeStringIsNum.search('12 34567890') == None
True
```

#### The Wildcard Character

```python
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
```

#### Encontrando todo con el punto '.'

```python
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'
```

#### Encontrando nuevas líneas con el '.'

```python
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
'Serve the public trust.'

>>> newlineRegex = re.compile('.*', re.DOTALL)
>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'

```

### Hacerlas insensibles a mayúsculas y minúsculas

```python
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'

>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

>>> robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'
```

#### Sustituir cadenas con sum()

```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

```python
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
Eve knew Agent Bob was a double agent.')
A**** told C**** that E**** knew B**** was a double agent.'
```

#### Manejando expresiones complejas

```python
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```

#### Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

```python
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```

## Repaso

Este capítulo cubrió mucha notación, así que aquí hay una revisión rápida de lo que aprendiste:
* El '?' coincide con cero o uno del grupo anterior.
* El '*' coincide con cero o más del grupo anterior.
* El '+' coincide con uno o más del grupo anterior.
* La {n} coincide exactamente con n del grupo anterior.
* La {n,} coincide con n o más del grupo anterior.
* El {, m} coincide con 0 a m del grupo anterior.
* La {n, m} coincide con al menos n y como máximo m del grupo anterior.
* {n, m}? o *? o +? realiza un partido no 'codicioso' del grupo anterior (non greedy matching).
* '^spam' significa que la cadena debe comenzar con spam.
* 'spam$' significa que la cadena debe terminar con spam.
* Los '.' coincide con cualquier carácter, excepto los caracteres de nueva línea.
* \d, \w y \s coinciden con un dígito, palabra o carácter de espacio, respectivamente.
* \D, \W y \S coinciden con cualquier cosa excepto un dígito, palabra o espacio, respectivamente. 
* [abc] coincide con cualquier carácter entre los paréntesis (como a, b, o c).
* [^abc] coincide con cualquier carácter que no esté entre los paréntesis.

>**tip**
>
>### Ahora en vídeo
>
>{% youtube %}https://www.youtube.com/watch?v=m4cOCrageIU{% endyoutube %}


