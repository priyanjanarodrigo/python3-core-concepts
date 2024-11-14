print('\nClass 11 - Operators - Relational Operators\n')

'''
========================================================================================================================
* Operators
========================================================================================================================

Operators are used to perform operations on variables and values. Python has the following operators:

    1. Arithmetic Operators
    2. Relational Operators or Comparison Operators
    3. Logical Operators
    4. Bitwise Operators
    5. Assignment Operators
    6. Special Operators
    

1. Arithmetic Operators
-------------------------
Arithmetic operators are used with numeric values to perform common mathematical operations.

    +	Addition	                x + y	
    -	Subtraction	                x - y	
    *	Multiplication	            x * y	
    /	Division	                x / y	
    %	Modulus/ Modulo             x % y	
    //	Floor Division	            x // y
    **	Exponentiation/ Exponent	x ** y
'''

print('1. Arithmetic Operators -------------------------------------------------------------------------------------\n')

a = 10
b = 3
print(f'a = {a} and b = {b}\n')  # Output: a = 10 and b = 2

'''
 1.1 Addition operator (+)
 =========================
 
 The addition operator (+) is used to add two operands.
'''
print(f'a + b = {a + b}')  # Output: a + b = 13

'''
 1.2 Subtraction operator (-)
 ============================
 
 The subtraction operator (-) is used to subtract the second operand from the first operand.
'''
print(f'a - b = {a - b}')  # Output: a - b = 7

'''
 1.3 Multiplication operator (*)
 ===============================
 
 The multiplication operator (*) is used to multiply two operands.
'''
print(f'\na * b = {a * b}')  # Output: a * b = 30

'''
 1.4 Division operator (/)
 =========================

 Returns the quotient (including the digits after the decimal point also) when one operand is divided by the other. 

 Division operator will always return a float value (Division operator always works on floating point arithmetic).
 (ex : 10 / 2 = 5.0)
'''
print(f'\na / b = {a / b}')  # Output: a / b = 3.333333333333333
print(f'20.5 / 2 = {20.5 / 2}')  # Output: 20.5 / 2 = 10.25

print(f'\na % b = {a % b}')  # Output: a % b = 1

'''
 1.5 Modulo operator (%)
 =======================
 
 The modulo operator returns the remainder when the first operand (dividend) is divided by the second operand (divisor).
'''
print(f'\na % b = {a % b}')  # Output: a % b = 1

'''
 1.6 Floor Division operator (//)
 ================================
 
 The division of operands where the result is the quotient in which the digits after the decimal point are discarded.
 The result is always floored to the nearest lower integer value. (floor - before the nearest number)

 * IMPORTANT !!

 - If both the arguments are int, the result will be an integer (discarding the digits after the decimal point).
   
 - If at least one of the arguments is a float, the result will be a float but the digits after the decimal point 
   will be discarded. (Nearest integer value as a float value where the digits after the decimal point are discarded)
   
 - Depending on the arguments, the floor division may return an integer or a float value. (If we desperately want to get
   the int value, we can use typecasting int(a // b))
'''
print(f'\na // b = {a // b}')  # Output: a // b = 3
print(f'20.5 // 2 = {20.5 // 2}')  # Output: 20.5 // 2 = 10.0

'''
 1.7 Exponentiation operator (**)
 ================================
 
 The exponentiation operator raises the first operand to the power of the second operand.
'''
print(f'\na ** b = {a ** b}')  # Output: a ** b = 1000 (10 to the power of 3)

print(f'\n10 ** -3 = {10 ** -3}')  # Output: 10 ** -3 = 0.001 (10 to the power of -3)

print(f'4+23j ** 2+10j = {4 + 23J ** 2 + 10j}')  # Output: 4+23J ** 2+10j = (-525+10j)

print(f'10+2j ** 10+3j = {10 + 2j ** 10 + 3j}')  # Output: 4+23J ** 2+10j = (-1014+3j)

# Power of 0 of any number is 1
print(f'10 ** 0 = {10 ** 0}')  # Output: 10 ** 0 = 1

