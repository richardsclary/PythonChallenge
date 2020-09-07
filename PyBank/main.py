##### MAIN.PY------------------------------
##### This python script was created to analyze the financial
##### data of a company located in the file, "budget_data.csv"
##### located in the Resources folder, both of which are located 
##### under the home directory, 'PyBank'.
 

import os
import csv

#filename = "budget_data.csv"

##### VARIABLE DECLARATION AND VALUES
totalMonth = 0
months = []
currentMonthRevenue = 0
previousMonthRevenue = 0
totalRevenue = 0
changeRevenue = 0
changesRevenue = []
thisMonthRevenue = 0
previousMonthRevenue = 0

##### READING OF CSV FILE INTO MEMORY

with open("/Users/rsc/BCSDataFiles/budget_data.csv", mode = 'r', newline = "") as csvFile: 
    csvreader = csv.reader(csvFile, delimeter=",") 
    
    next(csvreader)
    
##### DETERMINE MONTHLY CHANGES IN REVENUE BY ITERATING OVER ALL ROWS

    for row in csvreader:
        totalMonth = totalMonth + 1
        months.append(row[0])
        currentMonthRevenue = int(row[1])
        totalRevenue = totalRevenue + currentMonthRevenue
        
        if totalMonth > 1:
                changeRevenue = currentMonthRevenue - previousMonthRevenue
                changesRevenue.append(changeRevenue)
        previousMonthRevenue = currentMonthRevenue

##### ANALYZE DATA FROM ABOVE ITERATION

sumChangesRevenue = sum(changesRevenue)
averageChange = sumChangesRevenue / (totalMonth - 1)
maxChange = max(changesRevenue)
minChange = min(changesRevenue)
maxMonthIndex = changesRevenue.index(maxChange)
minMonthIndex = changesRevenue.index(minChange)
maxMonth = months[maxMonthIndex]
minMonth = months[minMonthIndex]

##### SUMMARY OUTPUT TO SCREEN

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {totalMonth}")
print(f"Total Revenue: ${totalRevenue}")
print(f"Average Revenue Change: ${averageChange}")
print(f"Greatest Increase in Revenue: {maxMonth} (${maxChange}")
print(f"Greatest Decrease in Revenue: {minMonth} (${minChange}")
print("-------------------------")

with open("output.txt", 'w+') as file:

    file.write("Financial Analysis" + "\n") 
    file.write("-------------------------" + "\n")
    file.write(f"Total Months: {totalMonth}" + "\n")
    file.write(f"Total Revenue: ${totalRevenue}" + "\n")
    file.write(f"Average Revenue Change: ${averageChange}" + "\n")
    file.write(f"Greatest Increase in Revenue: {maxMonth} (${maxChange}" + "\n")
    file.write(f"Greatest Decrease in Revenue: {minMonth} (${minChange}" + "\n")
    file.write("-------------------------")







            




