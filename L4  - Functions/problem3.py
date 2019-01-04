user_entry = input("Please enter your favorite word:")

reverse_entry = []
for letter in user_entry:

  reverse_entry.insert(0,letter)

# join source: https://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string
output_reverse_entry = "".join(reverse_entry)
print (user_entry)
print (output_reverse_entry)
