# Importing the os module
# This will allow us to create the file paths
import os
import csv

# Setting the path for the CSV file in csvpath
csvpath = os.path.join('Resources', 'election_data.csv')

# Variable Initialization
total_votes_cast = 0
vote_one = 0
vote_two = 0
vote_three = 0
vote_four = 0

# Set Path For File
#csvpath = os.path.join('Resources', 'election_data.csv')

# Opening the the CSV file using the path set in csvpath
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    # This reads through the rows in the CSV file
    for row in csvreader:
       
        total_votes_cast += 1
        
        # Total Votes accumulates by Khan, Correy, Li, and O'Tooley

        if (row[2] == "Khan"):
            vote_one += 1
        elif (row[2] == "Correy"):
            vote_two += 1
        elif (row[2] == "Li"):
            vote_three += 1
        else:
            vote_four += 1
            
    # Percentage Votes receives by Khan, Correy, Li, and O'Tooley
    percent_one = vote_one / total_votes_cast
    percent_two = vote_two / total_votes_cast
    percent_three = vote_three / total_votes_cast
    percent_four = vote_four / total_votes_cast
    
    # Maximum number of votes ccumulates to determine the winner
    winner = max(vote_one, vote_two, vote_three, vote_four)

    if winner == vote_one:
        winner_name = "Khan"
    elif winner == vote_two:
        winner_name = "Correy"
    elif winner == vote_three:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Printing Election Result
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes_cast}")
print(f"---------------------------")
print(f"Kahn: {percent_one:.3%}({vote_one})")
print(f"Correy: {percent_two:.3%}({vote_two})")
print(f"Li: {percent_three:.3%}({vote_three})")
print(f"O'Tooley: {percent_four:.3%}({vote_four})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Set path to Output the result to an external file
output_file = os.path.join('Resources', 'output.text')
 # Write the Output result to an external file as text
with open(output_file, 'w',) as txtfile:

# Write the final Output result
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes_cast}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {percent_one:.3%}({vote_one})\n")
    txtfile.write(f"Correy: {percent_two:.3%}({vote_two})\n")
    txtfile.write(f"Li: {percent_three:.3%}({vote_three})\n")
    txtfile.write(f"O'Tooley: {percent_four:.3%}({vote_four})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
