# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")

# Define variables to track the polling data
total_votes = 0  
candidates=[]
vote_counts={}
cur_candidate=""
cntr=0
new_nominee=""
percents=[]
greatest=""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    
    
    # Count the total votes, and the number of candidates
    for row in reader:

        
        total_votes=total_votes+1
        if cntr==0:
            cur_candidate=row[2]
            candidates.append(cur_candidate)
            cntr+=1
        else:
            if candidates.count(row[2])==0:
                candidates.append(row[2])
                cur_candidate=row[2]
                
    vote_counts = {candidate: 0 for candidate in candidates}
    
    
#looping through the csv again to add the votes to the dictionary
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    #skip for header
    header = next(reader)
        
    #Add the votes to the value aspect of the dictionary if the name matches up with the key
    for row in reader:
        new_nominee = row[2]
        if new_nominee in vote_counts:
            vote_counts[new_nominee]+=1             
    
    #saving the keys and values in seperate lists
    x=list(vote_counts.keys())
    y=list(vote_counts.values())  
      
    #calcualting the percentage of votes each candidate got
    for i in y:
        percents.append(round(i/total_votes*100,3))
        
    #calculating the highest vote    
    top=y[0]
    for i in y:
        if top<i:
            top=i        

    #searching for the name of the winner
    greatest= max(vote_counts,key=vote_counts.get)
    



# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    # Write the total vote count to the text file
    txt_file.write("Total Votes: " + str(total_votes)+"\n")
    txt_file.write("-------------------------\n")

    # Loop through the candidates to print all of their information
    for i in range(len(candidates)):
        txt_file.write(x[i]+": "+str(percents[i])+"% ("+str(y[i])+")\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: "+greatest)   
                        
        
        
        

  


    
