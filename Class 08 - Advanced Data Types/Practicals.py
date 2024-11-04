print('\nPython Program : 8 - Core Python - Class 8')

# Reusability
print('\nReusability')

a = 10
b = 10
c = 10

print(a is b)  # Ture
print(b is c)  # Ture
print(a is c)  # Ture
print(a is b is c)  # Ture

q = 1.2
o = 1.2
print(id(q))
print(id(o))

# bytes data type -------------------------------------------------------------------------------------------
print('\nbytes data type')

x = [10, 20, 30, 40]  # x is not the bytes type. This is just a group of values
b = bytes(x)  # Now this b itself is nothing but bytes data type

print(type(x))
print(type(b))

# Accessing values with index (positive or negative)
print(b[-1])  # 40
print(b[0])  # 10

# Slice operator
print(b[0:3])  # b'\n\x14\x1e' (some object reference)

# Printing values using simple for loop
# output is
# 10
# 20
# 30
# 40
# print each byte i in bytes b
for i in b:
    print(i)

# numGroup = bytes([100,200,256,257]) # ValueError: bytes must be in range(0, 256)

# Immutability. Item assignment is not possible once created
numbers = [2, 4, 6, 8]
myB = bytes(numbers)

# myB[0] = 77 # TypeError: 'bytes' object does not support item assignment ('myB' does not support item assignment)


# bytearray data type. Both bytes and bytearray are the same except for bytearray is mutable (item assignment after creation is  possible)
print('\nbytearray')
byteNumbers = [23, 45, 56, 78]
ba = bytearray(byteNumbers)

print(type(ba))

print(ba[0])  # 23
ba[0] = 111  # item assignment is possible

# output:
# 111
# 45
# 56
# 78
for i in ba:
    print(i)

# ba[-2] = 257 # ValueError: byte must be in range(0, 256)


# list data type
print('\nlist data type')
l = []  # representing an emply list
print(type(l))  # <class 'list'>

# Adding objects
l.append(10)
l.append(20)
l.append(30)
l.append(10)  # duplications are allowed
l.append('Priyanjana')  # Hetrogeneous objects are allowed
l.append(None)  # None insertion is possible

print(l)  # [10, 20, 30, 10, 'Priyanjana', None] (Insertion order is preserved)

# accessing with index
print(l[4])  # Priyanjana
print(l[-1])  # None

# accessing with slice operator
print(l[1:5])  # [20, 30, 10, 'Priyanjana'] (1st index to 5-1 index)

# remove function
print(l) # [10, 20, 30, 10, 'Priyanjana', None]
l.remove(10) # the object to be removed should be provided as the argument for remove function
print(l) # [20, 30, 10, 'Priyanjana', None]
