import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import tomd
import time

r = requests.get('https://books.trinket.io/pfe/08-lists.html')
soup = BeautifulSoup(r.text, 'html.parser')

texto_markdown = tomd.convert(str(soup.body))
lista = texto_markdown.splitlines()
comillas = 0

with open('listas.md', 'a') as file:
	for item in lista:
		translator = Translator(service_urls=['translate.google.es'])
		if str(item).startswith('```') and comillas == 0:
			comillas = 1
			continue
		elif comillas == 1:
			continue
		elif str(item).startswith('```') and comillas == 1:
			comillas = 0
			continue

		objeto_traducido = translator.translate(str(item), dest='es')
		file.writelines(objeto_traducido.text)
		print(objeto_traducido.text)
		time.sleep(30)

print('¡Hecho!')

