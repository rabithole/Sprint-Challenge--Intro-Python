# The following list comprehension exercises will make use of the 
# defined Human class. 
import math
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
# a = []
# for name in humans:
a = [name.name for name in humans if name.name[0] == 'D']
    # a = [name[0] for name in humans]
    # if name.name[0] == 'D':
    #     a.append(name.name)
        # print(name.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [name.name for name in humans if name.name[-1] == 'e']
# for name in humans:
#     if name.name[-1] == 'e':
#         b.append(name.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [name.name for name in humans if name.name[0] == 'C' or name.name[0] == 'D' or name.name[0] == 'E' or name.name[0] == 'F' or name.name[0] == 'G']
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [name.age + 10 for name in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [name.name + '-' + format(name.age) for name in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [human.name + ', ' +  format(human.age) for human in humans if human.age >= 27 and human.age <= 32]
# f = [ ]

print('Line 68: ', f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [name.name.upper() + ', ' + format(name.age + 5) for name in humans]
# g = []
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(human.age) for human in humans]
print(h)
