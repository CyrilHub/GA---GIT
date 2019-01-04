"""
Problem 2: Financial Analysis
You a private equity analyst doing due diligence on a company’s financial health.

I’ve given you a two lists:

Monthly_Revenue contains a list where each element represents a specific month’s revenue.
Monthly_Cost.       Contains a list where each element represents a specific month’s cost.

In both lists, the first element represents January 2015, the second element represents February 2015, and so on.

Find the following, in the most elegant (DRY) code possible:

A list of every month’s profit (Revenue - Cost). Return this list in a function called list_profit()
Define a function called average_profit() that takes a list of profits (your output from part 1) and returns the average profit across the time window (sum the profits and divide by number of months).
Define a function called max_profit() that accepts a list of profits (your output from part 1) and returns the max profit it achieved in the time window. I don’t care which month this profit was achieved in, simply the profit amount.


"""

monthly_revenue = [1099155, 1146339, 1110887, 1163262, 1041463, 1019497, 1022815, 1131341, 1021525, 1102913, 1097125, 1157347, 1046182, 1107676, 1168910, 1170435, 1059196, 1000517, 1078106, 1129654, 1184759, 1167499, 1140578, 1134326]
monthly_costs   = [945060, 979951, 925308, 995034, 971441, 968235, 923906, 907451, 904476, 960334, 920517, 990514, 974620, 923660, 911224, 976986, 986440, 963230, 900295, 961553, 951197, 961831, 949710, 974820]

def list_profit(revenues, costs):
    profit = []
    for i in range(len(monthly_revenue)):
        profit.append(monthly_revenue[i] - monthly_costs[i])

    return profit

def average_profit(profits):
    sum_profit = 0
    for elem in profits:
        sum_profit += elem
    return sum_profit / len(profits)

def max_profit(profits):
    max_profit = -1
    for elem in profits:
        if elem > max_profit:
            max_profit = elem
        else:
            pass
    return max_profit

print("List of monthly profits:")
print(list_profit(monthly_revenue, monthly_costs), "\n\n")

print("Average profit across all months:")
profit = list_profit(monthly_revenue, monthly_costs)
print(average_profit(profit), "\n\n")

print("Max Profit Over all Months:")
profit = list_profit(monthly_revenue, monthly_costs)
print(max_profit(profit), "\n\n")
