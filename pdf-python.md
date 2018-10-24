# Usando Python para trabajar con pdfs

Artículo principal [aqui](https://automatetheboringstuff.com/chapter13/)

Primero instalaremos la librería:

```python
pip install pypdf2
```

## Abriendo un pdf

Podéis descargaros este [pdf de muestra](http://www.estadistica.mat.uson.mx/Material/elmuestreo.pdf) y correr el siguiente programa:

```python
>>> import PyPDF2
>>> pdfFileObj = open('meetingminutes.pdf', 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> pdfReader.numPages
   19
>>> pageObj = pdfReader.getPage(0)
>>> pageObj.extractText()
```

## Creando un pdf

```python
>>> import PyPDF2
>>> pdf1File = open('elmuestreo.pdf', 'rb')
>>> pdf2File = open('elmuestreo1.pdf', 'rb')
>>> pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
>>> pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
>>> pdfWriter = PyPDF2.PdfFileWriter()
   
>>> for pageNum in range(pdf1Reader.numPages):
    	pageObj = pdf1Reader.getPage(pageNum)
    	pdfWriter.addPage(pageObj)

>>> for pageNum in range(pdf2Reader.numPages):
		pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

>>> pdfOutputFile = open('combinedminutes.pdf', 'wb')
>>> pdfWriter.write(pdfOutputFile)
>>> pdfOutputFile.close()
>>> pdf1File.close()
>>> pdf2File.close()
```

## Rotando páginas

```python
>>>import PyPDF2
>>>minutesFile = open('meetingminutes.pdf', 'rb')
>>>pdfReader = PyPDF2.PdfFileReader(minutesFile)
>>> page = pdfReader.getPage(0)
>>> page.rotateClockwise(90)
   {'/Contents': [IndirectObject(961, 0), IndirectObject(962, 0),
   --snip--
   }
>>>pdfWriter = PyPDF2.PdfFileWriter()
>>>pdfWriter.addPage(page)
>>> resultPdfFile = open('rotatedPage.pdf', 'wb')
>>>pdfWriter.write(resultPdfFile)
>>>resultPdfFile.close()
>>>minutesFile.close()
```

## Superpeniendo imágenes como logos o marcas de agua

```python
>>>import PyPDF2
>>>minutesFile = open('meetingminutes.pdf', 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
>>> minutesFirstPage = pdfReader.getPage(0)
>>> pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
>>> minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
>>> pdfWriter = PyPDF2.PdfFileWriter()
>>> pdfWriter.addPage(minutesFirstPage)

>>> for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
>>>resultPdfFile = open('watermarkedCover.pdf', 'wb')
>>>pdfWriter.write(resultPdfFile)
>>>minutesFile.close()
>>>resultPdfFile.close()
```

>**info**
>
>Para comentar varias líneas de código de golpe en Visual Studio Code:
>
>Ctrl + k Ctrl + c
>Ctrl + k Ctrl + u

### Ejercicio [18](https://docs.google.com/forms/d/e/1FAIpQLSdeY3XFANtnxm6mwwPeStnRm-C4sx5nFXrAWcHH9m4mXSCkgA/viewform?authuser=0)

Si no lo has hecho ya, descarga este documentohttp://www.estadistica.mat.uson.mx/Material/elmuestreo.pdf

Combina en un sólo pdf, dos copias del mismo, la segunda con todas las páginas rotadas.

%accordion%Solución%accordion%

```python
import PyPDF2
pdf1File = open('elmuestreo.pdf', 'rb')
pdf2File = open('elmuestreo1.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()
   
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
	pageObj = pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
```

%/accordion%

