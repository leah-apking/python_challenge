import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

total_votes = []

with open(election_csv, 'r') as election_csv:
    csvreader = csv.reader(election_csv, delimiter=",")

    next(csvreader)
    
    stockham = 0
    degette = 0
    doane = 0 
    row_count = 0
    
    for row in csvreader:
        row_count += 1
        if row[2] == "Charles Casper Stockham":
            stockham += 1
        elif row[2] == "Diana DeGette":
            degette += 1
        elif row[2] == "Raymon Anthony Doane":
            doane += 1
    total_votes = row_count
    
    stockham_percent = round(((stockham / total_votes) * 100), 1)
    degette_percent = round(((degette / total_votes) * 100), 1)
    doane_percent = round(((doane / total_votes) * 100), 1)

    
    print("Election Results")
    print("---------------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------------")
    print(f'Charles Casper Stockham: {stockham_percent}% ({stockham})')
    print(f'Diana Degette: {degette_percent}% ({degette})')
    print(f'Raymon Anthony Doane: {doane_percent}% ({doane})')
    print("---------------------------")
    
    if stockham < (degette and doane):
        print("Winner: Charles Casper Stockham")
    if degette < (stockham and doane):
        print("Winner: Diane Degette")
    if doane < (stockham and degette):
        print("Winner: Raymon Anthony Doane")    
    print("---------------------------")  

output_file = os.path.join("election_results.txt")

with open(output_file, "w") as file:
   
    file.write("Election Results:\n")
    file.write("---------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("---------------------------\n")
    file.write(f'Charles Casper Stockham: {stockham_percent}% ({stockham})\n')
    file.write(f'Diana Degette: {degette_percent}% ({degette})\n')
    file.write(f'Raymon Anthony Doane: {doane_percent}% ({doane})\n')
    file.write("---------------------------\n")

    if stockham < (degette and doane):
        file.write("Winner: Charles Casper Stockham\n")
    if degette < (stockham and doane):
        file.write("Winner: Diane Degette\n")
    if doane < (stockham and degette):
        file.write("Winner: Raymon Anthony Doane\n")    
    file.write("---------------------------\n") 

   
