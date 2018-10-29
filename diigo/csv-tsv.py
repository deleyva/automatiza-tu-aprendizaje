import csv
from bs4 import BeautifulSoup
import pprint
import re

filename = input('Introduce el nombre del archivo: ')
lista_out = []

with open(filename,'r') as csvin:
    csvin = csv.reader(csvin)
    lista_csvin = list(csvin)
    print(len(lista_csvin))
    for item in lista_csvin[1:]:
        lineas = item[4].replace('\nSticky note: ', 'Sticky note: ')
        lineas = lineas.splitlines()
        for linea in lineas:
            campos = {}
            items = re.findall(r'Highlight: (.*)Sticky note: (.*)', linea)
            if len(items) != 1:
                items = re.findall(r'Highlight: (.*)', linea)
                # print(items[0])
                campos['back'] = BeautifulSoup(items[0], 'html.parser')
                campos['front'] = ''
            else:
                # print(items[0][0], '\n', items[0][1])
                campos['back'] = BeautifulSoup(items[0][0], 'html.parser')
                campos['front'] = items[0][1]
            campos['title'] = item[0]
            campos['url'] = item[1]
            campos['tags'] = item[2]
            campos['description'] = item[3]
            lista_out.append(campos)
            

pprint.pprint(lista_out)

with open('export.txt', 'w') as tsvout:
    tsvout = csv.writer(tsvout, delimiter='\t')
    for item in lista_out:
        row = list(item.values())
        tsvout.writerow(row)


