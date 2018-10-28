import csv
from bs4 import BeautifulSoup
import pprint

filename = input('Introduce el nombre del archivo: ')


lista_out = []

with open(filename,'r') as csvin:
    csvin = csv.reader(csvin)
    lista_csvin = list(csvin)
    for item in lista_csvin[1:]:
        lineas = iter(item[4].splitlines())
        for linea in lineas:
            if linea.startswith('Highlight: '):
                campos = {}
                campos['back'] = BeautifulSoup(linea[11:], 'html.parser').text
                campos['title'] = item[0]
                campos['url'] = item[1]
                campos['tags'] = item[2]
                campos['description'] = item[3]
            elif linea.startswith('Sticky note: '):
                campos['front'] = str(linea[13:])
                lista_out.append(campos)
            else:
                try:
                    if next(lineas).startswith('Highlight: '):
                        lista_out.append(campos)
                except Exception as e:
                    print(e)

pprint.pprint(lista_out)

# with open('export.tsv', 'w') as tsvout:
#     tsvout = csv.writer(tsvout, delimiter='\t')
#     for item in lista_out:
#         row = list(item.values())
#         tsvout.writerow(row)


