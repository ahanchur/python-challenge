# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
cntr=0
greatest_increase=0
greatest_decrease=0
dates=[]
outcome=[]
difference=[]
counter=0
i_date=""
d_date=""

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    
    # Track the total and net change
    for row in reader:
        dates.append(row[0])
        outcome.append(int(row[1]))
    
greatest_increase=outcome[0]
greatest_decrease=outcome[0]
total_profit=0

for values in outcome:
    counter+=1
    
    if greatest_increase < values:
        greatest_increase=values
        i_count=counter
        
        
    if greatest_decrease>values:
        greatest_decrease=values
        d_count=counter
        
    total_profit=total_profit+values
    total_months+=1

    
# Calculate the average net change across the months
total_difference=0
for i in range(1,len(outcome)):
    total_difference=total_difference+(outcome[i]-outcome[i-1])
    difference.append(outcome[i]-outcome[i-1])
    
    
avg_change=total_difference/len(difference)
avg_change=round(avg_change,2)

greatest_increase=difference[0]
greatest_decrease=difference[0]

print(difference)

for i in range (len(difference)):
    if difference[i]>greatest_increase:
        greatest_increase=difference[i]
        i_date=dates[i+1]
        
    if difference[i]<greatest_decrease:
        greatest_decrease=difference[i]
        d_date=dates[i+1]
        
    

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("")
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: "+str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: $" +str(total_profit))
    txt_file.write("\n")
    txt_file.write("Average Change: $"+str(avg_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: "+i_date+" ($" +str(greatest_increase)+")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: "+d_date+" ($" +str(greatest_decrease)+")")
    
