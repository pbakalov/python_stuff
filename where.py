from numpy import linspace, where
a=linspace(1,10,10)

def test_where(w):
	return where(w>5)

print test_where(a)
	
