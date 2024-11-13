print('Class 09 - Advance Date Types (Continued)')

from collections import defaultdict

# Recap from last sessions ------------------------------------------------------------------------------
# bytes data type - bytes is immutable, only allowed values are 0 to 256
myTestList = [1, 2, 3, 22, 3]
print(f'myTestList : {myTestList}')
b = bytes(myTestList)

print('\nDisplaying bytes b :')
for i in b:
    print(i)

# bytearray data type - bytearray is mutable
mySecondTestList: list = [12, 43, 56, 87, 56, 34]
btArr = bytearray(mySecondTestList)
btArr.append(88)
btArr.remove(12)
btArr.remove(56)

print('\nDisplaying btArr bytesArray :')
for i in btArr:
    print(i)

# list data type - list is mutable, insertion order is preserved, heterogeneous objects are allowed
myList: list = [23, 345, 76, 8987, 78, 4535534, 45, None, 12.2, False, 10 + 2j]
myList.append(11)
myList.remove(4535534)

print('\nDisplaying myList list (Original order) :', myList)
myList.reverse()  # Reversing myList
print('Displaying myList list (Reverse order) :', myList, '\n')

# Usage if star (*) as the repetition operator with list
l1 = [10, None, True, 'Priyanjana']
l2 = l1 * 2

print('Using * operator :')
print(f'l1 = {l1}')  # Output: l1 = [10, None, True, 'Priyanjana']

print('\nMultiplied l2 list (l2 = l1 * 2)')
print(f'l2 = {l2}')  # Output: l2 = [10, None, True, 'Priyanjana', 10, None, True, 'Priyanjana']
print(f'type(l2) : {type(l2)}')  # Output: type(l2) : <class 'list'>

# tuple data type - By using parenthesis we can represent a tuple
print('\ntuple data type -------------------------------------------------------------------------------------------\n')
t: tuple = (12, 43, None, 56, False)  # This is a tuple
l: list = [2, 3, 5, 7, 8]  # This is a list

print(f't = {t}')  # Output: t = (12, 43, None, 56, False)

# Accessing with index (positive and negative)
print(f't[0] = {t[0]}')  # Output: t[0] = 12
print(f't[-3] = {t[-3]}\n')  # Output : t[-3] = None

# Using slice operator
print(f't[0: 3] : {t[0: 3]}\n')  # Output: t[0: 3] : (12, 43, None)

# Below line will not work as tuple is immutable
# t[0]=100 # TypeError: 'tuple' object does not support item assignment

print('Executing t1 = t * 2')
t1 = t * 2
print(f't1 = {t1}')  # Output: t1 = (12, 43, None, 56, False, 12, 43, None, 56, False)

# Consider following scenario. It is a tuple which consists of three objects. First two are int values and the other
# one is a list inside the tuple
t3 = (10, 20, [2, 6])
print(f't3 = {t3}')  # Output: t3 = (10, 20, [2, 6])

# range data type
print('\nrange data type -------------------------------------------------------------------------------------------\n')
print('Form 1 - range(end) function')

# Represents values from 0 to 9 (0 to end-1) but not 10
r = range(10)
print(f'r = {r}')  # Output: r = range(0, 10)
print(f'type(r) = {type(r)}\n')  # Output: type(r) = <class 'range'>

'''
Displaying the values (Output)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
'''
for i in r:
    print(i)

# Accessing with index
print('\nAccessing with index : ')
print(f'r[4] = {r[4]}')  # Output: r[4] = 4
print(f'r[-3] = {r[-3]}\n')  # Output: r[-3] = 7

# slice operator
print(f'r[0:3] : {r[0:3]}')  # Output : r[0:3] : range(0, 3)

print('\nUsing slice operator')
# Printing with the help of slice operator
# 0
# 1
for i in r[0:2]:
    print(i)

# Immutability is not applicable as item assignment is not supported
# r[2] = 700 # TypeError: 'range' object does not support item assignment


# Form 2 - range(start, end)
print('\nForm 2 - range(start,end) function')
r2 = range(10, 31)
print(f'r2 = {r2}')  # Output: r2 = range(10, 31)

# Following will print numbers from 10 to 30
for i in r2:
    print(i)

