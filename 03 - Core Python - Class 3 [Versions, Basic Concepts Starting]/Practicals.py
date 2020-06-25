import math
print('Python Program : 3 - Core Python - Class 3')


def calculateSquareRoot(value):
    return math.sqrt(value)


print(calculateSquareRoot(100))


def f1():
    print('this is f1()')


f1()

# function within an other function


def f2():
    print('this is f2()')
    f1()


f2()
