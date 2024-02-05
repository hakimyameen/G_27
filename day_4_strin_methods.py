Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String methods
>>> #''. wait for few sec then it will display list of methods it supports
>>> # u can also use dir()
>>> dir('')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> #-----------------------------
>>> # To check details of any method use help()
>>> help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

>>> nm = 'sham shivam pawar'
>>> nm.split()
['sham', 'shivam', 'pawar']
>>> ip = '198.162.10.109'
>>> ip
'198.162.10.109'
>>> ip.split('.') #default it takes space bt we are providing .
['198', '162', '10', '109']
>>> # On the basis of spearator split gives a list of string['']
>>> #-----------------------------
>>> nm
'sham shivam pawar'
>>> # uppercase
>>> nm.upper()
'SHAM SHIVAM PAWAR'
>>> # bt changes are temp.
>>> # str doesnt allow parmenent changes
>>> # titlecase
>>> nm.title()
'Sham Shivam Pawar'
>>> # capitalize : first letter caps only
>>> nm.capitalize()
'Sham shivam pawar'
>>> #----------
>>> t = 'TITANIC'
>>> t
'TITANIC'
>>> t.lower()
'titanic'
>>> #--------------
>>> a = 'AvInaSH'
>>> a
'AvInaSH'
>>> # convert upper to lower and vice versa
>>> a.swapcase()
'aViNAsh'
>>> #-----------------
>>> nm
'sham shivam pawar'
>>> # convert pawar to patil
>>> # replace(old,new)
>>> nm.replace('pawar','patil')
'sham shivam patil'
>>> nm
'sham shivam pawar'
>>> #-----------------
>>> x = 'azar'
>>> id(x)
2593992453568
>>> x = x.upper()
>>> x
'AZAR'
>>> id(x)
2593991863856
>>> y = 'azar'
>>> id(y)
2593992453568
>>> #-----------------
>>> s = '   shaktiman   '
>>> s
'   shaktiman   '
>>> # when we want to remove spaces in prefixz and suffix then use strip()
>>> s.strip()
'shaktiman'
>>> # in between spaces it doesnt remove
>>> s1 = ' gangadh  ar   '
>>> s1
' gangadh  ar   '
>>> s1.strip()
'gangadh  ar'
>>> # to remove all spaces use replace
>>> # bcz strip only works in prefix and suffix
>>> s1
' gangadh  ar   '
>>> s1.replace(' ','')# replace space , without space
'gangadhar'
>>> s = '#####shaktiman***'
>>> s
'#####shaktiman***'
>>> # remove # *
>>> s.strip('#*')
'shaktiman'
>>> s.strip('*#')
'shaktiman'
>>> #----------------
>>> #Assignment:Remove # and * using replace
>>> #------------------------
>>> print([line.strip() for line in open("akshay.py")])
["x = 'Akshay'", "print('Hello',x)"]
>>> # there must akshay.py file present in python location
