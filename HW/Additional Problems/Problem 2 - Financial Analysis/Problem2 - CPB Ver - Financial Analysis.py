


def pb_statement ():
    pass
    '''
    def pb_statement ():
        pass
    Problem 2: Financial Analysis
    You a private equity analyst doing due diligence on a company’s financial
    health.

    I’ve given you a two lists:

    Monthly_Revenue contains a list where each element represents a specific
    month’s
     revenue.
    Monthly_Cost.       Contains a list where each element represents a specific
    month’s cost.

    In both lists, the first element represents January 2015, the second element
    represents February 2015, and so on.

    Find the following, in the most elegant (DRY) code possible:

    - A list of every month’s profit (Revenue - Cost). Return this list in a function
    called list_profit()

    - Define a function called average_profit() that takes a list of profits
    (your output from part 1) and returns the average profit across the time window
    (sum the profits and divide by number of months).

    - Define a function called max_profit() that accepts a list of profits
    (your output from part 1) and returns the max profit it achieved in the time
    window. I don’t care which month this profit was achieved in, simply the profit
     amount.
     '''



monthly_revenue = [1099155, 1146339, 1110887, 1163262, 1041463, 1019497, 1022815, 1131341, 1021525, 1102913, 1097125, 1157347, 1046182, 1107676, 1168910, 1170435, 1059196, 1000517, 1078106, 1129654, 1184759, 1167499, 1140578, 1134326]
monthly_costs   = [945060, 979951, 925308, 995034, 971441, 968235, 923906, 907451, 904476, 960334, 920517, 990514, 974620, 923660, 911224, 976986, 986440, 963230, 900295, 961553, 951197, 961831, 949710, 974820]


'''- A list of every month’s profit (Revenue - Cost).
Return this list in a function called list_profit()'''
def list_profit(revenues, costs):
    profit_monthly_aggregate = []
    for i in range(len(revenues)):
        profit_monthly_aggregate.append(revenues[i] - costs[i])
    return profit_monthly_aggregate

#Test: for list_profit
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
list_profit_returned = list_profit(monthly_revenue, monthly_costs)
print(list_profit_returned)



#Define a function called average_profit() that takes a list of profits
#(your output from part 1) and returns the average profit across the time window
#sum the profits and divide by number of months).
def average_profit(profits):
    print ("TEST:1: in average_profit ")
    total_profit_value = 0
    for i in range(len(profits)):
        #TEMP TEST::
        print ("TEST:2: index for profit " + str(i))
        print ("TEST:3: profits[i]" + str(profits[i]))
        print ("TEST:4: total_profit_value " + str(total_profit_value))
        total_profit_value += profits[i]
    average_profit_value = total_profit_value / len(profits)
    return average_profit_value

#TEST
average_profit_returned = average_profit(list_profit_returned)
print("TEST:5: average_profit_value " + str(average_profit_returned))


'''
- Define a function called max_profit() that accepts a list of profits
(your output from part 1) and returns the max profit it achieved in the time
window. I don’t care which month this profit was achieved in, simply the profit
 amount.
'''

def max_profit(profits):
    max_profit_value = max(profits)
    return max_profit_value

max_profit_returned = max_profit(list_profit_returned)
print ("TEST:6: max_profit_returned = " + str(max_profit_returned))
