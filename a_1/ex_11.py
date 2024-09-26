# Exercise 11: Match Statement
# - Write a program that:
#     - Asks the user to input a grade (e.g., "A", "B", "C", "D", or "F").
#     - Use a match statement to print a corresponding message for each grade:
#         - "A": "Excellent!"
#         - "B": "Good job!"
#         - "C": "Fair."
#         - "D": "Needs improvement."
#         - "F": "Failing."
#     - Handle invalid input by printing a default message.

grades = {
    'A': 'Excellent!',
    'B': 'Good job!',
    'C': 'Fair.',
    'D': 'Needs improvement.',
    'F': 'Failing.',
}

user_grade = input('Enter your grade: ')

print(grades.get(user_grade, 'Invalid input!'))
