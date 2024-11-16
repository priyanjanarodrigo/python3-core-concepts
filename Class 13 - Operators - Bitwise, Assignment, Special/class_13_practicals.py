print('Class 13 - Operators - Bitwise, Assignment, Special')

'''
Summary from Class 12
'''
print('Summary from Class 12')
print(f'4 & 5 = {4 & 5}')  # Output: 4 & 5 = 4
print(f'4 | 5 = {4 | 5}')  # Output: 4 | 5 = 5
print(f'4 ^ 5 = {4 ^ 5}')  # Output: 4 ^ 5 = 1
print(f'~4 = {~4}')  # Output: ~4 = -5
print(f'~Ture = {~True}\n')  # Output: ~True = -2

'''
Shift Operators
========================================================================================================================

 Python provides two types of bitwise shift operators:

	1. Left Shift (<<) : Shifts the bits of a number to the left by a specified number of positions.
	2. Right Shift (>>): Shifts the bits of a number to the right by a specified number of positions.

 In Python we don't have unsigned shift operators like in Java. ( >>> or <<<)
'''
print('Bitwise Shift Operators\n')

print('Bitwise Left Shift (<<) ---------------------------------------------------------------------------------------')
'''
------------------------------------------------------------------------------------------------------------------------
 1.  Bitwise Left Shift (<<)
------------------------------------------------------------------------------------------------------------------------

 * Example 1 :   10 << 2
    
    - The left shift operator (<<) shifts the bits of the number 10 to the left by 2 positions. 
      Each left shift effectively multiplies the number by 2 raised to the power of the number of positions shifted.
      
    - 10 in binary is (32 bit representation) : 0000 0000 0000 0000 0000 0000 0000 1010
      
    - Add two zeros to the right of the binary representation:
      This means that, the first two bits are removed from the binary representation of 10 and two 0 bits are appended
      at the end as follows:

    * Complete binary representation of 10          ==>     0000 0000 0000 0000 0000 0000 0000 1010
    
    1. Removing the first two bits from the left    ==>     __00 0000 0000 0000 0000 0000 0000 1010
    
    2. Now there are 2 vacant positions on the right==>     0000 0000 0000 0000 0000 0000 0010 10__
    
    3. Add 2 zero bits to the right                 ==>     0000 0000 0000 0000 0000 0000 0010 1000
      
    - The resulting binary representation is 0000 0000 0000 0000 0000 0000 0010 1000, 
      which is equivalent to 40 in decimal. 
      
 * Mathematical Confirmation:
	    
    - Left shifting by 2 is equivalent to multiplying by 2**2 = 4 (2 to the power of 2)
    
    - Therefore,
        10 << 2 = 10 x (2 ** 2) 
        10 << 2 = 10 x 4
        10 << 2 = 40
'''

print(f'Binary value of 10 : {bin(10)}')  # Output: Binary value of 10 : 0b1010
print(f'Binary value of 40 : {bin(40)}')  # Output: Binary value of 40 : 0b101000
print(f'10 << 2 = {10 << 2}')  # Output: 10 << 2 = 40

'''
 * Practical Explanation:

    - The operation 10 << 2 shifts all bits two positions to the left, effectively multiplying 10 by 4.
	- It’s a quick way to multiply by powers of 2.
	
 * Key Takeaways:

    - 10 << 2 shifts the bits of 10 (00001010) two places left, resulting in 40.
    - Left shifts are useful for efficient multiplication by powers of 2.

 * Example 2 :  Multiply 5 by 2**3 / In other words = 5 x (2 x 2 x 2)

    5 << 3 = 5 * (2 ** 3)
    5 << 3 = 5 * 8
    5 << 3 = 40
'''
print(f'5 << 3 = {5 << 3}')  # Output: 5 << 3 = 40

# Some more examples:
print(f'True << 2 = {True << 2}')  # Output: True << 2 = 4
print(f'False << 2 = {False << 2}\n')  # Output: False << 2 = 0

