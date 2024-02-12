""""""
"""
Flow Control blocks
1. Conditional or selective statement
if <condition>
if else
if elif else
if elif elif .... else
--------------------------
num = 59
# check num is divisible by 5 if yes then print Accept

if num%5==0:
    print('Accept')
else:
    print('Reject')
-------------------------
num = 35
# check num is divisible by 5 &7  if yes then print Accept

if (num%5==0) and (num%7==0):
    print('Accept')
else:
    print('Reject')
--------------------------
Nested if: if inside if

temp = 83
rtpcr = True

if rtpcr==True:
    
    if temp>90:
        print('Admit the patient')
    else:
        print('Home Isolation')
else:
    print('Go Home')
# Make it dynamic: means take inputs from user
# and test the system
-----------------------------------------
Q. if vs else vs elif
Q. difference between if and elif
Q. what is else
Q. when to use elif
========================================
Iterative statements
1. for loop
2. while loop
---------------
for loop: is used to fetch elements from an iterable 
one by one

Iterables in python- list,set,tuple,dict,str,range
----------------------------------
s = [100,34,55,78,90,120]

# for var_name in iterable:
for num in s:
    print(num,end='\n\n')
    # \n\n means 2 lines after each object gets printed
--------------------------------
s = [100,34,55,78,90,120]
for num in s:
    if num%2!=0:
        print(num,'is odd number')
    else:
        print(num,'is even number')
------------------------
n = [22,-10,-29,3,9,10]

for num in n:
    if num>0:
        print(num,'is +ve')
    else:
        print(num, 'is -ve')
------------------------
display separate list of +ve and -ve numbers

n = [22,-10,-29,3,9,10]
ps = []
ng = []
for num in n:
    if num>0:
        ps.append(num)
    else:
        ng.append(num)

print('List of +ve numbers:',ps)
print('List of -ve numbers:',ng)
-------------------------------------
n = [22,-10,-29,3,9,10]
ps = []
ng = []
for num in n:
    if num>0:
        ps.append(num)
    else:
        ng.append(num)

print('List of +ve numbers:',ps)
print('List of -ve numbers:',ng)
---------------------------------------
s = 'hello ankit i m sending the code 45678 and other one is 76589'
# Q. Find out n display numbers/code only
for i in s:
    if i.isdigit():
        print(i,end='')
----------------------------------
s = 'hello ankit i m sending the code 45678 and other one is 76589'
#print(s.split())
# Q. Find out n display code separately
for i in s.split():
    #print(i)
    if i.isdigit():
        print(i)
------------------------------------
"""

















































































































