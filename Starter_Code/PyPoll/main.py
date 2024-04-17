print("Election Results")
print("--------------------------")

#import os
import os

#Import module for reading CSVs
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')


#open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    #read header
    csv_header = next(csvreader)
    #print(csv_header)

    #count all rows for total votes
    csv_info = list(csvreader)
    All_votes = len(csv_info)
    print("Total Votes:", All_votes)
    print("--------------------------")

    #create dictionary for candidates who recieved votes
    candidate_votes = {}
    
    #count votes
    for row in csv_info:
        for candidate in row[2:]:
            if candidate:
                if candidate in candidate_votes:
                    candidate_votes [candidate] += 1
                else:
                    candidate_votes[candidate] = 1

    #calculate total number of votes
    total_votes = sum(candidate_votes.values())

    for candidate, votes in candidate_votes.items():
        percentage = (votes/total_votes) * 100
        #print totals       
        print(f"{candidate}: {percentage: .3f}% ({votes})")

#Export results as text file
output_file = "election_results.txt"

with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {All_votes}\n")
    file.write("--------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"Candidate: {candidate}, {percentage:.3f}%, ({votes})\n")
    
  

   

    
