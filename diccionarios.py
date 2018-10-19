name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senders = {}

for line in handle:
	if line.startswith('From '):
		sender = line.split()
		sender = sender[1]
		senders[sender] = senders.get(sender, 0) + 1

num_envios = max(senders.values())

for k, v in senders.items():
	if v == num_envios:
		print(k, v)


