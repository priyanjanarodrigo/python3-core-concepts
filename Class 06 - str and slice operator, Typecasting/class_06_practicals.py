print('Class 06 - str and slice operator, Typecasting\n')

print('\nstr data type - Continuation ------------------------------------------------------------------------------\n')

print('Accessing index values - Positive and Negative indexes ------------------------------------------------------\n')
# Accessing index values
s = 'MYTEXT'

'''
 <------ Negative indexes
 
 -6  -5  -4  -3  -2  -1
_________________________
| M | Y | T | E | X | T |
-------------------------
  0   1   2   3   4   5
  
 Positive indexes ------->
'''

print(f's : {s}')  # Output: s : MYTEXT

print('\nPositive indexes (starts with 0)')
print(f's[0] : {s[0]}')  # Output: s[0] : M
print(f's[3] : {s[3]}')  # Output: s[3] : E
print(f's[5] : {s[5]}')  # Output: s[5] : T
# print(s[6])  # output: IndexError: string index out of range

# Negative indexes (starts with -1)
print('\nNegative indexes (starts with -1)')
print(f's[-2] : {s[-2]}')  # Output: s[-2] : X
print(f's[-1] : {s[-1]}')  # Output: s[-1] : T
# print(s[-7])  # output: IndexError: string index out of range


print('\nslice operator examples')
text = 'Python'
print(f'text : {text}')  # Output: text : python
print(f'text[1:4] : {text[1:4]}')  # Output: text[1:4] : yth

# Even if the end index is greater than the length of the string, it will not throw any exception and will print the string till the end
print(f'text[1:6] : {text[1:6]}')  # Output: text[1:6] : ython
print(f'text[1:7] : {text[1:7]}')  # Output: text[1:7] : ython

print('\nSlice operator and default values -------------------------------------------------------------------------\n')

testString = 'Hello World'

print(f'testString : {testString}\n')  # Output: testString : Hello World

# end index is not specified, so the default value for the end index is end of the string
print(f'testString[2:] : {testString[2:]}')  # Output: testString[2:] : llo World

# begin index is not specified, so the default value for the begin index is 0
print(f'testString[:4] : {testString[:4]}\n')  # Output: testString[:4] : Hell

# If both begin and end index are not specified, then the default value for both begin and end index is 0 and end of the string respectively
print(f'testString[:] : {testString[:]}')  # Output: testString[:] : Hello World

# Here nothing will be printed because begin index is not lower than end index (-1 is higher than -4). Here Slice operator does not throw exceptions
print('\nHere nothing will be printed because begin index is not lower than end index (-1 is higher than -4). '
      'Slice operator does not throw exceptions here')
print(f'testString[-1:-4] : {testString[-1:-4]}\n')  # Output: testString[-1:-4] :

'''
This works as begin index is lower than end index (-4 is lower than -1). output: orl
On the following line, negative indexes are used to access the characters from the end of the string

begin value should be lower than end index
'''
print('This works as begin index is lower than end index (-4 is lower than -1). output: orl. '
      'On the following line, negative indexes are used to access the characters from the end of the string')
print(f'testString[-4:-1] : {testString[-4:-1]}\n')  # Output: testString[-4:-1] : orl

sVal = 'Sample string'
print(f'sVal : {sVal}\n')  # Output: sVal : Sample string
print(f'sVal[1:10] : {sVal[1:10]}')  # Output: sVal[1:10] : ample str
print(f'sVal[3:] : {sVal[3:]}')  # Output: sVal[3:] : ple string
print(f'sVal[:5] : {sVal[:5]}')  # Output: sVal[:5] : Sampl
print(f'sVal[:] : {sVal[:]}')  # Output: sVal[:] : Sample string
print(f'sVal[1:223] : {sVal[1:223]}\n')  # Output: sVal[1:223] : ample string
# print(sVal[100])  # output: IndexError: string index out of range

print('Nothing is displayed as -3 is not lower than -11')
print(f'sVal[-3:-11] : {sVal[-3:-11]}\n')  # Output: sVal[-3:-11] :

