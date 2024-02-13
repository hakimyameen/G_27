""""""
"""
Flow Control blocks-
Iterative statements
for loop

for var_name in iterable:
    process
    
# pattern programs on for loop

*
**
***
****
*****

for i in range(1,6):
    print(i*'*')
    
* * * *
* * * *
* * * *
* * * *

for i in range(4):
    print('* '*4)
---------------------
print ur name 5 times

for i in range(5):
    print('ur name')
# execution of for loop is based on number of elements
# present in an iterable
-------------------------------
# Caps. alphabets starts from 65
for i in range(1,5): # 1 2 3 4
    #print(chr(65+i)*i)
    print(chr(64+i)*i)
--------------------------
dddd 100
 ccc  99
  bb  98
   a  97
#print(ord('c'))

for i in range(1,5):
    for j in range(1,5):
        #print(chr(101-j),end='')
        print(chr(101 - i), end='')
    print()

for i in range(1,5):
    for j in range(i+1):
        #print(chr(101-j),end='')
        print(' '*i+chr(101 - i), end='')
    print()

# Youtube: Amulyas Academy Pattern Programs
========================================
2. While loop
Conditionally infinite loop

syntax
while <condition>:
    process
    
num = 8
while num>2:
    print('Hello')
    num-=1
# programmer has to write the logic 
# which can make the condition result False
--------------------------------------- 
# Print 'python' 5 times

count = 1
while count<=5:
    print('python')
    count+=1
-----------------------------
k = ['aditi','tejas','deepa','siddhesh']
# we need 0-3 index as we have 4 elemtns
index = 0
while index <4:
    print(k[index])
    index+=1
---------------------
# Solve 10 Problem on for loop
# Solve 10 problems on while loop
"""




















































