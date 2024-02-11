"""
Multiline comment
Contents inside this scope wont be a part of project/code

It is also termed as Docstring
"""
"""
Flow control blocks
3 types
1. Selective /Conditional statements
Used for selection/performing the operations
based on condition

If condition is True then Perform operation otherwise
exit

Syntax:
if <condition>:
    # Execute process_1 if condition is True
-------------------------
# Perform operation if number is +ve
num = -8
if num >0:
    print('Perform an Operation')
-------------------------
# for placement per>=60
per = 7
if per>=60:
    print('Allowed for Campus placement')
else:
    print('Per!>=60, Sorry you are not allowed')
# we can use else to go for alternate option

# else follows if: means if condition is False then 
# automatically else block will get executed

# if is condition based, else is Condition less
-----------------------------------------
amt = 8000

if amt>= 10000:
    print('You can purchase MI Phone')
else:
    print('You can purchase Vivo')
------------------------
If we want to test multiple conditions then use 
elif <condition>:
----------------------------
amt = 80000

if amt>= 100000:
    print('You can purchase iPhone')
elif amt>=50000:
    print('You can purchase RealMe/Vivo')
elif amt>=40000:
    print('You can purchase MI')
else:
    print('You can purchase Any other Cell Phone')
----------------------------------
Take an input from user

amt = input('Enter your amount:')

print('Amount:',amt)
print(type(amt))

# As input default data type is str
hence it is needed to convert into int/float
-------------------------------
amt = int(input('Enter your amount:'))
print('Amount:',amt)
if amt>= 100000:
    print('You can purchase iPhone')
elif amt>=50000:
    print('You can purchase RealMe/Vivo')
elif amt>=40000:
    print('You can purchase MI')
else:
    print('You can purchase Any other Cell Phone')
--------------------------------------------
# Assignment: Solve 10 Examples on if elif and else 
"""

































