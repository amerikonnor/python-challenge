import os
import csv
#setting up the file path
polling = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_list = {}



with open(polling) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
  
    for row in csvreader:
        print(row)