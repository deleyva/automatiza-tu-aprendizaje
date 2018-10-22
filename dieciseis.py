import requests
from bs4 import BeautifulSoup

req = requests.get('http://py4e-data.dr-chuck.net/known_by_Faith.html')

for i in range(7):
	soup = BeautifulSoup(req.text, 'html.parser')
	enlace = soup.find_all('a')
	print(enlace[17].text)
	req = requests.get(enlace[17]['href'])