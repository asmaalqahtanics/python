Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="apple "
>>> y="orange "
>>> z="limon "
>>> basket= x+y+z
>>> print(basket)
apple orange limon 
>>> n=6
>>> [basket[i:i+n] for i in range(0,len(basket),n)]
['apple ', 'orange', ' limon', ' ']
>>> 
