print('Class 10 - Data Types Summary, Escape Characters\n')

# None data type
print('None data type ----------------------------------------------------------------------------------------------\n')


# def is used to define a function in Python
# f1() does not return any value

def f1():
    a = 10


def f2():
    print('Hello ! don\'t be like None')


f2()  # Hello ! don't be like None

# returns None automatically as f1 does not return anything. We can use None to handle such type of scenarios
print(f1())  # Output :  None


# pass keyword
def f3():
    pass  # passing without doing anything


f3()

print('\nEscape Characters -----------------------------------------------------------------------------------------\n')


def show_escape_characters():
    print('This is a backslash \\')

    print('This is a single quote \'')

    print('This is a double quote \"')

    print('This is a tab\tThis content is after the tab')

    print('This is a new line \nThis content is after the new line')

    print('This is a carriage return \rThis content is after the carriage return\rthis should be at the beginning')

    print('Th\fis is a form fe\f\fed inclusive cont\fent')

    print('This t\vext has ve\vrti\vcal t\v\vabs in between t\vhe let\v\vters')


show_escape_characters()

# Constants
print('\nConstants -------------------------------------------------------------------------------------------------\n')
print('There is no way to define constants in Python\n')
