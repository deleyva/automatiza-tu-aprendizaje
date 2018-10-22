import requests

req = requests.get('http://data.pr4e.org/intro-short.txt')
headers = req.headers
print(headers['Last-Modified'])

# etc
