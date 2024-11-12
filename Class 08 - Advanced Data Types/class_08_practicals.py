print('Class 08 - Advance Date Types')

# bytes data type
print('\nbytes data type -------------------------------------------------------------------------------------------\n')

x = [10, 20, 30, 40]  # Here, x is not the bytes type. This is just a group of values
print('This x is not the bytes type. This is just a group of values')
print(f'x = {x}')  # Output: x = [10, 20, 30, 40]
print(f'type(x) : {type(x)}')  # Output: type(x) : <class 'list'>

print('\nConverting list to bytes type by using bytes(x) function')
b = bytes(x)  # Now this b itself is nothing but bytes data type
print(f'b = {b}')  # Output: b = b'\n\x14\x1e('
print(f'type(b) : {type(b)}')  # Output: type(b) : <class 'bytes'>

print('\nAccessing values with index (positive or negative)')
print(f'b[-1] : {b[-1]}')  # Output: b[-1] : 40
print(f'b[0] : {b[0]}')  # Output: b[0] : 10

print('\nPerforming Slice operator on bytes type')
print(f'b[0:3] : {b[0:3]}')  # Output: b[0:3] : b'\n\x14\x1e'

print('\nIterating over bytes type/ Printing values using a simple for loop')
'''
Output:
    10
    20
    30
    40
'''
# print each byte i in bytes b
for i in b:
    print(i)

'''
The bytes data type can only store integers between 0 and 255 (inclusive) because a byte can only represent 8 bits of 
data (2^8 = 256 possible values)

In the following example, 
    - 100 and 200 are valid values as they are within the range 0-255
    - 256 and 257 are invalid values as they exceed 255

That's why Python raises a ValueError with the message "bytes must be in range(0, 256)

This behavior is consistent with how bytes work in computer memory, where each byte can only store values from 0 to 255.
'''
# numGroup = bytes([100,200,256,257]) # ValueError: bytes must be in range(0, 256)


'''
Immutability

Item assignment is not possible once created
 
The following example raises a TypeError because bytes objects are immutable - once created, their contents cannot be 
changed. This is similar to how strings work in Python.

If you need a mutable sequence of bytes, you can use bytearray instead as the bytearray type allows modification after
creation while maintaining all other properties of bytes
'''
numbers = [2, 4, 6, 8]
myB = bytes(numbers)

# myB[0] = 77 # TypeError: 'bytes' object does not support item assignment ('myB' does not support item assignment)


print('\nbytearray data type ---------------------------------------------------------------------------------------\n')
'''
Both bytes and bytearray are the same except for bytearray is mutable (item assignment after creation is possible)
 
When we need a mutable sequence of bytes, we can use bytearray instead as the bytearray type allows modification after
creation while maintaining all other properties of bytes
'''
byteNumbers = [23, 45, 56, 78]
print(f'byteNumbers = {byteNumbers}')  # Output: byteNumbers = [23, 45, 56, 78]
print(f'type(byteNumbers) : {type(byteNumbers)}')  # Output: type(byteNumbers) : <class 'list'>

print('\nConverting byteNumbers list to bytearray type by using bytearray(byteNumbers) function')
ba = bytearray(byteNumbers)
print(f'ba = {ba}')  # Output: ba = bytearray(b'\x17-8N')
print(f'type(ba) : {type(ba)}')  # Output: type(ba) : <class 'bytearray'>

print('\nAccessing values with index (positive or negative)')
print(f'ba[0] : {ba[0]}')  # Output: ba[0] : 23
print(f'ba[-2] : {ba[-2]}')  # Output: ba[-2] : 56

# Assigning a new value to the 0th index of the bytearray. Modifying the bytearray values after creation is possible
ba[0] = 111
print(f'ba[0] : {ba[0]}')  # Output: ba[0] : 111

print('\nIterating over bytearray type')
'''
Output:
    111
    45
    56
    78
'''
for i in ba:
    print(i)

'''
The bytearray data type can only store integers between 0 and 255 (inclusive)
'''
# ba[-2] = 257 # ValueError: byte must be in range(0, 256)


# list data type
print('\nlist data type --------------------------------------------------------------------------------------------\n')
l = []  # representing an empty list
print(f'l = {l}')  # Output: l = [])
print(f'type(l) : {type(l)}\n')  # Output: type(l) : <class 'list'>

# Appending values to the list
l.append(10)
l.append(20)
l.append(30)
l.append(10)  # duplications are allowed
l.append('Hello')  # Hetrogeneous objects are allowed
l.append(None)  # None insertion is possible

print(f' l = {l}')  # [10, 20, 30, 10, 'Hello', None] (Insertion order is preserved, Heterogeneous objects are allowed)

print('\nAccessing values with index (positive or negative)')
print(f'l[4] = {l[4]}')  # Output: l[4] = Hello
print(f'l[-1] = {l[-1]}')  # Output: l[-1] = None

print('\nAccessing values with slice operator')
print(f'l[1:5] : {l[1:5]}')  # Output: l[1:5] : [20, 30, 10, 'Hello'] (1st index to 5-1 index)

# remove function
print(f'\nl = {l}')  # Output: l = [10, 20, 30, 10, 'Hello', None]
'''
the object to be removed should be provided as the argument for remove function

In this case the first occurrence of the value 10 is removed from the list
'''
print('removing 10 from the list with l.remove(10)')
l.remove(10)
print(f'l = {l}')  # Output: l = [20, 30, 10, 'Hello', None]
