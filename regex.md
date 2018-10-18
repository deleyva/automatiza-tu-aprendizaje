utilizando métodos de cadena como `split` y` find` y utilizando listas y corte de cadena para extraer partes de las líneas.



Esta tarea de búsqueda y extracción es tan común que Python tiene una biblioteca muy poderosa llamada ** expresiones regulares ** que maneja muchas de estas tareas con bastante elegancia. La razón por la que no hemos introducido expresiones regulares anteriormente en el libro es que, si bien son muy potentes, son un poco complicadas y su sintaxis requiere un tiempo para acostumbrarse.

Las expresiones regulares son casi su propio lenguaje de programación para buscar y analizar cadenas. De hecho, se han escrito libros completos sobre el tema de las expresiones regulares. En este capítulo, solo cubriremos los conceptos básicos de las expresiones regulares. Para más detalles sobre expresiones regulares, vea:

[http://en.wikipedia.org/wiki/Regular_expression](http://en.wikipedia.org/wiki/Regular_expression)

[https://docs.python.org/2/library/re.html](https://docs.python.org/2/library/re.html)

La biblioteca de expresiones regulares `re` debe importarse en su programa antes de poder usarla. El uso más simple de la biblioteca de expresiones regulares es la función `search ()`. El siguiente programa demuestra un uso trivial de la función de búsqueda.



Abrimos el archivo, recorramos cada línea y usamos la expresión regular `search ()` para imprimir solo las líneas que contienen la cadena "De:". Este programa no utiliza el poder real de las expresiones regulares, ya que podríamos haber utilizado `line.find ()` con la misma facilidad para lograr el mismo resultado.



El poder de las expresiones regulares llega cuando agregamos caracteres especiales a la cadena de búsqueda que nos permiten controlar con mayor precisión qué líneas coinciden con la cadena. Agregar estos caracteres especiales a nuestra expresión regular nos permite realizar comparaciones y extracciones sofisticadas mientras escribimos muy poco código.

Por ejemplo, el carácter de intercalación se usa en expresiones regulares para coincidir con "el principio" de una línea. Podríamos cambiar nuestro programa para que solo coincida con las líneas donde "De:" estaba al principio de la línea de la siguiente manera:

Ahora solo haremos coincidir las líneas que ** comiencen con ** la cadena "De:". Este es todavía un ejemplo muy simple que podríamos haber hecho de manera equivalente con el método `startswith ()` de la biblioteca de cadenas. Pero sirve para introducir la idea de que las expresiones regulares contienen caracteres de acción especiales que nos dan más control en cuanto a qué coincidirá con la expresión regular.



## [Coincidencia de caracteres en expresiones regulares] (# expresiones de coincidencia de caracteres en expresiones regulares)

Hay una serie de otros caracteres especiales que nos permiten construir expresiones regulares aún más potentes. El carácter especial más utilizado es el punto o punto final, que coincide con cualquier carácter.



En el siguiente ejemplo, la expresión regular "F..m:" coincidiría con cualquiera de las cadenas "De:", "Fxxm:", "F12m:" o "F! @M:", ya que los caracteres del período en el Expresión regular coincide con cualquier carácter.

Esto es particularmente poderoso cuando se combina con la capacidad de indicar que un carácter se puede repetir cualquier número de veces utilizando los caracteres "*" o "+" en su expresión regular. Estos caracteres especiales significan que, en lugar de coincidir con un solo carácter en la cadena de búsqueda, coinciden con cero o más caracteres (en el caso del asterisco) o uno o más de los caracteres (en el caso del signo más) .

Podemos restringir aún más las líneas con las que combinamos utilizando un carácter repetido ** de comodín ** en el siguiente ejemplo:

La cadena de búsqueda "` ^ `From:. + @" Coincidirá con las líneas que comienzan con "From:", seguido de uno o más caracteres (". +"), Seguido de un signo de at. Así que esto coincidirá con la siguiente línea:

** `From:` ** `uct.ac.za`

Puede pensar que el comodín ". +" Se expande para hacer coincidir todos los caracteres entre el carácter de dos puntos y el signo de inicio.

** `De:` **

Es bueno pensar que los caracteres de más y asterisco son "agresivos". Por ejemplo, la siguiente cadena coincidiría con la última at-sign en la cadena cuando el ". +" Empuja hacia afuera, como se muestra a continuación:

** `From:` ** `iupui.edu`

Es posible decirle a un asterisco o signo de más que no sea tan "codicioso" agregando otro personaje. Consulte la documentación detallada para obtener información sobre cómo desactivar el comportamiento codicioso.



## [Extracción de datos usando expresiones regulares] (# extracting-data-using-regular-expresiones)

Si queremos extraer datos de una cadena en Python, podemos usar el método `findall ()` para extraer todas las subcadenas que coinciden con una expresión regular. Usemos el ejemplo de querer extraer todo lo que parece una dirección de correo electrónico desde cualquier línea, independientemente del formato. Por ejemplo, queremos extraer las direcciones de correo electrónico de cada una de las siguientes líneas:

```From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008Return-Path: &lt;postmaster@collab.sakaiproject.org&gt;          for &lt;source@collab.sakaiproject.org&gt;;Received: (from apache@localhost)Author: stephen.marquard@uct.ac.za```
No queremos escribir código para cada uno de los tipos de líneas, dividir y dividir de manera diferente para cada línea. Este programa siguiente utiliza `findall ()` para encontrar las líneas con direcciones de correo electrónico en ellas y extraer una o más direcciones de cada una de esas líneas.



El método `findall ()` busca la cadena en el segundo argumento y devuelve una lista de todas las cadenas que parecen direcciones de correo electrónico. Estamos utilizando una secuencia de dos caracteres que coincide con un carácter que no es un espacio en blanco (`\` S).

La salida del programa sería:

```['csev@umich.edu', 'cwen@iupui.edu']```
Al traducir la expresión regular, estamos buscando subcadenas que tengan al menos un carácter que no sea un espacio en blanco, seguido de un signo en, seguido de al menos un carácter más que no sea un espacio en blanco. La "` \ `S +" coincide con la mayor cantidad posible de caracteres que no sean espacios en blanco.

La expresión regular coincidiría dos veces (csev@umich.edu y cwen@iupui.edu), pero no coincidiría con la cadena "@ 2PM" porque no hay caracteres que no estén en blanco ** antes ** del signo de inicio. Podemos usar esta expresión regular en un programa para leer todas las líneas de un archivo e imprimir cualquier cosa que parezca una dirección de correo electrónico de la siguiente manera:

Leemos cada línea y luego extraemos todas las subcadenas que coinciden con nuestra expresión regular. Como `findall ()` devuelve una lista, simplemente verificamos si el número de elementos en nuestra lista devuelta es más que cero para imprimir solo las líneas donde encontramos al menos una subcadena que parece una dirección de correo electrónico.

Si ejecutamos el programa en `mbox.txt` obtenemos el siguiente resultado:

```['wagnermr@iupui.edu']['cwen@iupui.edu']['&lt;postmaster@collab.sakaiproject.org&gt;']['&lt;200801032122.m03LMFo4005148@nakamura.uits.iupui.edu&gt;']['&lt;source@collab.sakaiproject.org&gt;;']['&lt;source@collab.sakaiproject.org&gt;;']['&lt;source@collab.sakaiproject.org&gt;;']['apache@localhost)']['source@collab.sakaiproject.org;']```
Algunas de nuestras direcciones de correo electrónico tienen caracteres incorrectos como "` & lt; `" o ";" Al principio o al final. Declaramos que solo nos interesa la parte de la cadena que comienza y termina con una letra o un número.

Para hacer esto, usamos otra característica de las expresiones regulares. Los corchetes se utilizan para indicar un conjunto de múltiples caracteres aceptables que estamos dispuestos a considerar que coincidan. En cierto sentido, el "` \ `S" está pidiendo que coincida con el conjunto de "caracteres que no son espacios en blanco". Ahora vamos a ser un poco más explícitos en términos de los caracteres con los que coincidiremos.

Aquí está nuestra nueva expresión regular:

```[a-zA-Z0-9]\S*@\S*[a-zA-Z]```
Esto se está complicando un poco y puedes empezar a ver por qué las expresiones regulares son su propio lenguaje. Al traducir esta expresión regular, estamos buscando subcadenas que comiencen con una ** sola ** minúscula, mayúscula o número "[a-zA-Z0-9]", seguido de cero o más caracteres que no estén en blanco (" `\` S * "), seguido de un signo at, seguido de cero o más caracteres que no estén en blanco (" `\` S * "), seguido de una letra mayúscula o minúscula. Tenga en cuenta que cambiamos de "+" a "*" para indicar cero o más caracteres que no están en blanco ya que "[a-zA-Z0-9]" ya es un carácter que no está en blanco. Recuerde que el "*" o "+" se aplica al carácter único inmediatamente a la izquierda del signo más o asterisco.



Si usamos esta expresión en nuestro programa, nuestros datos son mucho más limpios:

```...['wagnermr@iupui.edu']['cwen@iupui.edu']['postmaster@collab.sakaiproject.org']['200801032122.m03LMFo4005148@nakamura.uits.iupui.edu']['source@collab.sakaiproject.org']['source@collab.sakaiproject.org']['source@collab.sakaiproject.org']['apache@localhost']```
Observe que en las líneas "source@collab.sakaiproject.org", nuestra expresión regular eliminó dos letras al final de la cadena ("` & gt; `;"). Esto se debe a que cuando agregamos "[a-zA-Z]" al final de nuestra expresión regular, estamos exigiendo que cualquier cadena que encuentre el analizador de expresiones regulares debe terminar con una letra. Entonces, cuando ve "" & gt; `" después de "sakaiproject.org` & gt;` " simplemente se detiene en la última letra "coincidente" que encontró (es decir, la "g" fue la última buena coincidencia).

También tenga en cuenta que la salida del programa es una lista de Python que tiene una cadena como elemento único en la lista.

## [Combinando búsqueda y extracción] (# combinando, buscando y extrayendo)

Si queremos encontrar números en líneas que comiencen con la cadena "X-", como por ejemplo:

```X-DSPAM-Confidence: 0.8475X-DSPAM-Probability: 0.0000```
No solo queremos números de punto flotante de ninguna línea. Solo queremos extraer números de líneas que tengan la sintaxis anterior.

Podemos construir la siguiente expresión regular para seleccionar las líneas:

```^X-.*: [0-9.]+```
Tras traducir esto, estamos diciendo que queremos líneas que comiencen con "X-", seguidas de cero o más caracteres (". *"), Seguidas de dos puntos (":") y luego un espacio. Después del espacio, estamos buscando uno o más caracteres que sean un dígito (0-9) o un punto "[0-9.] +". Tenga en cuenta que dentro de los corchetes, el período coincide con un período real (es decir, no es un comodín entre los corchetes).

Esta es una expresión muy tensa que coincidirá prácticamente solo con las líneas que nos interesan de la siguiente manera:

Cuando ejecutamos el programa, vemos que los datos están bien filtrados para mostrar solo las líneas que estamos buscando.

```X-DSPAM-Confidence: 0.8475X-DSPAM-Probability: 0.0000X-DSPAM-Confidence: 0.6178X-DSPAM-Probability: 0.0000```
Pero ahora tenemos que resolver el problema de extraer los números. Si bien sería lo suficientemente simple como para usar `split`, podemos usar otra característica de las expresiones regulares para buscar y analizar la línea al mismo tiempo.



Los paréntesis son otro carácter especial en las expresiones regulares. Cuando agrega paréntesis a una expresión regular, se ignoran cuando coinciden con la cadena. Pero cuando está utilizando `findall ()`, los paréntesis indican que mientras desea que la expresión completa coincida, solo le interesa extraer una parte de la subcadena que coincida con la expresión regular.



Entonces hacemos el siguiente cambio a nuestro programa:

En lugar de llamar a `search ()`, agregamos paréntesis a la parte de la expresión regular que representa el número de punto flotante para indicar que solo queremos que `findall ()` nos devuelva la parte del número de punto flotante de la cadena correspondiente .

La salida de este programa es la siguiente:

```['0.8475']['0.0000']['0.6178']['0.0000']['0.6961']['0.0000']..```
Los números aún están en una lista y deben convertirse de cadenas a puntos flotantes, pero hemos utilizado el poder de las expresiones regulares para buscar y extraer la información que encontramos interesante.

Como otro ejemplo de esta técnica, si observa el archivo, hay varias líneas del formulario:

```Details: http://source.sakaiproject.org/viewsvn/?view=rev&amp;rev=39772```
Si quisiéramos extraer todos los números de revisión (el número entero al final de estas líneas) utilizando la misma técnica anterior, podríamos escribir el siguiente programa:

Tras traducir nuestra expresión regular, buscamos líneas que comiencen con "Detalles:", seguidas de cualquier número de caracteres (". *"), Seguidas de "rev =" y luego con uno o más dígitos. Queremos encontrar líneas que coincidan con la expresión completa, pero solo queremos extraer el número entero al final de la línea, por lo que rodeamos "[0-9] +" con paréntesis.

Cuando ejecutamos el programa, obtenemos el siguiente resultado:

```['39772']['39771']['39770']['39769']...```
Recuerde que el "[0-9] +" es "codicioso" y trata de hacer una cadena de dígitos tan grande como sea posible antes de extraer esos dígitos. Este comportamiento "codicioso" es la razón por la que obtenemos los cinco dígitos para cada número. La biblioteca de expresiones regulares se expande en ambas direcciones hasta que encuentra un no dígito, o el principio o el final de una línea.

Ahora podemos usar expresiones regulares para rehacer un ejercicio anterior en el libro en el que estábamos interesados ​​en la hora del día de cada mensaje de correo. Buscamos líneas de la forma:

```From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008```
Y quería extraer la hora del día para cada línea. Anteriormente hicimos esto con dos llamadas a `split`. Primero, la línea se dividió en palabras y luego sacamos la quinta palabra y la dividimos nuevamente en el carácter de dos puntos para sacar los dos caracteres que nos interesaban.

Si bien esto funcionó, en realidad resulta en un código bastante frágil que asume que las líneas están bien formateadas. Si tuviera que agregar suficientes comprobaciones de errores (o un bloque grande de try / except) para asegurarse de que su programa nunca fallara cuando se le presentaban líneas de formato incorrecto, el código se inflaría a 10-15 líneas de código que era bastante difícil de leer.

Podemos hacer esto de una manera mucho más simple con la siguiente expresión regular:

```^From .* [0-9][0-9]:```
La traducción de esta expresión regular es que estamos buscando líneas que comiencen con "De" (note el espacio), seguido de cualquier número de caracteres (". *"), Seguido de un espacio, seguido de dos dígitos "[0 -9] [0-9] ", seguido de un carácter de dos puntos. Esta es la definición de los tipos de líneas que estamos buscando.

Para extraer solo la hora usando `findall ()`, agregamos paréntesis alrededor de los dos dígitos de la siguiente manera:

```^From .* ([0-9][0-9]):```
Esto resulta en el siguiente programa:

<iframe src="https://trinket.io/embed/python3/f6f0612e41" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## El caracter de escape

Para utilizar en nuestras expresiones regulares caracteres propios de las expresiones regulares, utilizaremos la contrabarra '\' para que nuestro código no identifique el caracter al que acompaña como elemento propio de la regex.

```python
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
```