print('Bitwise Right Shift (>>) --------------------------------------------------------------------------------------')
'''
------------------------------------------------------------------------------------------------------------------------
 2. Bitwise Right Shift (>>)
------------------------------------------------------------------------------------------------------------------------

 * Example 1 :   10 >> 2
    
    - The right shift operator (>>) shifts the bits of the number 10 to the right by 2 positions. 
      Each right shift effectively performs integer division by 2 raised to the power of the number of positions 
      shifted, discarding any remainder.
    
    - 10 in binary is (32 bit representation) : 0000 0000 0000 0000 0000 0000 0000 1010
    
    - Remove the last two bits from the right of the binary representation:
      This means that, the last two bits are removed from the binary representation of 10 and two sign bits
      are prepended at the beginning as follows:
      
    - We should be careful when the sign bit is prepended. If the number is positive, the sign bit is 0.
      If the number is negative, the sign bit is 1.

    * Complete binary representation of 10          ==>     0000 0000 0000 0000 0000 0000 0000 1010

    1. Removing the last two bits on the right      ==>     0000 0000 0000 0000 0000 0000 0000 10__     
    
    2. Now there are 2 vacant positions on the left ==>     __00 0000 0000 0000 0000 0000 0000 0010
    
    3. Prepend 2 sign bits to the left              ==>     0000 0000 0000 0000 0000 0000 0000 0010
       (In this case two 0 as 10 is positive)              
       
    - The resulting binary representation is 0000 0000 0000 0000 0000 0000 0000 0010, which is equivalent to 2 in 
      decimal.
      
 * Mathematical Confirmation:

	- Right shifting by 2 is equivalent to performing integer division by 2**2 = 4 (2 to the power of 2)
    
    - Therefore,
        10 >> 2 = 10 / (2 ** 2) 
        10 >> 2 = 10 / 4
        10 >> 2 = 2.5 (remainder is discarded)
        10 >> 2 = 2
'''
print(f'10 >> 2 = {10 >> 2}')  # Output: 10 >> 2 = 2

'''
 * Practical Explanation:

    - The operation 10 >> 2 shifts all bits two positions to the right, effectively dividing 10 by 4 (integer division).
    - Any bits shifted out on the right are discarded.
    - its a quick way to divide by powers of 2.

 * Key Takeaways:

    - 10 >> 2 shifts the bits of 10 (00001010) two places right, resulting in 2.
    - Right shifts are useful for efficient division by powers of 2.

 * Example 2:  Divide 10 by 2**3 / In other words = 10 / (2 x 2 x 2)
 
    10 >> 3 = 10 / (2 ** 3)
    10 >> 3 = 10 / 8
    10 >> 3 = 1.25 (remainder is discarded)
    10 >> 3 = 1
'''
print(f'10 >> 3 = {10 >> 3}')  # Output: 10 >> 3 = 1

'''
 * In case if the number is negative, the sign bit is 1. And internally the number is represented as 2's complement form.
   (in the below example, the number is -10 so the sign bit be 1)

 * It is recommended to use the bit level computation (as in both the above examples) to figure out the result.
'''
print(f'-10 >> 2 = {-10 >> 2}\n')  # Output: -10 > -2 = -3

# Some more examples:
print(f'True >> 2 = {True >> 2}')  # Output: True >> 2 = 0
print(f'False >> 2 = {False >> 2}\n')  # Output: False >> 2 = 0

'''
 * IMPORTANT:
 ============
 
 * In either left (<<) or right shift (>>), the shift count must be a positive integer. Otherwise, 
   it will raise a ValueError.

'''
# print(10 << -3) # ValueError: negative shift count

# print(10 >> -5) # ValueError: negative shift count


print('Assignment Operators -`--------------------------------------------------------------------------------------\n')
'''
5. Assignment Operators
========================================================================================================================

 Assignment operators are used to assign or update the value of a variable. In Python, these operators can be combined
 with other operations (like arithmetic, bitwise operations, etc.) to perform assignments and modifications 
 simultaneously.

 -----------------------------------------------------------------------------------------------------------------------
 5.1 Basic Assignment Operator (=)
 -----------------------------------------------------------------------------------------------------------------------
 
 - The basic assignment operator assigns the value on the right to the variable on the left.
 
 - In Python we can assign multiple values to multiple variables in a single line of code.
'''
print('Basic Assignment Operator (=) -------------------------------------------------------------------------------\n')

