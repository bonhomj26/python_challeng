#First, we will import the os module
# This will allow us to create file paths
import os
# Module for reading the CSV file
import csv

#joining path
budget_data = os.path.join("Resources", "budget_data.csv")

# Now, we will read and open the CSV file :
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # Creating the list to store the net amount of profit and loss data:
    profit_amount = []
    months = []
    change_in_revenue = []

    # Using the for loop to read each row in the data:
    for rows in csvreader:
        profit_amount.append(int(rows[1]))
        months.append(rows[0])

    # Using the for loop to calculate the change in the revenue:
    #revenue_change = []

    for x in range(1, len(profit_amount)):
        change_in_revenue.append((int(profit_amount[x]) - int(profit_amount[x-1])))
    
    # Change in the average of revenue
    average_revenue = sum(change_in_revenue) / len(change_in_revenue)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(change_in_revenue)
    # greatest decrease in revenue
    greatest_decrease = min(change_in_revenue)


    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(profit_amount)))

    print("Average change: " + "$" + str(average_revenue))

    print("Greatest Increase in Profits: " + str(months[change_in_revenue.index(max(change_in_revenue))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[change_in_revenue.index(min(change_in_revenue))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(profit_amount)) + "\n")

    file.write("Average change: " + "$" + str(average_revenue) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[change_in_revenue.index(max(change_in_revenue))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[change_in_revenue.index(min(change_in_revenue))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()





    



