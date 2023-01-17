import os
import csv
from statistics import mean

budget_csv = os.path.join("Desktop", "Bootcamp", "2.Python", "Mod.3", "3.Challenge", "Resources", "budget_data.csv")

total_votes = []

with open(budget_csv, 'r') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")
    
    next(csvreader)
    
    row_count = 0
    value = 0
    max = 0
    min = 0
    max_date = []
    min_date = []
    
    for row in csvreader:
        
        row_count += 1
        value = int(row[1]) + int(value)
        
        average = round((value/row_count))

        if max < int(row[1]):
            max = int(row[1])
        else:
            max = max
        
        if min > int(row[1]):
            min = int(row[1])
        else:
            min = min

        if max == int(row[1]):
            max_date = str(row[0])
        if min == int(row[1]):
            min_date = str(row[0])

    print("Financial Analysis:")
    print("---------------------------")  
    print(f'Total Months: {row_count}')
    print(f'Net total: ${value}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {max_date} ${max}')
    print(f'Greatest Decrease in Profits: {min_date} ${min}')

output_file = os.path.join("Desktop", "Bootcamp", "2.Python", "Mod.3", "3.Challenge", "financial_analysis.txt")

with open(output_file, "w") as file:
   
    file.write("Financial Analysis:\n")
    file.write("---------------------------\n")
    file.write(f'Total Months: {row_count}\n')
    file.write(f'Net total: ${value}\n')
    file.write(f'Average Change: ${average}\n')
    file.write(f'Greatest Increase in Profits: {max_date} ${max}\n')
    file.write(f'Greatest Decrease in Profits: {min_date} ${min}\n')