# Assigning multiple values to multiple variables
x, y, z = 10, 20, 30
print(f'x = {x}, y = {y}, z = {z}')  # Output: x = 10, y = 20, z = 30

# Swapping the values of two variables without using a temporary variable
myVal = 111
yourVal = 222

print(f'Before swapping: myVal = {myVal}, yourVal = {yourVal}')  # Output: Before swapping: myVal = 111, yourVal = 222

myVal, yourVal = yourVal, myVal
print(f'After swapping: myVal = {myVal}, yourVal = {yourVal}')  # Output: After swapping: myVal = 222, yourVal = 111

'''
 How many variables are declared in line, that much values should be provided on the right side.
 Otherwise, it will raise a ValueError.
 
 Here in the below example, we are trying to assign 4 values to 3 variables. Therefore, it will raise a ValueError.
'''
# v1,v2,v3 = 10,20,30,40 # ValueError: too many values to unpack (expected 3)

# Assigning a single value to multiple variables
a = b = c = 10
print(f'a = {a}, b = {b}, c = {c}\n')  # Output: a = 10, b = 10, c = 10

'''
 -----------------------------------------------------------------------------------------------------------------------
 5.2 Compound Assignment Operators
 -----------------------------------------------------------------------------------------------------------------------
 
 These combine an operation (arithmetic, bitwise, etc.) with assignment, performing the operation and updating the 
 variable in one step.
 
 ________________________________________________________________________________________________________________
 |  Operator  |     Usage   |	Equivalent To   |                       Description                             |
 ----------------------------------------------------------------------------------------------------------------
 |     +=     |     x += y	|     x = x + y	    | Adds y to x and assigns the result to x                       |
 ----------------------------------------------------------------------------------------------------------------
 |     -=     |     x -= y	|     x = x - y	    | Subtracts y from x and assigns the result to x                |
 ----------------------------------------------------------------------------------------------------------------
 |     *=     |     x *= y	|     x = x * y	    | Multiplies x by y and assigns the result to x                 |
 ----------------------------------------------------------------------------------------------------------------
 |     /=     |     x /= y	|     x = x / y	    | Divides x by y and assigns the result to x                    |
 ----------------------------------------------------------------------------------------------------------------
 |     //=    |     x //= y	|     x = x // y	| Performs floor division of x by y and assigns the result to x |
 ----------------------------------------------------------------------------------------------------------------
 |     %=     |     x %= y	|     x = x % y	    | Calculates the modulus of x by y and assigns the result to x  |
 ----------------------------------------------------------------------------------------------------------------
 |     **=    |     x **= y	|     x = x ** y	| Raises x to the power of y and assigns the result to x        |
 ----------------------------------------------------------------------------------------------------------------

* IMPORTANT:
 ============

 * In Python, increment ++ and decrement -- operators are not supported.
 
 * Prefix increment and decrement (assume that value = 10)
 
    ++value : This is internal treated as +(+x), which means it will be treated as +(+10)
    
    --value : This is internal treated as -(-x), which means it will be treated as -(-10)
    
 * Postfix increment and decrement (assume that value = 10)
 
    value++ # SyntaxError: invalid syntax
    
    value-- # SyntaxError: invalid syntax
'''
myValue = 10
print(f'myValue = {myValue}')  # Output: myValue = 10
print('Trying to execute ++myValue and --myValue')

# ++x is internally treated as +(+x) and --x is internally treated as -(-x)
print('++myValue = ', ++myValue, '  :   Output is still 10 as ++ is not supported in Python')
print('--myValue = ', --myValue, '  :   Output is still 10 as -- is not supported in Python')

'''
 These will raise a SyntaxError: invalid syntax
'''
# myValue++ # SyntaxError: invalid syntax
# = myValue-- # SyntaxError: invalid syntax


print('\nCompound Assignment Operator (=) ----------------------------------------------------------------------------')

'''
+= Operator
'''
print('\n+= Operator\n --------------------------')
p = 10
print(f'p = {p}')  # Output: p = 10
print('Performing p += 5 operation')
p += 5  # Equivalent to p = p + 5
print(f'p = {p}')  # Output: p = 15

