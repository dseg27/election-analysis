# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies 
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
file_to_Save = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables we will need to keep track of votes and candidates
total_votes = 0
candidate_options = [] 
candidate_votes = {}

# Winning candidate and count tracker variables

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the data 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header rows
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1 
        candidate_name = row[2]

        if candidate_name not in candidate_options:   
            # Add candidate to options list     
            candidate_options.append(candidate_name)

            # Begin tracking vote count for each candidate using dictionary
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )
    print(winning_candidate_summary)



