Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # combine strings and numbers by using format() method
>>> age = 24
>>> x= "Hi , Iam Asma {}"
>>> print (x.format(age))
Hi , Iam Asma 24
>>> day = 22
>>> month=4
>>> year=1416
>>> x="Iam 24 years , My birth day is {} in month{} year{}"
>>> print(x.format(day, month, year))
Iam 24 years , My birth day is 22 in month4 year1416
>>> x="Iam 24 years, in {2} {1} {0} "
>>> print(x.format(day, month , year ))
Iam 24 years, in 1416 4 22 
>>> 
