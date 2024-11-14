print('Class 10 - Data Types Summary, Escape Characters\n')

# Data types summary
print('Data types summary ------------------------------------------------------------------------------------------\n')

# 1. int

employee_id: int = 100
print(f'employee_id = {employee_id}\n')  # Output: employee_id = 100

# 2. float

salary: float = 120300.50
print(f'salary = {salary}\n')  # Output: salary = 120300.34

# 3. complex

complex_number: complex = 10 + 2j
print(f'complex_number = {complex_number}\n')  # Output: complex_number = (10+2j)

# 4. bool

is_permanent: bool = True
print(f'isPermanent = {is_permanent}\n')  # Output: is_permanent = True

# 5. str

name: str = 'John Doe'
print(f'name = {name}\n')  # Output: name = John Doe

# 6. bytes

number_list: list = [10, 20, 30, 40, 50]
bytes_data: bytes = bytes(number_list)
print(f'bytes_data = {bytes_data}')  # Output: bytes_data = b'\n\x14\x1e('
for b in bytes_data:
    print(b)

text: str = 'hello_all'
bytes_data_of_string = bytes(text, 'utf-8')
print(f'\nbytes_data_of_string = {bytes_data_of_string}')  # Output: bytes_data = b'hello_all'
for b in bytes_data_of_string:
    print(b)

# 7. byteArray

new_number_list: list = [10, 20, 30, 40, 50]
byte_array_data: bytearray = bytearray(new_number_list)
print(f'\nbyte_array_data = {byte_array_data}')  # Output: byte_array_data = bytearray(b'\n\x14\x1e(')
for b in byte_array_data:
    print(b)

# 8. range

range_data: range = range(3)
print(f'\nrange_data = {range_data}')  # Output: range_data = range(0, 3)
for num in range_data:
    print(num)

# 9. list

flower_list: list = ['rose', 'lily', 'jasmine', 'lotus']
flower_list.append('sunflower')
flower_list.remove('jasmine')
print(f'\nflower_list = {flower_list}')  # Output: flower_list = ['rose', 'lily', 'lotus', 'sunflower']

# 10. tuple

brands: tuple = ('BMW', 'Audi', 'Mercedes', 'Toyota')
print(f'\nbrands = {brands}')  # Output: brands = ('BMW', 'Audi', 'Mercedes', 'Toyota')
# tuple[1] = 'Honda'  # TypeError: 'type' object does not support item assignment

# 11. set

my_character_set: set = {'a', 'e', 'i', 'o', 'u'}
my_character_set.add('z')
my_character_set.remove('a')
print(f'\nmy_character_set = {my_character_set}')  # Output: my_character_set = {'i', 'e', 'z', 'o', 'u'}

# 12. frozenset

words_frozenset: frozenset = frozenset({'hello', 'world'})
print(f'\nwords_frozenset = {words_frozenset}')  # Output: words_frozenset = frozenset({'hello', 'world'})
# frozenset[0] = 'hi' # TypeError: 'type' object does not support item assignment

# 13. dict

employee_dict: dict = {'id': 100, 'name': 'John Doe', 'salary': 120300.50}
employee_dict.update({'salary': 120300.50})
employee_dict.pop('name')
employee_dict['age'] = 30
print(f'\nemployee_dict = {employee_dict}')  # Output: employee_dict = {'id': 100, 'salary': 120300.5, 'age': 30}

# 14. defaultdict

from collections import defaultdict

my_default_dict: defaultdict = defaultdict(int)
print(f'\nmy_default_dict = {my_default_dict}')  # Output: my_default_dict = defaultdict(<class 'int'>, {})

phrase: str = 'hello'

for c in phrase: my_default_dict[c] += 1

# my_default_dict = defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})
print(print(f'\nmy_default_dict = {my_default_dict}'))

# None data type
print('\nNone data type --------------------------------------------------------------------------------------------\n')


# def is used to define a function in Python
# f1() does not return any value

def f1():
    a = 10


# returns None automatically as f1 does not return anything. We can use None to handle such type of scenarios
print(f1())  # Output :  None


def f2():
    print('Hello ! don\'t be like None')


f2()  # Hello ! don't be like None


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
