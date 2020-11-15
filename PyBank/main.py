import os
import csv

months = 0
total = 0

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  
    csv_header = next(csvreader)

    for row in csvreader:
        month = row[0]
        amount = int(row[1])
        months += 1
        total += amount
        

print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')