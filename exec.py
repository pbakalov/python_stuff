#execute a string of python code within python

some_code='print "hello world"'

exec some_code

some_more_code= ''' 
def simple_function(some_code):
	exec some_code
a=3
b=33
'''

exec some_more_code

simple_function(some_code)
print a, b

