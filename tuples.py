name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

horas = {}

for line in handle:
	if line.startswith('From '):
		pos = line.find(':')
		hora = line[pos-2:pos]
		horas[hora] = horas.get(hora, 0) + 1

lista_horas = list(horas.items())
lista_horas.sort()

for k, v in lista_horas:
	print(k + ' ' + str(v) )
