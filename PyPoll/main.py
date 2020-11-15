import os
import csv
#setting up the file path
polling = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = {}



with open(polling) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
  
    for row in csvreader:
        total_votes += 1
        vote = row[2]
        if vote in candidates:
            candidates[vote] += 1
        else:
            candidates[vote]=1

print(f'Election Results')
print(f'--------------------')
print(f'Total Votes: {total_votes}')