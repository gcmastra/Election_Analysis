#PyPoll template for lesson 3.4.x

import datetime
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary that will hold candidate names and vote counts.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count in the dictionary
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1



# Leave some space in the print out
print("\n")

# Print the candidate list.
print("List of Candidates")
print(candidate_options)

print("\n")
# print the candidate votes dictionary 
print("Candidate Votes: ")
print(candidate_votes)
print("\n")

print("Total_votes = ", total_votes)
# Leave some space in the print out
print("\n")


# Determine the percentage of votes for each candidate by looping through the counts.
# This code computes and prints the percentages but does not save them in another list to be used elsewhere
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print the candidate(s) name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote ({votes:,}).")

    # modified version with percent rounded
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    
# # print out the winning candidate, vote count and percentage
# print("\n", "The winning candidate  is: ", winning_candidate)
# print("\n", "The winning vote count is: ", winning_count)
# # CLM - the name and count are correct but the percentage does not show the winning value
# print("\n", "The winning percentage is: ", vote_percentage)
# # Leave some space in the print out
# print("\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# # Close the file.
election_data.close()
