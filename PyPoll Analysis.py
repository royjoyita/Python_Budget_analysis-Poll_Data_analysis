#!/usr/bin/env python
# coding: utf-8

# In[2]:


#PyPoll

# incorporated  the dependencies
import csv
import os

file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("Pypoll_analysis.txt")


# Total Vote Counter

total_votes = 0

# Candidate options and vote counter
candidate_options = []
candidate_votes = {}

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Read the Header
    header = next(reader)
    
    for row in reader:
        
        # Run the loader animation
        # print(". ", end=""),
        
        # Add to total vote count
        total_votes = total_votes + 1
        
        # Extract the candidate name for each row
        candidate_name = row[2]
        
        # If the candiate does not match any existing. candidate
        # (In a way loop is discovering candidates as it goes)
        
        if candidate_name not in candidate_options:
            # add it ot the list of candidates in the running
            candidate_options.append(candidate_name)
            
            # begin tracking the candidate voter count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:
    # print the final vote count
    
    election_results = (
         "\n\nElection Results\n" +
         "---------------------\n" +
         "Total Votes: " + str(total_votes) + "\n" +
         "----------------------\n"
    )
    print(election_results, end="")
    
    # save the final vote count to text file
    
    txt_file.write(election_results)
    
    # Determine the winner by looping through the counts 
    for candidate in candidate_votes:
        
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        # Print each candidate's voter count and percentage to terminal
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        print(voter_output, end="")
        
        txt_file.write(voter_output)
        
    #print the winning candidates
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"----------------------------\n"
    )
    print(winning_candidate_summary)
    
    # save the winning candidate name to text file
    txt_file.write(winning_candidate_summary)
        
        
        
        
        
        


# In[ ]:





# In[ ]:




