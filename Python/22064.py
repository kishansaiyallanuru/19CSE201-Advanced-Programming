Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> my_neighbours = ["Siddhu" , "Kishan" , "Supraj"]
>>> print(len(my_neighbours))
3
>>> print(my_neighbours(0:))
  File "<stdin>", line 1
    print(my_neighbours(0:))
                         ^
SyntaxError: invalid syntax
>>> print(my_neighbours)
['Siddhu', 'Kishan', 'Supraj']
>>> my_neighbours.append("Parvati")
>>> print(my_neighbours)
['Siddhu', 'Kishan', 'Supraj', 'Parvati']
>>> my_neighbours.insert(0,"Sravan")
>>> print(my_neighbours)
['Sravan', 'Siddhu', 'Kishan', 'Supraj', 'Parvati']
>>> cys.pop(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cys' is not defined
>>> my_neighbours.pop(0)
'Sravan'
>>> print(my_neighbours)
['Siddhu', 'Kishan', 'Supraj', 'Parvati']
>>> my_neighbours.pop(3)
'Parvati'
>>> print(my_neighbours)
['Siddhu', 'Kishan', 'Supraj']
>>> my_neighbours.sort()
>>> print(my_neighbours)
['Kishan', 'Siddhu', 'Supraj']
>>> my_neighbours.reverse()
>>> print(my_neighbours)
['Supraj', 'Siddhu', 'Kishan']
>>> my_neighbours.sort(reverse = 2)
>>> print(my_neighbours)
['Supraj', 'Siddhu', 'Kishan']
>>> my_neighbours.sort(reverse = TRUE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
>>> my_neighbours.sort(reverse = True)
>>> print(my_neighbours)
['Supraj', 'Siddhu', 'Kishan']
>>> my_neighbours.sort(reverse = -2)
>>> print(my_neighbours)
['Supraj', 'Siddhu', 'Kishan']
>>> my_neighbours.sort(reverse = 0)
>>> print(my_neighbours)
['Kishan', 'Siddhu', 'Supraj']
>>> my_neighbours[0] = my_neighbours[1]
>>> print(my_neighbours)
['Siddhu', 'Siddhu', 'Supraj']
>>> my_neighbours.swap(0,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'swap'
>>>
