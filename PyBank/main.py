import os
import csv

months = 0
total = 0
total_change = 0

greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 0
greatest_decrease_month = ""
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  
    csv_header = next(csvreader)

    for row in csvreader:
        
        month = row[0]
        amount = int(row[1])
       
        #count the total months
        months += 1

        #keep track of the total
        total += amount
        
        #to keep track of the month to month change, skip it the first time
        #but the first month will have the greatest increase and decrease in profits so far
        if months == 1:
            greatest_increase = amount
            greatest_increase_month = month
            greatest_decrease = amount
            greatest_decrease_month = month
        else:
            pass

        
average_change = total_change/months
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: {average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')