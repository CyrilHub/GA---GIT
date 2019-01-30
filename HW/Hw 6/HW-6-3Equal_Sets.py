fruits = ['orange', 'pear', 'kiwi', 'apple', 'banana']
fruits_copy = ['orange', 'pear', 'kiwi', 'apple', 'banana']
fruits_reordered = ['pear', 'apple', 'kiwi', 'orange', 'banana']
print("Copy comparison", fruits == fruits_copy)
print("Reordered comparison", fruits == fruits_reordered)

print()

# Converted above list to sets
fruits = {'orange', 'pear', 'kiwi', 'apple', 'banana'}
fruits_copy = {'orange', 'pear', 'kiwi', 'apple', 'banana'}
fruits_reordered = {'pear', 'apple', 'kiwi', 'orange', 'banana'}
print("Copy comparison", fruits == fruits_copy)
print("Reordered comparison", fruits == fruits_reordered)

# Does the output of the two print statements change?
    # Yes
# Why?
    # Because sets don't have order, as oppose to list, where order matter.

    