'''
-= Operator
'''
print('\n-= Operator\n --------------------------')
q = 30
print(f'q = {q}')  # Output: q = 30
print('Performing q -= 10 operation')
q -= 10  # Equivalent to q = q - 10
print(f'q = {q}')  # Output: q = 20

'''
*= Operator
'''
print('\n*= Operator\n --------------------------')
r = 100
print(f'r = {r}')  # Output: r = 100
print('Performing r *= 2 operation')
r *= 2  # Equivalent to r = r * 2
print(f'r = {r}')  # Output: r = 200

'''
/= Operator
'''
print('\n/= Operator\n --------------------------')
s = 40
print(f's = {s}')  # Output: s = 40
print('Performing s /= 4 operation')
s /= 4  # Equivalent to s = s / 4
print(f's = {s}')  # Output: s = 10.0 (result is float due to division)

'''
//= Operator
'''
print('\n//= Operator\n --------------------------')
t = 40
print(f't = {t}')  # Output: t = 40
print('Performing t //= 4 operation')
t //= 4  # Equivalent to t = t / 4
print(f't = {t}')  # Output: t = 10 (result is int due to floor division)

'''
%= Operator
'''
print('\n%= Operator\n --------------------------')
u = 5
print(f'u = {u}')  # Output: u = 5
print('Performing u %= 2 operation')
u %= 2  # Equivalent to u = u % 2
print(f'u = {u}')  # Output: u = 1 (remainder of 5 divided by 2)

'''
**= Operator
'''
print('\n**= Operator\n --------------------------')
v = 2
print(f'v = {v}')  # Output: v = 2
print('Performing v **= 3 operation')
v **= 3  # Equivalent to v = v ** 3 which is equivalent to v = v * v * v
print(f'v = {v}')  # Output: v = 8 (2 raised to the power of 3)

'''
 5.3 Bitwise Assignment Operators
 
 ________________________________________________________________________________________________________________
 |  Operator  |     Usage   |	Equivalent To   |                       Description                             |
 ----------------------------------------------------------------------------------------------------------------
 |     &=     |     x &= y	|     x = x & y	    | Performs bitwise AND on x and y and assigns the result to x   |
 ----------------------------------------------------------------------------------------------------------------
 |     |=     |     x |= y	|     x = x | y	    | Performs bitwise OR on x and y and assigns the result to x    |
 ----------------------------------------------------------------------------------------------------------------
 |     ^=     |     x ^= y	|     x = x ^ y	    | Performs bitwise XOR on x and y and assigns the result to x   |
 ----------------------------------------------------------------------------------------------------------------
 |     <<=    |     x <<= y	|     x = x << y	| Shifts x left by y bits and assigns the result to x           |
 ----------------------------------------------------------------------------------------------------------------
 |     >>=    |     x >>= y	|     x = x >> y	| Shifts x right by y bits and assigns the result to x          |
 ----------------------------------------------------------------------------------------------------------------

'''
print('\nBitwise Assignment Operators --------------------------------------------------------------------------------')

'''
&= Operator
'''
print('\n&= Operator\n --------------------------')
g = 4
print(f'g = {g}')  # Output: g = 4
print('Performing g &= 5 operation')
g &= 5  # Equivalent to g = g & 5
print(f'g = {g}')  # Output: g = 4

'''
|= Operator
'''
print('\n|= Operator\n --------------------------')
h = 4
print(f'h = {h}')  # Output: h = 4
print('Performing h |= 5 operation')
h |= 5  # Equivalent to h = h | 5
print(f'h = {h}')  # Output: h = 5

'''
^= Operator
'''
print('\n^= Operator\n --------------------------')
i = 4
print(f'i = {i}')  # Output: i = 4
print('Performing i ^= 5 operation')
i ^= 5  # Equivalent to i = i ^ 5
print(f'i = {i}')  # Output: i = 1

'''
<<= Operator
'''
print('\n<<= Operator\n --------------------------')
k = 10
print(f'k = {k}')  # Output: k = 10
print('Performing k <<= 2 operation')
k <<= 2  # Equivalent to k = k << 2
print(f'k = {k}')  # Output: k = 40

