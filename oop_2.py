""""""
"""
OOP Properties/ Pillars of OOP
- Inheritance
- Encapsulation
- Abstraction
- Polymorphism
---------------------
- Inheritance: building parent child relationship among the classes
Due to inheritance, we can access members of a Parent class

class RBI:#Parent class/root class
    def fund(self):
        print('funds from RBI')
class SBI(RBI): #child class/derived class
    pass
s1 = SBI()
s1.fund()
------------------

# Multilevel inheritance
class Director:
    def admin_help(self):
        print('Director help')
class Principal(Director):
    def cancel_admission(self):
        print('Approve/Disapprove')
    def leave(self):
        print('Principal:leave approval')
class Teacher(Principal):
    def leave(self):
        print('teacher: leave approval')

class Student(Teacher):
    pass
s = Student()
s.admin_help()
s.leave()
#Student--->Teacher---> Principal--> DIrector
---------------------------------------------
class Sample_1:
    a = 20

class Sample_2(Sample_1):
    b = 30

class Sample_3(Sample_2):
    pass
s = Sample_3()
print(s.a)
print(s.b)
-------------------------------------
Types of Inheritance:
- Simple 
1 Parent 1 Child

- Multilevel inheritance
..SuperParent<--Parent<---Child
Ex.
We have multiple parents and 1 child
Ex.
class SP:
    def call_1(self):
        print('Sharad Pawar NCP')

class AP(SP):
    def call_2(self):
        print('Ajit Pawar NCP')

class Party(AP):
    pass
p = Party()
p.call_1()
---------------------------------------
- Multiple
More than one parent
Ex.
class SP:
    def new(self):
        print('New Admission')

class AP:
    def call_1(self):
        print('A Pawar NCP')
    def call_2(self):
        print('Ajit Pawar NCP')
    def new(self):
        print('New admission at AP')

class Party(AP,SP):
    pass
p = Party()
p.call_1()
p.call_2()
p.new()
----------------------------------
class Mother:
    def money(self):
        print('Mothers Money')

class Father:
    def money(self):
        print('Father Money')
    def car(self):
        print('Fathers car')


class Child(Mother,Father):
    def m1(self):
        Father.money(self)


c = Child()
c.money()
c.car()
c.m1()
--------------------------
class Mother:
    def money(self):
        print('Mothers Money')

class Father(Mother):
    def money(self):
        print('Father Money')
        super().money()

    def car(self):
        print('Fathers car')


class Child(Father):
    pass

c = Child()
c.money()
c.car()
----------------------------------
- Hierarchical 
         P
    c1        c2
r1     r2  t1    t2       

- Hybrid Inheritance
         p 
c1       c2       c3
     g1       g2
---------------------------------
"""
class Bigbro:
    def bike(self):
        print('Bike of BigB')
    def balance(self):
        print('AMIRI')

class Avinash(Bigbro):
    def bike(self):
        print('My bike')
        super().bike()
        super().balance()
        # when we want to access members of parent in child method
        # then use super()
a = Avinash()
a.bike()












































































