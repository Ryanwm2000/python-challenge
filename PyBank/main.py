import os
import csv

numonths = 0
tc = 0
maxinc = 0
maxincdate = ""
maxdec = 0
maxdeccdate = ""
previous = 0.0
avgchange = 0
    
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    for row in csvreader:
        current = float(row[1])
        if numonths == 0:
            maxinc = 0.0
            maxdec = 0.0
            maxincdate = row[0]
            maxdecdate = row[0]
        else:
            answer = current - previous
            avgchange += answer
            if answer > maxinc:
                maxinc = answer
                maxincdate = row[0]
            elif answer < maxdec:
                maxdec = answer
                maxdecdate = row[0]

        previous = current
        numonths += 1
        tc += float(row[1])

avgchange = avgchange / (numonths-1)

results = []
results.append("Financial Analysis\n----------------------------")
results.append(f"Total Months: {numonths}")
results.append(f"Total: ${round(tc)}")
results.append(f"Average Change: ${round(avgchange,2)}")
results.append(f"Greatest Increase in Profits: {maxincdate} (${round(maxinc)})")
results.append(f"Greatest Decrease in Profits: {maxdecdate} (${round(maxdec)})")

filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
        
        
