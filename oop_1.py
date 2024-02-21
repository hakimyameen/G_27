""""""
"""
Advance Python
OOP: Object oriented Programming

Object: an entity which exist physically in the env.
Everything in python is an object

12
3.44
[]
()
{}
# Each object has a predefined structure
#that structure is called as class
-------------------------
p = ()
print(type(p))
------------------------------
class---> template/blueprint/structure
using class we create an object
-----------------------------
class is a container which contains 
properties(variables) + behaviour(methods)

class Human:
    #properties
    legs = 2
    hands = 2
    head = 1

    # operations/behaviours
    def talk(self):
        print('Start talking')
    def sleep(self):
        print('Start Sleeping')
    def work(self):
        print('Start working')
# to allocate a memory for the class
# create the constructor
# Constructor has same name as  that of className
# Constructor == className() class calling
p1 = Human()
# p1 is an object of Human class
print(p1)
print(dir(p1))
p1.talk()
print(p1.head)
----------------------------------------
FIrst we have to create a class
it has a specific structure

We can access members of a class using a constructor

when constructor gets called an object gets created automatically
in above case p1 is an object and Human() is a constructor
-------------------------------------------
# we can create n number of objects
# so we must have to call multiple constructors

class Human:
    #properties
    legs = 2
    hands = 2
    head = 1

    # operations/behaviours
    def talk(self):
        print('Start talking')
    def sleep(self):
        print('Start Sleeping')
    def work(self):
        print('Start working')
janata = Human()
print(janata.head)
janata.sleep()
print('----------------')
ravan = Human()
ravan.head = 10
print(ravan.head)
print(Human.head)
ravan.talk()
--------------------------------------------
what is self?
-> is a reference variable inside a method
used to access members of a class inside a method
-
It is present in instance method
Instance method is a method whose structure can be changed
-------------------------------------
class Sample:
    a = 10 # class level variable
   
    def show(self):
        #access a in show
        print('show')
        print(self.a)
   
    def test(self):
        # call show from test
        print('test')
        self.show()

s1 = Sample()
s1.show()
s1.test()
-----------------------------------------
# What is __init__ method:
It is a method associated with constructor
means when we call constructor then init method
gets called automatically
Ex.
class Sample:
    def __init__(self):
        print('Init called')

Sample()
Sample()
-------------------------------------
"""
# Can we pass values to method/constructore
# Ans: Yes
class Sample:
    def __init__(self,name,age,salary):
        print(name,age,salary)

Sample('amit',44,98000)
Sample(age=23,salary=45000,name='hitesh')
# Assignment: take one more method show and apass values to show and print it
# then create one more method test and try to access argument from show method

# Assignment: Create a class for BankApplication
# Assignment: Cretae a class for Dmart Activities







































