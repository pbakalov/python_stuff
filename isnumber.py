def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

a='1.2'
b='-324.2'
c='1.2e5'
d='33'
e='33a'
list=[a,b,c,d,e]
for x in list:
	print x, is_number(x)

