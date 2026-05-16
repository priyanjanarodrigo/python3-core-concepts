print('Class 03 - Versions, Basic Concepts\n')

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


def print_text(msg: str):
    print(f'Message:  {msg}')

print_text(' Hello, welcome to Python programming!')

if __name__ == '__main__':
    print_text('Hello, welcome to Python programming!')
