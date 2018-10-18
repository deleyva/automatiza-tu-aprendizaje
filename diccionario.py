line = 'brontosaurus asdf ñjñlkj asdf'
d = {}
for c in line:
	d[c] = d.get(c,0) + 1
	
print(d)