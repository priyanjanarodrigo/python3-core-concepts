from random import randint  # or we can use 'from random import randint' to import all
import math
print('Python Practicals Class 2')

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


def f1():
    print("Your id is : ", id)


f1()

print(math.sqrt(4))

# Generating a sample OTP - One Time Password
print(randint(0, 9), randint(0, 9), randint(0, 9))

# removing separated spaces with sep
print(randint(0, 9), randint(0, 9), randint(0, 9),
      randint(0, 9), randint(0, 9), randint(0, 9), sep='')
