import csv

with open('export.csv','r') as csvin, open('export.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)



import csv
with open('export.csv','r') as csvin:
    csvin = csv.reader(csvin)
csvin
csvin[0]
lista_csvin = list(csvin)
with open('export.csv','r') as csvin:
    csvin = csv.reader(csvin)
lista_csvin = list(csvin)
file = open('export.csv','r')
csvin = csv.reader(file)
lista_csvin = list(csvin)
lista_csvin
csvin[0]
lista_csvin[0]
dict_csvin = {}
patern = re.compile(r'(Highlight: )(.*)(Sticky note: )?(Highlight: )')
import re
patern = re.compile(r'(Highlight: )(.*)(Sticky note: )?(Highlight: )')
patern.search(lista_csvin[1][4])
patern.group()
result = patern.search(lista_csvin[1][4])
result
result.group()
lista_csvin[1][4]
patern = re.compile(r'(Highlight: )(.*)(Sticky note: )?(Highlight: )?')
soup
result = patern.search(lista_csvin[1][4])
result
result.group()
result = re.findall(patern, lista_csvin[1][4])
result
result.group()
result = re.findall(patern, lista_csvin[1][4])
result