# Exercise 17: Simple Calculator
# - Write a program that:
#     - Defines a function calculate which takes three parameters: two numbers and an operator (+, -, *, /).
#     - Performs the operation and returns the result.
#     - Ask the user for the two numbers and the operator, then call the function and print the result.

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'Invalid operator'


number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))
operator = input('Enter the operator (+, -, *, /): ')

result = calculate(number_1, number_2, operator)

print('Result:', result)
