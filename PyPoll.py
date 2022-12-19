#Add our Dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save a file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter.
total_votes = 0
#candidate options
candidate_options = []
#declaring empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        total_votes += 1
    #print(total_votes)

        #print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

Winning_candidate_summary = (
    f"-----------------\n"
    f"Winner: {winning_candidate} \n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------")
print(Winning_candidate_summary)


