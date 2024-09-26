# Exercise 15: List Comprehension
# - Create a list of numbers from 1 to 10.
# - Use list comprehension to create a new list that contains the squares of these numbers.
# - Print the new list.

numbers = list(range(1, 11))

squares = [number ** 2 for number in numbers]

print(squares)