'''
>>= Operator
'''
print('\n>>= Operator\n --------------------------')
j = 10
print(f'j = {j}')  # Output: j = 10
print('Performing j >>= 2 operation')
j >>= 2  # Equivalent to j = j >> 2
print(f'j = {j}')  # Output: j = 2

'''
5.4 Walrus Operator (:=)

 ____________________________________________________________________________________________________________________
 |  Operator  |     Usage   |	         Description                                                                |
 --------------------------------------------------------------------------------------------------------------------
 |     : =   |     x := y	| Assigns y to x and returns x (introduced in Python 3.8, known as the walrus operator) |
 --------------------------------------------------------------------------------------------------------------------   
'''
print('\nWalrus Operator (:=) ----------------------------------------------------------------------------------------')
n1 = 23
n2 = 455

print(f'n1 = {n1}')  # Output: n1 = 23
print(f'n2 = {n2}')  # Output: n2 = 455

print('n1 := n2 =', n1 := n2)  # Output: n1 := n2 = 455
# print(f'n1 := n2 = {(n1 := n2)}') # Output: n1 := n2 = 455 (Enclosing Bracket is necessary here (n1 := n2) whe ued with f-string)


'''
 5.5 Ternary Operator (?:)
 
  In python, the ternary operator with syntax ?: is not directly supported. Instead, you can use if-else statements 
  or the walrus operator (:=) for inline assignments.
  
  1. Using if-else statements:

    result = <value_if_true> if <condition> else <value_if_false>

  2. Using the walrus operator (:=)
     Here response and check are both variables. The check variable is assigned to the result of the condition, 
     and the response variable is assigned to the result of the if-else statement.
    
    response = <value_if_true> if (check := <condition>) else <value_if_false>
 
'''
print('\nTernary Operator  -----------------------------------------------------------------------------------------\n')

# result = (10 < 20)  ? 'Yes' : 'No' # SyntaxError: invalid syntax

'''
Option 1 - We can use if-else statement
'''
output = 'Yes' if 10 < 20 else 'No'

print("output = 'Yes' if 10 < 20 else 'No' statement executed: ")
print("output = 'Yes' if 10 < 20 else 'No'")
print(f'output = {output}\n')  # Output: output = Yes

'''
Option 2 - We can use walrus operator (:=)

The check variable is assigned to the result of the condition, and the response variable is assigned to the result
of the if-else statement.

Here the check is a boolean value and the result is a string value. With this approach, we can obtain both the response 
and the check in the same expression.
'''
response = 'Hi' if (check := 200 < 50) else 'Hello'

print("response = 'Hi' if (check := 200 < 50) else 'Hello' statement executed: ")
print(f'response = {response}')  # Output: response = No
print(f'check = {check}')  # Output: check = False

'''
5.6 Summary

 - Assignment operators are essential for updating variable values efficiently. Here’s when to use them:
    1. Use basic assignment (=) to initialize or update variables.
    2. Increment (++) and decrement (--) operators are not supported in Python.
	3. Use compound operators (+=, -=, etc.) for concise arithmetic and bitwise updates.
	4. Use the walrus operator (:=) for inline assignments in expressions
	5. In python, the traditional ternary operator with the syntax ?: is not supported. Instead, you can use if-else 
	   statements or the walrus operator (:=) for inline assignments.
'''

# Nesting the single line if-else statement
print("\n Nesting the single line if-else statement\n")
marks = 82
status = 'Excellent' if marks > 90 else 'Great' if marks > 80 else 'Good'

print(f'status = {status}')  # Output: status = Great

number_output = 100 if 2 > 3 else 200 if 5 > 7 else 300
print(f'number_output = {number_output}\n')  # Output: number_output = 300

# REFER TO THE SAMPLE PROGRAMS FOR NESTED TERNARY OPERATIONS - class_13_program_1.py anc class_13_program_2.py

