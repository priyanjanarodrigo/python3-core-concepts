print('Class 04 - Practical - S02 - Reserved Words\n')

# Import keyword is used to import modules in Python.
import keyword
# from keyword is used to import specific functions or variables from a module.
from random import randint

'''
keyword.kwlist shows all the hard keywords in Python that are strictly reserved and cannot be used as identifiers 
(variable names, function names, etc.). These include words like 'if', 'else', 'while', 'for', 'def', 'class', etc.
'''
print(f'keyword.kwlist:\n{keyword.kwlist}')
print(f"Total keywords: {len(keyword.kwlist)}\n")

'''
keyword.softkwlist shows the soft keywords in Python, which are context-sensitive and have special meaning only in 
specific contexts. They can sometimes be used as identifiers in other contexts. For example, 'match' and 'case' are soft
keywords used in pattern matching (introduced in Python 3.10).
'''
print(f'keyword.softkwlist:\n{keyword.softkwlist}\n')

print('\nimport and as keywords\n-----------------------------------------------------------------------------------\n')

# Importing the math module as math_module_alias
import math as math_module_alias

print(f'math_module_alias.sqrt(16) = {math_module_alias.sqrt(16)}')

print('\nTrue, False, and None keywords\n-----------------------------------------------------------------------------')

initial_value = None
print(f'initial_value: {initial_value}')

# myBoolean=true is not valid
myBoolean = True
print(myBoolean)

# yourBoolean=false is not valid.
yourBoolean = None
print(yourBoolean)

print(type(yourBoolean))  # Prints the type of the variable
id(yourBoolean)  # Prints the memory address of the variable

# This does not assign False as the default value if we are not explicitly assigning a value to the variable.
isPermitted: bool

isPermitted = True if randint(0, 100) > 50 else False

print(f'isPermitted: {isPermitted}\n')

print('\nand, or, not, is, if, else and elif keywords\n---------------------------------------------------------------')

num1, num2 = randint(-10, 10), randint(-10, 10)
print(f'num1: {num1}, num2: {num2}\n')

if num1 > 0 and num2 > 0:
    print(f'Both {num1} and {num2} are positive numbers')
elif num1 < 0 and num2 < 0:
    print(f'Both {num1} and {num2} are negative numbers')
else:
    print(f'One of {num1} and {num2} is negative and the other is positive')

word1, word2 = 'hello', 'world'
print(f'\nword1: {word1}, word2: {word2}\n')

'''
The == operator in Python automatically calls __eq__() behind the scenes, so there's no need to call it explicitly. 
This is a great example of Python's principle of explicit is better than implicit, while still maintaining clean and 
readable code.

if str.__eq__('hello', word1) or str.__eq__('hello', word2):

Therefore the above code can be simplified to the following:
'''

if word1 == 'hello' or word2 == 'hello':
    print(f'"{word1}" or "{word2}" is equal to "hello"')

value = randint(-10, 10)

# Using not keyword ( we have "not" keyword instead of ! operator)
if not (value > 0):
    print(f'{value} is not greater than 0')
else:
    print(f'{value} is greater than 0')

# The is keyword checks for object identity, meaning it returns True if two variables point to the same object in memory.
listA = [1, 2, 3]
listB = listA  # Both a and b refer to the same list
listC = [1, 2, 3]  # obamaList is a different list with the same content

print(f'\nlistA is listB : {listA is listB}')
print(f'\nlistA is listC : {listA is listC}')

sampleText: str = '  '
isValidText = True if sampleText is not None and len(sampleText.strip()) > 0 else False
print(f'\nisValidText: {isValidText}')

print('\nwhile, for, break, continue, return, in and yield keywords\n-------------------------------------------------')

counter = 0
while counter < 10:

    # if the counter value is equals to 3, then break the loop
    if counter == 3:
        print(f'counter is equals to {counter}, therefore breaking the loop\n')
        break

    print(f'counter: {counter}')
    counter += 1

''' 
in keyword checks for membership in a sequence (like lists, tuples, dictionaries, strings range, etc.) 

continue keyword is used to skip the current iteration of a loop and move to the next iteration.
'''
for i in range(5):
    if i == 2:
        print(f'i is equals to 2, therefore skips the current iteration and continue to the next iteration in loop')
        continue

    # this will be skipped if i value is equals to 2
    print(f'square of {i} is {i * i}')


# return keyword is used to exit a function and return a value.
def get_largest_number(firstNumber, secondNumber):
    return firstNumber if firstNumber > secondNumber else secondNumber


print(f'\nthe largest number between 33 and 66 is {get_largest_number(33, 66)}\n')

