from numpy import linalg
from numpy import zeros,ones,dot

a = ones([2,2],float)
a[0,0]=2.
a[1,1]=2.
b = linalg.inv(a)
print "a:\n", a
print "linalg.inv(a):\n", linalg.inv(a)
print "a*b: \n", a*b
print "dot(a,b): \n", dot(a,b)