'''
6. Special Operators
========================================================================================================================

 - There are 2 special operators in Python:
 
    1. Identity operators
    2. Membership operators

6.1 Identity Operators
------------------------------------------------------------------------------------------------------------------------

 - Identity operators are used to check whether two variables refer to the same object in memory, not just whether they 
   have the same value.
   
 - Python provides two identity operators:
 
	1)	is      :   Returns True if two variables point to the same object in memory
	2)	is not  :   Returns True if two variables do not point to the same object in memory
   
 ____________________________________________________________________________________________________________-_______  
 | Operator	|                   Description	                                          |   Example   |    Output     |
 --------------------------------------------------------------------------------------------------------------------
 |    is	| Returns True if two variables refer to the same object in memory        |	x is y	    | True or False |
 --------------------------------------------------------------------------------------------------------------------
 |  is not	| Returns True if two variables do not refer to the same object in memory |	x is not y  | True or False |
 --------------------------------------------------------------------------------------------------------------------
 

 - Identity operators are often useful:
	1.	To check if a variable is None (a common practice in Python).
	2.	When you need to confirm whether two variables refer to the same object.
 
 
 6.1.1 is Operator
 -------------------
    - The is operator checks if two variables refer to the same object (i.e., they have the same memory address).
	- It does not compare the values of the variables.
'''

myValue = None
if myValue is None:
    print("myValue is None\n")

yourValue = 'Hello World'
if yourValue is not None:
    print("yourValue is not None\n")

o1 = [1, 2, 3]
o2 = o1
o3 = [1, 2, 3]

print(f'o1 = {o1}')  # Output: o1 = [1, 2, 3]
print(f'o2 = {o2}')  # Output: o2 = [1, 2, 3]
print(f'o3 = {o3}')  # Output: o3 = [1, 2, 3]

print(f'o1 is o2 : {o1 is o2}')  # Output: o1 is o2 : True (Because they are the same object in memory)
print(f'o1 is o3 : {o1 is o3}\n')  # Output: o1 is o3 : False (Because they are different objects in memory)

testValue1 = 10
testValue2 = 10
print(f'testValue1 = {testValue1}')  # Output: testValue1 = 10
print(f'testValue2 = {testValue2}')  # Output: testValue2 = 10

# Here testValue1 and testValue2 are pointing to the same object in memory
# All fundamental data types are immutable in Python, therefore testValue1 and testValue2 are pointing to the same object in memory as they are int types
print(
    f'testValue1 is testValue2 : {testValue1 is testValue2}\n')  # Output: testValue1 is testValue2 : True (the same object in memory within 0 - 256 buffer)

# Here testValue3 and testValue4 are not pointing to the same object in memory as they are out of 0 - 256 buffer
testValue3 = 257
testValue4 = 257
print(f'testValue3 = {testValue3}')  # Output: testValue3 = 257
print(f'testValue4 = {testValue4}')  # Output: testValue2 = 257
# Here testValue3 and testValue4 are not pointing to different objects in memory
print(
    f'testValue3 is testValue4 : {testValue3 is testValue4}\n')  # Output: testValue3 is testValue4 : False (on Python IDLE - different objects in memory)

'''
 6.1.2 is not Operator
 ----------------------
    - The is not operator checks if two variables refer to different objects in memory.
    - It is the negation of is.
'''
p1 = ['jelly fish', 'shark', 'whale']
p2 = ['jelly fish', 'shark', 'whale']

print(f'p1 = {p1}')  # Output: p1 = ['jelly fish', 'shark', 'whale']
print(f'p2 = {p2}')  # Output: p2 = ['jelly fish', 'shark', 'whale']
print(f'p1 is not p2 : {p1 is not p2}\n')  # Output: p1 is not p2 : True (p1 and p2 are different objects in memory)

'''
 Key Points About Identity Operators
 -----------------------------------
 
 - The difference between is and ==

     • is checks if two variables refer to the same object.
	    
	 • == checks if the values of two variables are equal.
'''
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]

print(f'obj1 = {obj1}')  # Output: obj1 = [1, 2, 3]
print(f'obj2 = {obj2}\n')  # Output: obj2 = [1, 2, 3]

print(f'obj1 is obj2 : {obj1 is obj2}')  # Output: obj1 is obj2 : False (Because they are different objects in memory)
print(f'obj1 == obj2 : {obj1 == obj2}')  # Output: obj1 == obj2 : True (Because they have the same values)
