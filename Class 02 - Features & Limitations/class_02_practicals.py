print('Class 02 - Features and Limitations \n')

# Importing the math module
import math

# Importing randint from the random module
from random import randint  # or we can use 'from random import * ' to import all

# prints line after line from 0 to 2 (but not 3)
for i in range(3):
    print(i)

# Conditional checks
a, b = 23, 32
x = 10 if a > b else 20
print(x)

# Dynamically typed
val = 23
print(type(val))
val = 23.43
print(type(val))

# Procedural way
id = 102


def get_id():
    print("Your id is : ", id)


get_id()

# Finding the square root of 4 using the math module sqrt() function
print(math.sqrt(4))

# Generating a sample OTP - One Time Password
print(randint(0, 9), randint(0, 9), randint(0, 9))

# removing separated spaces with sep
print(randint(0, 9), randint(0, 9), randint(0, 9),
      randint(0, 9), randint(0, 9), randint(0, 9), sep='')

print('\n"end =" statement')
# end=' ' is used to print the next statement in the same line
print('Your OPT is :', end=f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}\n')
print('This is a new line. ', end='This is the end part of the line.\n')

print('\n"sep =" statement')
# sep=' ' is used to separate the values with the given separator
print('this', 'is', 'a', 'separated', 'phrase', sep=':')
print(randint(0, 9), randint(0, 9), randint(0, 9), sep=',')
