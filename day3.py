Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> y = "john"
>>> print(x)
5
>>> print(y)
john
>>> x=4 # x is type of int
>>> x='sally' #x is type of string
>>> print(x)
sally
>>> x,y,z = 'orange','banana','apple'
>>> print (x)
orange
>>> print(y)
banana
>>> print(z)
apple
>>> x=y=z="orange"
>>> print(x,y,z)
orange orange orange
>>> x="awesome"
>>> print('python is '+x)
python is awesome
>>> x='python is'
>>> y='awesome'
>>> z=x+y
>>> print(z)
python isawesome
>>> x=5
>>> y=6
>>> print(x+y)
11
>>> x=f
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x=f
NameError: name 'f' is not defined
>>> x=5
>>> y='john'
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
