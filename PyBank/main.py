##### MAIN.PY------------------------------
##### This python script was created to analyze the financial
##### data of a company located in the file, "budget_data.csv"
##### located in the Resources folder, both of which are located 
##### under the home directory, 'PyBank'.
##### 

import os
import csv

##### VARIABLE DECLARATION AND VALUES
totalMonth = 0
months = []
currentMonthRevenue = 0
previousMonthRevenue = 0
totalRevenue = 0
changeRevenue = 0
changesRevenue = []
##### READING OF CSV FILE INTO MEMORY

filepath = os.path("budget_data.csv", filename)

with open (filepath, 'r', newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
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
        else previousMonthRevenue = currentMonthRevenue

##### ANALYZE DATA FROM ABOVE ITERATION

sumChangesRevenue = sum(changesRevenue)
averageChange = sumChangesRevenue / (totalMonth - 1)
maxChange = max(changesRevenue)
minChange = min(changesRevenue)
maxMonthIndex = changesRevenue.index(maxChange)
minMonthIndex = changesRevenue.index(minChange)
maxMonth = months[maxMonthIndex]
minMonth = months[minMonthIndex]





            
        

##### PRINT TO TERMINAL




