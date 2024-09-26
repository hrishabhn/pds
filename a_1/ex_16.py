# Exercise 16: Nested Data Structures
# - Create a dictionary where the keys are names of students and the values are lists of their grades.
# - Write a function that takes the dictionary and prints the average grade for each student.

students = {
    'Larry': [100, 95, 90],
    'Jeff': [10, 20, 30],
    'Cheryl': [40, 50, 60],
    'Suzie': [70, 80, 90],
    'Leon': [100, 100, 100],
}


def print_avg_grades(students):
    for student, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f'{student}: {avg}')


print_avg_grades(students)
