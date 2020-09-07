##### MAIN.PY------------------------------
##### This python script was created to analyze the financial
##### data of a company located in the file, "budget_data.csv"
##### located in the Resources folder, both of which are located 
##### under the home directory, 'PyBank'.
##### 

import os
print(os.getcwd())

import csv

#filename = "budget_data.csv"

##### VARIABLE DECLARATION AND VALUES
#totalMonth = 0
#months = []
#currentMonthRevenue = 0
#previousMonthRevenue = 0
#totalRevenue = 0
#changeRevenue = 0
#changesRevenue = []

##### READING OF CSV FILE INTO MEMORY

headers = []
#rows = []
#filepath = '~/Users/rsc/Desktop/BCS Homework Assignments/HW #3/PythonChallenge/PyBank/Resources/
# opening the CSV file 
with open('Users/rsc/iCloud Drive/Desktop/budget_data.csv', mode ='r') as file: 
    
# reading the CSV file 
    csvFile = csv.reader(file) 
  
# displaying the contents of the CSV file 
    for lines in csvFile: 
        print(lines) 


#with open ('budget_data.csv', mode = 'r') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter = ',')
  #  headers = csvreader.next()
   # for row is csvreader:
   #     rows.append()
   # print("Total Number of Rows: %d"%).csvreader.line_num
   # print('Header Names are:' + ', '.join(field for field in fields))


   # next(csvreader) 

##### DETERMINE MONTHLY CHANGES IN REVENUE BY ITERATING OVER ALL ROWS

 #   for row in csvreader:
 #       totalMonth = totalMonth + 1
 #       months.append(row[0])
 #       currentMonthRevenue = int(row[1])
 #       totalRevenue = totalRevenue + currentMonthRevenue
 #       if totalMonth > 1:
 #           changeRevenue = currentMonthRevenue - previousMonthRevenue
 #           changesRevenue.append(changeRevenue)
    
 #       previousMonthRevenue = currentMonthRevenue

##### ANALYZE DATA FROM ABOVE ITERATION

#sumChangesRevenue = sum(changesRevenue)
#averageChange = sumChangesRevenue / (totalMonth - 1)
#maxChange = max(changesRevenue)
#minChange = min(changesRevenue)
#maxMonthIndex = changesRevenue.index(maxChange)
#minMonthIndex = changesRevenue.index(minChange)
#maxMonth = months[maxMonthIndex]
#minMonth = months[minMonthIndex]

##### SUMMARY OUTPUT TO SCREEN

#print("Financial Analysis")
#print("-------------------------")
#print(f"Total Months: {totalMonth}")
#print(f"Total Revenue: ${totalRevenue}")
#print(f"Average Revenue Change: ${averageChange}")
#print(f"Greatest Increase in Revenue: {maxMonth} (${maxChange}")
#print(f"Greatest Decrease in Revenue: {minMonth} (${minChange}")
#print("-------------------------")

#saveFile = filename.strip(".csv") + "_results.txt"
#filepath
#with open(filepath, 'w') as text:
#    text.write("Financial Analysis" + "\n")
#    text.write("-------------------------" + "\n")
#    text.write(f"Total Months: {totalMonth}" + "\n")
#    text.write(f"Total Revenue: ${totalRevenue}" + "\n")
#    text.write(f"Average Revenue Change: ${averageChange}" + "\n")
#    text.write(f"Greatest Increase in Revenue: {maxMonth} (${maxChange}" + "\n")
#    text.write(f"Greatest Decrease in Revenue: {minMonth} (${minChange}" + "\n")
 #   text.write("-------------------------")







            




