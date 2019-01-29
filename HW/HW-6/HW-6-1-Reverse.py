state_capitals = {
"Alaska" : "Juneau",
"Colorado" : "Denver",
"Oregon" : "Salem",
"Texas" : "Austin"
}

# Input value to find matching key to
# Take dictionary and print the key - > value
# compare if the value printed is the same
## if so print the key
# Input value

def reverse_lookup(dictionary, target):
    for dict_key in dictionary:
        dict_value = dictionary[dict_key]      
        if dict_value == target:
            print  (dict_key)

        


reverse_lookup(state_capitals, "Denver")
# Prints Colorado