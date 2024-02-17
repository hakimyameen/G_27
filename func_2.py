""""""
"""
function

# function with return:
return : it is a keyword used in function to bring the values/objects
from inside the function to outside

def operation(x,y):
    #print(x*y)
    return x*y
result = operation(4,3)
print(result)
-------------------
Can we return multiple objects--> YES

def operation(x,y):
    #print(x*y)
    expr = x*y,x**y,x+100
    return expr
#result = operation(4,3)
x1,x2,x3 = operation(10,2)
print(result)
------------------------------
# in string we have some methods those have return
#EX.
s= 'sample lecture'
i = s.index('lec')
print(s[i:])
--------------------
# show directly
s= 'sample lecture'
print(s.index('lec'))
-----------------------
==================================
Function Arguments/Parameters
There 4 types
- Positional Arguments
- Keyword args.
- default args.
- Variable length args
---------------------------------
1. Positional: in which sequence order of objects matter
Ex.
def details(day,month,year):
    print('Day:',day)
    print('Month:', month)
    print('Year:', year)
details(16,'feb',2024)

details(2024,10,'feb')
# if we change the sequence then it will give u
# wrong allocation
# in same order we have to give values
---------------------------------------
Above problem gets solved by 
2. Keyword args:
Ex.
def details(day,month,year):
    print('Day:',day)
    print('Month:', month)
    print('Year:', year)
details(16,'feb',2024) #positional

# use keyword args
details(year=2024,day=10,month='feb')
-----------------------------------
3. default args: we use in declaration

def account(name='guest',branch='ICICI'):
    print('Name is:',name)
    print('Branch is:', branch)

account() # takes default args
print('--------------')
account('Narayan','ICICI Katraj')
print('--------------')
account(branch='SBI')
-----------------------------
4. Variable leng. args:
- Positional var. len: *args

#supplying var leng args through function calling is not allowed

def numbers(n):
    print(n)
numbers(1)
numbers(3,4,5)
numbers()
numbers(1,2,3,4,5)

So the solution to above problem is: *n

def numbers(*n):
    print(n)
numbers(1)
numbers(3,4,5)
numbers()
numbers(1,2,'ajit','seema')
------------------------------------
- Keyword var. len: **kwargs
Ex.
def numbers(**kwargs):
    print(kwargs)

numbers(name='Python')
numbers(name='Ketan',age=33)
numbers()
----------------------
Q. *args vs **kwargs
========================
lambda function/Anonymous/Nameless function

It is a short representation of a function 
syntax: 
lambda parameter/s:express

lambda- keyword
we can supply args/parameters
we can give only one expression

lambda function has default return

convert = lambda name:name.upper()
print(convert('virat kohli'))
print(convert)
def add():
    pass
print(add)
-------------------------
def sample():
    print('hello')

siddhesh = sample
#function aliasing

siddhesh()
siddhesh()
#convert=lambda
-----------------------------
def add(x,y):
    return x+y,x-y
print(add(20,30))


ad = lambda x,y:x+y,x-y #only one expression is allowed
print(ad(80,90))
-----------------------------------
# but we can give multiple expressions
# using brackets

def add(x,y):
    return x+y,x-y
print(add(20,30))


ad = lambda x,y:(x+y,x-y) #only one expression is allowed
print(ad(80,90))
------------------------------------
# Solve 5 examples of each type of arguments and upload on github
"""





























