print(f'sVal[-11:-3] : {sVal[-11:-3]}')  # Output: sVal[-11:-3] : mple str
print(f'sVal[-11:] : {sVal[-11:]}')  # Output: sVal[-11:] : mple string
print(f'sVal[:-3] : {sVal[:-3]}')  # Output: sVal[:-3] : Sample str

print('\nSlice Operator - Step -------------------------------------------------------------------------------------\n')

'''
Syntax : string[begin:end:step]
'''

myStr = 'durgasoftwaresolutions'

print(f'myStr : {myStr}')  # Output: myStr : durgasoftwaresolutions

# We will get 1 to 9 characters
print(f'myStr[1:10] : {myStr[1:10]}\n')  # Output : myStr[1:10] : urgasoftw

# prints characters from 1 to 10-1, stepping 2 indexes forward
explanation = '''
    _________________________________________________________________________________________
    | d | u | r | g | a | s | o | f | t | w | a | r | e | s | o | l | u | t | i | o | n | s |
    -----------------------------------------------------------------------------------------
      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21 
        
        _____________________________________
        | u | r | g | a | s | o | f | t | w |
        -------------------------------------
          1   2   3   4   5   6   7   8   9     
          
          ^       ^       ^        ^       ^
          |.......|.......|........|.......|
          Stepping 2 indexes forward
          
            ______________________
            | u | g | s | f | w |
            ----------------------
              1   3   5   7   9 
              
              Final output: ugsfw
'''

print(f'myStr[1:10:2] : {myStr[1:10:2]}')  # Output : myStr[1:10:2] : ugsfw
print(f'{explanation}')

# Printing multiple str values easily using repetition operator
print('\nPrinting multiple str values easily using repetition operator ---------------------------------------------\n')
repStr = 'How are you ? '

# output: How are you ? How are you ? How are you ? How are you ? How are you ?
print(repStr * 5)

# len() function which  will return the length of a string
print('\nlen() function --------------------------------------------------------------------------------------------\n')
strValue = 'this is a simple string'
print(f'strValue : {strValue}')  # Output: strValue : this is a simple string
print(f'len(strValue) : {len(strValue)}')  # Output: len(strValue) : 23

# char type is not available in Python and even char values are represented with str
print('\nchar type is not available in Python and even char values are represented with str')
myChar = 'a'
print(type(myChar))  # output : <class:str>

print('\nType casting/ Type Coercion -------------------------------------------------------------------------------\n')

print('int() function -------------------------- \n')

print('float to int - int(123.456) : ', int(123.456))  # Output: float to int - int(123.456) : 123

# print('complex to int',int(10+20j)) # output: TypeError: can't convert complex to int (complex is incompatible with int)

print('\nbool to int - int(True) : ', int(True))  # Output: bool to int - int(True) : 1
print('bool to int - int(False) : ', int(False))  # Output: bool to int - int(False) :  0

print("\nstr to int - int('10') : ", int('10'))  # Output: str to int - int('10') :  10
print("str to int - int('1500') : ", int('1500'))  # Output: str to int - int('1500') :  1500

# print('str to int : ',int('0B1111')) # output : ValueError: invalid literal for int() with base 10: '0B1111'(Value must be a Base 10 value)
# print('str to int : ',int('23.45')) # output : ValueError: invalid literal for int() with base 10: '23.45'

print('\nfloat() function -------------------------')
print('\nint to float - float(10) : ', float(10))  # Output: int to float - float(10) :  10.0

# print('complex to float : ',float(10+20j))  # output: TypeError: can't convert complex to float

# True is interpreted as 1 and False is interpreted as 0
print('\nbool to float - float(True) : ', float(True))  # Output: bool to float - float(True) :  1.0
print('bool to float - float(False) : ', float(False))  # Output: bool to float - float(False) :  0.0

print("\nstr to float - float('10') : ", float('10'))  # Output: str to float - float('10') :  10.0
print("str to float - float('10.5') :  ", float('10.5'))  # Output: str to float - float('10.5') :  10.5

# print('str to float : ',float('ten'))  # output: ValueError: could not convert string to float: 'ten'
# print('str to float : ',float('0B111'))  # output: ValueError: could not convert string to float: '0B111'
