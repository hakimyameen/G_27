""""""
"""
Function: A single unit of a program which
is declared ones and used/called multiple times
-------
There 2 steps
- Declaration
Syntax:
def func_name():
    pass
    
- Calling
Syntax:
func_name()
------------------------------
2 types
- Built-in function
Ex. print,help,dir()......
- User defined function

def calc():
    a = 10
    b = 20
    print('Addition is:',a+b)
    print('Subtraction is:', a - b)
# calling will actually execute a function
calc()
calc()
# Advantage: Code Re-usabilit
--------------------------
# Supply value to func
def calc(a,b):
    print('Addition is:',a+b)
    print('Subtraction is:', a - b)

calc(40,20)
# we can supply other values too
calc(9,4)

# Rule: numbers of parameters in
# declaration== number of values passed in calling
-----------------------------------------
first we hav to declare function
then we can call it
------------------------------------
# supply values at runtime
# Supply value to func
def calc(a,b):
    print('Addition is:',a+b)
    print('Subtraction is:', a - b)

for i in range(3):
    val1 = int(input('Enter first value:'))
    val2 = int(input('Enter Second value:'))
    calc(val1,val2)
    # Call by reference
    #10-->val1-->a
--------------------------------
"""



























