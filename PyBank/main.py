##### MAIN.PY------------------------------
##### This python script was created to analyze the financial
##### data of a company located in the file, "budget_data.csv"
##### located in the Resources folder, both of which are located 
##### under the home directory, 'PyBank'.
##### 

import os
import csv

##### VARIABLE DECLARATION AND INITIAL VALUES
date = []
revenue = [] 
months = []
averageRevenueChange = []

##### INITIAL VALUES FOR VARIABLES
monthTotal = 0
totalRevenue = 0
greatestIncreaseRevenue = 0
greatestDecreaseRevenue = 0
averageRevenue = 0

revenueChange = 0
revenueChanges = 

currentMonthRevenue = 0
previousMonthRevenue = 0



##### READING OF CSV FILE INTO MEMORY

filepath = os.path("rawData", filename)

with open (filepath, 'r', newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader) 

##### DETERMINE MONTHLY CHANGES IN REVENUE

    for row in csvreader:
        monthTotal = monthTotal + 1
        months.append(row[0])
        currentMonthRevenue = int(row[1])
        totalRevenue = totalRevenue + currentMonthRevenue
        if monthTotal > 1:
            revenueChange = currentMonthRevenue - previousMonthRevenue
            revenueChanges.append(revenueChange)

            
        

##### PRINT TO TERMINAL




