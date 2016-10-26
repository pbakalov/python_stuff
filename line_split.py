#testing line.split()
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

line="3.14 551 6544.2 this"

for x in  line.split():
	if is_number(x):
		print x, float(x)
	else:	
		print x

new_line=[x for x in line.split()]
numbers=[x for x in line.split() if is_number(x)]
print line
print line.split()
print new_line
print numbers

