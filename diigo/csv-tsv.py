import csv
from bs4 import BeautifulSoup
import pprint
import re

# Introducimos el nombre del archivo e inicializamos la lista_out
# que llenaremos con diccionarios
filename = input('Introduce el nombre del archivo: ')
lista_out = []

with open(filename,'r') as csvin:
    csvin = csv.reader(csvin)
    # Convertimos el reader en lista para poder acceder a todos sus valores
    lista_csvin = list(csvin)

    # Vamos recorriendo las distintas filas del csv
    for item in lista_csvin[1:]:
        # Accedemos a la 5ª celda de cada fila, donde sse almacenan los subrayados
        # los comentarios que hayamos añadido.
        # Por defecto, Sticky note y Highlight vienen en líneas de texto
        # distintas. Con la funcion replace sobre esa cadena de texto,
        # le quitamos el caracter de nueva línea, simplificando el problema.
        lineas = item[4].replace('\nSticky note: ', 'Sticky note: ')
        lineas = lineas.splitlines()
        for linea in lineas:
            campos = {}
            # Intentamos encontrar 3 grupos: subrayado, comentario, historia inverosímil
            items = re.findall(r'Highlight: (.*)Sticky note: (.*)HIN: (.*)', linea)
            if len(items) !=1:
                # Si no, intentamos encontrar 2 grupos: subrayado, comentario
                items = re.findall(r'Highlight: (.*)Sticky note: (.*)', linea)
                if len(items) == 1:
                    campos['back'] = BeautifulSoup(items[0][0], 'html.parser').text
                    campos['front'] = items[0][1]
                    campos['hin'] = ''
            elif len(items) != 1:
                # Si no, intentamos encontrar 1 grupo: subrayado
                items = re.findall(r'Highlight: (.*)', linea)
                if len(items) == 1:
                    campos['back'] = BeautifulSoup(items[0], 'html.parser').text
                    campos['front'] = ''
                    campos['hin'] = ''
            else:
                campos['back'] = BeautifulSoup(items[0][0], 'html.parser').text
                campos['front'] = items[0][1]
                campos['hin'] = items[0][2]
            campos['title'] = item[0]
            campos['url'] = item[1]
            campos['tags'] = item[2]
            campos['description'] = item[3]
            lista_out.append(campos)
            
# Observamos cómo ha quedado la lista de diccionarios
pprint.pprint(lista_out)

# Construimos el csv a partir de la lista_out de diccionarios
with open('export.txt', 'w') as tsvout:
    tsvout = csv.writer(tsvout, delimiter='\t')
    for item in lista_out:
        row = list(item.values())
        tsvout.writerow(row)


