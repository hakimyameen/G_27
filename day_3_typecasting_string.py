Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Builtin function from Python
>>> print()

>>> # print(object,sep=' ',end='\n')
>>> print(10,20,30)
10 20 30
>>> # instead of space
>>> print(10,20,30,sep='-')
10-20-30
>>> print(10,20,30,sep='\n') #\n - new line
10
20
30
>>> print(10,20,30,sep='\t') #\t - tab with 4 space
10	20	30
>>> # we can work on end
>>> print('I am 23',end=' yr old')
I am 23 yr old
>>> print('I am 23',end=' yrs old')
I am 23 yrs old
>>> print(end='\n\n')


>>> print('Helo Good evening Pythonist')
Helo Good evening Pythonist
>>> print('Hello \nGood evening \nPythonist')
Hello 
Good evening 
Pythonist
>>> print('Hello');print('GE')
Hello
GE
>>> #---------------------------------
>>> f = [10,20,30,40]
>>> f
[10, 20, 30, 40]
>>> # do addition of all numbers
>>> sum(f)
100
>>> # find max num
>>> max(f)
40
>>> # find min num
>>> min(f)
10
>>> # count total elements present in list
>>> len(f)
4
>>> # reverse the elements
>>> reversed(f)
<list_reverseiterator object at 0x000001DE656A9A58>
>>> # object we need to convert
>>> list(reversed(f))
[40, 30, 20, 10]
>>> # temp
>>> f
[10, 20, 30, 40]
>>> # to sort we can use sorted()
>>> sorted(f)
[10, 20, 30, 40]
>>> sorted([100,7,18,5,0,150])
[0, 5, 7, 18, 100, 150]
>>> # default sorting is in ascending oder
>>> sorted([100,7,18,5,0,150],reverse=True)
[150, 100, 18, 7, 5, 0]
>>> #reverse=True will make it in descending order
>>> #------------------------
>>> # Typecasting: Conversion of a data
>>> d = '100'
>>> d
'100'
>>> # d is of str type
>>> d + 100
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d + 100
TypeError: can only concatenate str (not "int") to str
>>> int(d) + 100
200
>>> float(d)
100.0
>>> list(d)
['1', '0', '0']
>>> # Implicite typecasting: performed by python
>>> 3 + 4 + 1.
8.0
>>> # int--> float--> complex
>>> 10/2
5.0
>>> # Explicite typecasting: Conversion by user
>>> int(10/2)
5
>>> complex(10/2)
(5+0j)
>>> #-------------------------------------
>>> # problems with data types
>>> 100 + 100
200
>>> '100' + '100' # concatenation
'100100'
>>> # for int+ str will throw an error
>>> 3 * 4
12
>>> 3 * '4'
'444'
>>> # 4 repeated 3 times
>>> 3 * int('4')
12
>>> #--------------------------------
>>> # String Data type
>>> # syntax: ''
>>> ""
''
>>> ''
''
>>> # Feattures of String
>>> # String is a global acceptor: accepts all types of data
>>> # Stores a data in sequential order
>>> # Background data structure is an Array
>>> s = 'Sachin Tendulkar'
>>> s
'Sachin Tendulkar'
>>> # each character is one block
>>> # We can fetch single char using an index
>>> # index starts with 0
>>> # and stop at (n-1)
>>> len(s)
16
>>> s[0]
'S'
>>> s[5]
'n'
>>> s[6] #space
' '
>>> s[10]
'd'
>>> # index gives an access to singe char
>>> s
'Sachin Tendulkar'
>>> # We also have slicing in str
>>> # which can access substring from string
>>> s[:]
'Sachin Tendulkar'
>>> # s[start:stop]
>>> # when we r nt giving start and stop , it takes everything
>>> # fetch Sachin
>>> s[0:6]
'Sachin'
>>> s[:6]
'Sachin'
>>> # default it starts with 0
>>> s[7:]
'Tendulkar'
>>> s[7:10]
'Ten'
>>> s
'Sachin Tendulkar'
>>> s[2:6]
'chin'
>>> s[13:]
'kar'
>>> # Python has -ve indexing
>>> s[15]
'r'
>>> s[-1]
'r'
>>> s[0]
'S'
>>> s[-16]
'S'
>>> s
'Sachin Tendulkar'
>>> s[-3:]
'kar'
>>> # want in reverse
>>> s[-1:-4]
''
>>> s[-1:-4:-1]
'rak'
>>> 
>>> s
'Sachin Tendulkar'
>>> # reverse the string
>>> s[::-1] #start reading from right side
'rakludneT nihcaS'
>>> s
'Sachin Tendulkar'
>>> # Sachin in reverse order
>>> s[:6]
'Sachin'
>>> s[:6][::-1]
'nihcaS'
>>> #------
>>> s[-11::-1]
'nihcaS'
>>> #-----
>>> s[:6:-1]
'rakludneT'
>>> s
'Sachin Tendulkar'
>>> s[5::-1]
'nihcaS'
>>> # Assignment: +ve and -ve indexing each 10 examples
>>> s
'Sachin Tendulkar'
>>> # Ten in reverse order
>>> s[9]
'n'
>>> s[9:6:-1]
'neT'
>>> # Assignment: +ve and -ve slicing each 10 examples
>>> 
