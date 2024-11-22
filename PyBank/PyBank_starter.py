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
greatest_increase=0
greatest_decrease=0
dates=[]
outcome=[]
difference=[]
counter=0
i_date=""
d_date=""
total_profit=0


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    
    # Read the values and save them in seperate lists
    for row in reader:
        dates.append(row[0])
        outcome.append(int(row[1]))
    
    

# Calculate the total profit along with the total months
for values in outcome:    
    total_profit=total_profit+values
    total_months+=1

    
# Calculate the total difference and saving the differences in a list for further use
total_difference=0
for i in range(1,len(outcome)):
    total_difference=total_difference+(outcome[i]-outcome[i-1])
    difference.append(outcome[i]-outcome[i-1])
    
# Calculating and rounding the average change
avg_change=total_difference/len(difference)
avg_change=round(avg_change,2)

# Setting the increase and decrease values to the first values so the loop can work properly
greatest_increase=difference[0]
greatest_decrease=difference[0]

# Calculating the greatest increase and the mathing date
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
    
