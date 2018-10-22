import csv
from bs4 import BeautifulSoup
import pprint

def csv_to_txv(filename):
    with open('export.csv','r') as csvin, open('export.txt', 'w') as tsvout:
        csvin = csv.reader(csvin)
        tsvout = csv.writer(tsvout, delimiter='\t')

        for row in csvin:
            tsvout.writerow(row)


filename = input('Introduce el nombre del archivo: ')


lista_out = []

with open(filename,'r') as csvin:
    csvin = csv.reader(csvin)
    lista_csvin = list(csvin)
    for item in lista_csvin:
        soup = BeautifulSoup(item[4], 'html.parser')
        lineas = soup.text.splitlines()
        for linea in lineas[1:]:
            is_sticky = False
            if linea.startswith('Highlight: ') or lineas.index(linea) == 1:
                campos = {}
                campos['back'] = campos.get('back', str(linea))
                is_sticky = False
                campos['title'] = item[0]
                campos['url'] = item[1]
                campos['tags'] = item[2]
                campos['description'] = item[3]
            elif linea.startswith('Sticky note: '):
                campos['front'] = campos.get('front', str(linea))
                is_sticky = True
            elif is_sticky:
                campos['front'] = campos['front'], '\n', str(linea)
            else:
                campos['back'] = campos.get('back', str(linea)), '\n', str(linea)
            lista_out.append(campos)

pprint.pprint(lista_out)

