print("Financial Analysis")
print("--------------------------")
#import os
import os

#Import module for reading CSVs
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

total_months = 0
total_profits_losses = 0
previous_profit_loss = None
total_changes = 0
greatest_increase = 0
greatest_increase_date = None
greatest_decrease = 0
greatest_decrease_date = None

#open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    #read header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #count months
        total_months += 1
        #count profit/loss total amount
        profit_loss = int(row[1])
        total_profits_losses += profit_loss
        #calculate profit/losses changes
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_changes += change

            #update increase & decrease 
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
        previous_profit_loss = profit_loss

#Get average of changes
if total_months > 1:
    average_change = total_changes / (total_months - 1)
    average_change_formatted = "${:.2f}".format(average_change)
else:
    average_change_formatted = "0.00"

print("Total Months:", total_months)
print("Total: ${}".format(total_profits_losses))
print("Average change: ", average_change_formatted)
print("Greatest increase in profits:", greatest_increase_date, "(${})".format(greatest_increase))
print("Greatest decrease in profits:", greatest_decrease_date, "(${})".format(greatest_decrease))

#Export results to a text file
with open('results.txt', 'w') as f:
    f.write("Total months: {}\n".format(total_months))
    f.write("Total: ${}\n".format(total_profits_losses))
    f.write("Average change: ${:.2f}\n".format(average_change))
    f.write("Greatest increase in profits: {} (${})\n".format(greatest_increase_date, greatest_increase))
    f.write("Greatest decrease in profits: {} (${})\n".format(greatest_decrease_date, greatest_decrease))