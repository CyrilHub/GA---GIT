num = 5
my_list = [1, 2, 3, 4]
index = 0

for ini_list_value in my_list:
  new_num = num * ini_list_value
  my_list.pop(index)
  my_list.insert(index,new_num)
  index += 1

print(my_list)
