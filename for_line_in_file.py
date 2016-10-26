#Test the behavior of nested "for line in file:" loops and file-reading functions within 
#such loops.
#It turns out that the inner for loop picks up where the outer left off, and does not 
#rewind to start from the first line (i.e. each line is read once only). 
#This is quite different from  nested for "i in range(N):" loops using the same loop index.
#When a function is called within the loop that takes the file as input, it also picks up at
#the line following the last line that was read in the loop.
#May 2013
def read_sonnet(file):
	for line in file:
		print 'function ', line
		if ('authority' in line): break
file=open('test_file.txt', 'r')

counter=0
for line in file:
	print 'outer: ', line
	if ('piety' in line):
		for line in file:
			print 'inner ', line
			if ('Omar' in line):
				read_sonnet(file)
				print 'finish ', line
