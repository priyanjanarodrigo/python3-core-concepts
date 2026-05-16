print('Class 04 - Practical - S03 - Data Types\n')

print('print(), type() and id() functions --------------------------------------------------------------------------\n')
piValue = 3.14

print(f'pyValue : {piValue}')  # Prints the value of piValue
print(f'type(piValue) : {type(piValue)}')  # Prints the type of piValue
print(f'id(piValue) : {id(piValue)}')  # Prints the memory address of piValue

print('\nint data type -----------------------------------------------------------------------------------------------')
# int data type

'''
We can represent a number in Python in 4 ways:
    1. Decimal Values
    2. Binary Values
    3. Octal Values
    4. Hexadecimal Values
    
Whenever we use print() just to print a number from any of the above forms (without applying base conversions by using 
bin(), oct(), hex()), Python will print it in decimal format
'''

# 1. Decimal Values
print('\nDecimal Values')
positiveDecimalValue = 1111
negativeDecimalValue = -8900

print(f'Decimal 1111 value : {positiveDecimalValue}')  # output: 1111
print(f'Decimal -8900 value : {negativeDecimalValue}')  # output: -8900

# 2. Binary Values
print('\nBinary Values')
positiveBinaryValue1 = 0b1111
positiveBinaryValue2 = 0B1111
negativeBinaryValue = -0B10

print(f'Binary 0b1111 value : {positiveBinaryValue1}')  # output: 15
print(f'Binary 0B1111 value : {positiveBinaryValue2}')  # output: 15
print(f'Binary -0B10 value : {negativeBinaryValue}')  # output: -2

# 3. Octal Values
print('\nOctal Values')
positiveOctalValue1 = 0O777
positiveOctalValue2 = 0o777
negativeOctalValue = -0o167

print(f'Octal 0O777 value : {positiveOctalValue1}')  # output: 511
print(f'Octal 0o777 value : {positiveOctalValue2}')  # output: 511
print(f'Octal -0o167 value : {negativeOctalValue}')  # output: -119

# 4. Hexadecimal Values
print('\nHexadecimal Values')
# Hexadecimal positive values
positiveHexVal1 = 0xFace
positiveHexVal2 = 0XFace

# Hexadecimal negative values
negativeHexVal = -0xBeef

print(f'Hexadecimal 0xFace value : {positiveHexVal1}')  # output: 64206
print(f'Hexadecimal 0XFace value : {positiveHexVal2}')  # output: 64206
print(f'Hexadecimal -0xBeef value : {negativeHexVal}')  # output: -48879

# Other code examples
print('\nOther code examples -----------------------------------------------------------------------------------------')
isPermitted: bool = 1

print(f'isPermitted: {isPermitted}')

if isPermitted:
    print('isPermitted is True')
else:
    print('isPermitted is False')

isAccessible = 0

if isAccessible:
    print('isAccessible is True')
else:
    print('isAccessible is False')

b = b'Hello'
mv = memoryview(b)
print(mv)
print(mv[0])  # Output: 72 (ASCII value of 'H')
