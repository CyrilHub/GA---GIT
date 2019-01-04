def finder(object,target):
    index = 0
    for name in object_list:
        #? Is it possible to get the index based on item of name?
        if name == target:
            return index
        index += 1
    return None


object_list = ["Maria","Dana","David","Lauren","David"]
look_for = "Dan"

finder(object_list,look_for)
