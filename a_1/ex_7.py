# Exercise 7: Sets
# - Create a set called colors with the values: "red", "green", "blue".
# - Add another color to the set.
# - Try adding a duplicate color and observe what happens.
# - Print the set and remove one color from it.
# - Create another set named light_colors and merge colors and light_colors.

colors = {'red', 'green', 'blue'}
colors.add('yellow')
colors.add('red')

print('Set:', colors)

colors.remove('yellow')
light_colors = {'light_red', 'light_green', 'light_blue'}
colors.update(light_colors)

print('Updated Set:', colors)
