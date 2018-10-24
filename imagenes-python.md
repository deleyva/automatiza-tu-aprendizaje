# Tratando imágenes con Python

Artículo [aquí]()

Documentación [aquí](https://pillow.readthedocs.io/en/5.3.x/)

```python
>>> from PIL import ImageColor
>>> ImageColor.getcolor('red', 'RGBA')
   (255, 0, 0, 255)
>>> ImageColor.getcolor('RED', 'RGBA')
  (255, 0, 0, 255)
>>> ImageColor.getcolor('Black', 'RGBA')
   (0, 0, 0, 255)
>>> ImageColor.getcolor('chocolate', 'RGBA')
   (210, 105, 30, 255)
>>> ImageColor.getcolor('CornflowerBlue', 'RGBA')
   (100, 149, 237, 255)
```

## Manipulando imágenes con Pillow

Puedes descargarte la imagen de prueba de [aquí](https://github.com/deleyva/automatiza-tu-aprendizaje/blob/master/img/zophie?raw=true).

```python
>>> from PIL import Image
>>> catIm = Image.open('zophie.png')
>>> catIm.size
 (816, 1088)
>>> width, height = catIm.size
>>> width
 816
>>> height
  1088
>>> catIm.filename
   'zophie.png'
>>> catIm.format
   'PNG'
>>> catIm.format_description
   'Portable network graphics'
>>> catIm.save('zophie.jpg')
```

Podemos crear una imagen nueva:

```python
>>> from PIL import Image
>>> im = Image.new('RGBA', (100, 200), 'purple')
>>> im.save('purpleImage.png')
>>> im2 = Image.new('RGBA', (20, 20))
>>> im2.save('transparentImage.png')
```

## Cortando imágenes

```python
>>> croppedIm = catIm.crop((335, 345, 565, 560))
>>> croppedIm.save('cropped.png')
```

## Copiando y pengando en otras imágenes

```python
>>> catIm = Image.open('zophie.png')
>>> catCopyIm = catIm.copy()
>>> faceIm = catIm.crop((335, 345, 565, 560))
>>> faceIm.size
(230, 215)
>>> catCopyIm.paste(faceIm, (0, 0))
>>> catCopyIm.paste(faceIm, (400, 500))
>>> catCopyIm.save('pasted.png')
```

## Cambiando el tamaño de una imagen

```python
>>> width, height = catIm.size
>>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
>>> quartersizedIm.save('quartersized.png')
>>> svelteIm = catIm.resize((width, height + 300))
>>> svelteIm.save('svelte.png')
```

## Rotando y volteando imágenes

```python
>>> catIm.rotate(90).save('rotated90.png')
>>> catIm.rotate(180).save('rotated180.png')
>>> catIm.rotate(270).save('rotated270.png')
```

El método rotate() tiene un argumento opcional 'extend' que se puede establecer en 'True' para ampliar las dimensiones de la imagen para que se ajuste a la imagen nueva girada por completo. Por ejemplo, ingrese lo siguiente en el shell interactivo:

```python
>>> catIm.rotate(6).save('rotated6.png')
>>> catIm.rotate(6, expand=True).save('rotated6_expanded.png')
```

### Volteando

```python
>>> catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
>>> catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
```

