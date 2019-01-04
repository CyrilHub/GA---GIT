"""
Problem 1: Linear Search

Skills: Defining a function, using parameters, looping through a list, using Break effectively.

Define a function called finder() that takes two parameters: a list of arbitrary objects, and a target. The goal is to determine if the target object is in the list, and if so, where?
The function should return the index position of the target in the list, if the target exists. The function should return None if otherwise.

Concretely, consider the following examples:
    example_list =  [”Maria”, “Dana”, “David”, “Lauren”, “David”]
    finder(example_list, “Maria”) # returns 0
    finder(example_list, “David”) # returns 2
    finder(example_list, “Heather”) # returns None
"""



# Solution
def finder(objects, target):
    for i in range(len(objects)):
        if objects[i] == target:
            return i

    return None


# Tests
names = ["Maria", "Dana", "David", "Lauren", "David"]
print(finder(names, "Maria"), " should return 0")
print(finder(names, "David"), " should return 2")
print(finder(names, "Heather"), " should return None")
