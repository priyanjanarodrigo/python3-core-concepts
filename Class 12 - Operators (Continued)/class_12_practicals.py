print('Class 12 - Operators (Continued)')

'''
* Equality Operators
========================================================================================================================

 Following are the equality operators in Python:

    == -> Equal to operator always talks about content comparison in Python and it never performs the address comparison.
         (For address comparison we can use 'is` operator) If the contents of two operands are equal, then the condition
          becomes true, otherwise false.
    
    !=  -> Not equal to
'''

print('Equality Operators ------------------------------------------------------------------------------------------\n')

print(f'10 == 10 : {10 == 10}')  # Output: 10 == 10 : True
print(f'20 != 10 : {20 != 10}')  # Output: 20 != 10 : True
print(f'10 == True : {10 == True}')  # Output: 10 == True : False
print(f'False == False : {False == False}')  # Output: False == False : True
print(f'\'hello\' == \'hello\' : {"hello" == "hello"}\n')  # Output: 'hello' == 'hello' : True

'''
Event if the compatibility is not there (just like in the following example), it will not throw an error and simply 
return False. We can apply == operator on any two data types.
'''
print(f'10 == \'hello\' : {10 == "hello"}\n')  # Output: 10 == 'hello' : False

'''
Even for the equality operator, we can apply chaining concept. Same conditions apply here as well just like in 
relational operators chaining.
'''

print(f'10 == 10 == 10 : {10 == 10 == 10}')  # Output: 10 == 10 == 10 : True
print(f'20 == 20 == 30 == 30 : {20 == 20 == 30 == 30}')  # Output: 20 == 20 == 30 == 30 : False
print(f'10 == 5 + 5 == 3 + 7 == 2 * 5 : {10 == 5 + 5 == 3 + 7 == 2 * 5}\n')  # Output: 10 == 5+5 == 3 +7 == 2 * 5 : True

'''
When using equality operator with strings, it will not internally consider the ASCII or Unicode values. It will simply 
compare the contents.
'''
print(f'\'a\' == 97 : {"a" == 97}')  # Output: 'a' == 97 : False

'''
Here we are properly comparing the ASCII values of 'a' and 97. ord() function is used to get ASCII/Unicode value of 
a character
'''
print(f'ord(\'a\') == 97 : {ord("a") == 97}')  # Output: ord('a') == 97 : True

'''
On the other hand we can use chr() function to Convert ASCII/Unicode value to character.
'''
print(f'chr(97) == \'a\' : {chr(97) == "a"}\n')  # Output: chr(97) == 'a' : True

'''
Complex numbers are also supported by equality operator. == will never raise errors even for complex numbers.
'''
print(f'(10+2j) == (10+2j) : {(10 + 2j) == (10 + 2j)}')  # Output: (10+2j) == (10+2j) : True
print(f'(10+2j) == \'hello\' : {(10 + 2j) == "hello"}')  # Output: (10+2j) == 'hello' : False
print(f'(10+2j) != \'hello\' : {(10 + 2j) != "hello"}\n')  # Output: (10+2j) != 'hello' : True

'''
In this case where types are compatible (ex int and float), the smaller type (int 10 in this case) is converted to the 
larger type (as 10.0). Internally 10.0 == 10.0 is evaluated.
'''
print(f'10 == 10.0 : {10 == 10.0}')  # Output: 10 == 10.0 : True)

# This returns False as the types are not compatible. (int and str)
print(f'10 == \'10\' : {10 == "10"}')  # Output: 10 == '10' : False

# This returns True as the types are compatible (int and bool). bool True is internally 1.
print(f'1 == True : {1 == True}\n')  # Output: 1 == True : True

'''
3. Logical Operators
========================================================================================================================
 Following are the logical operators in Python:

    1. and
    2. or
    3. not
    
We can apply logical operators to boolean and non-boolean types
'''
print('Logical Operators -------------------------------------------------------------------------------------------\n')

'''
3.1 Logical operators with bool type / Behaviour of logical operators with respect to bool
========================================================================================================================

- If we apply logical operators to bool values, then the result will always be bool.

- The following are the rules for the logical operators with respect to bool types:
 
     and    -> If both the arguments are True, then the condition becomes True, otherwise False.
    
     or     -> If at least one argument is True, then the condition becomes True, otherwise False (if both arguments are 
               False).
    
     not    -> It is used to reverse the logical state of its operand. If a condition is True, then Logical NOT operator 
               will make it False, otherwise True.

- This behaviour is pretty much straightforward and simple when it comes to bool types.
'''
print('Logical Operators with respect to bool type -----------------------------------------------------------------\n')

