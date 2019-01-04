object_list = ["Maria","Dana","David","Lauren","David"]
look_for = "David"

def finder(object,target):
    index = 0
    for name in object_list:
        #? Is it possible to get the index based on item of name?

        if name == target:
            print (name + "-->" + format(index))
        index += 1


finder(object_list,look_for)
