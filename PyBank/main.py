# Dependencies
import os 
import csv

# File location
budget_csv = os.path.join('Resources/budget_data.csv')


# Create lists for the variables
months = []
profit = []
monthly_profit_change = []
 
# Open csv file
with open(budget_csv, newline="",) as budget:
    csvreader = csv.reader(budget, delimiter=",") 
    csv_header = next(csvreader)  

    # Loop through rows
    for row in csvreader: 

        # Add total months and total profit to lists
        months.append(row[0])
        profit.append(int(row[1]))

    # Loop through profit in order to get the monthly change in profit
    for i in range(len(profit)-1):
        
        # Summing up monthly profit changes
        monthly_profit_change.append(profit[i+1]-profit[i])
        
# Max and min from monthly profit change list
max_up = max(monthly_profit_change)
max_down = min(monthly_profit_change)

# Link up the max and min to the corresponding month using month list and index from max / min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print to Bash
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total Profit: ${sum(profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_up))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_down))})")

# Output file
output_file = os.path.join("Financial_Analysis_Summary.txt")

with open(output_file,"w") as datafile:
    
# Write Financial Analysis to .txt file 
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("----------------------------")
    datafile.write("\n")
    datafile.write(f"Total Months: {len(months)}")
    datafile.write("\n")
    datafile.write(f"Total Profit: ${sum(profit)}")
    datafile.write("\n")
    datafile.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_up))})")
    datafile.write("\n")
    datafile.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_down))})")


