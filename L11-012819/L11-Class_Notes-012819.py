import itertools 

credit_cards = [("123121113", "visa"),("12312311", "visa"),("123123242443", "visa"), ("123123", "mastercard")]


def filter (x):
    return x[1]

for x,y in itertools.groupby(credit_cards, filter): 
  print (x +":")
  for tup in x: 
    print(tup[0],"is a",tup[1])
  print("\n")