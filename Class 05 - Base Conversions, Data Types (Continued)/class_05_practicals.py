print('Class 05 - Base Conversions, Data Types (Continued)\n')

print('Dynamically typed Programming Language - Example ------------------------------------------------------------\n')
# Dynamically typed. The data type of a variable is considered based on the assigned value
x = 10
print(f'type(x) : {type(x)}')  # <class 'int'>

x = True
print(f'type(x) : {type(x)}')  # <class 'bool'>

print('\nBase Conversions ------------------------------------------------------------------------------------------\n')

# bin() function
print('bin() function : ')
x = 2
print(bin(x))  # output: 0b10
print(bin(15))  # output: 0b1111
print(bin(0o777))  # output: 0b111111111
print(bin(0X777))  # output: 0b11101110111

# oct() function
print('\noct() function : ')
print(oct(x))  # output: 0o2
print(oct(100))  # output: 0o144
print(oct(0B101))  # output: 0o5
print(oct(0XBeef))  # output: 0o137357

# hex() function
print('\nhex() function : ')
print(hex(10))  # output:0xa
print(hex(234))  # output:0xea
print(hex(0B111100001))  # output:0x1e1
print(hex(0O765))  # output:0x1f5

# Any to Decimal form
print('\nAny base to Decimal form : ')
value = 0XBeef
print(value)  # output 48879
print(0xface)  # output: 64206
print(0B10)  # output: 2
print(0O72)  # output: 58

# float
print('\nfloat variables -------------------------------------------------------------------------------------------\n')

PI = 3.14
print(PI)

f = 123.456  # VALID (Only decimal base is applicable for float)
print(f)  # output : 123.456

# f = 0B111.011  # INVALID
# f = 0O123.456  # INVALID
# f = 0X123.456  # INVALID

fValue = 1.2e3
print("\nExponential value (1.2e3) :", fValue)  # output: Exponential value (1.2e3) : 1200.0
print(f'Exponential value 12.2e100 : {12.2e100}')

# complex values
print('\ncomplex values with complex data type ---------------------------------------------------------------------\n')

myComplexValue = 2 + 7j
print(f'myComplexValue : {myComplexValue}')  # output: myComplexValue : (2+7j)
print(f'type(myComplexValue) : {type(myComplexValue)}\n')  # output: <class 'complex'>

p = 10 + 20j
print(f'p : {p}')  # Output: p : (10+20j)

q = 10.5 + 2.3j
print(f'q : {q}')  # Output: q : (10.5+2.3j)

# it is mandatory to use j character at the end. Otherwise, it is invalid
# r = 2.5+4y # Invalid

# it is mandatory to adhere to the format as well
# f = 1.2+j20 # Invalid format (format is a+bj)

print('\nReal part can be in any base but imaginary part must be specified only in Decimal: ')

cv1 = 12 + 20j  # Real part is in decimal base
print(cv1)  # output: (12+20j)

# Real part is in binary base
cv2 = 0B1101 + 18j
print(cv2)  # output: (13+18j)

# Real part is in octal base
cv3 = 0O765 + 18j
print(cv3)  # output: (501+18j)

# Real part is in hexadecimal base
cv4 = 0XBeef + 11j
print(cv4)  # output: (48879+11j)

# Real part is in binary base
cv5 = 0B10 + 1.23j
print(cv5)  # output: (2+1.23j)

# This is invalid because imaginary part (b) must be only in decimal base
# cv6 = 12+0B1011j # Invalid - Syntax error
# print(cv6)  # output: (2+1.23j)

print('\nPerforming some mathematical operations with complex types')
l = 10 + 20j
m = 20 + 30j

print(l + m)  # output : (30+50j)
print(l * m)  # output : (-400+700j)
print(l - m)  # output : (-10-10j)
print(l / m)  # output : (0.6153846153846154+0.0769230769230769j)

# Finding the real value of a complex number
print('\nFinding the real and imaginary value of a complex number')

v = 5 + 2j
print(f'v : {v}')  # output: v : (5+2j)

print(f'v.real : {v.real}')  # Output: v.real : 5.0
print(f'v.imag : {v.imag}')  # Output: v.imag : 2.0

# bool data type
print('\nbool data type --------------------------------------------------------------------------------------------\n')

isValid = True
isPermitted = False

print(type(isValid))  # output <class 'bool'>
print(f'isValid : {isValid}')  # Output: isValid : True
print(f'isPermitted : {isPermitted}')  # Output: isPermitted : False

# isValid = true # Invalid syntax (nameError : name true is not defined)
# isValid = false # Invalid syntax (nameError : name true is not defined)
# isValid = 'false' # Invalid  - This is considered as a str (String) value

num1 = 10
num2 = 20

opt1 = num1 < num2
print(f'{num1} < {num2} : {opt1}')  # Output: 10 < 20 :  True

opt2 = num1 > num2
print(f'{num1} > {num2} : {opt2}\n')  # Output: 10 > 20 :  False

# Internal representation of True is 1 and False is 0 (at memory level)
print(f'Internal representation of True (int form of True) : {int(True)}')
print(f'Internal representation of False (int form of False) : {int(False)}\n')

print(f'True + True : {True + True}')  # Output: True + True : 2
print(f'False + False : {False + False}')  # Output: False + False : 0
print(f'True - True : {True - True}')  # Output: True - True : 0
print(f'False + False : {False + False}')  # Output: False + False : 0
print(f'False - True : {False - True}')  # Output: False - True : -1
print(f'False < 4 : {False < 4}')  # Output: False < 4 :  True
print(f'True * False : {True * False}')  # Output: True * False : 0

# str - String data type
print('\nstr data type --------------------------------------------------------------------------------------------\n')

name: str = 'Tobey Maguire'

print(f'name : {name}')  # Output: name : Toby Maguire
print(f'type(name) : {type(name)}')  # Output: <class 'str'>

print('\nMulti line str values:')
myText = '''This is
                a multi line
                str
            value'''

print(f'{myText}\n')
# output of above is :
# This is
#                a multi line
#                str

feedback = '''This "Durga Class Tutorial" is 'really important' for us '''
print(f'feedback : {feedback}')  # Output: feedback : This "Durga Class Tutorial" is 'really important' for us

print('\nslice operator')
phrase = 'This is a small phrase'
print(f'\nphrase : {phrase}')

# Obtaining the characters from 2 to 15 index (includes 2nd index, excludes 15th index / 2 to (15-1))

'''
T  h  i  s     i  s     a     s  m  a  l  l     p  h  r  a  s  e
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21
      |------------------------------------|
'''

print(f'phrase[2:15] : {phrase[2:15]}')  # Output: phrase[2:15] : is is a small
