# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
nums = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence: "):
        count += 1
        nums += float(line[21:])
print("Average spam confidence: {0:.12f}".format(nums/count))