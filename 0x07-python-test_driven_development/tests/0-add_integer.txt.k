add_integer(a, b=98)
-----------------------


this function returns the addition of two integers"

Usage exemple
-------------

>>> add_integer = __import__('0-add_integer').add_integer

Adding two integer numbers
>>> add_integer(1, 2)
3

::

Adding an integer and a negative integer
>>> add_integer(100, -2)
98

::

Adding numbers using the default second argument (b=98)
>>> add_integer(2)
100

::

Adding an integer with floating-point numbers
>>> add_integer(100.3, -2)
98

::

Adding two arguments that aren't integers or float
>>> add_integer("python", "is fun")
Traceback (most recent call last):
TypeError: a must be an integer

::

This function also handles non-numbers with an error message
if an argument is not an integer or a float number
>>> add_integer(4, "School")
Traceback (most recent call last):
TypeError: b must be an integer

::

Adding two arguments where one is a string and the other is an integer
>>> add_integer("python", 3)
Traceback (most recent call last):
TypeError: a must be an integer

::

If the argument is None
>>> add_integer(None)
Traceback (most recent call last):
TypeError: a must be an integer

