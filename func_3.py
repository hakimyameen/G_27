""""""
"""
lambda function/Nameless/Anonymous

lambda parameter/s:expression


op = lambda x,y,z:x+z
print(op(2,3,4))
-----------------------------
we can use if else in lambda

op = lambda x:x**2 if x>0 else x
print(op(-10))

expression is called as Ternary operator

syntax:

process_1 if condition==True else process_2

-------------------------------
temp = 89
check = 'covid+ve' if temp>90 else 'covid-ve'
print(check)
#-------------------------------------
cv = lambda temp:'covid+ve' if temp>90 else 'covid-ve'
print(cv(97))
for i in range(3):
    pass
#-----------------------
print(cv(96))
-----------------------------------
check = lambda amt: 'vada pav' if amt<100 else 'pizza'
print(check(50))
-------------------------------------
=================================
Higher order functions
- filter
filter(func,iterable)
Used to filter the objects based on condtion
When True then select object else reject

Ex.
h = [35,78,56,77,90,10,3,7,80]
# filter even numbers
print(filter(lambda num:num%2==0,h))
# filter returns filter object
# to see actual values, typecast the filter object
print(list(filter(lambda num:num%2==0,h)))
---------------------------------
ck = ['virat','rohit','bumrah','dinesh','mahi']
# PS: fetch player whose name ends with 't'
print(tuple(filter(lambda name:name.endswith('t'),ck)))
# there is no need of if to give a condition
# just write condition only

# PS: select players whose name length >5
#print(tuple(filter(lambda nm:len(nm)>5,ck)))
suyash = filter(lambda nm:len(nm)>5,ck)
for nm in suyash:
    print(nm)
-----------------------------------------
- map
map(func,iterable)
Used to apply an expression/operation
over each element from the iterable
--------------------
ck = ['virat','rohit','bumrah','dinesh','mahi']
#PS: Convert names in Title case
print(list(map(lambda nm:nm.title(),ck)))
------------------------
salary = [2000,3500,6000,10000,5000]
# Create a new list with 10% bonus on each sal
# sal + 10% bonus
print(list(map(lambda sal:sal+sal*0.1,salary)))
---------------------------------
# same using normal function

salary = [2000,3500,6000,10000,5000]
# Create a new list with 10% bonus on each sal
# sal + 10% bonus
def change(amt):
    return amt+amt*0.1

# map(func,iterable)# only give function name
print(tuple(map(change,salary)))
------------------------
salary = [2000,3500,6000,10000,5000]
# Create a new list with 10% bonus on each sal
# give sal + 10% bonus to sal>5000
# and sal+20% bonus to sal<5000
def change(amt):
    if amt>5000:
        return amt+amt*0.1 #10%
    else:
        return amt + amt * 0.2 #20%

# map(func,iterable)# only give function name
print(tuple(map(change,salary)))
#Assignment: Try same using lambda
---------------------------------------
per = [78,45,69,80,90,93,96,98,35]
if per>75--> dist
per>65-->first
per>55-->second
per>45--> pass
per<45--> fail
--------------------------------------
- reduce
this is nt built in
it is present in functools module
we need to import it

Purpose it to reduce the sequence into single number

from functools import reduce
d = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,d))
-------------------------------------
from functools import reduce

a = [12,8,66,40,3,120]
# find out max number using reduce
print(reduce(lambda x,y:max(x,y),a))
------------------------------------
"""




















































































