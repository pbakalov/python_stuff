#this tests reading in numeric data from a file
#May 2013
import numpy , json
file=open('test_data.txt', 'r')

data=[]
counter=0
for line in file:
	if ('#' == line[0]):
		continue #skip comment lines
	else:
		data.append([float(item) for item in line.split()])

#print data[:10]
#print numpy.array(data)[:10]

file.close()

file=open('test_data.txt', 'r')
text = file.read() #text is just a long string with all the contents of the file
file.close()
#print len(text)

text_array= numpy.array(text)
#print text_array.shape
#print text_array

file=open('test_data.json', 'r')
stringmatrix = '['
for line in file:
    if "Self_Energy" in line:
        for line in file:
            if "VALUES" in line:
                for line in file:
                    if "}" in line:
                        break
                    else:
                        stringmatrix = stringmatrix+line
                break
        break
file.close()

print len(stringmatrix)
print stringmatrix
functiondata = json.loads(stringmatrix)
#print functiondata
datamatrix = numpy.matrix(functiondata)
#print datamatrix
#print datamatrix.shape


file=open('test_data.json', 'r')
text = file.read()
file.close()

i=0
valend =-1
while i<len(text):
	if text[i:i+len("Self_Energy")]=="Self_Energy":
		print 'SE', i
		i+=1
		while i < len(text):
			if text[i:i+len("VALUES")]=="VALUES":
				valstart = i+len("VALUES")+7
				print 'begin values', valstart
				print text[valstart]
				i+=1
				while i < len(text):
					if text[i]=="}":
						valend = i-5
						print "end values", valend
						print text[valend]
						break
					else:
						i+=1
			else:
				if valend>-1: break
				else: i+=1
	else:
		if valend>-1: break
		else: i+=1
print i, valstart, valend
print len(text)
