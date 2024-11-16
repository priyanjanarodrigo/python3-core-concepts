print('Print the status of two numbers\n')

fNum = int(input('Insert the first number: '))
sNum = int(input('Insert the second number: '))

output = f'{fNum} is greater than {sNum}' if fNum > sNum else f'{sNum} is greater than {fNum}' if sNum > fNum else f'{fNum} and {sNum} are equal'
print(output)
