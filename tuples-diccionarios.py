d = {}
d['title']= 'título de la web'
d['html'] = '<html....'

for key, val in list(d.items()):
	print(val, key)

for i, val in enumerate(d.values()):
	print(str(i) + val)