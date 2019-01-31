import csv
# This line opens or creates a `names.csv` file. 
with open('names.csv', 'w', newline='') as csvfile:
  # These are the header row values at the top.
  fieldnames = ['first_name', 'last_name']
  # This opens the `DictWriter`. 
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  # Write out the header row (this only needs to be done once!). 
  writer.writeheader()
  # Write as many rows as you want! 
  writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'}) 
  writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'}) 
  writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})