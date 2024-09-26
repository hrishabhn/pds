# Exercise 8: Conditional Statements
# - Write a program that:
#     - Takes an input number from the user.
#     - Checks if the number is positive, negative, or zero.
#     - Prints an appropriate message based on the result.

number = int(input('Enter a number: '))

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')
