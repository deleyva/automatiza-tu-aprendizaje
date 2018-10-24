# Scrapy

Se trata de un frame work que nos va a falicilitar la tarea de hacer webscrapying. [Aquí](https://scrapy.org/) tenéis la web del proyecto.

Para empezar instalaremos la librería:

```python
pip install scrapy
```

Después crearemos una carpeta y nos meteremos en ella:

```bash
mkdir proyecto_scrapy
cd proyecto_scrapy
```

Luego, en esa carpeta creamos un archivo llamado myspider.py con el siguiente contenido:

```python
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
```

Para testear, al igual que con ipython, scrapy trae una shell muy práctica.

```python
scrapy shell <url>
```

## Desplegando nuestra araña en scrapyd