'''
 More about + operator
 ======================

 + operator is applicable for str type also. This is called concatenation.
 
 If we want to apply + operator for str arguments, both the arguments must be of str type only. Otherwise, we will get
 a TypeError: can only concatenate str (not "int") to str.
'''

print('\nString concatenation with + operator')

print("'Hello' + ' ' + 'World' = ", 'Hello' + ' ' + 'World\n')  # Output: Hello World

# print('Hello' + 10) # TypeError: can only concatenate str (not "int") to str

'''
 More about - operator
 ======================
 
 Minus (-) Operator is not applicable for str. If we try to apply - operator for str, we will get a 
 TypeError: unsupported operand type(s) for -: 'str' and 'str'
'''
# print('hello world'-'hello') # TypeError: unsupported operand type(s) for -: 'str' and 'str'


'''
 More about * operator
 ======================

 * operator is applicable for str type also. This is called repetition.
 
 If we try to apply * operator for str arguments and the both the arguments are str type only, we will get a
 TypeError: can't multiply sequence by non-int of type 'str'.
 
 To perform repetition with * operator on strings, one argument must be a str and the other argument must be an int.
 If we are taking a non-int value as the second argument, we will get a TypeError: can't multiply sequence by non-int
 
 As long as one argument is int and the other argument is str, we can perform repetition with * operator and the order 
 of them does not matter.(either str or int can be the first argument)
'''

print('\'hello_all\' * 3 = ', 'hello_all' * 3)  # Output: 'hello_all' * 3 =  hello_allhello_allhello_all

print('2 * \'hi\' = ', 2 * 'hi')  # Output: 2 * 'hi' =  hihi

# print('test' * '2') # TypeError: can't multiply sequence by non-int of type 'str'

# print(2.4 * 'hi')  # TypeError: can't multiply sequence by non-int of type 'float'

# print(2.0 * 'hi')  # TypeError: can't multiply sequence by non-int of type 'float'


'''
 Some other important points about division (/) operator, floor division (//) and modulo (%) operator
 ====================================================================================================

 If we try to perform division, floor division or modulo on any number by 0, we will get a ZeroDivisionError.
'''

'''
Division by 0 (int and float examples)
'''
# print(f'10 / 0 = {10 / 0}')  # Output: ZeroDivisionError: division by zero

# print(f'10.5/0 = {10.5 / 0}')  # Output: ZeroDivisionError: float division by zero


'''
Modulo by 0 (int and float examples)
'''
# print(f'10 % 0 = {10 % 0}')  # Output: ZeroDivisionError: integer modulo by zero

# print(f'22.13 % 0 = {22.13 % 0}') # ZeroDivisionError: float modulo


'''
Floor division by 0 (int and float examples)
'''
# print(f'10 // 0 = {10 // 0}')  # Output: ZeroDivisionError: integer division or modulo by zero

# print(f'32.3 // 0 = {32.3 // 0}')  # Output: ZeroDivisionError: float floor division by zero


'''
2. Relational Operators
-------------------------
Relational operators are used for comparing the values. It either returns True or False according to the condition.

* Equality operators:
    1) ==	Equal to	                x == y
    2) !=	Not equal to	            x != y
    
* Relational operators:
    3) >	Greater than	            x > y
    4) <	Less than	                x < y
    5) >=	Greater than or equal to	x >= y
    6) <=	Less than or equal to	    x <= y
'''

print('\n* Relational Operators -----------------------------------------------------------------------------------\n')

'''
Behaviour of relational operators with respect to int and float
----------------------------------------------------------------
'''
print('Behaviour of relational operators with respect to int and float\n')

'''
Equal to (==) operator
'''
print(f'10.55 == 10.55 : {10.55 == 10.55}')  # Output: 10.55 == 10.55 : True
print(f'12 == 13 : {12 == 13}\n')  # Output: 10.55 == 10.55 : True

'''
Not equal to (!=) operator
'''
print(f'4 != 4 : {4 != 4}')  # Output: 4 != 4 : False
print(f'54.33 != 23.32 : {54.33 != 23.32}\n')  # Output: 54.33 != 23.32 : True

