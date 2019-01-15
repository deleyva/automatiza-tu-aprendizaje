
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

<li class = "has-dropdown"> [Usar bases de datos y SQL] (# using -atabases-bases-de-datos) <ul class = "dropdown">
- [¿Qué es una base de datos?] (# What-is-a-database)
- [Conceptos de base de datos] (# conceptos de base de datos)
- [Database Browser for SQLite] (# database-browser-for-sqlite)
- [Creando una tabla de base de datos] (# creating-a-database-table)
- [Resumen de lenguaje de consulta estructurado] (# estructurado de consulta-lenguaje-resumen)
- [Spidering Twitter usando una base de datos] (# spidering-twitter-using-a-database)
- [Modelado básico de datos] (# modelado básico de datos)
<li> [Programación con varias tablas] (# programación-con-tablas-múltiples) <ul>
- [Restricciones en tablas de base de datos] (# restricciones en tablas de base de datos)
- [Recuperar y / o insertar un registro] (# recuperar-andor-insertar-un-registro)
- [Almacenar la relación de amistad] (# relación de guardar el amigo)

# [Uso de bases de datos y SQL] (# using -atabases-and-sql)

## [¿Qué es una base de datos?] (# What-is-a-database)



Una ** base de datos ** es un archivo que está organizado para almacenar datos. La mayoría de las bases de datos están organizadas como un diccionario en el sentido de que se asignan de claves a valores. La mayor diferencia es que la base de datos está en el disco (u otro almacenamiento permanente), por lo que persiste después de que finalice el programa. Debido a que una base de datos se almacena en un almacenamiento permanente, puede almacenar muchos más datos que un diccionario, lo que se limita al tamaño de la memoria en la computadora.



Al igual que un diccionario, el software de base de datos está diseñado para mantener la inserción y el acceso de datos muy rápido, incluso para grandes cantidades de datos. El software de la base de datos mantiene su rendimiento mediante la creación de índices ** a medida que se agregan datos a la base de datos para permitir que la computadora salte rápidamente a una entrada en particular.

Hay muchos sistemas de bases de datos diferentes que se utilizan para una amplia variedad de propósitos, incluyendo: Oracle, MySQL, Microsoft SQL Server, PostgreSQL y SQLite. Nos centramos en SQLite en este libro porque es una base de datos muy común y ya está integrada en Python. SQLite está diseñado para ser ** integrado ** en otras aplicaciones para proporcionar soporte de base de datos dentro de la aplicación. Por ejemplo, el navegador Firefox también usa la base de datos SQLite internamente al igual que muchos otros productos.

[http://sqlite.org/](http://sqlite.org/)

SQLite se adapta bien a algunos de los problemas de manipulación de datos que vemos en Informática, como la aplicación de rastreo de Twitter que describimos en este capítulo.

## [Conceptos de base de datos] (# conceptos de base de datos)

Cuando miras por primera vez una base de datos, parece una hoja de cálculo con varias hojas. Las estructuras de datos principales en una base de datos son: ** tablas **, ** filas ** y ** columnas **.

Bases de datos relacionales

En las descripciones técnicas de las bases de datos relacionales, los conceptos de tabla, fila y columna se denominan más formalmente ** relación **, ** tupla ** y ** atributo **, respectivamente. Usaremos los términos menos formales en este capítulo.

## [Database Browser for SQLite] (# database-browser-for-sqlite)

Si bien este capítulo se centrará en el uso de Python para trabajar con datos en archivos de base de datos SQLite, muchas operaciones se pueden realizar de manera más conveniente utilizando el software denominado ** Database Browser for SQLite **, que está disponible gratuitamente en:

[http://sqlitebrowser.org/](http://sqlitebrowser.org/)

Con el navegador puede crear fácilmente tablas, insertar datos, editar datos o ejecutar consultas SQL simples en los datos de la base de datos.

En cierto sentido, el navegador de la base de datos es similar a un editor de texto cuando se trabaja con archivos de texto. Cuando desee realizar una o muy pocas operaciones en un archivo de texto, puede abrirlo en un editor de texto y realizar los cambios que desee. Cuando tienes muchos cambios que debes hacer en un archivo de texto, a menudo escribirás un programa Python simple. Encontrará el mismo patrón cuando trabaje con bases de datos. Hará operaciones simples en el administrador de bases de datos y las operaciones más complejas se realizarán de manera más conveniente en Python.

## [Creando una tabla de base de datos] (# creating-a-database-table)

Las bases de datos requieren una estructura más definida que las listas o los diccionarios de Python [<sup> 1 </sup>] (# fn1).

Cuando creamos una base de datos ** tabla ** debemos informar a la base de datos por adelantado los nombres de cada una de las ** columnas ** en la tabla y el tipo de datos que planeamos almacenar en cada ** columna **. Cuando el software de la base de datos conoce el tipo de datos en cada columna, puede elegir la forma más eficiente de almacenar y buscar los datos según el tipo de datos.

Puede ver los diversos tipos de datos admitidos por SQLite en la siguiente url:

[http://www.sqlite.org/datatypes.html](http://www.sqlite.org/datatypes.html)

Definir la estructura de sus datos por adelantado puede parecer inconveniente al principio, pero la recompensa es un acceso rápido a sus datos, incluso cuando la base de datos contiene una gran cantidad de datos.

El código para crear un archivo de base de datos y una tabla llamada `Tracks` con dos columnas en la base de datos es la siguiente:





La operación `connect` hace una" conexión "a la base de datos almacenada en el archivo` music.sqlite3` en el directorio actual. Si el archivo no existe, será creado. La razón por la que esto se denomina "conexión" es que a veces la base de datos se almacena en un "servidor de base de datos" independiente del servidor en el que ejecutamos nuestra aplicación. En nuestros ejemplos simples, la base de datos solo será un archivo local en el mismo directorio que el código Python que estamos ejecutando.

Un ** cursor ** es como un identificador de archivo que podemos usar para realizar operaciones en los datos almacenados en la base de datos. Llamar a `cursor ()` es muy similar conceptualmente a llamar a `open ()` cuando se trata de archivos de texto.

A Database Cursor

Una vez que tengamos el cursor, podemos comenzar a ejecutar comandos en el contenido de la base de datos usando el método `execute ()`.

Los comandos de la base de datos se expresan en un lenguaje especial que se ha estandarizado en muchos proveedores de bases de datos diferentes para permitirnos aprender un solo idioma de base de datos. El lenguaje de la base de datos se llama ** Lenguaje de consulta estructurado ** o ** SQL ** para abreviar.

[http://en.wikipedia.org/wiki/SQL](http://en.wikipedia.org/wiki/SQL)

En nuestro ejemplo, estamos ejecutando dos comandos SQL en nuestra base de datos. Como convención, mostraremos las palabras clave de SQL en mayúsculas y las partes del comando que estamos agregando (como los nombres de tablas y columnas) se mostrarán en minúsculas.

El primer comando SQL elimina la tabla `Tracks` de la base de datos si existe. Este patrón es simplemente para permitirnos ejecutar el mismo programa para crear la tabla `Tracks` una y otra vez sin causar un error. Tenga en cuenta que el comando `DROP TABLE` elimina la tabla y todo su contenido de la base de datos (es decir, no hay" deshacer ").

```cur.execute('DROP TABLE IF EXISTS Tracks ')
```
El segundo comando crea una tabla llamada `Tracks` con una columna de texto llamada` title` y una columna entera llamada `plays`.

```cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
```
Ahora que hemos creado una tabla llamada `Tracks`, podemos poner algunos datos en esa tabla usando la operación SQL` INSERT`. Nuevamente, comenzamos haciendo una conexión a la base de datos y obteniendo el `cursor`. Luego podemos ejecutar comandos SQL usando el cursor.

El comando SQL `INSERT` indica qué tabla estamos usando y luego define una nueva fila al enumerar los campos que queremos incluir` (título, jugadas) `seguido de los` VALORES` que queremos colocar en la nueva fila. Especificamos los valores como signos de interrogación `(?,?)` Para indicar que los valores reales se pasan como una tupla `('My Way', 15)` como el segundo parámetro a la llamada `execute ()`.

Primero, insertamos dos filas en nuestra tabla y usamos `commit ()` para forzar que los datos se escriban en el archivo de la base de datos.

Filas en una tabla

Luego usamos el comando `SELECT` para recuperar las filas que acabamos de insertar de la tabla. En el comando `SELECT`, indicamos en qué columnas nos gustaría` (título, jugamos) `e indicamos de qué tabla queremos recuperar los datos. Después de ejecutar la instrucción `SELECT`, el cursor es algo que podemos recorrer en una instrucción` for`. Por eficiencia, el cursor no lee todos los datos de la base de datos cuando ejecutamos la instrucción `SELECT`. En su lugar, los datos se leen a pedido a medida que recorramos las filas en la declaración `for`.

La salida del programa es la siguiente:

```Tracks:
('Thunderstruck', 20)
('My Way', 15)
```


Nuestro bucle `for` encuentra dos filas, y cada fila es una tupla de Python con el primer valor como` title` y el segundo valor como el número de `plays`.

** Nota: Puede ver cadenas que comienzan con `u'` en otros libros o en Internet. Esto era una indicación en Python 2 de que las cadenas son ** Unicode * cadenas que son capaces de almacenar conjuntos de caracteres no latinos. En Python 3, todas las cadenas son cadenas Unicode por defecto. *

Al final del programa, ejecutamos un comando SQL para 'BORRAR' las filas que acabamos de crear para que podamos ejecutar el programa una y otra vez. El comando `DELETE` muestra el uso de una cláusula` WHERE` que nos permite expresar un criterio de selección para que podamos pedir a la base de datos que aplique el comando solo a las filas que coincidan con el criterio. En este ejemplo, el criterio pasa a aplicarse a todas las filas, de modo que vaciamos la tabla para poder ejecutar el programa repetidamente. Después de que se realiza el `BORRAR`, también llamamos a` commit () `para forzar que los datos se eliminen de la base de datos.

## [Resumen de lenguaje de consulta estructurado] (# estructurado de consulta-lenguaje-resumen)

Hasta ahora, hemos estado utilizando el lenguaje de consulta estructurado en nuestros ejemplos de Python y hemos cubierto muchos de los conceptos básicos de los comandos SQL. En esta sección, analizamos el lenguaje SQL en particular y ofrecemos una descripción general de la sintaxis de SQL.

Dado que hay tantos proveedores de bases de datos diferentes, el lenguaje de consulta estructurado (SQL) se estandarizó para que pudiéramos comunicarnos de manera portátil a los sistemas de bases de datos de varios proveedores.

Una base de datos relacional está formada por tablas, filas y columnas. Las columnas generalmente tienen un tipo como datos de texto, numéricos o de fecha. Cuando creamos una tabla, indicamos los nombres y tipos de las columnas:

```CREATE TABLE Tracks (title TEXT, plays INTEGER)
```
Para insertar una fila en una tabla, usamos el comando SQL `INSERT`:

```INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)
```
La declaración `INSERT` especifica el nombre de la tabla, luego una lista de los campos / columnas que le gustaría establecer en la nueva fila, y luego la palabra clave` VALUES` y una lista de valores correspondientes para cada uno de los campos.

El comando SQL 'SELECT` se usa para recuperar filas y columnas de una base de datos. La declaración `SELECT` le permite especificar qué columnas desea recuperar, así como una cláusula WHERE` para seleccionar qué filas desea ver. También permite una cláusula opcional `ORDER BY` para controlar la clasificación de las filas devueltas.

```SELECT * FROM Tracks WHERE title = 'My Way'
```
Usar `*` indica que desea que la base de datos devuelva todas las columnas para cada fila que coincida con la cláusula `WHERE`.

Tenga en cuenta que, a diferencia de Python, en una cláusula SQL `WHERE` usamos un único signo igual para indicar una prueba de igualdad en lugar de un doble signo igual. Otras operaciones lógicas permitidas en una cláusula `WHERE` incluyen` & lt; `,` & gt; `,` & lt; = `,` & gt; = `,`! = `, Así como` AND` y `OR` y paréntesis para construir tus expresiones lógicas.

Puede solicitar que las filas devueltas se ordenen por uno de los campos de la siguiente manera:

```SELECT title,plays FROM Tracks ORDER BY title
```
Para eliminar una fila, necesita una cláusula `WHERE` en una sentencia SQL` DELETE`. La cláusula `WHERE` determina qué filas se van a eliminar:

```DELETE FROM Tracks WHERE title = 'My Way'
```
Es posible `ACTUALIZAR` una columna o columnas dentro de una o más filas en una tabla usando la declaración SQL` ACTUALIZACIÓN` de la siguiente manera:

```UPDATE Tracks SET plays = 16 WHERE title = 'My Way'
```
La declaración `UPDATE` especifica una tabla y luego una lista de campos y valores para cambiar después de la palabra clave` SET` y luego una cláusula opcional `WHERE` para seleccionar las filas que se actualizarán. Una sola instrucción `UPDATE` cambiará todas las filas que coincidan con la cláusula` WHERE`. Si no se especifica una cláusula `WHERE`, realiza el` UPDATE` en todas las filas de la tabla.

Estos cuatro comandos SQL básicos (INSERTAR, SELECCIONAR, ACTUALIZAR y BORRAR) permiten las cuatro operaciones básicas necesarias para crear y mantener datos.

## [Spidering Twitter usando una base de datos] (# spidering-twitter-using-a-database)

En esta sección, crearemos un programa de spidering simple que pasará por las cuentas de Twitter y creará una base de datos de ellas. ** Nota: Tenga mucho cuidado al ejecutar este programa. No desea extraer demasiados datos o ejecutar el programa durante demasiado tiempo y terminar con el cierre de su acceso a Twitter. **

Uno de los problemas de cualquier tipo de programa spidering es que debe poder detenerse y reiniciarse muchas veces y no quiere perder los datos que ha recuperado hasta ahora. No siempre desea reiniciar su recuperación de datos desde el principio, por lo que queremos almacenar datos a medida que los recuperamos para que nuestro programa pueda iniciarse nuevamente y continuar donde lo dejó.

Comenzaremos por recuperar los amigos de Twitter de una persona y sus estados, recorreremos la lista de amigos y agregaremos a cada uno de los amigos a una base de datos para recuperarlos en el futuro. Después de procesar los amigos de Twitter de una persona, revisamos nuestra base de datos y recuperamos a uno de los amigos del amigo. Hacemos esto una y otra vez, seleccionando a una persona "no visitada", recuperando su lista de amigos y agregando amigos que no hemos visto en nuestra lista para una futura visita.

También hacemos un seguimiento de cuántas veces hemos visto a un amigo en particular en la base de datos para tener una idea de su "popularidad".

Al almacenar nuestra lista de cuentas conocidas y si hemos recuperado la cuenta o no, y cuán popular es la cuenta en una base de datos en el disco de la computadora, podemos detener y reiniciar nuestro programa tantas veces como lo deseemos.

Este programa es un poco complejo. Se basa en el código del ejercicio anterior en el libro que utiliza la API de Twitter.

Aquí está el código fuente de nuestra aplicación de spidering de Twitter:

Nuestra base de datos se almacena en el archivo `spider.sqlite3` y tiene una tabla llamada` Twitter`. Cada fila en la tabla `Twitter` tiene una columna para el nombre de la cuenta, si hemos recuperado los amigos de esta cuenta y cuántas veces esta cuenta ha sido" amigable ".

En el ciclo principal del programa, le pedimos al usuario un nombre de cuenta de Twitter o "salir" para salir del programa. Si el usuario ingresa a una cuenta de Twitter, recuperamos la lista de amigos y estados de ese usuario y agregamos a cada amigo a la base de datos si aún no está en la base de datos. Si el amigo ya está en la lista, agregamos 1 al campo `friends` en la fila de la base de datos.

Si el usuario presiona Intro, buscamos en la base de datos la próxima cuenta de Twitter que aún no hemos recuperado, recuperamos los amigos y los estados de esa cuenta, los agregamos a la base de datos o los actualizamos, y aumentamos el recuento de sus "amigos".

Una vez que recuperamos la lista de amigos y estados, recorramos todos los elementos `user` en el JSON devuelto y recuperamos el` screen_name` para cada usuario. Luego usamos la declaración `SELECT` para ver si ya hemos almacenado este` screen_name` en particular en la base de datos y recuperar el recuento de amigos (`friends`) si el registro existe.

```countnew = 0
countold = 0
for u in js['users'] :
    friend = u['screen_name']
    print friend
    cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
        (friend, ) )
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
            (count+1, friend) )
        countold = countold + 1
    except:
        cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
            VALUES ( ?, 0, 1 )''', ( friend, ) )
        countnew = countnew + 1
print 'New accounts=',countnew,' revisited=',countold
conn.commit()
```
Una vez que el cursor ejecuta la instrucción `SELECT`, debemos recuperar las filas. Podríamos hacer esto con una declaración `for`, pero como solo estamos recuperando una fila (` LIMIT 1`), podemos usar el método `fetchone ()` para recuperar la primera (y única) fila que es el resultado de La operación `SELECT`. Como `fetchone ()` devuelve la fila como ** tupla ** (aunque solo hay un campo), tomamos el primer valor de la tupla usando para obtener el recuento actual de amigos en la variable `recuento '.

Si esta recuperación es exitosa, usamos la declaración SQL `UPDATE` con una cláusula` WHERE` para agregar 1 a la columna `friends` para la fila que coincide con la cuenta del amigo. Observe que hay dos marcadores de posición (es decir, signos de interrogación) en el SQL, y el segundo parámetro de `execute ()` es una tupla de dos elementos que contiene los valores que se sustituirán en el SQL en lugar de los signos de interrogación.

Si el código en el bloque `try` falla, es probable que no haya ningún registro que coincida con la cláusula WHERE name =? En la instrucción SELECT. Entonces, en el bloque `except`, usamos la declaración SQL` INSERT` para agregar el `screen_name` del amigo a la tabla con una indicación de que aún no hemos recuperado el` screen_name` y establecer el recuento de amigos en cero.

Entonces, la primera vez que se ejecuta el programa y entramos en una cuenta de Twitter, el programa se ejecuta de la siguiente manera:

```Enter a Twitter account, or quit: drchuck
Retrieving http://api.twitter.com/1.1/friends ...
New accounts= 20  revisited= 0
Enter a Twitter account, or quit: quit
```
Como esta es la primera vez que ejecutamos el programa, la base de datos está vacía y creamos la base de datos en el archivo `spider.sqlite3` y agregamos una tabla llamada` Twitter` a la base de datos. Luego recuperamos algunos amigos y los agregamos a la base de datos ya que la base de datos está vacía.

En este punto, podríamos querer escribir un dumper de base de datos simple para echar un vistazo a lo que está en nuestro archivo `spider.sqlite3`:

Este programa simplemente abre la base de datos y selecciona todas las columnas de todas las filas en la tabla `Twitter`, luego recorre las filas e imprime cada fila.

Si ejecutamos este programa después de la primera ejecución de nuestra araña de Twitter anterior, su salida será la siguiente:

```('opencontent', 0, 1)
('lhawthorn', 0, 1)
('steve_coppin', 0, 1)
('davidkocher', 0, 1)
('hrheingold', 0, 1)
...
20 rows.
```
Vemos una fila para cada `nombre_de_la pantalla`, que no hemos recuperado los datos para ese` nombre_de_la pantalla`, y todos en la base de datos tienen un amigo.

Ahora nuestra base de datos refleja la recuperación de los amigos de nuestra primera cuenta de Twitter (** drchuck **). Podemos ejecutar el programa nuevamente y decirle que recupere a los amigos de la próxima cuenta "sin procesar" simplemente presionando Intro en lugar de una cuenta de Twitter de la siguiente manera:

```Enter a Twitter account, or quit:
Retrieving http://api.twitter.com/1.1/friends ...
New accounts= 18  revisited= 2
Enter a Twitter account, or quit:
Retrieving http://api.twitter.com/1.1/friends ...
New accounts= 17  revisited= 3
Enter a Twitter account, or quit: quit
```
Desde que presionamos enter (es decir, no especificamos una cuenta de Twitter), se ejecuta el siguiente código:

```if ( len(acct) &lt; 1 ) :
    cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
    try:
        acct = cur.fetchone()[0]
    except:
        print 'No unretrieved twitter accounts found'
        continue
```
Usamos la instrucción SQL 'SELECT` para recuperar el nombre del primer usuario (`LIMIT 1`) que todavía tiene su valor de" hemos recuperado este usuario "establecido en cero. También utilizamos el patrón `fetchone () [0]` dentro de un bloque try / except para extraer un `screen_name` de los datos recuperados o para mostrar un mensaje de error y realizar un bucle de copia de seguridad.

Si recuperamos con éxito un `screen_name` sin procesar, recuperamos sus datos de la siguiente manera:

~ <sub> ~ </sub> {.python {url = twurl.augment (TWITTER_URL, {'screen_name': acct, 'count': '20'}) imprime 'Retrieving', url connection = urllib.urlopen (url ) data = connection.read () js = json.loads (data)

cur.execute ('UPDATE Twitter SET recuperado = 1 DÓNDE nombre =?', (acct,)) ~ <sub> ~ </sub>

Una vez que recuperamos los datos con éxito, usamos la instrucción `ACTUALIZAR` para establecer la columna `recuperado` en 1 para indicar que hemos completado la recuperación de los amigos de esta cuenta. Esto nos impide recuperar los mismos datos una y otra vez y nos mantiene progresando a través de la red de amigos de Twitter.

Si ejecutamos el programa de amigos y presionamos Intro dos veces para recuperar a los amigos de los siguientes amigos no visitados, luego ejecutamos el programa de descarga, nos dará el siguiente resultado:

```('opencontent', 1, 1)
('lhawthorn', 1, 1)
('steve_coppin', 0, 1)
('davidkocher', 0, 1)
('hrheingold', 0, 1)
...
('cnxorg', 0, 2)
('knoop', 0, 1)
('kthanos', 0, 2)
('LectureTools', 0, 1)
...
55 rows.
```
Podemos ver que hemos registrado correctamente que hemos visitado `lhawthorn` y` opencontent`. También las cuentas `cnxorg` y` kthanos` ya tienen dos seguidores. Como ahora hemos recuperado los amigos de tres personas (`drchuck`,` opencontent` y `lhawthorn`), nuestra tabla tiene 55 filas de amigos para recuperar.

Cada vez que ejecutamos el programa y presionamos enter, elegimos la siguiente cuenta no visitada (por ejemplo, la siguiente cuenta será `steve_coppin`), recuperará a sus amigos, los marcará como recuperados y, para cada uno de los amigos de` steve_coppin`, agregue hasta el final de la base de datos o actualice el recuento de sus amigos si ya están en la base de datos.

Dado que todos los datos del programa se almacenan en el disco en una base de datos, la actividad de rastreo se puede suspender y reanudar tantas veces como desee sin perder datos.

## [Modelado básico de datos] (# modelado básico de datos)

El poder real de una base de datos relacional es cuando creamos varias tablas y hacemos enlaces entre esas tablas. El acto de decidir cómo dividir los datos de su aplicación en varias tablas y establecer las relaciones entre las tablas se denomina ** modelado de datos **. El documento de diseño que muestra las tablas y sus relaciones se denomina ** modelo de datos **.

El modelado de datos es una habilidad relativamente sofisticada y solo presentaremos los conceptos más básicos del modelado de datos relacionales en esta sección. Para más detalles sobre el modelado de datos, puede comenzar con:

[http://en.wikipedia.org/wiki/Relational_model](http://en.wikipedia.org/wiki/Relational_model)

Digamos que para nuestra aplicación de araña de Twitter, en lugar de simplemente contar los amigos de una persona, queríamos mantener una lista de todas las relaciones entrantes para poder encontrar una lista de todas las personas que siguen una cuenta en particular.

Dado que potencialmente todos tendrán muchas cuentas que los siguen, no podemos simplemente agregar una sola columna a nuestra tabla `Twitter`. Así que creamos una nueva tabla que hace un seguimiento de parejas de amigos. La siguiente es una forma simple de hacer una tabla de este tipo:

```CREATE TABLE Pals (from_friend TEXT, to_friend TEXT)
```
Cada vez que nos encontramos con una persona que está siguiendo `drchuck`, insertamos una fila del formulario:

```INSERT INTO Pals (from_friend,to_friend) VALUES ('drchuck', 'lhawthorn')
```
Como estamos procesando a los 20 amigos del feed de Twitter `drchuck`, insertaremos 20 registros con" drchuck "como primer parámetro, por lo que terminaremos duplicando la cadena muchas veces en la base de datos.

Esta duplicación de datos de cadena viola una de las mejores prácticas para ** la normalización de la base de datos ** que básicamente dice que nunca debemos colocar los mismos datos de cadena en la base de datos más de una vez. Si necesitamos los datos más de una vez, creamos una clave numérica ** para los datos y hacemos referencia a los datos reales utilizando esta clave.

En términos prácticos, una cadena ocupa mucho más espacio que un entero en el disco y en la memoria de nuestra computadora, y toma más tiempo de procesador para comparar y ordenar. Si solo tenemos unos pocos cientos de entradas, el tiempo de almacenamiento y procesador apenas importa. Pero si tenemos un millón de personas en nuestra base de datos y una posibilidad de 100 millones de enlaces de amigos, es importante poder escanear los datos lo más rápido posible.

Almacenaremos nuestras cuentas de Twitter en una tabla llamada `People` en lugar de la tabla` Twitter` utilizada en el ejemplo anterior. La tabla `People` tiene una columna adicional para almacenar la clave numérica asociada a la fila para este usuario de Twitter. SQLite tiene una función que agrega automáticamente el valor clave para cualquier fila que insertamos en una tabla usando un tipo especial de columna de datos (`INTEGER PRIMARY KEY`).

Podemos crear la tabla `People` con esta columna adicional` id` de la siguiente manera:

```CREATE TABLE People
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)
```
Tenga en cuenta que ya no estamos manteniendo un recuento de amigos en cada fila de la tabla "Personas". Cuando seleccionamos `INTEGER PRIMARY KEY` como el tipo de nuestra columna` id`, estamos indicando que nos gustaría que SQLite administre esta columna y asigne una clave numérica única a cada fila que insertamos automáticamente. También agregamos la palabra clave `UNIQUE` para indicar que no permitiremos que SQLite inserte dos filas con el mismo valor para` name`.

Ahora, en lugar de crear la tabla `Pals` anterior, creamos una tabla llamada` Follows` con dos columnas enteras `from_id` y` to_id` y una restricción en la tabla que la combinación ** ** de `from_id` y` to_id `debe ser único en esta tabla (es decir, no podemos insertar filas duplicadas) en nuestra base de datos.

```CREATE TABLE Follows
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id) )
```
Cuando agregamos cláusulas `UNIQUE` a nuestras tablas, estamos comunicando un conjunto de reglas que le estamos pidiendo a la base de datos que aplique cuando intentemos insertar registros. Estamos creando estas reglas como una conveniencia en nuestros programas, como veremos en un momento. Las reglas nos impiden cometer errores y simplifican la escritura de algunos de nuestros códigos.

En esencia, al crear esta tabla "Siguiendo", estamos modelando una "relación" donde una persona "sigue" a otra persona y la representamos con un par de números que indican que (a) las personas están conectadas y (b) la dirección de la relación.

Relaciones entre tablas

## [Programación con varias tablas] (# programación-con-tablas-múltiples)

Ahora rehaceremos el programa de arañas de Twitter utilizando dos tablas, las claves principales y las referencias clave, como se describe anteriormente. Aquí está el código para la nueva versión del programa:

Este programa está empezando a complicarse un poco, pero ilustra los patrones que debemos usar cuando estamos usando claves de enteros para vincular tablas. Los patrones básicos son:

1. Crear tablas con claves primarias y restricciones.
1. Cuando tenemos una clave lógica para una persona (es decir, el nombre de la cuenta) y necesitamos el valor `id` para la persona, dependiendo de si la persona ya está en la tabla` Personas 'o bien debemos: ( 1) busque la persona en la tabla `People` y recupere el valor` id` para la persona o (2) agregue a la persona a la tabla `People` y obtenga el valor` id` para la fila recién agregada.
1. Inserte la fila que captura la relación "sigue".

Vamos a cubrir cada uno de estos a su vez.

### [Restricciones en tablas de bases de datos] (# restricciones-en-tablas-de-bases de datos)

A medida que diseñamos nuestras estructuras de tablas, podemos decirle al sistema de base de datos que nos gustaría aplicar algunas reglas. Estas reglas nos ayudan a cometer errores e introducir datos incorrectos en las tablas. Cuando creamos nuestras tablas:

```cur.execute('''CREATE TABLE IF NOT EXISTS People
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')
```
Indicamos que la columna `name` en la tabla` People` debe ser `UNIQUE`. También indicamos que la combinación de los dos números en cada fila de la tabla 'Siguiendo' debe ser única. Estas restricciones nos impiden cometer errores, como agregar la misma relación más de una vez.

Podemos aprovechar estas restricciones en el siguiente código:

```cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
    VALUES ( ?, 0)''', ( friend, ) )
```
Añadimos la cláusula `OR IGNORE` a nuestra declaración` INSERT` para indicar que si este `INSERT` en particular causaría una violación de la regla" `name` debe ser único", el sistema de la base de datos puede ignorar el `INSERT` . Estamos utilizando la restricción de la base de datos como una red de seguridad para asegurarnos de no hacer algo incorrecto sin querer.

De manera similar, el siguiente código asegura que no agregamos la misma relación exacta de 'Sigue' dos veces.

```cur.execute('''INSERT OR IGNORE INTO Follows
    (from_id, to_id) VALUES (?, ?)''', (id, friend_id) )
```
Una vez más, simplemente le pedimos a la base de datos que ignore nuestro intento de "INSERTAR" si viola la restricción de unicidad que especificamos para las filas de "Siguientes".

### [Recuperar y / o insertar un registro] (# recuperar-andor-insertar-un-registro)

Cuando solicitamos al usuario una cuenta de Twitter, si la cuenta existe, debemos buscar su valor 'id'. Si la cuenta aún no existe en la tabla `People`, debemos insertar el registro y obtener el valor` id` de la fila insertada.

Este es un patrón muy común y se realiza dos veces en el programa anterior. Este código muestra cómo buscamos el `id` para la cuenta de un amigo cuando hemos extraído un` screen_name` de un nodo `usuario` en el JSON de Twitter recuperado.

Dado que con el tiempo será cada vez más probable que la cuenta ya esté en la base de datos, primero verificamos si existe el registro 'Personas' usando una declaración 'SELECCIONAR'.

Si todo va bien [<sup> 2 </sup>] (# fn2) dentro de la sección `try`, recuperamos el registro usando` fetchone () `y luego recuperamos el primer (y único) elemento de la tupla devuelta y guárdalo en `friend_id`.

Si el `SELECT` falla, el código` fetchone () [0] `fallará y el control se transferirá a la sección` except`.

```    friend = u['screen_name']
    cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
        (friend, ) )
    try:
        friend_id = cur.fetchone()[0]
        countold = countold + 1
    except:
        cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
            VALUES ( ?, 0)''', ( friend, ) )
        conn.commit()
        if cur.rowcount != 1 :
            print 'Error inserting account:',friend
            continue
        friend_id = cur.lastrowid
        countnew = countnew + 1
```
Si terminamos en el código `except`, simplemente significa que no se encontró la fila, por lo que debemos insertar la fila. Usamos `INSERT OR IGNORE` solo para evitar errores y luego llamamos a` commit () `para forzar que la base de datos se actualice realmente. Una vez que se realiza la escritura, podemos verificar el `cur.rowcount` para ver cuántas filas se vieron afectadas. Ya que estamos intentando insertar una sola fila, si el número de filas afectadas es diferente a 1, es un error.

Si el `INSERT` tiene éxito, podemos ver` cur.lastrowid` para averiguar qué valor asignó la base de datos a la columna `id` en nuestra fila recién creada.

### [Guardando la relación de amistad] (# almacenando la relación de amistad)

Una vez que sepamos el valor clave tanto para el usuario de Twitter como para el amigo en el JSON, es muy sencillo insertar los dos números en la tabla `Siguiendo 'con el siguiente código:

```cur.execute('INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)',
    (id, friend_id) )
```
Tenga en cuenta que dejamos que la base de datos se encargue de evitar que "insertemos dos veces" una relación creando la tabla con una restricción de unicidad y luego agregando `OR IGNORE` a nuestra declaración` INSERT`.

Aquí hay una ejecución de muestra de este programa:

```Enter a Twitter account, or quit:
No unretrieved Twitter accounts found
Enter a Twitter account, or quit: drchuck
Retrieving http://api.twitter.com/1.1/friends ...
New accounts= 20  revisited= 0
Enter a Twitter account, or quit:
Retrieving http://api.twitter.com/1.1/friends ...
New accounts= 17  revisited= 3
Enter a Twitter account, or quit:
Retrieving http://api.twitter.com/1.1/friends ...
New accounts= 17  revisited= 3
Enter a Twitter account, or quit: quit
```
Comenzamos con la cuenta `drchuck` y luego dejamos que el programa seleccione automáticamente las siguientes dos cuentas para recuperar y agregar a nuestra base de datos.

A continuación se muestran las primeras filas de las tablas `People` y` Follows` después de completar esta ejecución:

```People:
(1, 'drchuck', 1)
(2, 'opencontent', 1)
(3, 'lhawthorn', 1)
(4, 'steve_coppin', 0)
(5, 'davidkocher', 0)
55 rows.
Follows:
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(1, 6)
60 rows.
```
Puede ver los campos `id`,` name` y `visited` en la tabla` People` y puede ver los números de ambos extremos de la relación en la tabla `Follows`. En la tabla "Personas", podemos ver que las tres primeras personas han sido visitadas y sus datos han sido recuperados. Los datos en la tabla `Follows` indican que` drchuck` (usuario 1) es un amigo para todas las personas que aparecen en las primeras cinco filas. Esto tiene sentido porque los primeros datos que recuperamos y almacenamos fueron los amigos de Twitter de `drchuck`. Si tuviera que imprimir más filas de la tabla `Follows`, también vería a los amigos de los usuarios 2 y 3.

## [Tres tipos de teclas] (# tres tipos de teclas)

Ahora que hemos empezado a construir un modelo de datos que coloca nuestros datos en varias tablas vinculadas y vincula las filas en esas tablas usando ** claves **, debemos analizar la terminología relacionada con las claves. En general, hay tres tipos de claves utilizadas en un modelo de base de datos.

- Una ** llave lógica ** es una clave que el "mundo real" puede usar para buscar una fila. En nuestro modelo de datos de ejemplo, el campo `nombre` es una clave lógica. Es el nombre de pantalla para el usuario y, de hecho, buscamos la fila de un usuario varias veces en el programa usando el campo `nombre`. A menudo encontrará que tiene sentido agregar una restricción 'ÚNICA' a una clave lógica. Dado que la clave lógica es la forma en que buscamos una fila del mundo exterior, no tiene mucho sentido permitir varias filas con el mismo valor en la tabla.
- Una ** clave principal ** suele ser un número que la base de datos asigna automáticamente. Por lo general, no tiene ningún significado fuera del programa y solo se utiliza para vincular filas de diferentes tablas. Cuando queremos buscar una fila en una tabla, generalmente buscar la fila con la clave principal es la forma más rápida de encontrar la fila. Dado que las claves primarias son números enteros, ocupan muy poco espacio de almacenamiento y se pueden comparar o clasificar muy rápidamente. En nuestro modelo de datos, el campo `id` es un ejemplo de una clave primaria.
- Una ** clave externa ** es generalmente un número que apunta a la clave principal de una fila asociada en una tabla diferente. Un ejemplo de una clave externa en nuestro modelo de datos es el `from_id`.

Una ** clave principal ** suele ser un número que la base de datos asigna automáticamente. Por lo general, no tiene ningún significado fuera del programa y solo se utiliza para vincular filas de diferentes tablas. Cuando queremos buscar una fila en una tabla, generalmente buscar la fila con la clave principal es la forma más rápida de encontrar la fila. Dado que las claves primarias son números enteros, ocupan muy poco espacio de almacenamiento y se pueden comparar o clasificar muy rápidamente. En nuestro modelo de datos, el campo `id` es un ejemplo de una clave primaria.

Estamos utilizando una convención de nomenclatura para llamar siempre el nombre de campo de la clave principal `id` y añadir el sufijo` _id` a cualquier nombre de campo que sea una clave externa.

## [Uso de JOIN para recuperar datos] (# using-join-to-retrieve-data)

Ahora que hemos seguido las reglas de normalización de la base de datos y hemos separado los datos en dos tablas, vinculadas entre sí mediante claves primarias y externas, debemos poder construir un 'SELECCIONAR' que vuelva a ensamblar los datos en todas las tablas.

SQL usa la cláusula `JOIN` para volver a conectar estas tablas. En la cláusula `JOIN` usted especifica los campos que se utilizan para volver a conectar las filas entre las tablas.

El siguiente es un ejemplo de un `SELECT` con una cláusula` JOIN`:

```SELECT * FROM Follows JOIN People
    ON Follows.from_id = People.id WHERE People.id = 1
```
La cláusula `JOIN` indica que los campos que estamos seleccionando cruzan las tablas` Follows` y `People`. La cláusula `ON` indica cómo se deben unir las dos tablas: tome las filas de` Follows` y agregue la fila de `People` donde el campo` from_id` en `Follows` es el mismo que el valor de` id` en el Tabla de personas.

Conectando tablas utilizando JOIN

El resultado de JOIN es crear "metarows" extra largos que tienen los campos de "Personas" y los campos correspondientes de los "Follows". Donde hay más de una coincidencia entre el campo `id` de` People` y el `from_id` de` People`, entonces JOIN crea un metarow para ** cada ** de los pares de filas correspondientes, duplicando los datos según sea necesario.

El siguiente código muestra los datos que tendremos en la base de datos después de que se haya ejecutado varias veces el programa de arañas de Twitter de múltiples tablas (arriba).

En este programa, primero desechamos 'People` y `Follows` y luego volcamos un subconjunto de los datos en las tablas unidas.

Aquí está la salida del programa:

```python twjoin.py
People:
(1, 'drchuck', 1)
(2, 'opencontent', 1)
(3, 'lhawthorn', 1)
(4, 'steve_coppin', 0)
(5, 'davidkocher', 0)
55 rows.
Follows:
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(1, 6)
60 rows.
Connections for id=2:
(2, 1, 1, 'drchuck', 1)
(2, 28, 28, 'cnxorg', 0)
(2, 30, 30, 'kthanos', 0)
(2, 102, 102, 'SomethingGirl', 0)
(2, 103, 103, 'ja_Pac', 0)
20 rows.
```
Verá las columnas de las tablas `People` y` Follows` y el último conjunto de filas es el resultado de `SELECT` con la cláusula` JOIN`.

En la última selección, estamos buscando cuentas que sean amigos de "opencontent" (es decir, `People.id = 2`).

En cada uno de los "metarows" en la última selección, las dos primeras columnas son de la tabla "Follows" seguidas por las columnas tres a cinco de la tabla "People". También puede ver que la segunda columna (`Follows.to_id`) coincide con la tercera columna (` People.id`) en cada uno de los "metarows" unidos.

## [Resumen] (# resumen)

Este capítulo ha cubierto mucho terreno para ofrecerle una descripción general de los conceptos básicos del uso de una base de datos en Python. Es más complicado escribir el código para usar una base de datos para almacenar datos que los diccionarios de Python o los archivos planos, por lo que hay pocas razones para usar una base de datos a menos que su aplicación realmente necesite las capacidades de una base de datos. Las situaciones en las que una base de datos puede ser bastante útil son: (1) cuando su aplicación necesita realizar muchas actualizaciones aleatorias dentro de un conjunto de datos grande, (2) cuando sus datos son tan grandes que no caben en un diccionario y necesita buscar actualice la información repetidamente, o (3) cuando tenga un proceso de larga ejecución que desee poder detener, reiniciar y conservar los datos de una ejecución a la siguiente.

Puede crear una base de datos simple con una sola tabla para satisfacer las necesidades de muchas aplicaciones, pero la mayoría de los problemas requerirán varias tablas y vínculos / relaciones entre filas en diferentes tablas. Cuando comienza a crear enlaces entre tablas, es importante hacer un diseño cuidadoso y seguir las reglas de normalización de la base de datos para aprovechar al máximo las capacidades de la base de datos. Dado que la motivación principal para usar una base de datos es que tiene una gran cantidad de datos con los que tratar, es importante modelar sus datos de manera eficiente para que sus programas se ejecuten lo más rápido posible.

## [depuración] (# depuración)

Un patrón común cuando desarrolle un programa Python para conectarse a una base de datos SQLite será ejecutar un programa Python y verificar los resultados utilizando el Explorador de bases de datos para SQLite. El navegador le permite verificar rápidamente si su programa está funcionando correctamente.

Debe tener cuidado porque SQLite se encarga de evitar que dos programas cambien los mismos datos al mismo tiempo. Por ejemplo, si abre una base de datos en el navegador y realiza un cambio en la base de datos y aún no ha presionado el botón "guardar" en el navegador, el navegador "bloquea" el archivo de la base de datos y evita que cualquier otro programa acceda al archivo. En particular, su programa Python no podrá acceder al archivo si está bloqueado.

Por lo tanto, una solución es asegurarse de cerrar el navegador de la base de datos o usar el menú ** Archivo ** para cerrar la base de datos en el navegador antes de intentar acceder a la base de datos desde Python para evitar el problema de su código Python debido a que la base de datos no funciona. está bloqueado.

## [Glosario] (# glosario)























---


1. SQLite realmente permite cierta flexibilidad en el tipo de datos almacenados en una columna, pero mantendremos nuestros tipos de datos estrictos en este capítulo para que los conceptos se apliquen por igual a otros sistemas de bases de datos como MySQL. [↩] (# fnref1)
1. En general, cuando una oración comienza con "si todo va bien", encontrará que el código debe usar try / except. [↩] (# fnref2)

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
