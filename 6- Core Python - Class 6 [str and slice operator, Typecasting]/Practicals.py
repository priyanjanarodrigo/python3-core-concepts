print('Python Program : 6 - Core Python - Class 6')

# Accessing index values
s = 'MYTEXT'

print(s[0])  # output: M
print(s[3])  # output: E
print(s[5])  # output: T
# print(s[6])  # output: IndexError: string index out of range

# Negative indexs (starts with -1)
print(s[-2])  # output: X
print(s[-1])  # output: T
# print(s[-7])  # output: IndexError: string index out of range

# Slice operator and default values - end
# The default value for the end index is end of the string (If we are not specifying explicitly)
print('\nSlice operator and default values')
testString = 'Hello World'
print(testString[2:])  # output:  llo World
print(testString[:4])  # output: Hell
print(testString[:])  # output: Hello World

# Here nothing will be printed because begin index is not lower than end index (-1 is higher than -4). Here Slice operator does not throw exceptions
print(testString[-1:-4])

# This works as begin index is lower than end index (-4 is lower than -1). output: orl
print(testString[-4:-1])


print('\n')
sVal = 'Sample string'
print(sVal[1:10])  # output: ample str
print(sVal[3:])  # output: ple string
print(sVal[:5])  # output: Sampl
print(sVal[:])  # output: Sample string
print(sVal[1:223])  # output: ample string
# print(sVal[100])  # output: IndexError: string index out of range

# output:  (Nothing is displayed as -3 is not lower than -11)
print(sVal[-3:-11])
print(sVal[-11:-3])  # output: mple str
print(sVal[-11:])  # output: mple string
print(sVal[:-3])  # output: Sample str

print('\nSlice operator - step')
myStr = 'durgasoftwaresolutions'

print(myStr[1:10])  # output:  urgasoftw (we will get 1 to 9 characters)
# output: ugsfw (will print and take 2 steps forward (onwards the index))
print(myStr[1:10:2])

# Printing multiple str values easily using repetition operator
print('\nPrinting multiple str values easily using repetition operator')
repStr = 'How are you ? '

# output: How are you ? How are you ? How are you ? How are you ? How are you ?
print(repStr*5)


# len() function which  will return the length of a string
print('\nlen() function')
strValue = 'this is a simple string'

print(len(strValue))  # outout : 23

# char type is not available in Python and even char values are represented with str
print('\nchar type is not available in Python and even char values are represented with str')
myChar = 'a'
print(type(myChar))  # output : <class:str>


print('\n Type casting')

print('\nint() function')
print('float to int : ', int(123.456))  # output: 123

# print('complex to int',int(10+20j)) # output: TypeError: can't convert complex to int (complex is incompatible with int)

print('bool to int : ', int(True))  # output: 1
print('bool to int : ', int(False))  # output: 0

print('str to int : ', int('10'))  # output : 10
print('str to int : ', int('1111'))  # output : 1111

# print('str to int : ',int('0B1111')) # output : ValueError: invalid literal for int() with base 10: '0B1111'(Value must be a Base 10 value)
# print('str to int : ',int('23.45')) # output : ValueError: invalid literal for int() with base 10: '23.45'

print('\nfloat() function')
print('int to float : ',float(10))  # output: 10.0
# print('complex to float : ',float(10+20j))  # output: TypeError: can't convert complex to float
print('bool to float : ',float(True))  # output: 1.0
print('bool to float : ',float(False))  # output: 0.0

print('str to float : ',float('10'))  # output: 10.0
print('str to float : ',float('10.5'))  # output: 10.5
# print('str to float : ',float('ten'))  # output: ValueError: could not convert string to float: 'ten'
# print('str to float : ',float('0B111'))  # output: ValueError: could not convert string to float: '0B111'