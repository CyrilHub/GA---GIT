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

ss = ['605459141','642780462', '502226390', '605459141', '605459141', '642780461']
ss_target = []
# '967844690', '822882635', '884194807',
#'324324322', '945418445', '967844690','715993228', '343416534', '360189400', '597138344',
#'889537330', '791174052', '514363366', '722787843', '109117347', '736257459',
#'133439624', '160806690', '889537330', '715993228']


'''
def real_damage_count(ss_numbers):

    # take first first number
    # creat new list with out number
    # if a duplicate is found it poped out of the main list

    for SS_number in ss
        i = 0
'''


def real_damage_count(base_list, no_duplicate_list):
    no_duplicate_list.append(base_list[0])

    for ss_number in base_list:

      if ss_number in no_duplicate_list:
          pass
      else:
          no_duplicate_list.append(ss_number)
      print ("base list :", base_list)
      print ("no duplicate list :", no_duplicate_list)


real_damage_count(ss, ss_target)
