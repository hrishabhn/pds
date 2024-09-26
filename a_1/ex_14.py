# Exercise 14: Function with Default Parameters
# - Write a function called multiply that takes two parameters, a and b, and returns their product. Set a default value of 1 for the parameter b.
# - Test the function with and without providing the second argument.

def multiply(a, b=1):
    return a * b


print(multiply(3, 2))
print(multiply(3))
