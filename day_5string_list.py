Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String methods
>>> # count()
>>> help(str.count)
Help on method_descriptor:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> s = 'i love India'
>>> s
'i love India'
>>> s.count(' ')
2
>>> s.count('i')
2
>>> s.count('INDIA')
0
>>> # startswith(): to check either str starts with given object
>>> s
'i love India'
>>> s.startswith('i') # returns boolean
True
>>> s.startswith('W')
False
>>> # endswith(): check for end
>>> s
'i love India'
>>> s.endswith('India')
True
>>> s.endswith('IN')
False
>>> #---------------
>>> # find(): will return an index where particular string /block/char is present
>>> s
'i love India'
>>> s.find('India')
7
>>> s.find('i') #returns lowest index
0
>>> # if u want index from right side then use rfind
>>> s.rfind('i')
10
>>> # to check index of all elements one by one use enumerate() function
>>> enumerate(s)
<enumerate object at 0x000001E356922120>
>>> # in order to get exact values , perform typecasting
>>> list(enumerate(s))
[(0, 'i'), (1, ' '), (2, 'l'), (3, 'o'), (4, 'v'), (5, 'e'), (6, ' '), (7, 'I'), (8, 'n'), (9, 'd'), (10, 'i'), (11, 'a')]
>>> tuple(enumerate(s))
((0, 'i'), (1, ' '), (2, 'l'), (3, 'o'), (4, 'v'), (5, 'e'), (6, ' '), (7, 'I'), (8, 'n'), (9, 'd'), (10, 'i'), (11, 'a'))
>>> # enumerate returns[(index,element)]
>>> #------------------------
>>> # index()
>>> # it also returns lowest index
>>> s
'i love India'
>>> s.index('love')
2
>>> s.index('i')
0
>>> # find vs index?
>>> s.find('VV')
-1
>>> s.index('VV')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.index('VV')
ValueError: substring not found
>>> s.find('VV');print('hi')
-1
hi
>>> s.index('VV');print('hi')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.index('VV');print('hi')
ValueError: substring not found
>>> s.index('VV');print('hi');print('Ge')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s.index('VV');print('hi');print('Ge')
ValueError: substring not found
>>> s.find('VV');print('hi');print('Ge')
-1
hi
Ge
>>> #-----------------------
>>> # split uses space as a default separator and retursn list[str]
>>> a = '101 299 345'
>>> a
'101 299 345'
>>> a.split()
['101', '299', '345']
>>> b = '234234-4353-msnf45'
>>> b
'234234-4353-msnf45'
>>> b.split('-')
['234234', '4353', 'msnf45']
>>> # str--> list[str]
>>> # but if we want to get list[str]-->str
>>> n = ['Ajit','Pawar']
>>> n
['Ajit', 'Pawar']
>>> ':'.join(n)
'Ajit:Pawar'
>>> ' '.join(n)
'Ajit Pawar'
>>> ','.join(n)
'Ajit,Pawar'
>>> #---------------------------
>>> # is methods in string
>>> 'abc'.isalpha()
True
>>> 'abc123'.isalpha()
False
>>> 'abc123'.isalnum() # alpha numeric
True
>>> '200'.isdigit()
True
>>> ' '.isspace()
True
>>> 'ABC'.isspace()
False
>>> # Assignment: format(),transform(), remaining ismethods
>>> #-------------------------
>>> #=============================
>>> # List
>>> # []
>>> []
[]
>>> list()
[]
>>> # Features of list
>>> # - background data structure is Array
>>> # - indexing and slicing is default
>>> k = [100,200,300,400,500]
>>> k
[100, 200, 300, 400, 500]
>>> k[0]
100
>>> k[-1]
500
>>> k[-3]
300
>>> # +ve and -ve indexing supported
>>> # Slicing also possible
>>> k[:]
[100, 200, 300, 400, 500]
>>> k[2:]
[300, 400, 500]
>>> k[::-1]
[500, 400, 300, 200, 100]
>>> k[-3::-1]
[300, 200, 100]
>>> k[-3::1]
[300, 400, 500]
>>> # Also contains duplicate records
>>> # preserves seqeunce order
>>> p = [10,20,30,10,10,10]
>>> p
[10, 20, 30, 10, 10, 10]
>>> # List is Mutable
>>> # It allowes changes to be performed directly in the same object/memory
>>> 
>>> p
[10, 20, 30, 10, 10, 10]
>>> id(p)
2075921568584
>>> # lets do some changes in list
>>> # change last 10 to 100
>>> p[-1]
10
>>> p[-1] = 100
>>> p
[10, 20, 30, 10, 10, 100]
>>> # start 10 replace by pooja
>>> p[0] = 'pooja'
>>> p
['pooja', 20, 30, 10, 10, 100]
>>> # using append() add 'java'
>>> p.append('java')
>>> p
['pooja', 20, 30, 10, 10, 100, 'java']
>>> # check id after change
>>> id(p)
2075921568584
>>> # Direct changes persist in the same object address
>>> # hence no need of new object to actually see the result
>>> #------
>>> # List accepts homo.[1,2,3] and hetro.[1,2,3.33,4+5j,'AM',[9,8]]
>>> #-------------------------------
>>> # List Methods
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # Add elements
>>> # append()
>>> d = []
>>> d
[]
>>> d.append(100)
>>> d
[100]
>>> d.append('c++') # will be added after 100(means at the end)
>>> d
[100, 'c++']
>>> d.append([1,2,3]) # will add complete list object
>>> d
[100, 'c++', [1, 2, 3]]
>>> # when we want to add elemens from a list then use extend()
>>> d.extend([1,2,3])
>>> d
[100, 'c++', [1, 2, 3], 1, 2, 3]
>>> # append() adds whole object
>>> # extend() adds elements from an iterable
>>> #------------------------
>>> t = []
>>> t.append('azar')
>>> t.
SyntaxError: invalid syntax
>>> t
['azar']
>>> t.extend('azar')
>>> t
['azar', 'a', 'z', 'a', 'r']
>>> # append(object)
>>> # extend(iterable)
>>> #----------------------
>>> t
['azar', 'a', 'z', 'a', 'r']
>>> t.append(900)
>>> t
['azar', 'a', 'z', 'a', 'r', 900]
>>> t.extend(900)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    t.extend(900)
TypeError: 'int' object is not iterable
>>> t.extend('900')
>>> t
['azar', 'a', 'z', 'a', 'r', 900, '9', '0', '0']
>>> #-------------------------------
>>> # clear()
>>> help([].clear)
Help on built-in function clear:

clear() method of builtins.list instance
    Remove all items from list.

>>> t
['azar', 'a', 'z', 'a', 'r', 900, '9', '0', '0']
>>> t.clear()
>>> t
[]
>>> #--------------------
>>> # copy(): which gives a shallow copy
>>> e1 = [10,20,30,40]
>>> e1
[10, 20, 30, 40]
>>> id(e1)
2075888482760
>>> e2 = e1.copy()
>>> e2
[10, 20, 30, 40]
>>> # but check address of e2
>>> id(e2)
2075921890888
>>> # Shallow copy means : just copy the contents and create a new object
>>> e1
[10, 20, 30, 40]
>>> # add 50 in e1
>>> e1.append(50)
>>> e1
[10, 20, 30, 40, 50]
>>> # now check e2
>>> e2
[10, 20, 30, 40]
>>> # Deep Copy: Copy the contents and address wil be same no new object will be created
>>> e2
[10, 20, 30, 40]
>>> e3 = e2
>>> e3
[10, 20, 30, 40]
>>> # now change in e3
>>> e3.append(100)
>>> e3
[10, 20, 30, 40, 100]
>>> e2
[10, 20, 30, 40, 100]
>>> e2[1] = 300
>>> e2
[10, 300, 30, 40, 100]
>>> e3
[10, 300, 30, 40, 100]
>>> # changes will persist in both e2 and e3 bcz its deep copy
>>> id(e2)
2075921890888
>>> id(e3)
2075921890888
>>> # Q. Shallow copy vs Deep copy
>>> #---------------------------------
>>> #[].insert(): add element at specific index
>>> e1
[10, 20, 30, 40, 50]
>>> # add 'python' between 30 40
>>> #e1.insert(index,object)
>>> # object will be addedd before given index
>>> e1.insert(3,'python')
>>> e1
[10, 20, 30, 'python', 40, 50]
>>> # only one element can be inserted at a time
>>> # Assignment: add 'java' before 10
>>> # add ur name after 50
>>> #-----------------------------------
>>> 
