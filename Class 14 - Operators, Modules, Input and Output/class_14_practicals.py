print('Class 14 - Operators, Modules, Input and Output\n')

'''
Class 13 (Previous) - Summary
........................................................................................................................
 * Special Operators
  
    1. Identity operators
    2. Membership operators
 
 1. Identity Operators
 ---------------------
    1) is
    2) is not
 
 * is operator is meant for reference comparison and the == operator is meant for content comparison.
'''
print('Class 13 (Previous) - Summary -------------------------------------------------------------------------------\n')

a = 10
b = 10
print(f'a is b = {a is b}')  # Output: a is b = True

list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Printing the memory addresses of both the lists
print(f'id(list1) = {id(list1)}')  # Output: id(list1) = 4369877376
print(f'id(list2) = {id(list2)}')  # Output: id(list2) = 4369879168

# Reference Comparison with is operator
print(f'list1 is list2 = {list1 is list2}')  # Output: list1 is list2 = False

# Content Comparison with == operator
print(f'list1 == list2 = {list1 == list2}\n')  # Output: list1 == list2 = True

'''
 2. Membership Operators
 -----------------------
    1) in
    2) not in
    
 * in can be used to check if a given value is present in a sequence (e.g., list, tuple, string) or a dictionary.
   In simple terms, whether the given value is a member of the sequence or not.
'''
list3 = [10, 20, 30, 40, 50]
print(f'10 in list3 = {10 in list3}')  # Output: 10 in list3 = True
print(f'30 in list3 = {30 in list3}')  # Output: 30 in list3 = True
print(f'90 not in list3 = {90 not in list3}')  # Output: 90 not in list3 = True
print(f'10 not in list3 = {10 not in list3}\n')  # Output: 10 not in list3 = False

# We can use in operator for other data types as well (not only for sequence data types)
sample_text = 'Hello, learning Python is really fun!'
print(f'sample_text = {sample_text}')  # Output: sample_text = Hello, learning Python is really fun!
print(f'\"really\" in sample_text = {"really" in sample_text}')  # Output: "really" in sample_text = True
print(f'\"fun!\" not in sample_text = {"fun" not in sample_text}')  # Output: "fun" not in sample_text = False
print(f'\" \" not in sample_text = {" " not in sample_text}')  # Output: " " not in sample_text = False
print(f'\"p\" in sample_text = {'p' in sample_text}')  # Output: "p" in sample_text = False

if 'e' in sample_text and 'Python' in sample_text:
    print('\"e\" and \"Python\" are present in sample_text\n')  # Output: "e" and "Python" are present in sample_text

'''
 Operator Precedence and Associativity
========================================================================================================================

* Precedence
------------------------------------------------------------------------------------------------------------------------

 * When there are multiple operators in a single expression, then the order of evaluation is determined by
   the operator precedence.
   
 * In Python, operator precedence and associativity determine the order of evaluation in an expression with multiple 
   operators.

 * Precedence Table - Highest to Lowest
   (Reference : https://docs.python.org/3/reference/expressions.html#operator-precedence)
   
    _________________________________________________________________________________________________________________
   | Operator	| Description                                                                                       |
   ------------------------------------------------------------------------------------------------------------------
   |  (expressions...),                     | Binding or parenthesized expression, list display, dictionary display |
   |  [expressions...], {key: value...},    | , set display                                                         |
   |  {expressions...}                      |                                                                       |
   ------------------------------------------------------------------------------------------------------------------
   |  x[index], x[index:index],             | Subscription, slicing, call, attribute reference                      |
   |  x(arguments...), x.attribute          |                                                                       |
   ------------------------------------------------------------------------------------------------------------------
   |  await x	                            | Await expression                                                      |
   ------------------------------------------------------------------------------------------------------------------
   |  **	                                | Exponentiation                                                        |
   ------------------------------------------------------------------------------------------------------------------
   | +x, -x, ~x	                            | Positive, negative, bitwise NOT        	                            |
   ------------------------------------------------------------------------------------------------------------------
   | *, @, /, //, %                         | Multiplication, matrix multiplication, division, floor division,      |
   |                                        | remainder	                                                            |
   ------------------------------------------------------------------------------------------------------------------
   | + , -	                                | Addition and subtraction	                                            |
   ------------------------------------------------------------------------------------------------------------------
   | << , >>	                            | Bitwise left and right shifts	                                        |
   ------------------------------------------------------------------------------------------------------------------
   | &	                                    | Bitwise AND	                                                        |
   ------------------------------------------------------------------------------------------------------------------
   | ^	                                    | Bitwise XOR	                                                        |                                                    
   ------------------------------------------------------------------------------------------------------------------
   | |	                                    | Bitwise OR	                                                        |                           
   ------------------------------------------------------------------------------------------------------------------
   | in, not in, is, is not, <, <=, >, >=,  | Comparisons, including membership tests and identity tests            |
   | !=, ==                                 |                                                                       |
   ------------------------------------------------------------------------------------------------------------------
   | not x	                                | Boolean NOT                                                           |	                                                                                  
   ------------------------------------------------------------------------------------------------------------------
   | and	                                | Boolean AND	                                                        |                            
   ------------------------------------------------------------------------------------------------------------------
   | or	                                    | Boolean OR	                                                        |                               
   ------------------------------------------------------------------------------------------------------------------
   | if-else	                            | Conditional expression (ternary operator)	                            |                                         
   ------------------------------------------------------------------------------------------------------------------
   | =, +=, -=, *=, @=, /=, //=, %=,        | Assignment operators                                                  |
   | &=, |=, ^=, >>=, <<=, **=              |	                                                                    |
   ------------------------------------------------------------------------------------------------------------------
   | lambda	                                | Lambda expression	                                                    |                                                                
   ------------------------------------------------------------------------------------------------------------------                       
   | :=	                                    | Walrus operator (assignment expression)	                            |                                       
   ------------------------------------------------------------------------------------------------------------------

* Associativity
------------------------------------------------------------------------------------------------------------------------

 - When operators of the same precedence appear, associativity decides the order of evaluation.

 - Rules of Associativity
    
    1. Left-to-Right Associativity: Most operators, including arithmetic, bitwise, comparison, and logical operators.
'''
# This is evaluated as (10 - 4) - 2
result = 10 - 4 - 2
print(f'result = {result}')  # Output: result = 4

