Del capítulo [Files](https://books.trinket.io/pfe/07-files.html)

### Text files and lines

Un archivo de texto puede considerarse como una secuencia de líneas, al igual que una cadena de Python puede considerarse como una secuencia de caracteres. Por ejemplo, esta es una muestra de un archivo de texto que registra la actividad de correo de varias personas en un equipo de desarrollo de proyectos de código abierto:

```bash
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Date: Sat, 5 Jan 2008 09:12:18 -0500
To: source@collab.sakaiproject.org
From: stephen.marquard@uct.ac.za
Subject: [sakai] svn commit: r39772 - content/branches/
Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
...
```

Puedes acceder al archivo completo [aquí](http://www.py4e.com/code3/mbox.txt) y a la versión reducida del mismo [aquí](http://www.py4e.com/code3/mbox-short.txt).

Para dividir el archivo en líneas, hay un carácter especial que representa el "final de la línea" llamado el carácter de nueva línea. En Python, representamos el carácter de nueva línea como una barra invertida-n en constantes de cadena. A pesar de que se ve como dos personajes, en realidad es un solo personaje. Cuando miramos la variable al ingresar "stuff" en el intérprete, nos muestra el \n en la cadena, pero cuando usamos imprimir para mostrar la cadena, vemos la cadena dividida en dos líneas por el carácter de nueva línea.

```python
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
```

También puede ver que la longitud de la cadena X \ nY es de tres caracteres porque el carácter de nueva línea es un solo carácter.

### Leyendo archivos

Si bien el identificador de archivo no contiene los datos para el archivo, es bastante fácil construir un bucle for para leer y contar cada una de las líneas en un archivo:

<iframe src="https://trinket.io/embed/python3/0cc77ee420" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Buscando a través del archivo

<iframe src="https://trinket.io/embed/python3/84802a5029" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Ahora sin líneas en blanco:

<iframe src="https://trinket.io/embed/python3/150836eeba" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Buscamos líneas que contengan "@uct.ac.za":

<iframe src="https://trinket.io/embed/python3/f2b21e4b6d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Try and except

<iframe src="https://trinket.io/embed/python3/6623b77431" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Escribiendo en un archivo

Para escribir en un archivo necesitamos ponerle el modo 'w' (write):

```python
>>> fout = open('output.txt', 'w')
>>> print(fout)
<_io.TextIOWrapper name='output.txt' mode='w' encoding='cp1252'>
```

Si el archivo ya existe, abrirlo en modo de escritura borra los datos antiguos y comienza de nuevo, ¡así que ten cuidado! Si el archivo no existe, se crea uno nuevo.

Cuando termines de escribir debes cerrar el archivo con el comando close()

```python
>>> fout.close()
```

### ¿Cómo evitar abrir y cerrar archivos?

```python
with open('prueba.txt', 'w') as file:
     for i in range(10):
         file.write(str(i))

```
