##### --------------------------------------------------
##### electionAnalysis.py
##### --------------------------------------------------
##### This python script will analyze polling data and 
##### summarize election results, including counting the 
##### votes and identifying the winner.  The polling data
##### is found in the file, 'election_data.csv' located
##### in the 'Resources' folder, while the output file with
##### the summary analysis, 'electionAnalysis.txt, is 
##### located in the 'Analysis' folder--both of which are 
##### located in the 'PyPoll' directory.
##### -------------------------------------------------- 

##### MODULE IMPORTATION

import os
import csv

##### VARIABLE DECLARATION AND VALUES

dashbreak = "-----------------------"
totalVotes = 0
winnerVotes = 0
candidate = ""
candidateVotes = {}
candidatePercentages = {}
winner = ""

##### READING OF CSV FILE INTO MEMORY

filename = "/Users/rsc/Desktop/BCS Homework Assignments/HW #3/PythonChallenge/PyPoll/Resources/election_data.csv"
with open(filename, mode = 'r', newline = "") as csvFile: 
    csvreader = csv.reader(csvFile) 
    next(csvreader)

##### DETERMINE THE VOTE COUNT FOR EACH CANDIDATE

    for row in csvreader:
        totalVotes = totalVotes + 1
        candidate = row[2]
        if candidate in candidateVotes:
            candidateVotes[candidate] = candidateVotes[candidate] + 1
        else:
            candidateVotes[candidate] = 1

##### CALCULATION OF CANDIDATE PERCENTAGES AND WINNER IDENTIFICATION

for person, voteCount in candidateVotes.items():
    candidatePercentages[person] = '{0:.0%}'.format(voteCount / totalVotes)
    if voteCount > winnerVotes:
        winnerVotes = voteCount
        winner = person

##### SUMMARY OUTPUT TO SCREEN

print("Election Results")
print(dashbreak)
print(f"Total Votes: {totalVotes})")
print(dashbreak)
for person, voteCount in candidateVotes.items():
        print(f"{person}: {candidatePercentages[person]} ({voteCount})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

##### WRITING THE RESULTS TO A TEXT FILE (electionAnalysis.txt)

outputFile = "/Users/rsc/Desktop/BCS Homework Assignments/HW #3/PythonChallenge/PyPoll/Analysis/electionAnalysis.txt"
with open(outputFile, 'w+') as file:
    file.write(dashbreak + "\n")
    file.write(f"Total Votes: {totalVotes}" + "\n")
    file.write(dashbreak + "\n")
    for person, voteCount in candidateVotes.items():
        file.write(f"{person}: {candidatePercentages[person]} ({voteCount})" + "\n")
    file.write(dashbreak + "\n")
    file.write(f"Winner: {winner}" + "\n")
    file.write(dashbreak + "\n")
    file.close()




