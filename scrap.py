import requests
from bs4 import BeautifulSoup
from py_translator import Translator
import tomd
import time

r = requests.get('https://books.trinket.io/pfe/08-lists.html')
soup = BeautifulSoup(r.text, 'html.parser')

texto_markdown = tomd.convert(str(soup.body))
lista = texto_markdown.splitlines()
comillas = 0

with open('listas.md', 'a') as file:
	for item in lista[60:]:
		translator = Translator()
		# if '```' in item and comillas == 0:
		# 	comillas = 1
		# 	continue
		# elif comillas == 1:
		# 	continue
		# elif '```' in item and comillas == 1:
		# 	comillas = 0
		# 	continue

		objeto_traducido = translator.translate(text=item, dest='es').text
		file.writelines(objeto_traducido + '\n')
		print(objeto_traducido)
		time.sleep(5)

print('¡Hecho!')

