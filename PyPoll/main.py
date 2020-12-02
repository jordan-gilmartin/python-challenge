#Dependencies
import os
import csv

#File location
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
# Create lists for the variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #Total Votes
    total_votes = (len(votes))

    #Votes by Candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    
    
    #Percentages
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

    #Print Statements

    print(f"Election Results")
    print(f"-----------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------------------------")
    print(f"Khan: {khan_percent}% ({khan_votes})")
    print(f"Correy: {correy_percent}% ({correy_votes})")
    print(f"Li: {li_percent}% ({li_votes})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    print(f"-----------------------------------")
    print(f"Winner: {winner}")
    print(f"-----------------------------------")


    # Output file
    output_file = os.path.join("python-challenge", "PyBank", "Election_Results.txt")

    with open(output_file,"w",) as datafile:
    
    # Write Financial Analysis to .txt file 
        datafile.write(f"Election Results \n") 
        datafile.write(f"----------------------------------- \n") 
        datafile.write(f"Total Votes: {total_votes} \n") 
        datafile.write(f"----------------------------------- \n") 
        datafile.write(f"Khan: {khan_percent}% ({khan_votes}) \n") 
        datafile.write(f"Correy: {correy_percent}% ({correy_votes}) \n") 
        datafile.write(f"Li: {li_percent}% ({li_votes}) \n") 
        datafile.write(f"O'Tooley: {otooley_percent}% ({otooley_votes}) \n") 
        datafile.write(f"----------------------------------- \n") 
        datafile.write(f"Winner: {winner} \n") 
        datafile.write(f"----------------------------------- \n") 