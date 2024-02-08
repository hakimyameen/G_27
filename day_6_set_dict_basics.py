Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List methods
>>> dit(list)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dit(list)
NameError: name 'dit' is not defined
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k = [33,55,66,77,90]
>>> k
[33, 55, 66, 77, 90]
>>> help(k.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> k.pop()
90
>>> k
[33, 55, 66, 77]
>>> # default it removes last element
>>> # if we want to remove element at specific index
>>> # remove 66
>>> k.pop(2)
66
>>> k
[33, 55, 77]
>>> # Assignmnet: Try with -ve index
>>> # Pop is index based removal
>>> k.pop(34)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    k.pop(34)
IndexError: pop index out of range
>>> #------------------
>>> help(k.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> # remove is value based
>>> k
[33, 55, 77]
>>> k.remove(55)
>>> k
[33, 77]
>>>  # try to remove absent element
>>> k.remove(100)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    k.remove(100)
ValueError: list.remove(x): x not in list
>>> # we cant keep remove()
>>> k.remove()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    k.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> # k.remove(value) value must be given
>>> #-----------------
>>> #Q. pop vs remove
>>> # Q. explain working of pop and remove
>>> #---------------------
>>> # reverse()
>>> f = [1,2,3,4,5]
>>> f
[1, 2, 3, 4, 5]
>>> f.reverse() # inplace means parmenant
>>> f
[5, 4, 3, 2, 1]
>>> #---------------------
>>> # sort(): used to sort list
>>> t = [99,1,18,33,55,1,0]
>>> t
[99, 1, 18, 33, 55, 1, 0]
>>> # default sorting is in ascending order
>>> t.sort()
>>> # this one is also inplace: direct change in original object
>>> t
[0, 1, 1, 18, 33, 55, 99]
>>> # if we want in descending order then user reverse=True
>>> t.sort(reverse=True)
>>> t
[99, 55, 33, 18, 1, 1, 0]
>>> nm = ['pooja','siddhesh','avinash','aditi','Uma']
>>> nm
['pooja', 'siddhesh', 'avinash', 'aditi', 'Uma']
>>> # sorting will be a-z
>>> nm.sort()
>>> nm
['Uma', 'aditi', 'avinash', 'pooja', 'siddhesh']
>>> # first it take Cap letters n then small case letters
>>> nm = ['pooja','siddhesh','avinash','aditi','uma']
>>> nm
['pooja', 'siddhesh', 'avinash', 'aditi', 'uma']
>>> nm.sort()
>>> nm
['aditi', 'avinash', 'pooja', 'siddhesh', 'uma']
>>> nm.sort(reverse=True)
>>> nm
['uma', 'siddhesh', 'pooja', 'avinash', 'aditi']
>>> # sort(key:function,reverse:bool)
>>> nm
['uma', 'siddhesh', 'pooja', 'avinash', 'aditi']
>>> # sort on the basis of len
>>> nm.sort(key=len)
>>> nm
['uma', 'pooja', 'aditi', 'avinash', 'siddhesh']
>>> nm.sort(key=len,reverse=True)
>>> nm
['siddhesh', 'avinash', 'pooja', 'aditi', 'uma']
>>> # here no concern with a-z
>>> #------------------------
>>> # We cant apply sort over hetro. data
>>> r = [100,20,0,'Z','D','A']
>>> r
[100, 20, 0, 'Z', 'D', 'A']
>>> r.sort()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    r.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> #------------------------
>>> #==================================
>>> # Set
>>> # {num}/set()
>>> # Features of Set
>>> # Set doesnt allow duplicates
>>> {2,5,7,2,2,2,5,5,5,7}
{2, 5, 7}
>>> # Sequence order nt get preserved
>>> {'python',0,9,5,'java',-1}
{0, 5, 'java', 9, 'python', -1}
>>> # Why????
>>> # Background data structure is Hash Table
>>> # Property of the hash is table does nt preserves sequence
>>> # EEven duplicates are not allowed
>>> # its not like what array does
>>> # In set we dont have indexing , slicing
>>> a = {6,7,'A'}
>>> a
{'A', 6, 7}
>>> type(a)
<class 'set'>
>>> a[-1]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a[-1]
TypeError: 'set' object does not support indexing
>>> a[:] #lsicing is not allowed
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a[:] #lsicing is not allowed
TypeError: 'set' object is not subscriptable
>>> #---------------
>>> # Homo/Hetro values allowed
>>> # It is Mutable in nature
>>> # check the methods those support mutable operations
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> a
{'A', 6, 7}
>>> id(a)
2056041508936
>>> # lets add 100
>>> a.add(100)
>>> a
{'A', 100, 6, 7}
>>> a.add('pooja')
>>> a
{100, 6, 7, 'A', 'pooja'}
>>> id(a)
2056041508936
>>> #----------------
>>> # pop vs remove vs discard
>>> help(set.pop)
Help on method_descriptor:

pop(...)
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> a
{100, 6, 7, 'A', 'pooja'}
>>> a.pop()
100
>>> a
{6, 7, 'A', 'pooja'}
>>> #------------------
>>> help(set.remove)
Help on method_descriptor:

remove(...)
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.

>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a
{6, 7, 'A', 'pooja'}
>>> a.remove('A') # u must hv to supply value
>>> a
{6, 7, 'pooja'}
>>> a.remove('suyash')
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.remove('suyash')
KeyError: 'suyash'
>>> #---------------
>>> help(set.discard)
Help on method_descriptor:

discard(...)
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

>>> k
[33, 77]
>>> a
{6, 7, 'pooja'}
>>> #a.discard(element)
>>> a.discard()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.discard()
TypeError: discard() takes exactly one argument (0 given)
>>> a.discard(7)
>>> a
{6, 'pooja'}
>>> a.discard('suyash')
>>> a
{6, 'pooja'}
>>> #lets use pop to remove unknown
>>> a.pop('amit')
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.pop('amit')
TypeError: pop() takes no arguments (1 given)
>>> # Q. Pls list out the points related to pop remove and discard of set
>>> #-------------------------------------
>>> # SET OPERATION
>>> d1 = {'A','B','C'}
>>> d1
{'A', 'C', 'B'}
>>> d2 = {'A','B','D','E'}
>>> d2
{'D', 'A', 'E', 'B'}
>>> # Intersetion: returns common elements
>>> d1.intersection(d2)
{'A', 'B'}
>>> # union: returns elements from both the set without duplicates
>>> d1.union(d2)
{'C', 'D', 'A', 'E', 'B'}
>>> d2.union(d1)
{'C', 'A', 'D', 'E', 'B'}
>>> # difference: returns uncommon element from set 1
>>> d1
{'A', 'C', 'B'}
>>> d2
{'D', 'A', 'E', 'B'}
>>> d1.difference(d2)
{'C'}
>>> d2.difference(d1)
{'D', 'E'}
>>> # symmetric_difference: uncommon element from both the sets
>>> d1.symmetric_difference(d2)
{'C', 'D', 'E'}
>>> # Assignment: update(),difference_update(),symmetric_difference_update(), intersection_update()
>>> d1
{'A', 'C', 'B'}
>>> d2
{'D', 'A', 'E', 'B'}
>>> #all above operations without update are temp.
>>> #----------------------------------
>>> #===============================
>>> # dict(): dictionary
>>> # {key:value}
>>> # Features:-
>>> # Background data structure is Hash Table
>>> # So No Array No Indexing No Slicing
>>> # Duplicates keys not allowed
>>> {1:100,1:200,1:300} # key 1 repeated 3 times
{1: 300}
>>> # Duplicate values allowed
>>> {1:100,2:100,3:100}
{1: 100, 2: 100, 3: 100}
>>> # Homo.Hetro key values are allowed
>>> {1:100,'name':'mayank',12:24.55}
{1: 100, 'name': 'mayank', 12: 24.55}
>>> {[1,2]:1000}
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    {[1,2]:1000}
TypeError: unhashable type: 'list'
>>> {(1,2):1000}
{(1, 2): 1000}
>>> # Immutable keys allowed
>>> #--------------------
>>> # Preserves sequence order
>>> {'':'avinash'}
{'': 'avinash'}
>>> # empty string is also valid key
>>> #---------------------------
>>> # Dict is MUTABLE in nature
>>> 
