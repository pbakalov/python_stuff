from sys import argv

filename = argv[1]

f = open(filename, 'r')
text = f.read()
f.close()

text = text.replace("old string", "new string")

f = open(filename, 'w')
f.write(text)
f.close()
