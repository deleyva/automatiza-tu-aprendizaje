fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'romeo.txt'
fh = open(fname)
lst = []

for line in fh:
    words = line.split()
    for word in words:
        if not word in lst:
            lst.append(word)

lst.sort()
print(lst)