'''
    2. Right-to-Left Associativity: Operators like ** (exponentiation) and assignment operators.
'''
# This is evaluated as 2 ** (3 ** 2)
result2 = 2 ** 3 ** 2
print(f'result2 = {result2}\n')  # Output: result2 = 512

'''
 - Examples
 
    1. Example 1: Using Precedence
    
        In this example, multiplication (*) has higher precedence than addition (+). Therefore, this is 
        evaluated as 10 + (5 * 2) = 20
'''
precedenceResult = 10 + 5 * 2
print(f'precedenceResult = {precedenceResult}')  # Output: precedenceResult = 20

'''
    2. Example 2: Using Associativity
    
        In this example, Division (/) and multiplication (*) have the same precedence. Therefore, this is evaluated as 
         (10 / 2) * 5. Because associativity is left-to-right
'''
associativityResult = 10 / 2 * 5
print(f'associativityResult = {associativityResult}')  # Output : associativityResult: result4 = 25.0

'''
    3. Example 3: Overriding Precedence with Parentheses

        In this example, Parentheses force addition first,  then multiplication. Therefore, this is evaluated as
        (10 + 5) * 2 = 30
        
        The reason for this is that the parentheses override the default precedence of the operators. Parentheses have 
        the highest precedence/ priority.
'''
overriddenPrecedenceResult = (10 + 5) * 2
print(f'overriddenPrecedenceResult = {overriddenPrecedenceResult}')  # Output: overriddenPrecedenceResult = 30

'''
    4. Example 4: Exponentiation and Associativity

        In this example, exponentiation is right-to-left associative. Therefore, this is evaluated as 2 ** (3 ** 2) = 512
'''
exponentiationResult = 2 ** 3 ** 2
print(f'exponentiationResult = {exponentiationResult}\n')  # Output: exponentiationResult = 512

'''
 Key Tips

    1. Use parentheses to make expressions clearer and ensure the desired order of operations.
	2. Be cautious with right-to-left associative operators like ** and assignments to avoid unexpected behavior.
 
 -  Considering about unary, binary, and ternary operators (Some examples in the table below).
    Unary operators has the highest priority, and then binary, and then ternary operators.
 
 ________________________________________________________________________________________________    
 |  Type	| Definition	                |   Examples                                        |
 |----------|-------------------------------|---------------------------------------------------|
 |  Unary	| Operates on one operand	    |  +x, -x, ~x, not x                                |
 |----------|-------------------------------|---------------------------------------------------| 
 |  Binary	| Operates on two operands      |  x + y, x > y, x and y                            |
 |----------|-------------------------------|---------------------------------------------------| 
 |  Ternary	| Operates on three operands    |  x if condition else y                            |
 ------------------------------------------------------------------------------------------------  
   
 - = assignment operator will get the last priority in general.
'''

v1 = 30
v2 = 20
v3 = 10
v4 = 5

# Example 1:
newResult1 = (v1 + v2) * v3 / v4
'''
This is evaluated as:

    newResult = (30 + 20) * 10 / 5
    newResult = 50 * 10 / 5
    newResult = 500 / 5
    newResult = 100
'''
print(f'newResult1 = {newResult1}')  # Output: newResult1 = 100.0

# Example 2:
newResult2 = (v1 + v2) * (v3 / v4)
'''
This is evaluated as:
    newResult2 = (30 + 20) * (10 / 5)
    newResult2 = 50 * 2
    newResult2 = 100.0
'''
print(f'newResult2 = {newResult2}\n')  # Output: newResult2 = 100.0

