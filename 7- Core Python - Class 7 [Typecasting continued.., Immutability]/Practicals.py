print('Python Program : 7 - Core Python - Class 7')

# complex() function ----------------------------------------------------------------------
print('\ncomplex() function - Form 1 complex(x)')

print(complex(10))  # outoput: 10+0j
# output: 10.12+0j (real part can be either integral or floating point)
print(complex(10.12))

print(complex(0B1111))  # output: (15+0j)
print(complex(0O234))  # output: (156+0j)
print(complex(0Xbeef))  # output: (48879+0j)

print(complex(True))  # output: (1+0j)
print(complex(False))  # output: 0j

print(complex('10'))  # output (10+0j)
print(complex('10.12'))  # output (10.12+0j)

# print(complex('ten')) # ValueError: complex() arg is a malformed string
# print(complex('0B1111')) # output: ValueError: complex() arg is a malformed string

print('\ncomplex() function - Form 2 complex(x,y)')

print(complex(10, 20))  # output : (10+20j)
print(complex(True, False))  # output : (1+0j)

print(complex(10, 20.5))  # output: (10+20.5j)

# print(complex('10', '20'))  # output: TypeError: complex() can't take second arg if first is a string


# bool() function ---------------------------------------------------------------------------
print('\nbool() function')

print(bool(0))  # output: False
print(bool(1))  # output: True

# output: True (For int arguments 0 means False and non 0 is True. If 0, it is False else it is True)
print(bool(10))
print(bool(-123))  # output: True
print(bool(222))  # output: True

print(bool(0.0))  # output: False
print(bool(0.1))  # output: True
print(bool(0.01))  # output: True

print(bool(10+20j))  # True
print(bool(0+2j))  # True
print(bool(0+0j))  # Flase

print(bool(''))  # output : False
print(bool(''''''))  # output : False
print(bool(""))  # output : False
print(bool(""""""))  # output : False

print(bool('hello'))  # output:  True
print(bool(None))  # output:  False
print(bool(' '))  # output:  True (Space is also treated as a character)


# str() function ---------------------------------------------------------------------------
print('\nstr() function')

print(str(10))  # output: 10
print(str(0B10))  # output: 2

print(str(10.5))  # output: 10.5

print(str(True))  # output: True
print(str(False))  # output: False

print(str(10+12.45j))  # output: (10+12.45j)


# immutability ---------------------------------------------------------------------------------------
print('\nimmutability')

x = 10
y = 10

# Only one object reference is there
print(id(x))  # output : 1884809280
print(id(y))  # output : 1884809280

w1 = "Hydrabad"
w2 = "Hydrabad"
w3 = "Hydrabad"
w10000000 = "Hydrabad"

print(id(w1))  # output: 20139288
print(id(w2))  # output: 20139288
print(id(w3))  # output: 20139288
print(id(w10000000))  # output: 20139288


# Another example
a = 10
b = 10
c = 10

# Memory addess is the same as all are poiting to ther same object reference
print(id(a))  # output: 1884809280
print(id(b))  # output: 1884809280
print(id(c))  # output: 1884809280

a = 20

# output: 1884809440 // This id is different as it is pointing to another object reference
print(id(a))

print(id(b))  # output: 1884809280
print(id(c))  # output: 1884809280

# is operator
# is operator will return true if the variables are pointing to the same object reference,else returns false
print('\nis Operator')
xValue = 10
yValue = 10
zValue = 20

print(xValue is yValue)  # True
print(xValue is zValue)  # False

# is operator example 2
print('\n256 and 257 limit')
v1 = 256
v2 = 256

print(v1 is v2)  # output : True (On Python IDEL)

v3 = 257
v4 = 257

print(v3 is v4)  # output : False (On Python IDEL)
# The reason for this is because, reusing same object, such type of flexibility is available from 0 to 256 only
print(id(v3))
print(id(v4))

# Reusability is not applicable for float type
val1 = 12.1
val2 = 12.1

print(val1 is val2)  # output: False (Find out more)

t = 10 + 20j
u = 10 + 20j

print(t is u)  # output: False (On Python IDEL)
