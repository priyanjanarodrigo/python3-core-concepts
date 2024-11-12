print('Class 07 - Typecasting(Continued), Immutability\n')

# complex() functions
print('\ncomplex() function - Form 1 complex(x) --------------------------------------------------------------------\n')

# Real part can be either integral, floating point or any other base
print(f'complex(10) : {complex(10)}')  # Output: 10+0j
print(f'complex(19) : {complex(19)}')  # Output: complex(9) : (19+0j)
print(f'complex(10.12) : {complex(10.12)}\n')  # Output: complex(10.12) : (10.12+0j)

# Passing the complex number - real part in binary, octal and hexadecimal bases is also possible
print(f'complex(0B1111) : {complex(0B1111)}')  # Output: complex(0B1111) : (15+0j)
print(f'complex(0O234) : {complex(0O234)}')  # Output: complex(0O234) : (156+0j)
print(f'complex(0Xbeef) : {complex(0Xbeef)}')  # Output: complex(0Xbeef) : (48879+0j)

# Passing the complex number real part in boolean (True is considered as 1 and False is considered as 0)
print(f'complex(True) : {complex(True)}')  # Output: complex(True) : (1+0j)
print(f'complex(False) : {complex(False)}')  # Output: complex(False) : 0j

# Passing the complex number real part in string
print(f'complex("10") : {complex("10")}')  # Output: complex("10") : (10+0j)
print(f'complex("11.12") : {complex("11.12")}')  # Output: complex("11.12") : (11.12+0j)

# Invalid values are not allowed in string form to be passed to complex() function
# print(complex('ten')) # ValueError: complex() arg is a malformed string

# Other base values are not allowed in string form to be passed to complex() function
# print(complex('0B1111')) # Output: ValueError: complex() arg is a malformed string
# print(complex('0O234')) # Output: ValueError: complex() arg is a malformed string
# print(complex('0Xbeef')) # Output: ValueError: complex() arg is a malformed string


print('\ncomplex() function - Form 2 complex(x,y) ------------------------------------------------------------------\n')

# Passing the values for both the real and imaginary parts of a complex number.
print(f'complex(10, 20) : {complex(10, 20)}')  # Output: complex(10, 20) : (10+20j)
print(f'complex(True, False) : {complex(True, False)}')  # Output: complex(True, False) : (1+0j)
print(f'complex(10, 20.5) : {complex(10, 20.5)}')  # Output: complex(10, 20.5) : (10+20.5j)

# Invalid values are not allowed in string form to be passed to complex() function - for both real and imaginary parts
# print(complex('10', '20'))  # output: TypeError: complex() can't take second arg if first is a string


# bool() function
print('\nbool() function -------------------------------------------------------------------------------------------\n')

print(f'bool(0) : {bool(0)}')  # Output: bool(0) : False
print(f'bool(1) : {bool(1)}\n')  # Output: bool(1) : True

'''
True (For int arguments 0 means False and non 0 is True. If 0, it is False else it is True)
'''
# Passing integer values into bool() function
print(f'bool(10) : {bool(10)}')  # Output: bool(10) : True
print(f'bool(-123) : {bool(-123)}')  # Output: bool(-123) : True
print(f'bool(222) : {bool(222)}\n')  # Output: bool(222) : True

# Passing floating point values into bool() function
print(f'bool(0.0) : {bool(0.0)}')  # Output: bool(0.0) : False
print(f'bool(0.1) : {bool(0.1)}')  # Output: bool(0.1) : True
print(f'bool(0.01): {bool(0.01)}\n')  # Output: bool(0.01): True

# Passing complex numbers into bool() function
print(f'bool(10 + 20j) : {bool(10 + 20j)}')  # Output: bool(10 + 20j) : True
print(f'bool(0 + 2j) : {bool(0 + 2j)}')  # Output: bool(0 + 2j) : True
print(f'bool(0 + 0j) : {bool(0 + 0j)}\n')  # Output: bool(0 + 0j) : False

# Passing string values into bool() function
'''
The behavior of bool() with strings in Python follows a simple rule:

1. For bool(''), bool(''''''), bool("") or bool(""""""):
    
    - Empty strings (including multi-line empty strings with multiple quotes) evaluate to False
    - This is because an empty string represents "nothingness" or absence of value

2. For bool('hello'):

    - Any non-empty string (containing at least one character) evaluates to True
    - The string 'hello' contains characters, so it's considered a "truthy" value

This is part of Python's "truth value testing" where:

    - Empty sequences (strings, lists, tuples) = False
    - Non-empty sequences = True
'''
print(f"bool('') : {bool('')}")  # Output : bool('') : False
print(f"bool('''''') : {bool('''''')}")  # Output : bool('''''') : False
print(f'bool("") : {bool("")}')  # Output : bool("") : False
print(f'bool("""""") : {bool("""""")}')  # Output : bool("""""") : False

