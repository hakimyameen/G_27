Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help(str.strip)
Help on method_descriptor:

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace remove.
    
    If chars is given and not None, remove characters in chars instead.

>>> d = '   devdas   '
>>> d.strip()
'devdas'
>>> d = 'aamanojaaa'
>>> d
'aamanojaaa'
>>> d.strip('a')
'manoj'
>>> d = 'aaamitaaa'
>>> d.strip('a')
'mit'
>>> d = '  aaamitaaa  '
>>> d.strip('a')
'  aaamitaaa  '
>>> #--0----------0-----
>>> # Shallow copy: same elements with different id
>>> # 2 different objects
>>> a1 = [3,4,5]
>>> a1
[3, 4, 5]
>>> a2 = a1.copy()
>>> a2
[3, 4, 5]
>>> # check ids
>>> id(a1)
2347060475464
>>> id(a2)
2347060951176
>>> #----------------------
>>> # Deep copy: same elements with same id
>>> a1
[3, 4, 5]
>>> a3 = a1
>>> a3
[3, 4, 5]
>>> a3.append('avinash')
>>> a3
[3, 4, 5, 'avinash']
>>> a1
[3, 4, 5, 'avinash']
>>> id(a1)
2347060475464
>>> id(a3)
2347060475464
>>> #-----------------------------
>>> s = '###reset***'
>>> s
'###reset***'
>>> s.strip('#*')
'reset'
>>> s.replace('#','')
'reset***'
>>> s.replace('#','').replace('*','')
'reset'
>>> #-----------------------
>>> s.translate({'#':'','*':''})
'###reset***'
>>> help(s.translate)
Help on built-in function translate:

translate(table, /) method of builtins.str instance
    Replace each character in the string using the given translation table.
    
      table
        Translation table, which must be a mapping of Unicode ordinals to
        Unicode ordinals, strings, or None.
    
    The table must implement lookup/indexing via __getitem__, for instance a
    dictionary or list.  If this operation raises LookupError, the character is
    left untouched.  Characters mapped to None are deleted.

>>> s.maketrans({'#':'','*':''})
{35: '', 42: ''}
>>> s
'###reset***'
>>> s.translate(s.maketrans({'#':'','*':''}))
'reset'
>>> t = '1111111100000000111111'
>>> t
'1111111100000000111111'
>>> s.translate(s.maketrans({'1':'0','0':'1'}))
'###reset***'
>>> t.translate(s.maketrans({'1':'0','0':'1'}))
'0000000011111111000000'
>>> p = 'sudhir will call me on 8744332211'
>>> p[-10:]
'8744332211'
>>> p.split()
['sudhir', 'will', 'call', 'me', 'on', '8744332211']
>>> p.split()[-1]
'8744332211'
>>> #-----------------------------
>>> tx1 = 'sudhir is very nice guy'
>>> tx2 = 'A guy name is sudhir'
>>> # find out unique words
>>> l1 = tx1.split()
>>> l1
['sudhir', 'is', 'very', 'nice', 'guy']
>>> l2 = tx2.split()
>>> l2
['A', 'guy', 'name', 'is', 'sudhir']
>>> set(l1).union(set(l2))
{'A', 'guy', 'nice', 'sudhir', 'is', 'very', 'name'}
>>> #-----------------------------------------
>>> k = 'koyana'
>>> k = 'KOYANA'
>>> k
'KOYANA'
>>> k.casefold()
'koyana'
>>> k.lower()
'koyana'
>>> ord('A') # gives a unicode of A
65
>>> ord('#')
35
>>> #-------------------------
>>> 3 + 4. + 3+ 5 + 6
21.0
>>> 3 + int(4.) + 3+ 5 + 6
21
>>> #------------------------------
>>> # Upcasting and Downcasting
>>> num = 23
>>> float(num)
23.0
>>> num
23
>>> num.__sizeof__()
28
>>> num2 = float(num)
>>> num2
23.0
>>> num2.__sizeof__()
24
>>> help(num2.__sizeof__)
Help on built-in function __sizeof__:

__sizeof__() method of builtins.float instance
    Size of object in memory, in bytes.

>>> # int-->float--> complex
>>> k1 = [1,2,3]
>>> k1
[1, 2, 3]
>>> k1.__sizeof__()
64
>>> k2 = [1.,2.,3.]
>>> k2
[1.0, 2.0, 3.0]
>>> k2.__sizeof__()
64
>>> 
