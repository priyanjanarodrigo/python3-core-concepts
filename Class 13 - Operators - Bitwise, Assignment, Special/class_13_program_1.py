print('Print the maximum of three numbers\n')

'''
- This program is to read three numbers from the user and print the maximum of the three numbers.

- In get the keyboard input from the user, we use the input() function.

- Whatever the user types in the keyboard, the input() function returns a string. Therefore, we need to convert the 
  string to an integer using the int() function.

- Note that we have not handled the exception if the user enters a non-numeric value.
'''

# Prompt the user to enter two numbers
a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number : '))
c = int(input('Please enter the third number : '))

'''
We can use max() function also to find the maximum of the three numbers (max(a, b, c))

If we use '&' instead of 'and' in the below if condition, then the program will not work as expected. 
Because & is a bitwise operator. and is a logical operator, therefore we should use 'and' instead of '&'
'''

max_value = a if (a > b and a > c) else b if (b > c) else c

print(f'The max value is : {max_value}')