# and
print(f'True and True : {True and True}')  # Output: True and True : True
print(f'True and False : {True and False}\n')  # Output: True and False : False
print(f'False and False : {False and False}\n')  # Output: False and False : False

# or
print(f'True or True : {True or True}')  # Output: True or True : True
print(f'True or False : {True or False}')  # Output: True or False : True
print(f'False or False : {False or False}\n')  # Output: False or False : False

# not
print(f'not True : {not True}')  # Output: not True : False
print(f'not False : {not False}')  # Output: not False : True
print(f'not (True or False) : {not (True or False)}')  # Output: not (True or False) : False
print(f'not (False and False) : {not (False and False)}')  # Output: not (False and False) : True

'''
Take note that here, with the brackets removed the precedence of the operators is changed. Therefore, the condition will 
internally be evaluated left to right

steps
    0. Initial declaration (not False and False)
    1. not False becomes True (True and False)
    2. True and False becomes False (False)
    
    And finally, the condition becomes False.
'''
print(f'not False and False : {not False and False}\n')  # Output: not False and False : False

'''
3.2 Logical operators with non-bool types / Behaviour of logical operators with respect to non-bool types
========================================================================================================================

- If we apply logical operators with non-bool types, the result will not be a boolean value.

* IMPORTANT :
.............
- The following are the rules for the logical operators with respect to non-bool types:

    1. 0 is considered as False
    2. Non-zero numbers are considered as True
    3. Empty strings are considered as False
    
    (empty list, tuple, set, dictionary are considered as False)

- Assume there are two variables called x and y. Keep in mind the following example is about the logical operators with
  respect to non-bool types.

------------------------------------------------------------------------------------------------------------------------
3.2.1. and operator with non-bool types
------------------------------------------------------------------------------------------------------------------------
        * Expression : x and y
    
            - First Python evaluates x against the rules mentioned above to figure out whether it is True or False.
            
            - If x evaluates to False, then then result returned is x, otherwise result is y.
              (if x evaluates to True, then the result is y)
        
        Example 1:
        ----------
            x = 10
            y = 20
            x and y

            - First, x is evaluated. Since x is 10, it is non-zero, so it is considered as True.
            - Then, the result is y.
            - Therefore, the result is 20.
'''
print('Logical Operators with respect to non-bool type -------------------------------------------------------------\n')

print('and operator with non-bool types')

# Example 1:
print(f'10 and 20 : {10 and 20}\n')  # Output: 10 and 20 : 20

'''
        Example 2:
        ---------
            x = 0
            y = 20
            x and y

            - First, x is evaluated. Since x is 0, it is considered as False.
            - Then, the result is x.
            - Therefore, the result is 0.
'''

# Example 2:
print(f'0 and 20 : {0 and 20}\n')  # Output: 0 and 20 : 0

'''
        Example 3: (list in this example)
        ---------------------------------
            x = []
            y = 20
            x and y
            - First, x is evaluated. Since x is an empty list, it is considered as False.
            - Then, the result is x.
            - Therefore, the result is [].
'''

# Example 3 :(Empty list, tuple, set, dictionary are considered as False)
print(f'[] and 10 : {[] and 12}')  # Output: [] and 12 : []
print(f'() and 10 : {() and 12}')  # Output: () and 12 : ()
print('{} and 10 : ', {} and 12, '\n')  # Output: {} and 12 :  {}

'''
        Example 4:
        ----------
            x = 1
            y = 'hello'
            x and y
            - First, x is evaluated. Since x is 1, it is non-zero, so it is considered as True.
            - Then, the result is y.
            - Therefore, the result is 'hello'.
'''

# Example 4:
print(f'1 and "hello" : {1 and "hello"}\n')  # Output: 1 and "hello" : hello

'''
------------------------------------------------------------------------------------------------------------------------
3.2.2. or operator with non-bool types
------------------------------------------------------------------------------------------------------------------------

        * Expression : x and y
    
            - First Python evaluates x against the rules mentioned above to figure out whether it is True or False.
            
            - with or operator, if x evaluates to True, then the result returned is x, otherwise result is y. 
              (kind of opposite behaviour of "and" operator)
              
        Example 1:
        ----------
            x = 10
            y = 20
            x or y
            
            - First, x is evaluated. Since x is 10, it is non-zero, so it is considered as True.
            - Then, the result is x.
            - Therefore, the result is 10.              
'''
print('or operator with non-bool types')

