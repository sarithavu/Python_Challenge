import os
import csv

csv_file_path = r'C:\Users\sarit\OneDrive\Desktop\Class_Folder\mygithub\Python_Challenge\PyBank\Resources\budget_data.csv'

#Specify the file to write to
output_file_path = r'C:\Users\sarit\OneDrive\Desktop\Class_Folder\mygithub\Python_Challenge\PyBank\Analysis\PyBank.txt'

with open(csv_file_path) as csv_file:

    csv_reader = csv.reader(csv_file)

# Skip the header row
    
    next(csv_reader)

# Initialize the variables
    total_months = 0
    net_total = 0
    previous_profit = None
    changes = []
    greatest_increase_date = ""
    greatest_increase_amount = 0
    greatest_decrease_date = ""
    greatest_decrease_amount = 0

    for row in csv_reader:

        total_months += 1
        net_total += int(row[1])
        profit_loss = int(row[1])
        date = row[0]
      
        if previous_profit is not None:
          change = profit_loss - previous_profit
          changes.append(change)

        
        # Check if the current change is the greatest increase and decrease
          if change > greatest_increase_amount:
             greatest_increase_amount = change
             greatest_increase_date = date
          elif change < greatest_decrease_amount:
             greatest_decrease_amount = change
             greatest_decrease_date = date

        previous_profit = profit_loss

    # Calculate the average of the changes
    if changes:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0  # Handle division by zero if no change


# Print total number of months, net_total, average_change, greatest increase in profits, greatest decrease in profits
print('Financial Analysis')
print('-------------------------------------')
print("Total Months:", total_months)
print("Total:", net_total)
print("Average Change:", average_change)
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")


# Export analysis results to a text file
with open(output_file_path, mode='w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase_amount}\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease_amount}\n")








 

        