#this tests reading in numeric data from a file
#May 2013
import numpy , json
file=open('test_data.txt', 'r')

### Reading in a file with tab separated floats
#data=[]
#counter=0
#for line in file:
#	if ('#' == line[0]):
#		continue #skip comment lines
#	else:
#		data.append([float(item) for item in line.split()])
#
##print data[:10]
##print numpy.array(data)[:10]
#
#file.close()
#
#file=open('test_data.txt', 'r')
#text = file.read() #text is just a long string with all the contents of the file
#file.close()
##print len(text)
#
#text_array= numpy.array(text)
##print text_array.shape
##print text_array


### getting the funciton data from a json
file=open('test_data.json', 'r')
stringmatrix = '['
line_count=0
function_name="Self_Energy"
for line in file:
    line_count+=1
    if function_name in line:
        for line in file:
            line_count+=1
            if "VALUES" in line:
                start_line=line_count
                for line in file:
                    line_count+=1
                    if "}" in line:
                        end_line = line_count
                        break
                    else:
                        stringmatrix = stringmatrix+line
                break
        break
file.close()

print 'line count: ', line_count
print 'start values:', start_line #where the data starts
print 'end values:', end_line #where the data ends

functiondata = json.loads(stringmatrix)
datamatrix = numpy.matrix(functiondata)

#print len(stringmatrix)
#print stringmatrix
#print functiondata
#print datamatrix
#print datamatrix.shape

### replace part of the contents of the file
file= open('test_data.json', 'r')
data=[]
for line in file:
	data.append(line)
file.close()

for i in range(start_line-1, end_line-1):
	print data[i]
	print data[i].split()

### reading the file as string and finding the start and end of the data as string positions, not lines
#file=open('test_data.json', 'r')
#text = file.read()
#file.close()
#
#i=0
#valend =-1
#while i<len(text):
#	if text[i:i+len("Self_Energy")]=="Self_Energy":
#		print 'SE', i
#		i+=1
#		while i < len(text):
#			if text[i:i+len("VALUES")]=="VALUES":
#				valstart = i+len("VALUES")+7
#				print 'begin values', valstart
#				print text[valstart]
#				i+=1
#				while i < len(text):
#					if text[i]=="}":
#						valend = i-5
#						print "end values", valend
#						print text[valend]
#						break
#					else:
#						i+=1
#			else:
#				if valend>-1: break
#				else: i+=1
#	else:
#		if valend>-1: break
#		else: i+=1
#print i, valstart, valend
#print len(text)