'''
Greater than (>) operator
'''
print(f'10 > 10 : {10 > 10}')  # Output: 10 > 10 : False
print(f'102.32 > 88.5 : {102.32 > 88.5}\n')  # Output: 102.32 > 88.5 : True

'''
Less than (<) operator
'''
print(f'2 < 43 : {2 < 43}')  # Output: 2 < 43 : True
print(f'99.99 < 100.01 : {99.99 < 100.01}\n')  # Output: 99.99 < 100.01 : True

'''
Greater than or equal to (>=) operator
'''
print(f'10 >= 10 : {10 >= 10}')  # Output: 10 >= 10 : True
print(f'89.23 >= 20.06 : {89.23 >= 20.06}\n')  # Output: 89.23 >= 20.06 : True

'''
Less than or equal to (<=) operator
'''
print(f'2 <= 4 : {2 <= 4}')  # Output: 2 <= 4 : True
print(f'100 <= 80 : {100 <= 80}\n')  # Output: 100 <= 80 : False

'''
Behaviour of relational operators with respect to str

Relational operators are applicable for str type and it compares the ASCII values of the characters in the strings.
(Basically the alphabetical order of the characters)

This means that strings are compared character by character from left to right, using the Unicode code points of each 
character Here’s a breakdown of how these operations work:

 1.	Lexicographic Order:
 
    • When comparing two strings, Python starts with the first character of each string.
    • If the characters are the same, it moves to the next character in each string and continues this until it finds
      a character that differs or reaches the end of one of the strings.
    • For example, "apple" < "banana" because 'a' (in "apple") comes before 'b' (in "banana").

 2.	Case Sensitivity:
 
	• String comparisons in Python are case-sensitive. Uppercase letters come before lowercase letters in Unicode, 
	  so "Apple" < "apple" returns True because 'A' has a lower Unicode value than 'a'.
	
 3.	String Length:
	• If one string is a prefix of another, the shorter string is considered smaller. For example, "app" < "apple" 
	  returns True because "app" is a prefix of "apple" and is shorter.
	
 4.	Equality Check (==, !=):
	• Strings are equal if and only if they have the exact same characters in the exact same order.
	• For instance, "apple" == "apple" returns True, while "apple" != "Apple" also returns True due to case 
	  sensitivity.

'''
print('Behaviour of relational operators with respect to str\n')

'''
Equal to (==) operator
'''
print(f"'apple' == 'banana' : {'apple' == 'banana'}")  # Output: 'apple' == 'banana' : False
print(f"'apple' == 'apple' : {'apple' == 'apple'}")  # Output: 'apple' == 'apple' : True

# Unicode values: A = 65 and a = 97
print(f"'apple' == 'Apple' : {'apple' == 'Apple'}\n")  # Output: 'apple' == 'Apple' : False

'''
Not equal to (!=) operator
'''
print(f"'apple' != 'banana' : {'apple' != 'banana'}")  # Output: 'apple' != 'banana' : True
print(f"'apple' != 'apple' : {'apple' != 'apple'}\n")  # Output: 'apple' != 'apple' : False

'''
Greater than (>) operator
'''
print(f"'apple' > 'banana' : {'apple' > 'banana'}")  # Output: 'apple' > 'banana' : False
print(f"'apple' > 'apple' : {'apple' > 'apple'}\n")  # Output: 'apple' > 'apple' : False

# Unicode values: A = 65 and a = 97
print(f"'apple' > 'Apple' : {'apple' > 'Apple'}\n")  # Output: 'apple' > 'Apple' : False

'''
Greater than or equal to (>=) operator
'''
print(f"'apple' >= 'apple' : {'apple' >= 'apple'}")  # Output: 'apple' >= 'apple' : True
print(f"'apple' >= 'banana' : {'apple' >= 'banana'}\n")  # Output: 'apple' >= 'banana' : False

'''
Less than (<) operator
'''
print(f"'apple' < 'banana' : {'apple' < 'banana'}")  # Output: 'apple' < 'banana' : True
print(f"'apple' < 'apple' : {'apple' < 'apple'}\n")  # Output: 'apple' < 'apple' : False

