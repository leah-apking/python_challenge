import os
import csv

# Define file path
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read budget_csv
with open(budget_csv, 'r') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")
    
    # Skip header row
    next(csvreader)
    
    # Set variables
    row_count = 0
    net_total = 0
    max_change = 0
    min_change = 0
    max_date = []
    min_date = []
    previous_row = 0
    rev_changes = []

    # Loop through csv rows
    for row in csvreader:
        # Count total months
        row_count += 1
        # Sum row values to find net total
        net_total = int(row[1]) + net_total
        
        # Determine month to month change
        change = int(row[1]) - previous_row
        # Redefine previous row
        previous_row = int(row[1])
        # Add change to list
        rev_changes.append(change)

        # Find max change and capture date
        if max_change < change:
            max_change = change
            max_date = row[0]
        else:
            max_change = max_change
            max_date = max_date
        
        # Find min change and capture date
        if min_change > change:
            min_change = change
            min_date = row[0]
        else:
            min_change = min_change
            min_date = min_date

    # Calculate average change
    average_change = round((sum(rev_changes) / (row_count - 1)) ,2)

    # Print analysis
    print("Financial Analysis:")
    print("---------------------------")  
    print(f'Total Months: {row_count}')
    print(f'Net total: ${net_total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_date} ${max_change}')
    print(f'Greatest Decrease in Profits: {min_date} ${min_change}')

# Write analysis to txt file
output_file = os.path.join("financial_analysis.txt")

with open(output_file, "w") as file:
   
    file.write("Financial Analysis:\n")
    file.write("---------------------------\n")
    file.write(f'Total Months: {row_count}\n')
    file.write(f'Net total: ${net_total}\n')
    file.write(f'Average Change: ${average_change}\n')
    file.write(f'Greatest Increase in Profits: {max_date} ${max_change}\n')
    file.write(f'Greatest Decrease in Profits: {min_date} ${min_change}\n')