# Example 3:
newResult3 = v1 + (v2 * v3) / v4
'''
This is evaluated as:
    newResult3 = 30 + (20 * 10) / 5
    newResult3 = 30 + 200 / 5
    newResult3 = 30 + 40
    newResult3 = 70.0
'''
print(f'newResult3 = {newResult3}\n')  # Output: newResult3 = 70.0

'''
Simple introduction to modules and libraries
------------------------------------------------------------------------------------------------------------------------

 1. Module
 ---------
 - Module is a file containing Python definitions and statements. In other words, a module is a group of functions, 
   variables, classes, etc. In Python, for every requirement, there is a module available. For example, the math module.
   We should import the module to use it as those are not available by default.
   
 - Module is a low-level component
   
 2. Library
 -----------

 - A library is a collection of modules. In other words, a library is a group of modules.
 
 - Library is a high-level component

* In general we say that Python has a large collection of batteries/libraries.

* Importing the math module. If not imported, it will throw an error as follows:
  NameError: name 'math' is not defined. Did you forget to import 'math'?
'''
# import math
#
# # Accessing the value of pi from the math module
# print(f'math.pi = {math.pi}')  # Output: math.pi = 3.141592653589793
#
# # Using the sqrt function from the math module
# print(f'math.sqrt = {math.sqrt(25)}')  # Output: math.sqrt = 5.0

'''
 Aliasing
 ---------
 
 - When we import a module, we can use a different name for the module. This is called aliasing.
'''
import random as r

# Generate a random integer between 1 and 10
random_number = r.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}\n")

'''
 - We can alias not only a module but also a function, class, etc. as well
'''
from json import dumps as alias_dump

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "hobbies": ["reading", "gaming", "hiking"]
}

# Convert Python dictionary to JSON string
json_data = alias_dump(data, indent=4)
print(f'json_data = {json_data}')

'''
 After aliasing, we can't use the original name of the module again in the code. In that case we will get an error.
 Once aliasing is done, we should stick to the aliased name only
'''
# random.randint(1, 10)  # NameError: name 'random' is not defined. Did you forget to import 'random'?

'''
 Accessing a specific function from a module.
 
 - Consider the following code
 
     import  os
    
    # Get the current working directory
    print(f'os.getcwd() : {os.getcwd()}')

 - Instead of importing the entire module, we can import a specific function from the module.
'''

# Here we are importing the getcwd and getenv functions only from the os module.
from os import getcwd, getenv, name

# Get the current working directory
print(f'getcwd() : {getcwd()}')

# Get the value of an environment
print(f'getenv("PATH") : {getenv("PATH")}')

# Get the name of the operating system
print(f'name : {name}')

'''
 - This approach can also be used to import multiple functions from a module. But it is not recommended.
   (In general, implicit imports are not recommended to be used in the code)

   from math import *
   print(sqrt(16)
   print(pi)
   
 - Instead of importing the entire module, we can import a specific function from the module as mentioned in the previous
   examples.
   
 - if we import as,
 
    1) import math
        
        We must use module name to call the functions and variables of the module. (ex: math.sqrt(16), math.pi)
        Importing the entire module is not recommended.
                     
    2) from math import sqrt

        We can use the function directly without using the module name. (ex: sqrt(16)). This is limited to the functions
        and variables imported. In this case, we can't use any other member of the module except sqrt.
        This is the recommended approach.
    
    3) from math import *
        
        We can use all the functions and variables of the module without using the module name.
        (ex: sqrt(16), pi, etc.). This is not a recommended approach.
'''

'''
 Some functions and values within math module
 --------------------------------------------
 
 1. pi: Returns the value of pi (3.141592653589793)
 2. e: Returns the value of e (2.718281828459045)
 3. inf: Returns the value of infinity
 4. nan: Returns the value of NaN (Not a Number)
 
 5. sin(x): Returns the sine of x (x is in radians)
 6. sqrt(x): Returns the square root of x.
 8. ceil(x): Returns the smallest integer greater than or equal to x.
 9. floor(x): Returns the largest integer less than or equal to x.
 10. pow(x, y): Returns x raised to the power of y.
 11. log(x): Returns the natural logarithm of x.
 12. factorial(x): Returns the factorial of x.
 13. gcd(x, y): Returns the greatest common divisor of x and y.
 14. cos(x): Returns the cosine of x (x is in radians)
 15. tan(x): Returns the tangent of x (x is in radians)
 
 And more....
'''

'''
 input and output statements
 =======================================================================================================================

 - In Python, input and output statements are used to interact with the user and display information to the user.
 
 1) input function
 ------------------
  
 - We can use input() function to dynamically take input from the user and read it.
 
 1) raw_input()
 2) input()
 
v 14 - 58:30
'''
