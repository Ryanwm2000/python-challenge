import os
import csv

total_votes = 0
candidates = []
votesPerCandidates = []

csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    for row in csvreader:
        total_votes += 1
        if total_votes == 1:
            candidates.append(row[2])
            votesPerCandidates.append(1)
        else:
            try:
                ican = candidates.index(row[2])
                votesPerCandidates[ican] += 1
            except:
                candidates.append(row[2])
                votesPerCandidates.append(1)

results = []
results.append("Election Results\n-------------------------")
results.append(f"Total Votes: {total_votes}\n-------------------------")

winner = candidates[0]
maxvotes = votesPerCandidates[0]
for i in range(len(candidates)):
    if votesPerCandidates[i] > maxvotes:
        winner = candidates[i]
        maxvotes = votesPerCandidates[i]
    percent = 100 * votesPerCandidates[i] / total_votes
    results.append(f"{candidates[i]}: {round(percent,3)} % ({votesPerCandidates[i]})")

results.append(f"-------------------------\nWinner: {winner}\n-------------------------")

filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
