# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Challenge 1 - Calculator

# Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

operation = input('What calculation would you like to do? (add, sub, mult, div)')
number1 = int(input('What is number 1?'))
number2 = int(input('What is number 2?'))


if (operation == 'add'):
    print(f'Your result is {number1 + number2}')
elif (operation == 'sub'):
    print(f'Your result is {number1 - number2}')
elif(operation == 'mult'):
    print(f'Your result is {number1 * number2}')
elif(operation == 'div'):
    print(f'Your result is {number1 / number2}')
else:
    print('Looks like something went wrong.')
    