'''
yield keyword:
------------------------------------------------------------------------------------------------------------------------
yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like 
an iterator object.

In layman terms, the yield keyword will turn any expression that is given with it into a generator object and return it
to the caller. Therefore, you must iterate over the generator object if you wish to obtain the values stored there.

Difference between return and yield Python:
------------------------------------------------------------------------------------------------------------------------
The yield keyword in Python is similar to a return statement used for returning values in Python which returns a 
generator object to the one who calls the function which contains yield, instead of simply returning a value. The main
difference between them is, the return statement terminates the execution of the function. Whereas, the yield statement
only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield
statements are executed when the function resumes its execution.

Source: (https://www.geeksforgeeks.org/python-yield-keyword/, 2024)

The yield keyword in Python is used within a function to turn it into a generator. When yield is used, it allows the 
function to return a value and “pause” its state, enabling it to resume from that point the next time it’s called. 
This is useful for producing a sequence of values over time without having to create and store them in memory all 
at once.
'''

'''
Explanation:

1.	Generator Function  : count_up_to is a generator function because it uses yield. Instead of returning a 
	                      single value, it yields values one at a time.
2.	Yielding Values     : Each time yield is called, the function’s state is saved, and it produces the next value in 
                          the sequence (count).
3.	Iterating           : When used in a loop, like for number in count_up_to(5), it goes through each yielded value one
                          by one, printing numbers from 1 to 5.
'''


# yield keyword is used to return a value from a function and suspend the function's state so that it can be resumed
def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1


# Using the generator
for number in count_up_to(5):
    print(f'num: {number}')

print('\nclass, def, try, except, finally, as, raise, pass and assert keywords\n--------------------------------------')


# Custom exception class definition
class MyCustomException(Exception):

    # Default constructor
    def __init__(self, message: str = 'Default exception message'):
        super().__init__(message)


def divide_numbers(firstNumber, secondNumber):
    try:
        return firstNumber / secondNumber
    except ZeroDivisionError:
        print('ZeroDivisionError exception occurred')
        raise MyCustomException('This is a custom exception. Division by zero is not possible')
    except Exception as otherException:
        print(f'Exception occurred: {otherException}')
    finally:
        print('This is the end of the program')


divide_numbers(randint(1, 10), randint(0, 2))

'''
Explanation:
	try: The code within this block is attempted first. If it raises an exception, Python will move to the appropriate
	except block.
	•	except ValueError as e: Catches and handles cases where the input cannot be converted to an integer.
	•	except ZeroDivisionError as e: Handles the specific error of dividing by zero.
	•	except Exception as e: Acts as a catch-all for any other exceptions, allowing flexibility if the exact error 
	    type is unknown.
	•	else: Executes if no exceptions occur, showing the result.
	•	finally: Runs regardless of whether an exception occurred, often used for cleanup actions.
'''
try:
    num = randint(0, 5)
    result = 10 / num
except ValueError as e:
    print(f"ValueError: {e} - You must enter a valid number.")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e} - Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("Execution complete.")


def demo_pass():
    for i in range(5):
        if i < 3:
            # pass keyword is used to define a null statement in Python.
            pass
        else:
            print(f'i is equals to {i}')


demo_pass()

'''
assert Keyword in Python
-------------------------

In simpler terms, we can say that assertion is the boolean expression that checks if the statement is True or False. 
If the statement is true then it does nothing and continues the execution, but if the statement is False then it stops
the execution of the program and throws an error.

Syntax:
--------

assert <CONDITION>, <ERROR_MESSAGE(optional)> 

CONDITION       : The boolean condition returning true or false. 
ERROR_MESSAGE   : The optional argument to be printed in console in case of AssertionError

Returns: Returns AssertionError, in case the condition evaluates to false along with the error message which when
provided. 
'''

xValue = "test123"
assert xValue == "test123", "xValue should be 'test123'"

yValue = "hello"
assert yValue == "hello", "yValue should be 'hello'"

# This will raise an AssertionError as yValue is not equal to "yes"
# assert yValue == "yes", "yValue should be 'hello'"

print('\nglobal, nonlocal, lambda, dell, and with keywords\n----------------------------------------------------------')

'''
global Keyword

The global keyword allows you to modify a variable that exists in the global scope (outside the current function or 
local scope). Without using global, any assignment to a variable inside a function would create a local variable.

Explanation: 

Here, myNumber is defined as a global variable. Inside the increment_my_number function, we use global 
myNumber to modify the global myNumber variable rather than creating a new local variable.
'''

