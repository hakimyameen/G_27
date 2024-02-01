Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Identifier: names given to the objects
>>> 100
100
>>> 200
200
>>> 'python'
'python'
>>> # above all are objects
>>> x = 100
>>> # 100 is an object & x is identifier
>>> y = 'python'
>>> # y is an identifier
>>> # How to check memory adderes on an object
>>> id(x)
140723224764544
>>> id(y)
2517372108728
>>> #----------------------
>>> # Rules of an identifiers
>>> # a-z alphabates are allowed
>>> # words allowed
>>> info = 'Pune'
>>> info
'Pune'
>>> # _ underscore is allowed
>>> _a = 'Good evening'
>>> _a
'Good evening'
>>> _ = 500
>>> _
500
>>> #--------------
>>> # Space is not valid
>>> bank pin = 1234
SyntaxError: invalid syntax
>>> #  _ wil help u to make it valid
>>> bank_pin = 1234
>>> bank_pin
1234
>>> #------------------
>>> # Special symbols and characters are nt valid identifiers
>>> @ = 'sham'
SyntaxError: invalid syntax
>>> b@ = 800
SyntaxError: invalid syntax
>>> bank$ifsc = 'SBI5656'
SyntaxError: invalid syntax
>>> #------------------------
>>> # Reserved keywords are nt valid
>>> in = 'income'
SyntaxError: invalid syntax
>>> True = 160
SyntaxError: can't assign to keyword
>>> #-----------------------------
>>> # numbers ar nt valid
>>> 4 = 400
SyntaxError: can't assign to literal
>>> # number is prefix is nt valid
>>> 2x = 500
SyntaxError: invalid syntax
>>> # in suffix allowed
>>> x2 = 500
>>> x2
500
>>> #---------------------------------
>>> # PEP 8 standards: CHeck on website
>>> #----------------------------------
>>> # Operators in python
>>> # Arithmatic operator: + - * / % // **
>>> 1 + 2
3
>>> 3 - 4
-1
>>> 4 * 2
8
>>> 45/5
9.0
>>> # mod: % returns remainder
>>> 45//5
9
>>> 45%5
0
>>> 46%5
1
>>> # // floor division
>>> # 12(floor).55(ceil)
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 8/3
2.6666666666666665
>>> 8//3
2
>>> # difference between / and //
>>> # power of operator/exponential
>>> 2**8 # 2 num and 8 is a power
256
>>> 3**3 # 3 cube
27
>>> 3**21
10460353203
>>> #-------------------
>>> # Assignment operator
>>> d = 80
>>> d
80
>>> d + 100
180
>>> # d =  d + 100
>>> d += 100
>>> d
180
>>> d -= 40
>>> d
140
>>> d /= 7
>>> d
20.0
>>> d *= 2
>>> d
40.0
>>> d **= 3
>>> d
64000.0
>>> 40 * 40 * 40
64000
>>> #------------------
>>> # Comparison / Conditional / Relational operators
>>> # < > <= >= == !=
>>> # It returns boolean output(True,False)
>>> 3 > 2
True
>>> 3 >= 2
True
>>> 'Amit' == 'amit'
False
>>> 4 != 5
True
>>> # = (assignment) & == (comparison)
>>> #--------------------------------
>>> # Membership: we check the object is a member or not
>>> # in , not in
>>> 'Suyash' in 'Suyash Pawar'
True
>>> # return bolean value
>>> 'sumit' in 'Suyash Pawar'
False
>>> 'yash' in 'Suyash Pawar'
True
>>> 6 in [2,3,4,5,6]
True
>>> 16 in [2,3,4,5,6]
False
>>> # if object is  present it returns True else False
>>> # Assignmnt: Check working of not in
>>> #---------------
>>> # Identity operator
>>> # Returns boolean value and it check identity of an object
>>> # means if ids of both objects are same then those objects are identical
>>> # id means address
>>> # if address are same then True else False
>>> # type: is , is not
>>> # ex.
>>> 'python' is 'Python'
False
>>> id('python')
2517372108728
>>> id('Python')
2517333202512
>>> x = 'sam'
>>> y = 'sam'
>>> x is y
True
>>> id(x)
2517372603280
>>> id(y)
2517372603280
>>> #---------------
>>> e1 = 10.0
>>> e2 = 10.0
>>> e1 is e2
False
>>> id(e1)
2517332442088
>>> id(e2)
2517332440624
>>> #--------------------------
>>> d1 = [1,2,3,4]
>>> d1
[1, 2, 3, 4]
>>> d2 = d1
>>> d2
[1, 2, 3, 4]
>>> d1 is d2
True
>>> id(d1)
2517372886920
>>> id(d2)
2517372886920
>>> # add 100 in d2
>>> d2.append(100)
>>> d2
[1, 2, 3, 4, 100]
>>> d1
[1, 2, 3, 4, 100]
>>> #---------------------
>>> # Logical operators
>>> # returns Boolean output
>>> # type: and or not
>>> 1 and 1
1
>>> 1 and 0
0
>>> 0 and 1
0
>>> 0 and 0
0
>>> name = 'aditi'
>>> name
'aditi'
>>> place = 'pune'
>>> place
'pune'
>>> name=='swati'
False
>>> place == 'mumbai'
False
>>> name=='swati' and place == 'mumbai'
False
>>> name=='swati' and place == 'pune' # 0 1
False
>>> name=='aditi' and place == 'Une' #1 0
False
>>> name=='aditi' and place == 'pune' #1 1
True
>>> #----------------
>>> # or
>>> # assignment
>>> #----------------
>>> # not: negation
>>> name == 'aditi
SyntaxError: EOL while scanning string literal
>>> name == 'aditi'
True
>>> not name == 'aditi'
False
>>> not True
False
>>> not False
True
>>> #----------------------------
>>> 
