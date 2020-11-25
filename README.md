# python-challenge
Repository contains four seperate python programs

1. PyPoll
  Reads a csv of polling data with headers Voting ID, County, Candidate
  Outputs a list of candidates and their respective vote totals/vote percentages, and declares a winner. Writes the results to a text file as well
2. PyBank
  Read a csv of financial data with headers of Date(formatted month-year), and Profits/Losses
  Outputs an analysis of total months, total profit/loss, average monthly change, month with greatest increase, month with greatest decrease
  Also writes the results to a text file
3. PyBoss
  main.py reads in a csv of employee data with headers employee id, name, dob (year-month-day), ssn, state name
  Uses the function in conversion.py (couldn't figure out how to import it right, so it's just rewritten in main)
    to convert to employee id, first name, last name, dob(mm/dd/yyyy), ssn (*** - ** - 1234), state abbreviation
  Rewrites the converted data into a new csv
4. PyParagraph
  Reads in a text file and performs analysis to check the complexity of the writing
  Computes an approximate word count and sentence count, as well as an average word length (in letters) and average sentence length (in words)
  Having trouble getting python to split on sentences that end in a quotation. 
    I got the second text file about movies to condense to one line (without all the new line  characters), 
    but not sure why it isn't recognizing the periods at the end of the sentences that have a quotation mark. 
    Oddly enough, it still gets close because it did split sentences on the period used for someone's middle initial.

    
  
 