# Declare a global variable called 'myNumber'
myNumber = 0


def increment_my_number():
    global myNumber  # Declare that we want to use the global 'myNumber' variable
    # myNumber = 0 will not work because it creates a local variable
    myNumber += 1


increment_my_number()
print(f'myNumber : {myNumber}')  # Output: 1

'''
nonlocal Keyword

The nonlocal keyword is used in nested functions to modify a variable in the nearest enclosing (non-global) scope.

Explanation:

nonlocal count allows the inner function to modify the count variable from the outer function’s scope.
'''


def outer():
    count = 0

    def inner():
        nonlocal count  # Modify the 'count' variable in the enclosing 'outer' function
        count += 1
        print("Inner count:", count)

    inner()
    print("Outer count:", count)


outer()

'''
lambda Keyword

The lambda keyword is used to create small anonymous functions without a name. Lambda functions are often used for 
short, simple operations and are limited to a single expression.

Explanation: lambda x, y: x + y creates an anonymous function that takes x and y as parameters and returns their sum. 
Here, add is a reference to this function, which we can call like a regular function.
'''

# Lambda function to add two numbers
add = lambda x, y: x + y
print(f'lambda function output : {add(5, 3)}')  # Output: 8

# Another example of lambda function
get_phrase = lambda message, number1, number2: f'{message} : {(number1 + number2)}'
print(get_phrase('The sum of 10 and 2 is', 10, 2))  # Output: The sum of 5 and 3 is 8

'''
del Keyword

The del keyword deletes an object, such as a variable, list item, or dictionary entry.

Explanation:

del temp_variable deletes the variable temp_variable. del my_list[2] removes the element at index 2 from the list, 
and del my_dict['a'] removes the key 'a' from my_dict.
'''

# Delete a variable
temp_variable = 10
del temp_variable  # Now, 'temp_variable' is no longer defined

# Delete a list element
my_list = [1, 2, 3, 4]
print(f'my_list before : {my_list}')

del my_list[2]
print(f'my_list after : {my_list}')  # Output: [1, 2, 4]

# Delete a dictionary key
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f'my_dict before : {my_dict}')

del my_dict['a']
print(f'my_dict after : {my_dict}')  # Output: {'b': 2, 'c': 3}

'''
with Keyword

The with statement simplifies exception handling in context management. It’s commonly used for managing resources like 
file handling, where the file is automatically closed after the block is executed, even if an error occurs.

Explanation:

with open('example.txt', 'r') as file: opens a file and assigns it to the variable file. After the block of code 
finishes executing, the file is automatically closed, even if an error occurs within the block.
'''

print('\nprinting the content of the file using with keyword\n')

# Open a file, read its contents, and automatically close it after the block
with open('resources/example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to explicitly close the file; 'with' handles it.

print('\nmatch and case keywords\n------------------------------------------------------------------------------------')

'''
 Explanation: 
	•	match shape: Begins a match block on the shape dictionary.
	•	case {“type”: …}: Each case pattern matches a specific dictionary structure.
	•	For instance, {"type": "circle", "radius": r} matches if shape is a dictionary with type equal to "circle" and 
	    has a radius key. If it matches, r is assigned the radius value.
	•	case _: The underscore (_) is a wildcard and acts as a “default” case, catching anything that doesn’t match the
	    previous cases.

 This approach is especially useful in Python when handling JSON-like data structures or other dictionaries with various
 formats.
'''

print('\nmatch and case keywords based example 1 :\n')


def describe_shape(shape):
    match shape:
        case {"type": "circle", "radius": r}:
            print(f"A circle with radius {r}")
        case {"type": "rectangle", "width": w, "height": h}:
            print(f"A rectangle with width {w} and height {h}")
        case {"type": "square", "side": s}:
            print(f"A square with side {s}")
        case _:
            print("Unknown shape")


describe_shape({"type": "circle", "radius": 5})
describe_shape({"type": "rectangle", "width": 10, "height": 20})
describe_shape({"type": "square", "side": 15})
describe_shape({"type": "triangle", "base": 5, "height": 10})

print('\nmatch and case keywords based example 2 :\n')


def check_value(case_value):
    match case_value:
        case 1:
            print("The value is one.")
        case "hello":
            print("The value is a greeting.")
        case [x, y]:
            print(f"The value is a list with two elements: {x} and {y}")
        case _:
            print("Unknown value")


# Examples
check_value(1)  # Output: The value is one.
check_value("hello")  # Output: The value is a greeting.
check_value([3, 4])  # Output: The value is a list with two elements: 3 and 4
check_value(42)  # Output: Unknown value
