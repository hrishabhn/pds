# Exercise 5: Dictionaries
# - Create a dictionary called student with keys: name, age, and grade, and assign appropriate values to each key.
# - Write a program that prints each key-value pair in the dictionary.

student = {
    'name': 'Hrishabh',
    'age': 23,
    'grade': 100,
}

for key, value in student.items():
    print(f'{key}: {value}')
