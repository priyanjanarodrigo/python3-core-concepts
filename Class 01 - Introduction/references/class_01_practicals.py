print('Class 01 - Introduction \n')

# Concise code with Python - Comparison with Java
'''
Java Program to print Hello World

    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello World");
        }
    }
'''

'''
The following is the Python equivalent of the above Java program.
With Python, we only needed one line of code to print Hello World.
'''

print("Hello World")

'''
Java program to calculate the total of two numbers

    public class Calculation {
        public static void main(String[] args) {
            int a = 10;
            int b = 20;
            int total = a + b;
            System.out.println("Total = " + total);
        }
    }
'''

'''
The following is the Python equivalent of the above Java program.
With Python, we only needed two lines of code to print Hello World.
'''

a, b = 20, 10
print(f'Total = {a + b}')

'''
Dynamic Typing - Python allows variables to change their data type during runtime. In the code, variable 'a' first holds
an integer value (10) and then is reassigned to hold a boolean value (True). The type() function shows this dynamic type
change.
'''

# Declaring the variables a, b and assigning initial values as 10 and 20 accordingly
a, b = 10, 20
print(f'Data type of a is {type(a)}')

# Reassigning a boolean value to a
a = True
print(f'Data type of a is {type(a)}')


# Example function definition. This functions can exist without having a class definition.
def say_hello():
    print("Hello World", end='. Python is easy to learn')


# Calling the function
say_hello()  # Output: Hello World. Python is easy to learn
