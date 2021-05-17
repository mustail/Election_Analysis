# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")



# candidate options
candidate_options = []
# initialize a total vote counter
total_votes = 0
# candidate votes tallying
candidate_votes = {}

# winner candidate, count and percentage trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # print(headers)

    # print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        # identify the candidate name from each row
        candidate_name = row[2]
        # add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
        
print(winning_count) 
print(candidate_options)    
print(total_votes)
print(candidate_votes)


# determine the percentage of votes for each candidate by looping through the dict
# iterate throught the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # print the name of the candidate and the percentage
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    # determine winning vote
    # determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true, then set winning_count equal to votes and so on
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

print(f"---------------------\n{winning_candidate} won the election\nwith {winning_count:,} number of votes\nequal to {winning_percentage:.1f}% of all votes.\n---------------------")
