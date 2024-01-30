Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  # Python introduction
>>> # is used for comment purpose
>>> print('Abhilash')
Abhilash
>>> print(9876543211)
9876543211
>>> # 3.x version of Python
>>> # open source
>>> # Huge community support
>>> # Simple and easy to use
>>> # generate 2-20 even numbers
>>> list(range(2,21))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> list(range(2,21,2)) #jump by 2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> n = 'avinash'
>>> n
'avinash'
>>> n
'avinash'
>>> n.upper()
'AVINASH'
>>> n.title()
'Avinash'
>>> n[::-1]
'hsaniva'
>>> #---------------------------
>>> # Python world = Data Structures(14) + Keywords(35)
>>> # Data Structures
>>> # Numeric: int,float,complex
>>> #int: 0-9 values
>>> 100
100
>>> 340
340
>>> 45
45
>>> #float: decimal point
>>> 2.3
2.3
>>> 3.14
3.14
>>> 6.77
6.77
>>> #complex: real+img
>>> 3+4j
(3+4j)
>>> 2+5j
(2+5j)
>>> # int a = 22  # static typing
>>> # python support dynamic typing
>>> x = 10
>>> y = 4.55
>>> z = 4+5j
>>> # to check type of any variable use type() function
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(z)
<class 'complex'>
>>> #----------------
>>> # Boolean: True False
>>> True
True
>>> False
False
>>> # python is case senstive language
>>> 2 > 4
False
>>> 3 == 3
True
>>> 'tej' == 'Tej'
False
>>> # While comparing the objects we get boolean outputs
>>> #----------------------------------------
>>> # String
>>> # syntax: '' ""
>>> a = 'python'
>>> a
'python'
>>> type(a)
<class 'str'>
>>> b = '300'
>>> b
'300'
>>> type(b)
<class 'str'>
>>> # Check for ""
>>> #----------------------
>>> # List
>>> # Syntax: []
>>> []
[]
>>> # empty list
>>> type([])
<class 'list'>
>>> v = [3,4,5,77,899999]
>>> v
[3, 4, 5, 77, 899999]
>>> # collection of elements
>>> #------------------------
>>> # Tuple
>>> # syntax: ()
>>> ()
()
>>> type(())
<class 'tuple'>
>>> # empty tuple
>>> t = (7,8,9,'go','stop')
>>> t
(7, 8, 9, 'go', 'stop')
>>> type(t)
<class 'tuple'>
>>> #--------------------------
>>> # Set:
>>> # syntax:{1,}
>>> s = set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> # empty set
>>> p = {}
>>> type(p)
<class 'dict'>
>>> # empty {} is nt set its dict
>>> #----------------------
>>> # dict
>>> # syntax: {key:value}
>>> {}
{}
>>> r = {10:1,20:2,30:300}
>>> r
{10: 1, 20: 2, 30: 300}
>>> y = {'a':'apple','b':'ball'}
>>> y
{'a': 'apple', 'b': 'ball'}
>>> y['a']
'apple'
>>> y['b']
'ball'
>>> #--------------------------------
>>> # frozenset(), bytes(), bytearray(),range(),None
>>> None
>>> # null/nothing
>>> #-------------------------------------
>>> # Keywords: Reserved words in python
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> or = 80
SyntaxError: invalid syntax
>>> len(keyword.kwlist)
35
>>> a
'python'
>>> del a #will delete a
>>> a
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
