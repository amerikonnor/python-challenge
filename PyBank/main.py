import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#setting counters for months and totals to 0
months = 0
total = 0

#keeping track of previous month amount outside the loop
#to calculate month-to-month changes

previous_month = 0
change = 0
total_change = 0

#setting up to log the greatest increase, decrease data
greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 0
greatest_decrease_month = ""


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
        if months == 1:
         pass
        else:
            change = amount - previous_month
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = month
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = month
        
        previous_month = amount

average_change = total_change/months
#printing to the console
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

#creating/opening the analysis text file
output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w", newline="") as analysis:
    
    #writing the analysis to the text file
    analysis.write(f'Financial Analysis\n')
    analysis.write(f'-------------------------\n')
    analysis.write(f'Total Months: {months}\n')
    analysis.write(f'Total: ${total}\n')
    analysis.write(f'Average Change: ${average_change:.2f}\n')
    analysis.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    analysis.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