# Example 1:
print(f'10 or 20 : {10 or 20}\n')  # Output: 10 or 20 : 10

'''
        Example 2:
        ---------
            x = 0
            y = 20
            x or y

            - First, x is evaluated. Since x is 0, it is considered as False.
            - Then, the result is y.
            - Therefore, the result is 20.
'''

# Example 2:
print(f'0 or 20 : {0 or 20}\n')  # Output: 0 or 20 : 20

'''
        Example 3: (list in this example)
        ---------------------------------
            x = []
            y = 20
            x or y
            
            - First, x is evaluated. Since x is an empty list, it is considered as False.
            - Then, the result is y.
            - Therefore, the result is 20.
'''

# Example 3: (Empty list, tuple, set, dictionary are considered as False)
print(f'[] or 10 : {[] or 12}')  # Output: [] or 12 : 12
print(f'() or 10 : {() or 12}')  # Output: () or 12 : 12
print('{} or 10 : ', {} or 12, '\n')  # Output: {} or 12 :  12

'''
        Example 4:
        ----------
            x = 1
            y = 'hello'
            x or y
            
            - First, x is evaluated. Since x is 1, it is non-zero, so it is considered as True.
            - Then, the result is x.
            - Therefore, the result is 1.
'''

# Example 4:
print(f'1 or "hello" : {1 or "hello"}\n')  # Output: 1 or "hello" : 1

'''
------------------------------------------------------------------------------------------------------------------------
3.2.3. not operator with non-bool types
------------------------------------------------------------------------------------------------------------------------

- not operator will always return a boolean value only

- If the operand is True, then the result is False, otherwise the result is True.
'''

print('not operator with non-bool types')

'''
 Example 1:
 ----------
    x = 10
    not x

    - First, x is evaluated. Since x is 10, it is non-zero, so it is considered as True.
    - Then, the result is False.
     - Therefore, the result is False.
'''

# Example 1:
print(f'not 10 : {not 10}\n')  # Output: not 10 : False

# Some other examples in the similar manner
print(f'not 10.55 : {not 10.55}')  # Output: not 10.55 : False
print(f'not 0 : {not 0}')  # Output: not 0 : True
print(f'not [] : {not []}\n')  # Output: not [] : True

'''
Interesting example : or operator 
---------------------------------

Here the reason that we don't get ZeroDivisionError is because of the way Python evaluates the expression.

With or operator, if x evaluates to True, then the result returned is x, otherwise result is y.

In this case, 10 is non-zero, so it is considered as True. Therefore, 10 is returned but the other expression 10/0 is 
not evaluated. As a result, ZeroDivisionError is not raised and the output is returned as 10.
'''
print(f'10 or 10/0 : {10 or 10 / 0}\n')  # Output: 10 or 10/0 : 10

'''
Interesting example : and operator
----------------------------------

Here the reason that we get ZeroDivisionError is because of the way Python evaluates the expression.

With and operator, if x evaluates to False, then the result returned is x, otherwise result is y.

In this case, 10 is non-zero, so it is considered as True. Therefore, the other expression 10/0 is evaluated and
ZeroDivisionError is raised.
'''
# print(f'10 and 10 / 0 : {10 and 10 / 0}')  # Output: ZeroDivisionError: division by zero

'''
4. Bitwise Operators
========================================================================================================================
 The following bitwise operators are supported by Python language.
 
     1) & 	Bitwise AND
        - If both the bits are 1, then the result is 1. Otherwise, the result is 0.
     
     2) | 	Bitwise OR
        - If at least one of the bits is 1, then the result is 1. Otherwise, the result is 0.
     
     3) ^ 	Bitwise XOR
        - Exclusive OR operator
        - Either the first one or the second one, but not both.
        - If both the bits(arguments) are different, then the result is 1. Otherwise, the result is 0.
     
     4) ~ 	Bitwise Complement/NOT
        - Bitwise complement operator
        - It is a unary operator. 1 will become 0 and 0 will be replaced with 1.
     
     5) << 	Bitwise Left Shift
     6) >> 	Bitwise Right Shift
     
 There bitwise operators are applicable for int and bool data types only. In case if we try to apply for any other data 
 type, we'll get an error.
 
 4 & 5 => Valid statement (4)
 
 True & True => Valid statement (True)
 
 10.2 & 4 => TypeError: unsupported operand type(s) for &: 'float' and 'int'
 
 10.2 & 4.2 => TypeError: unsupported operand type(s) for &: 'float' and 'float'
'''

