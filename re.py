import re
fh = open('regex_sum_145554.txt')
lista = re.findall('[0-9]+', fh.read())
lista_num = map(int, lista)
print(sum(list(lista_num)))