# Scrapy

Se trata de un framework que nos va a falicilitar la tarea de hacer webscrapying. [Aquí](https://scrapy.org/) tenéis la web del proyecto.

Para empezar instalaremos la librería:

```python
pip install scrapy
```

Después crearemos una carpeta y nos meteremos en ella:

```bash
mkdir proyecto_scrapy
cd proyecto_scrapy
```

Luego, en la terminal, podemos correr el siguiente comando para probar:

```python
scrapy shell -s USER_AGENT="Mozilla/5.0" http://www.gumtree.com/p/studios-bedsits-rent/
```

Se nos abrirá una shell interactiva de scrapy

Podemos probar el siguiente comando a ver qué salida nos da:

```python
>>> response.xpath('//h1/text()').extract()
[u'set unique family well']
```

## Más ejemplos


```python
>>> response.xpath('//h1').extract()
[u'<h1 itemprop="name" class="space-mbs">set unique family well</h1>']
>>> response.xpath('//*[@itemprop="price"][1]/text()').extract()
[u'\xa3334.39pw']
>>> response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
[u'334.39']
>>> response.css('.ad-price').xpath('text()')
[<Selector xpath='text()' data=u'\xa3334.39pw'>]
```

### ¿Qué sacaría el siguiente path?

//*[@itemprop="image"][1]/@src

## Empezando un proyecto en Scrapy

Estas cosas son las que hace un framwork. Te gestiona todo el proyecto y sus directorios. **Las librerías se usan igual que el lenguaje (python), el framework hay que aprenderlo**:

**info**

Los usuarios de Windows probablemente tengan que instalar la librería Win32

```python
pip install pywin32
```

```python
scrapy startproject citas
cd citas
```

Podemos generar nuestra primera araña con el comando:

```python
scrapy genspider citas https://www.goodreads.com/quotes
```

Nos generará un archivo citas.py

Más en el siguiente vídeo:



Pregunta [23](https://classroom.google.com/c/MTg0NjkwNjQzMjVa/sa/MjI4MDc0NzA4Mzha/details)

<!--
%accordion%Solución%accordion%

//div[@class="greyText smallest Text"]

%/accordion%
-->

## Desplegando nuestra araña en scrapyd

Para tener tu araña corriendo en la web [aquí](https://scrapinghub.com/scrapy-cloud) tienes una plataforma muy interesante.