print(f"bool('hello') : {bool('hello')}")  # Output : bool('hello') : True
print(f"bool(' ') : {bool(' ')}")  # Output: bool(' ') : True. (Space is also treated as a character)
print(f"bool('a') : {bool('a')}")  # Output: bool('a') : True

# Null values are considered as False
print(f'bool(None) : {bool(None)}')  # Output:  bool(None) : False

# str() function
print('\nstr() function --------------------------------------------------------------------------------------------\n')

# Passing integer values of different bases into str() function
print(f'str(10) : {str(10)}')  # Output: str(10) : 10
print(f'str(0B10) : {str(0B10)}')  # Output: str(0B10) : 2
print(f'str(0O10) : {str(0O10)}')  # Output: str(0O10) : 8
print(f'str(0xBeef) : {str(0xBeef)}\n')  # Output: str(0xBeef) : 48879

# Passing floating point values into str() function
print(f'str(10.5) : {str(10.5)}')  # Output: str(10.5) : 10.5
print(f'str(312.523) : {str(312.523)}')  # Output: str(312.523) : 312.523

# Passing boolean values into str() function
print(f'str(True) : {str(True)}')  # Output: str(True) : True
print(f'str(False) : {str(False)}')  # Output: str(False) : False

# Passing complex numbers into str() function
print(f'str(10 + 12.45j) : {str(10 + 12.45j)}')  # Output: str(10 + 12.45j) : (10+12.45j)

# immutability
print('\nimmutability ----------------------------------------------------------------------------------------------\n')

x = 10
y = 10

print(f'x = {x}\ny = {y}')

# Only one object reference is there as both x and y are pointing to the same object reference
print(f'id(x) : {id(x)}')  # Output: id(x) : 4318140176 (same id which is dynamically allocated)
print(f'id(y) : {id(y)}')  # Output: id(y) : 4318140176 (same id which is dynamically allocated)

# All the following variables are pointing to the same object reference
w1 = "Hydrabad"
w2 = "Hydrabad"
w3 = "Hydrabad"
w10000000 = "Hydrabad"
print(f'w1 = {w1}\nw2 = {w2}\nw3 = {w3}\nw10000000 = {w10000000}\n')

print(f'id(w1) : {id(w1)}')  # Output: id(w1) : 4318140176
print(f'id(w2) : {id(w2)}')  # Output: id(w2) : 4318140176
print(f'id(w3) : {id(w3)}')  # Output: id(w3) : 4318140176
print(f'id(w10000000) : {id(w10000000)}\n')  # Output: id(w10000000) : 4318140176

# Another example
a = 10
b = 10
c = 10

# Memory adders is the same as all are pointing to the same object reference
print(f'id(a) : {id(a)}')  # Output : id(a) : 1884809280
print(f'id(b) : {id(b)}')  # Output : id(b) : 1884809280
print(f'id(c) : {id(c)}')  # Output : id(c) : 1884809280

# Now changing the value of 'a' which internally changes the object reference
a = 20

# Now the current id of 'a' is different from the previous one as it is pointing to another object reference
print(f'id(a) : {id(a)}')  # Output : id(a) : 1884809440

print(f'id(b) : {id(b)}')  # Output : id(b) : 1884809280
print(f'id(c) : {id(c)}')  # Output : id(c) : 1884809280

# is operator
# is operator will return true if the variables are pointing to the same object reference,else returns false
print('\nis Operator')
xValue = 10
yValue = 10
zValue = 20

print(f'xValue is yValue : {xValue is yValue}')  # Output : xValue is yValue : True
print(f'xValue is zValue : {xValue is zValue}')  # Output : xValue is zValue : False

# is operator example 2
print('\n256 and 257 limit')
v1 = 256
v2 = 256
print(f'v1 = {v1}\nv2 = {v2}\n')

'''
Python IDLE Output: 
    id(v1) : 4327393920
    id(v2) : 4327393920 (id of v1 and v2 are same)
    v1 is v2 : True 
    v1 == v2 : True
    
PyCharm Output:
    id(v1) : 4330943952
    id(v2) : 4330943952 (id of v1 and v2 are same)
    v1 is v2 : True
    v1 == v2 : True
'''
print(f'id(v1) : {id(v1)}')
print(f'id(v2) : {id(v2)}')
print(f'v1 is v2 : {v1 is v2}')
print(f'v1 == v2 : {v1 == v2}\n')

