import requests
from bs4 import BeautifulSoup
from py_translator import Translator
import tomd
import time

r = requests.get('https://books.trinket.io/pfe/01-intro.html')
soup = BeautifulSoup(r.text, 'html.parser')

texto_markdown = tomd.convert(str(soup.body))
lista = texto_markdown.splitlines()

flag_entre_comillas = False

with open('intro.md', 'a') as file:
	for item in lista:
		translator = Translator()
		if '```' in item:
			file.writelines('```')
			flag_entre_comillas = not flag_entre_comillas
			continue
		if not flag_entre_comillas:
			objeto_traducido = translator.translate(text=item, dest='es').text
			file.writelines(objeto_traducido + '\n')
			print(objeto_traducido)
			time.sleep(5)
		else:
			file.writelines(item.replace('&gt;&gt;&gt;', '>>>') + '\n')

print('¡Hecho!')

