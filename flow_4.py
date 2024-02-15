""""""
"""
Flow control block
3. Transfer statements: must be added inside the block
- break
- continue
- pass
All are keywords used for the specific purpose
===============================
- break: to exit from current execution if condition gets 
satisfied

num = [10,20,40,-1,60,77,84,-20,99]
# PS: stop if we get -ve number
for i in num:
    if i<0:
        break
    else:
        print('num:',i)
------------------------------
# Ps: stop if age<18

age = 11
if age<18:
    break
else:
    print('Age:',age)

# We can ONLY use break/continue inside for/while loop
-----------------------------------------
num = [10,20,40,-1,60,77,84,-20,99]
# PS: skip the  -ve number
for i in num:
    if i<0:
        continue
    else:
        print('num:',i)
-------------------------
cart = [499,800,2900,1999,199,599,99,700,100,500]
# skip items below 500 and print the total bill
f = []
for item in cart:
    if item<500:
        continue
    else:
        print('Iter price:',item)
        f.append(item)
print('Total items selected:',len(f))
print('Total bill:',sum(f))
-------------------------------------
Q. break vs continue

for i in range(6):
    if i==3:
        #break
        continue
    else:
        print(i)
-----------------------------------------
pass: used to create empty blocks
for i in range(4):
    pass
--------------------------------------
"""



