'''
Less than or equal to (<=) operator
'''
print(f"'apple' <= 'apple' : {'apple' <= 'apple'}")  # Output: 'apple' <= 'apple' : True
print(f"'apple' <= 'banana' : {'apple' <= 'banana'}\n")  # Output: 'apple' <= 'banana' : True

'''
Behaviour of relational operators with respect to bool

True is interpreted as 1 and False is interpreted as 0, therefore the comparison is done based on the internal numerical
values.
'''

print('Behaviour of relational operators with respect to bool\n')

print(f'True == False : {True == False}')  # Output: True == False : False
print(f'True != False : {True != False}')  # Output: True != False : True
print(f'True > False : {True > False}')  # Output: True > False : True
print(f'True >= False : {True >= False}')  # Output: True >= False : True
print(f'True < False : {True < False}')  # Output: True < False : False
print(f'True <= False : {True <= False}\n')  # Output: True <= False : False

'''
Boolean and str comparing related important points:
'''

print(f'True == \'Hello\' : {True == 'Hello'}')  # Output: True == 'Hello' : False
print(f'True == \'True\' : {True == 'True'}')  # Output: True == 'True' : False
print(f'False == \'False\' : {False == 'False'}\n')  # Output: True == 'True' : False

# print(f'\'Hello\' > False : {"Hello" > False}')  # Output: TypeError: '>' not supported between instances of 'str' and 'bool'
# print(f'\'Hello\' >= False : {"Hello" >= False}')  # Output: TypeError: '>' not supported between instances of 'str' and 'bool'
# print(f'\'Hello\' < True : {"Hello" < True}')  # Output: TypeError: '>' not supported between instances of 'str' and 'bool'
# print(f'\'Hello\' <= True : {"Hello" <= True}')  # Output: TypeError: '>' not supported between instances of 'str' and 'bool'


'''
Chaining of relational operators:
---------------------------------
 - In Python, we can chain multiple relational operators together. 
 
 - Consider what might happen when we do a comparison like the following ?
  
    10 < 20 < 30 < 40

 - if all the comparisons are true, then the entire expression is true.

 - If at least one of the comparisons is false, then the entire expression is false.
 
 - The chaining comparison is performed from left to right. Which means:
    
    10 < 20 < 30 < 40 is equivalent to (10 < 20) and (20 < 30) and (30 < 40)

 - Comparison steps:

     1. On the first comparison, 10 is less than 20, so the expression is true.
     2. On the second comparison, 20 is less than 30, so the expression is true.
     3. On the third comparison, 30 is less than 40, so the expression is true.
     
     * Therefore, the entire expression 10 < 20 < 30 < 40 is true.
'''

print(f'10 < 20 < 30 < 40 : {10 < 20 < 30 < 40}')  # Output: 10 < 20 < 30 < 40 : True

'''
 The following chaining comparison can be thought of as 10 < 20 and 20 > 30 and 30 < 40

 - Comparison steps:
    
    1. On the first comparison, 10 is less than 20, so the expression is true.
    2. On the second comparison, 20 > 30 is false, so the expression is false.
 
    * Therefore, the entire expression 10 < 20 < 30 < 40 is false.
'''
print(f'10 < 20 > 30 < 40 : {10 < 20 > 30 < 40}\n')  # Output: 10 > 20 < 30 < 40 : False

'''
Other General Points:
----------------------
 In Python indentation is very important. It is used to indicate a block of code.
  
 Example 1 Consider if and else syntax. We use indents to define a block of code. brackets are not required to separate 
           the code. Refer the below example
'''
a = 10
b = 20

if a > b:
    print('a is greater than b')
# print('This line causes error') # SyntaxError: invalid syntax (Because of indentation error)
else:
    print('a is not greater than b\n')

'''
 Example 2 :
'''

if len('hello_world') > 5:
    print('Length of string is greater than 5')  # This line is inside the if block
print('This line is outside the if block')  # This is an independent statement outside the if block
#  print('This line causes error') # IndentationError: unexpected indent (Because of indentation error)