v3 = 257
v4 = 257

'''
Python IDLE Output: 
    id(v3) : 4365631696
    id(v4) : 4365631600 (id of v3 and v4 are different)
    v3 is v4 : False
    v3 == v4 : True

PyCharm Output:
    id(v3) : 4381345904
    id(v4) : 4381345904
    v3 is v4 : True
    v3 == v4 : True
'''
print(f'id(v3) : {id(v3)}')
print(f'id(v4) : {id(v4)}')
print(f'v3 is v4 : {v3 is v4}')
print(f'v3 == v4 : {v3 == v4}\n')

'''
Clarification for the above scenario:

    - The reason for this is because, reusing same object, such type of flexibility is available from 0 to 256 only
    
    - This is an interesting behavior related to Python's integer caching and how different Python implementations 
      handle object reuse.

    - The reason for the different behavior is:
    
        Python internally caches small integers between -5 to 256 for performance optimization. Any integer in this 
        range will always reference the same object.
    
        For integers outside this range (like 257), Python's behavior depends on the implementation:
    
        In Python IDLE/interpreter: New objects are created for each assignment of integers > 256
        
        In PyCharm: The IDE's implementation of Python may optimize and reuse objects even for larger integers during
        code execution
    
        This is why:
    
            v1 = 257
            v2 = 257
            v1 is v2  # False in IDLE, True in PyCharm
            
    - The is operator checks for object identity (if they point to the same memory location). While == checks for value
      equality.

    - For reliable code, you should:
    
        1. Use == for value comparisons
        
        2. Only use is for comparing with None or when you specifically need to check if two variables reference the 
           exact same object
           
        3. Don't rely on implementation-specific integer caching behavior beyond the guaranteed -5 to 256 range
        
    - This behavior is an implementation detail and can vary across different Python environments, which is exactly what
      you're observing between IDLE and PyCharm.
'''

'''
The reusability concept is indeed not applicable for Python floats! This is by design, as floating-point numbers have 
different memory handling compared to small integers.

While Python caches small integers (-5 to 256) for performance optimization, it does not implement the same caching 
mechanism for floats. This is because:

    - Floats are more complex data types that represent decimal numbers
    - They require more precise memory handling
    - They follow IEEE 754 standard for floating-point arithmetic
    
In the standard Python implementation (CPython/IDLE), each float assignment creates a new object in memory. That's why 
using the is operator with floats can give different results across environments.

The correct approach is to always use the == operator for float comparisons, which checks for value equality rather 
than object identity.

This design choice in Python helps maintain precision and consistency in floating-point operations across different 
platforms and implementations.

Reusability is not applicable for float type as float does not have a caching mechanism like small integers do.
'''
val1 = 12.1
val2 = 12.1

'''
Python IDLE Output: 
    id(val1) : 4315509808
    id(val2) : 4315503920 (ids of val1 and val2 are different)
    val1 is val2 : {val1 is val2} : False
    val1 == val2 : {val1 == val2} : True
    
PyCharm Output:
    id(val1) : 4375923024
    id(val2) : 4375923024
    val1 is val2 : {val1 is val2} : True
    val1 == val2 : {val1 == val2} : True
'''
print(f'id(val1) : {id(val1)}')
print(f'id(val2) : {id(val2)}')
print(f'val1 is val2 : {val1 is val2}')
print(f'val1 == val2 : {val1 == val2}\n')

'''
complex numbers behave similarly to floats in Python regarding object reusability. Complex numbers don't have a caching
mechanism like small integers do.

In standard Python (IDLE):

    - Each complex number assignment creates a new object
    - Different memory addresses for t and u
    - t is u returns False
    - t == u returns True
    
In PyCharm:

    - The IDE's optimization might reuse objects
    - Same memory address for t and u
    - t is u returns True
    - t == u returns True

The reliable way to compare complex numbers is using the == operator, which checks for value equality rather than object
identity. This ensures consistent behavior across all Python implementations.

This design aligns with how Python handles other non-cached numeric types like floats, maintaining consistency in the 
language's object model.
'''
t = 10 + 20j
u = 10 + 20j
print(f't = {t}\nu = {u}\n')

'''
Python IDLE Output: 
    id(t) : 4365632432
    id(u) : 4365632336 (ids of t and u are different)
    t is u : False
    t == u : True

PyCharm Output:
    id(t) : 4307159696
    id(u) : 4307159696 (ids are the same)
    t is u : True
    t == u : True
'''
print(f'id(t) : {id(t)}')
print(f'id(u) : {id(u)}')
print(f't is u : {t is u}')
print(f't == u : {t == u}')
