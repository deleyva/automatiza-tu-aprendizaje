# Gestionando archivos

Original [aqui](https://automatetheboringstuff.com/chapter9/)

Gracias a Python podemos gestionar archivos de manera cómoda y rápida sin tener que aprender los comandos del sistema operativo (bash, cmd...). De esta manera, sin importar en el sistema operativo en el que te encuetres, podrás manejar tus ficheros eficientemente.

Utilizaremos las librerías 'os, syste, y shutil'.

## Ejemplos

Copiando un solo archivo:

```python
>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
   'C:\\delicious\\spam.txt'
>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
   'C:\\delicious\\eggs2.txt'
```

#### Copiando carpetas completas:

```python
>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'
```

#### Moviendo y renombrando:

```python
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'
```

#### Borrando

```python
os.rmdir()  # Borra una carpeta vacía
os.rm()
shutil.rmtree() # Borra carpeta y su contenido
```

#### Enviando a la papelera

```python
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```

### Moviéndonos por el directorio

```python
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
```

La función os.walk () devolverá tres valores en cada iteración a través del bucle: 
1. Una cadena del nombre de la carpeta actual
2. Una lista de cadenas de las carpetas en la carpeta actual
3. Una lista de cadenas de los archivos en la carpeta actual 

(Por carpeta actual , Me refiero a la carpeta para la iteración actual del bucle for. El directorio de trabajo actual del programa no es cambiado por os.walk ().)

## Comprimiendo archivos

```python
   >>> import zipfile, os
   >>> os.chdir('C:\\')    # move to the folder with example.zip
   >>> exampleZip = zipfile.ZipFile('example.zip')
   >>> exampleZip.namelist()
   ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
   >>> spamInfo = exampleZip.getinfo('spam.txt')
   >>> spamInfo.file_size
   13908
   >>> spamInfo.compress_size
   3828
  >>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
   .compress_size, 2))
   'Compressed file is 3.63x smaller!'
   >>> exampleZip.close()
```

## Extrayendo archivos

```python
   >>> import zipfile, os
   >>> os.chdir('C:\\')    # move to the folder with example.zip
   >>> exampleZip = zipfile.ZipFile('example.zip')
   >>> exampleZip.extractall()
   >>> exampleZip.close()
```

```python
>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
```

## Creando y añadiendo archivos a contenedores zip

```python
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
```

**info**

Para este ejercicio te vendrán bien los siguientes comandos:

```python
os.mkdir('carpeta')
os.getcwd() # Te devuelve la ruta en la que te encuentras
```

Pregunta [24](https://classroom.google.com/c/MTg0NjkwNjQzMjVa/sa/MjI4MDk2NDY2MzBa/details)

%accordion%Solución%accordion%

```python

```

%/accordion%
