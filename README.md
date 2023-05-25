# python_challenge

### PyBank:

The task in PyBank was to analyze the provided csv data set to determine the total months included in the data, the net total over the entire period, the average change, and greatest increase and decrease in profits in a single month. Those results were then printed to the terminal and exported in a separate text file.

To do this I used the csv reader to cycle through the data file and set my variables. After skipping the header row, the reader continued through the file counting each row to provide the total number of months and added each row together to provide the net total. To determine the monthly change in revenue I subtracted the previous month's value from the current row, then reset the previous month value for the next row in the csv file, appended each value to a list, and finally summed those values and divided by the total number of months to calculate the average change. To find the maximum increase in profits I used if/else statements which determined if the calculated change value from that month was greater than the previous greatest value found, if so that value became the maximum the process repeated through the data set resulting in the maximum profit value. The date was also retrieved in this process. The same method was used to retrieve the greatest decrease in profits. These values were then used to print the analysis in the format provided and written to a text file.

### PyPoll:

In PyPoll we were asked to determine the election results given a dataset showing voter ID, county, and the candidate the individual voted for. The election results included total number of votes cast, the number of votes received and percentage of votes received for each candidates who received votes, and the winner of the election based on popular vote.

Again, I set my variables and used the csv reader to cycle through the data set. After skipping the header row, I used a row counter to find the total number of votes cast. Since I knew the candidates in advance, I used an if statement to check if the value of the “Candidate” cell in each row to determine which candidate name matched the cell and added one to the corresponding candidate’s vote count. To determine the percentage won by each candidate I divided each vote count by the total number of votes cast.

The results were then displayed next to each candidate’s name under the number of total votes. I used a series of if statements to determine which candidate had won the most votes and printed the winning candidate’s name. The full election results were printed in the format provided to the terminal and exported as a text file.
