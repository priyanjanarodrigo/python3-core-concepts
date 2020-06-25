import keyword
print('Python Program : 4 - Core Python - Class 4')


def display(message):
    print(message)


display('Hello Python')

# a=true is not valid
a = True
print(a)

# b=true is not valid.
b = None
print(b)

# Displaying all the available keywords
print(keyword.kwlist)

print(type(a))
print(id(a))

# int data type
# Decimal Values
value1 = 1111
print(value1)  # output - 1111

# Binary Values
myNumber = 0b1111
mySecondNumber = 0B1111

print(myNumber)  # output - 15
print(mySecondNumber)  # output - 15

# Octal Values
ocatlVal = 0O777
octalVal2 = -0o167

print(ocatlVal)  # output is:511
print(octalVal2)  # output is:-119

# Hexadecimal possitive values
hexVal = 0xFace

# Hexadecimal negative values
hexVal2 = -0xBeef

print(hexVal)  # output is:64206
print(hexVal2)  # output is:-48879
