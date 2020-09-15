# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [i.name for i in humans if i.name[0] == 'D']
print(a)

# for i in humans:
#     if i.name[0] == 'D':
#         print('')
#         print(i.name)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# b = [i.name for i in humans if i.name[-1] == 'e']
b = [i.name for i in humans if i.name.endswith('e')]
print(b, '\n')

# for i in humans:
#     if i.name[-1] == 'e':
#         print('')
#         print(i.name)

# # Write a list comprehension that creates a list of names of everyone
# # whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [i.name for i in humans if i.name[0] >= 'C' and i.name[0] <= 'G']
print(c, '\n')

# for i in humans:
#     if i.name[0] >= 'C' and i.name[0] <= 'G':
#         print('')
#         print(i.name)


# # Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age + 10 for i in humans]
print(d, '\n')

# for i in humans:
#     i.age + 10
#     print(i.age)


# # Write a list comprehension that creates a list of strings which are the name
# # joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# e = [i.name + '-' + format(i.age) for i in humans]
# print('["%s"]' % '", "'.join(map(str, e)), '\n')
e = [f'{person.name} - {person.age}' for person in humans]
print(e)

# for i in humans:
#     together = f'"{i.name} - {format(i.age)}"'
#     print(together)


# # Write a list comprehension that creates a list of tuples containing name and
# # age, for example ("David", 31), for everyone between the ages of 27 and 32,
# # inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if human.age > 26 and human.age < 33]
print(f)
print('')


# for i in humans:
#     print((i.name, i.age))

# # Write a list comprehension that creates a list of new Humans like the old
# # list, except with all the names uppercase and the ages with 5 added to them.
# # The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(human.name.upper(), human.age+5) for human in humans]
print('')
print(g, '\n')

# for i in humans:
#     print(i.name.upper(), i.age + 5) 

# # Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
# h = [i.name + ', ' + f'{(math.sqrt(i.age))}' for i in humans]
h = [math.sqrt(human.age) for human in humans]
print(h)
print('')
