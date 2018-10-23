## Trabajando con archivos word usando Python

Artículo original [aquí](https://automatetheboringstuff.com/chapter13/)

Python puede crear y modificar documentos de Word, que tienen la extensión de archivo .docx, con el módulo python-docx. Puedes instalar el módulo ejecutando 'pip install python-docx'.

Para hacer pruebas puedes bajarte este [archivo word](https://github.com/deleyva/automatiza-tu-aprendizaje/blob/master/demo.docx?raw=true).

Cada pequeño cambio de estilo, py-docx lo considera como un 'run':

![](img/https://automatetheboringstuff.com/images/000017.png)

## Leyendo documentos de Word

```python
>>>import docx
>>> doc = docx.Document('demo.docx')
>>> len(doc.paragraphs)
   7
>>> doc.paragraphs[0].text
   'Document Title'
>>> doc.paragraphs[1].text
   'A plain paragraph with some bold and some italic'
>>> len(doc.paragraphs[1].runs)
   4
>>> doc.paragraphs[1].runs[0].text
   'A plain paragraph with some '
>>> doc.paragraphs[1].runs[1].text
   'bold'
>>> doc.paragraphs[1].runs[2].text
   ' and some '
>>> doc.paragraphs[1].runs[3].text
   'italic'
```

## Obteninendo el texto completo de un archivo docx

```python
import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('demo.docx'))
```

## Escribiendo un archivo de word

```python
>>> import docx
>>> doc = docx.Document()
>>> doc.add_paragraph('Hello world!')
<docx.text.Paragraph object at 0x0000000003B56F60>
>>> doc.save('helloworld.docx')
```

## Añadiendo encabezados

```python
>>> doc = docx.Document()
>>> doc.add_heading('Header 0', 0)
<docx.text.Paragraph object at 0x00000000036CB3C8>
>>> doc.add_heading('Header 1', 1)
<docx.text.Paragraph object at 0x00000000036CB630>
>>> doc.add_heading('Header 2', 2)
<docx.text.Paragraph object at 0x00000000036CB828>
>>> doc.add_heading('Header 3', 3)
<docx.text.Paragraph object at 0x00000000036CB2E8>
>>> doc.add_heading('Header 4', 4)
<docx.text.Paragraph object at 0x00000000036CB3C8>
>>> doc.save('headings.docx')
```

## Añadiendo saltos de línea y de página

```python
 >>> doc = docx.Document()
 >>> doc.add_paragraph('This is on the first page!')
<docx.text.Paragraph object at 0x0000000003785518>
>>> doc.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)
>>> doc.add_paragraph('This is on the second page!')
<docx.text.Paragraph object at 0x00000000037855F8>
>>> doc.save('twoPage.docx')
```

## Añadiendo imágenes

```python
>>> doc.add_picture('zophie.png', width=docx.shared.Inches(1),
height=docx.shared.Cm(4))
<docx.shape.InlineShape object at 0x00000000036C7D30>
```
