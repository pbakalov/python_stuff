# coding: utf-8
#олимпиада по програмиране, Варна 2016
#задача А: цифра


n =5

a = n**n

a_str = str(a)

print a
print a_str
if len(a_str)>n-1:
    print a_str[n-1]
else:
    print "*"
