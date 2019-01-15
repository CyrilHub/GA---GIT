swanson = {
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": ",000"
}

knope = {
    "name": "Leslie Knope",
    "age": 11,
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": ",111"
}

dwyer = {
    "name": "Andy Dwyer",
    "age": 22,
    "department": "Shoe Shining",
    "phone": "555-1122",
    "salary": ",222"
}

ludgate = {
    "name": "April Ludgate",
    "age": 33,
    "department": "Administration",
    "phone": "555-3345",
    "salary": ",333"
}

employees = [swanson, knope, dwyer, ludgate]


def print_info(name):
    print (name["name"], " in ", name["department"], " can be reached at ", name["phone"], ".", sep="")


def print_info_all(list):
    for i in list:
        print (print_info(i))

print_info_all(employees)
