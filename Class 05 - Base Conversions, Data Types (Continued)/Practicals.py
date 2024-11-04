print('Python Program : 5 - Core Python - Class 5')

# Dynamically typed. Data type of a variable is considered based on the assigned value
x = 10
print(type(x))  # <class 'int'>

x = True
print(type(x))  # <class 'bool'>

# Base convertions ----------------------------------------------------

# bin() function
print('\nbin() function : ')
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
print('\nfloat variables : ')
PI = 3.14
print(PI)

f = 123.456   # VALID (Only decimal base is applicable for float)
print(f)  # output : 123.456

# f = 0B111.011  # INVALID
# f = 0O123.456  # INVALID
# f = 0X123.456  # INVALID

fValue = 1.2e3

# output: Representing exponentials (1.2e3) : 1200.0
print("\nRepresenting exponentials (1.2e3) :", fValue)

print(12.2e100)

# complex values
print('\ncomplex values with complex data type')
p = 10+20j
print(p)  # output: (10+20j)

q = 10.5+2.3j
print(q)  # output : (10.5+2.3j)

# it is mandatory to use j character at the end. Otherwise it is invalid
# r = 2.5+4y

# it is mandatory to adere to the format as well
# f = 1.2+j20 # Invalid format (format is a+bj)

print('\nReal part in any format: ')
cv1 = 12+20j
print(cv1)  # output: (12+20j)

cv2 = 0B1101+18j
print(cv2)  # output: (13+18j)

cv3 = 0O765+18j
print(cv3)  # output: (501+18j)

cv4 = 0XBeef+11j
print(cv4)  # output: (48879+11j)

cv5 = 0B10+1.23j
print(cv5)  # output: (2+1.23j)

# This is invalid because imaginary part (b) must be only in decimal base
# cv6 = 12+0B1011j # Invalid - Syntax error
# print(cv6)  # output: (2+1.23j)

print('\nPerforming some mathematical operations with complex types')
l = 10+20j
m = 20+30j

print(l+m)  # output : (30+50j)
print(l*m)  # output : (-400+700j)
print(l-m)  # output : (-10-10j)
print(l/m)  # output : (0.6153846153846154+0.0769230769230769j)

# Finding the real value of a complex number
print('\nFinding the real and imaginary value of a complex number')
v = 5+2j

print(v.real)  # output: 5.0
print(v.imag)  # output: 2.0

# bool data type
print('\nbool data type')
isValid = True
isPermitted = False

print(type(isValid))  # output <class 'bool'>
print(isValid)  # output: True
print(isPermitted)  # output: False

# isValid = true # Invalid syntax (nameError : name true is not defined)
# isValid = false # Invalid syntax (nameError : name true is not defined)
# isValid = 'false' # Invalid  - This is considered as a str (String) value

num1 = 10
num2 = 20

opt1 = num1 < num2
print('opt1 : ', opt1)  # output: opt1 :  True

opt2 = num1 > num2
print('opt2 : ', opt2)  # output: opt2 :  False

# Internal representation of True is 1 and False is 0
print(True+True)  # output: 2
print(False+False)  # output: 0
print(True-True)  # output: 0
print(False+False)  # output: 0
print(False-True)  # output: -1
print(False < 4)  # output: False
print(True*False)  # output: 0


# str - String data type
print('/n str data type')
name = 'Toby Maguire'
print(type(name))  # output: <class 'str'>
print(name)  # output: Toby Maguire

print('\nMulti line str values:')
myText = '''This is
                a multi line
                str'''

print(myText)
# output of above is :
# This is
#                a multi line
#                str

feedback = '''This "Durga Class Tutorial" is 'really important' for us '''
print(feedback) # output: This "Durga Class Tutorial" is 'really important' for us

phrase='This is a small phrase'
# Obtaining the characters from 2 to 15 index (includes 2nd index, excludes 15th index / 2 to (15-1))
print(phrase[2:15]) # output: is is a small