''' 
------------------------------------------------------------------------------------------------------------------------
1. Bitwise AND (&)
------------------------------------------------------------------------------------------------------------------------
'''
print('Bitwise AND (&)\n')
print(f'binary value of 4 : {bin(4)}')  # Output: binary value of 4 :  0b100
print(f'binary value of 5 : {bin(5)}')  # Output: binary value of 5 :  0b101

'''
(Hint - AND gate, 0 and 0 = 0, 1 and 0 = 0, 0 and 1 = 0, 1 and 1 = 1)

 Binary value of 4          : 1 0 0
 Binary value of 5          : 1 0 1
 ----------------------------------
 Bitwise & operation        : 1 0 0
 
 Decimal value of 1 0 0    : 4
 
 Therefore, 4 & 5 = 4
'''
print(f'4 & 5 = {4 & 5}\n')  # Output: 4 & 5 : 4

'''
------------------------------------------------------------------------------------------------------------------------
2. Bitwise OR (|)
------------------------------------------------------------------------------------------------------------------------
'''
print('Bitwise OR (|)\n')
print(f'binary value of 4 : {bin(4)}')  # Output: binary value of 4 :  0b100
print(f'binary value of 5 : {bin(5)}')  # Output: binary value of 5 :  0b101

'''
(Hint - OR gate, 0 or 0 = 0, 1 or 0 = 1, 0 or 1 = 1, 1 or 1 = 1)

 Binary value of 4          : 1 0 0
 Binary value of 5          : 1 0 1
 ----------------------------------
 Bitwise | operation        : 1 0 1

 Decimal value of 1 0 1    : 5

 Therefore, 4 | 5 = 5
'''
print(f'4 | 5 = {4 | 5}\n')  # Output: 4 | 5 : 5

'''
------------------------------------------------------------------------------------------------------------------------
3. Bitwise XOR (^)
------------------------------------------------------------------------------------------------------------------------
'''
print('Bitwise XOR (^)\n')
print(f'binary value of 4 : {bin(4)}')  # Output: binary value of 4 :  0b100
print(f'binary value of 5 : {bin(5)}')  # Output: binary value of 5 :  0b101

'''
(Hint - XOR gate, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0)

 Binary value of 4          : 1 0 0
 Binary value of 5          : 1 0 1
 ----------------------------------
 Bitwise ^ operation        : 0 0 1

 Decimal value of 0 0 1    : 1

 Therefore, 4 ^ 5 = 1
'''
print(f'4 ^ 5 = {4 ^ 5}\n')  # Output: 4 ^ 5 : 1

'''
------------------------------------------------------------------------------------------------------------------------
4. Bitwise Complement / NOT (~)
------------------------------------------------------------------------------------------------------------------------
'''
print('Bitwise Complement / NOT (~)\n')

