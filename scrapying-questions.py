import requests
from bs4 import BeautifulSoup
import re
from py_translator import Translator

r = requests.get('https://automatetheboringstuff.com/chapter11/')
soup = BeautifulSoup(r.text, 'html.parser')
numero = re.compile(r'^\d.*')
translator = Translator()

questions = soup.find_all('p')
for question in questions:
	is_question = numero.search(question.text)
	if is_question != None:
		print(translator.translate(text=question.text[2:], dest='es').text)