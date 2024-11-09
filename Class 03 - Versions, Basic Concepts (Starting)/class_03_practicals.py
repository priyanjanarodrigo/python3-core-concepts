print('Class 03 - Versions, Basic Concepts (Starting)\n')

import math


def calculate_square_root(value):
    return math.sqrt(value)


print(calculate_square_root(100))


def f1():
    print('this is f1()')


f1()


# function within another function
def f2():
    print('this is f2()')
    f1()


f2()
