#
# Problem 3: How many are we talking?
# You’re an IT manager at a large (and totally made-up) credit-monitoring company,
# Equifacts. Your team reports they detected a breach, in which an unknown number
# of social security numbers have been leaked.
#
# You go to “SocialSecurityNumbersForCheap.com” and download the database of numbers stolen
# from your database. But the data is messy, and there seems to be many duplicates.
#
# I’ve provided the list of social security numbers below:
#
# ss_numbers = [“1234567890”, “4353453390”, “5564435678”, ...]
#
# This list contains duplicates. Find the number of UNIQUE social security numbers
# leaked ASAP so you can send the report to your boss.

# Problem Solving Advice: I strongly recommend that you start with your own SIMPLIFIED and SHORTENED
# list of "social security numbers" for easier debugging. You can run your function on the real
# list I've provided later :)

ss = ['605459141','642780462', '502226390', '605459141', '967844690', '822882635', '884194807',
'324324322', '945418445', '967844690','715993228', '343416534', '360189400', '597138344',
'889537330', '791174052', '514363366', '722787843', '109117347', '736257459',
'133439624', '160806690', '889537330', '715993228']


# Intuition: iterate through the list. For each element,
# determine if we had already seen the element before, by tracking, in a
# separate list, the elements we had already seen.


# I copied over the solution from problem 1.
def finder(objects, target):
    for i in range(len(objects)):
        if objects[i] == target:
            return i

    return None

def real_damage_count(ss_numbers):

    seen_already = [] # a list to keep track of which numbers we'd already seen.


    for elem in ss_numbers:
        if finder(seen_already, elem) == None:
            seen_already.append(elem)
        else:
            pass

    return len(seen_already)
    # return the size of the list of elements we have already seen,
    # since it should contain everything we'd seen exactly once.



## Test Code
test_list = ["1", "2", "3", "4", "1", "2", "3"]
print(real_damage_count(test_list), "should return 4.")


test_list = ["1", "2", "3", "4", "1", "1", "1", "5"]
print(real_damage_count(test_list), "should return 5.")

test_list = []
print(real_damage_count(test_list), "should return 0.")
