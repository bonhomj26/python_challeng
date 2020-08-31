# Importing the os module
# This will allow us to create file paths
import os
import csv
# Setting the path for the CSV file in csvpath
csvpath = os.path.join("Resources", "budget_data.sv")

# Opening the the CSV file using the path set in csvpath
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    #Storing the variables
    profit_amount = []
    months = []
    change_in_revenue = []

    # This reads the rows in the csv file
    for rows in csvreader:
        profit_amount.append(int(rows[1]))
        months.append(rows[0])

    # This Calculates the change in revenue, average revenue

    for x in range(1, len(profit_amount)):
        change_in_revenue.append((int(profit_amount[x]) - int(profit_amount[x-1])))
    average_revenue = sum(change_in_revenue) / len(change_in_revenue)
    total_months = len(months)
    
    # Here, max is used to determine the greatest increase in the revenue
    greatest_increase = max(change_in_revenue)
    # greatest decrease in revenue
    greatest_decrease = min(change_in_revenue)

    # Budget Result
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(profit_amount)))

    print("Average change: " + "$" + str(average_revenue))

    print("Greatest Increase in Profits: " + str(months[change_in_revenue.index(max(change_in_revenue))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[change_in_revenue.index(min(change_in_revenue))+1]) + " " + "$" + str(greatest_decrease))


    #  Set path to Output the result to an external file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(profit_amount)) + "\n")

    file.write("Average change: " + "$" + str(average_revenue) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[change_in_revenue.index(max(change_in_revenue))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[change_in_revenue.index(min(change_in_revenue))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()
    