# Bitwise Complement / NOT (~) of 4
print(f'binary value of 4 : {bin(4)}')  # Output: binary value of 4 :  0b100
print(f'binary value of 5 : {bin(5)}')  # Output: binary value of 5 :  0b101
'''
(Hint - NOT gate, ~0 = 1, ~1 = 0). This is negation.

    The binary 32bits representation of 4 is 0000 0000 0000 0000 0000 0000 0000 0001
    
    The first bit is considered as the sign bit (AKA the most significant bit). There, 0 indicates positive and 
    1 indicates negative. In this case sign bit is 0, because 4 is a positive number.
 
    Positive numbers are represented directly in binary form in the memory (like above) but negative numbers are 
    represented in 2's complement form.

    * 4 in binary is                        ==>     0000 0000 0000 0000 0000 0000 0000 0100

    * ~4 (negation) in binary will be       ==>     1111 1111 1111 1111 1111 1111 1111 1011  

    After negation, the sign bit is 1 (1st bit, most significant bit) which means it is a negative number.

    The following is how a negative number is represented in 2's complement form.:
    ..............................................................................

    Sign bit is 1 (negative number)

    The remaining 31 Bits are               ==>     111 1111 1111 1111 1111 1111 1111 1011
    (This should be represented in 2's
    complement form)

    Representing Other 31 Bits: 111 1111 1111 1111 1111 1111 1111 1011 in 2's complement form:

    Conversion Steps:
        1. Flip all the bits (0s will be replaced with 1 and 1s will be replaced with 0) to get 1's complement form.

        2. Add 1 to the 1's complement form to get 2's complement form.


    Remaining 31 bits (Negated)                 ==>  111 1111 1111 1111 1111 1111 1111 1011
    --------------------------------------------------------------------------------------- 
    
    1) 1's complement form (opposite of each)   ==>  000 0000 0000 0000 0000 0000 0000 0100
    2) Add 1 (binary representation of 1)       ==>                                       1     
    ---------------------------------------------------------------------------------------
    2's complement form (after adding 1)        ==>  000 0000 0000 0000 0000 0000 0000 0101


    * With that, 2's complement form of the rest of the 31 bits is 000 0000 0000 0000 0000 0000 0000 0101

    * The Complete 32bit internal representation ==>  sign bit followed by 2's complement form of the rest of the 31 bits

                                                 ==>  1000 0000 0000 0000 0000 0000 0000 0101

    * The decimal value of the remaining 31bits  ==>  5
      (000 0000 0000 0000 0000 0000 0000 0101)
      (binary 101 is the decimal value of 5)

    * Sign bt is 1, so the final value should be ==>  -5
      minus. Which makes the final value -5

    * Therefore, the output for ~4 is         ==>  -5
'''
print(f'~4 = {~4}\n')  # Output: ~4 : -5

# Bitwise Complement / NOT (~) of True
print(f'Binary value of True : {bin(True)}')  # Output: Binary value of True is 0b1
print(f'Binary value of 2 : {bin(2)}')  # Output: Binary value of 2 : 0b10
'''
(Hint - NOT gate, ~0 = 1, ~1 = 0). This is negation.

    True is internally represented as 1 and the 32bits representation is 0000 0000 0000 0000 0000 0000 0000 0001
    (sign bit is 0, because 1 is a positive number)
    
    * 1 in binary is                        ==>     0000 0000 0000 0000 0000 0000 0000 0001
    
    * ~1 (negation) in binary will be       ==>     1111 1111 1111 1111 1111 1111 1111 1110  
    
    After negation, the sign bit is 1 (1st bit, most significant bit) which means it is a negative number.
    
    The following is how a negative number is represented in 2's complement form.:
    ..............................................................................
    
    Sign bit is 1 (negative number)
    
    The remaining 31 Bits are               ==>     111 1111 1111 1111 1111 1111 1111 1110
    (This should be represented in 2's
    complement form)
    
    Representing Other 31 Bits: 111 1111 1111 1111 1111 1111 1111 1110 in 2's complement form:
    
    Conversion Steps:
        1. Flip all the bits (0s will be replaced with 1 and 1s will be replaced with 0) to get 1's complement form.
        
        2. Add 1 to the 1's complement form to get 2's complement form.
    
    
    Remaining 31 bits (Negated)                 ==>  111 1111 1111 1111 1111 1111 1111 1110
    ---------------------------------------------------------------------------------------
      
    1) 1's complement form (opposite of each)   ==>  000 0000 0000 0000 0000 0000 0000 0001
    2) Add 1 (binary representation of 1)       ==>                                       1     
    ---------------------------------------------------------------------------------------
    2's complement form (after adding 1)        ==>  000 0000 0000 0000 0000 0000 0000 0010


    * With that, 2's complement form of the rest of the 31 bits is 000 0000 0000 0000 0000 0000 0000 0010

    * The Complete 32bit internal representation ==>  sign bit followed by 2's complement form of the rest of the 31 bits
                
                                                 ==>  1000 0000 0000 0000 0000 0000 0000 0010
    
    * The decimal value of the remaining 31bits  ==>  2
      (000 0000 0000 0000 0000 0000 0000 0010)
      (binary 10 is the decimal value of 2)
      
    * Sign bt is 1, so the final value should be ==>  -2
      minus. Which makes the final value -2

    * Therefore, the output for ~True is         ==>  -2
'''
print(f'~True = {~True}\n')  # Output: ~True : -2
