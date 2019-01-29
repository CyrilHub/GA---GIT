user_calc = input("What calculation would you like to do? (add, sub, mult, div):")
user_num1 = int(input("What is number 1?"))
user_num2 = int(input("What is number 2?"))


def print_result(output_print):
  print ("Your result is " + format(output_print) + ". Calc U later!")


if user_calc == "add":
  output_calc = user_num1 + user_num2
  print_result(output_calc)

elif user_calc == "sub":
  output_calc = user_num1 - user_num2
  print_result(output_calc)

elif user_calc == "mult":
  output_calc = user_num1 * user_num2
  print_result(output_calc)

elif user_calc == "div":
  output_calc = user_num1 / user_num2
  print_result(output_calc)

else:
  print("This is why we can't have nice things!")