print('\nForm 3 - range(start,end,step) function')
r3 = range(10, 31, 5)
print(f'r3 = {r3}')  # Output: r3 = range(10, 31, 5)

'''
Output:
    10
    15
    20
    25
    30
'''
for i in r3:
    print(i)

# Range is not applicable for float objects
# r4 = range(1.2,2.9) # TypeError: 'float' object cannot be interpreted as an integer


# set data type
print('\nset data type ---------------------------------------------------------------------------------------------\n')
s = {10, 20, 30, 10, 20, 30, None, 'Hello', None}
# Duplicates will be ignored and only unique values will be added
print(f's = {s}\n')  # Output: s = {10, None, 20, 'Hello', 30}

# Cannot access via elements or perform slice as there is no guarantee about the index position of elements
# print(s[0]) # TypeError: 'set' object is not subscriptable
# print(s[1:]) # TypeError: 'set' object is not subscriptable

# Set is mutable so we can change the content
s.add('New Value')
s.remove(None)
print(f's = {s}')  # Output: s = {10, 20, 'New Value', 'Hello', 30}

print('\nCoding practise examples  :')
s2 = set({})  # Initializing a blank set
print(f's2 = {s2}')  # Output: s2 = set()
print(f'type(s2) = {type(s2)}\n')  # Output: type(s2) = <class 'set'>

testList = list([])  # Initializing a blank list (Just as an example)
print(f'testList = {testList}\n')  # Output: testList = []

# testTuple = tuple(())  # Initializing a blank tuple # N/A
testTuple = tuple(())
print(f'testTuple = {testTuple}')  # Output: testTuple = ()

for i in range(5):
    s2.add(i)

s2.add('Priyanjana')
s2.add(None)
s2.add('Rodrigo')

print(f's2 = {s2}')  # Output: s2 = {0, 1, 2, 3, 4, 'Priyanjana', None, 'Rodrigo'})

# frozenset data type
print('\nfrozenset data type ---------------------------------------------------------------------------------------\n')

s = (10, 20, 30, 40)  # Initializing a set
fs = frozenset(s)  # Assigning available values to a frozenset
print(f'fs = {fs}')  # Output: fs = frozenset({40, 10, 20, 30})

# Following operation is not applicable as frozenset is immutable
# fs.add(50) # AttributeError: 'frozenset' object has no attribute 'add'

# dict data type
print('\ndict data type --------------------------------------------------------------------------------------------\n')

# Setting key->value pairs
dc = {100: 'Priyanjana', 200: 'Rodrigo', 'Other': 'Michal', None: 'No value'}
print(f'dc = {dc}')  # Output: dc = {100: 'Priyanjana', 200: 'Rodrigo', 'Other': 'Michal', None: 'No value'}
print(f'type(dc) = {type(dc)}\n')  # Output: type(dc) = <class 'dict'>

# Initializing an empty dictionary. This declaration is by default treated as a dict type BUT NOT set
dc2 = {}
print(f'dc2 = {dc2}')  # Output: dc2 = {}
print(f'type(dc2) = {type(dc2)}')  # Output: type(dc2) = <class 'dict'>

# Approach - dc2[KEY] = VALUE
dc2[100] = 'Bean'
dc2['isAvailable'] = False
dc2[True] = 123

print(f'dc2 = {dc2}')  # Output: dc2 = {100: 'Bean', 'isAvailable': False, True: 123}

dc2[100] = 'Michal'
print(f'dc2 = {dc2}\n')  # Output: dc2 = {100: 'Michal', 'isAvailable': False, True: 123}

# Initializing an empty set
mySet = set()
print(f'mySet = {mySet}')  # Output: mySet = set()
print(f'type(mySet) = {type(mySet)}')  # Output: type(mySet) = <class 'set'>

# defaultdict data type ---------------------------------------------------------------------------------------------
print('\ndefaultdict data type', end='\n')


def count_occurrences(numbers: list):
    counter = defaultdict(int)

    for num in numbers:
        counter[num] += 1

    print(counter)


numbersList: list = [1, 2, 3, 2, 1, 3, 2, 4, 5, 2, 1, 4]
count_occurrences(numbersList)
