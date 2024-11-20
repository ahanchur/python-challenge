# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")

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
    
    
    
    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

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
    
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
        
    for row in reader:
        new_nominee = row[2]
        if new_nominee in vote_counts:
            vote_counts[new_nominee]+=1             
    
    x=list(vote_counts.keys())
    y=list(vote_counts.values())  
      
    for i in y:
        percents.append(round(i/total_votes*100,3))
        
        
    top=y[0]
    for i in y:
        if top<i:
            top=i        

    greatest= max(vote_counts,key=vote_counts.get)
    

                
                
                
                

            
            
        
            
            
       
        

        



# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    # Write the total vote count to the text file
    txt_file.write("Total Votes: " + str(total_votes)+"\n")
    txt_file.write("-------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for i in range(len(candidates)):
        txt_file.write(x[i]+": "+str(percents[i])+"% ("+str(y[i])+")\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: "+greatest)   
                        
        
        
        

    # Get the vote count and calculate the percentage


    # Update the winning candidate if this one has more votes


    # Print and save each candidate's vote count and percentage


    
