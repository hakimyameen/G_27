Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Tuple: ()
>>> t = ()
>>> t
()
>>> t2 = tuple()
>>> t2
()
>>> # It has same features as that of list
>>> # Except tuple is immutable
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t = (2,100,40,100,5,6)
>>> t
(2, 100, 40, 100, 5, 6)
>>> t.count(100)
2
>>> t.count(66)
0
>>> # index
>>> # returns lowest index
>>> t.index(100)
1
>>> # Tuple is faster than list
>>> # Tuple is Immutable
>>> t
(2, 100, 40, 100, 5, 6)
>>> # try to change elements
>>> t[-1]
6
>>> t[-1] = 'abhi'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t[-1] = 'abhi'
TypeError: 'tuple' object does not support item assignment
>>> # As direct item assignment is nt possible n tuple doesnt have methods which cn replace or change or add or delete the contents
>>> # Hence tuple is IMMUTABLE
>>> #------------------
>>> # q. which one is better?
>>> #--> Based on requirement it will b decided
>>> #--------------------------------
>>> # Tuple packing and unpacking
>>> # comma separated value are tuple
>>> 10,20,30
(10, 20, 30)
>>> 'A','B','C'
('A', 'B', 'C')
>>> # When we give a single name to multiple objects then its packing
>>> char = 'A','B','C'
>>> char
('A', 'B', 'C')
>>> num = 100,-200,400
>>> num
(100, -200, 400)
>>> # Unpacking: use separate var. names for an individual object
>>> v1,v2,v3 = num
>>> v1
100
>>> v2
-200
>>> v3
400
>>> num1,num2 = (1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    num1,num2 = (1,2,3,4)
ValueError: too many values to unpack (expected 2)
>>> #---------------------------
>>> (1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
>>> a1 = (1,2,3)
>>> a1
(1, 2, 3)
>>> a2 =  (4,5,6)
>>> a2
(4, 5, 6)
>>> a1+a2
(1, 2, 3, 4, 5, 6)
>>> a1
(1, 2, 3)
>>> a2
(4, 5, 6)
>>> # a1 and a2 unchanged
>>> # + operator does concatenation it didt chn
>>> # changed original object
>>> #---------------------------------------------
>>> #======================================
>>> # frozenset(): its a set with same properties except this one is IMMUTABLE
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> dir(frozenset)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> # Assignment: Check all above methods on frozen set
>>> t
(2, 100, 40, 100, 5, 6)
>>> # convert tuple to frozenset
>>> t2 = frozenset(t)
>>> t2
frozenset({2, 100, 5, 6, 40})
>>> #=====================================
>>> # range(): It is used to generate sequence of numbers
>>> # range(stop): default range starts with 0 and stop at given number
>>> range(11)
range(0, 11)
>>> # range returns range object: to see the output u have to typecast
>>> list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(11,21))
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # 2nd approach
>>> # range(start,stop)
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> # 3rd approach
>>> # range(start,stop,step)
>>> list(range(1,11,1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(1,11,2))
[1, 3, 5, 7, 9]
>>> # 2-20 evenumbers
>>> list(range(2,21,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> #--------------------------------
>>> #Assignemnt: Try with -ve numebrs
>>> #----------------------------------
>>> 
