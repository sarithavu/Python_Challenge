import os
import csv

# Specify the file path 
csv_file_path = r'C:\Users\sarit\OneDrive\Desktop\Class_Folder\mygithub\Python_Challenge\PyPoll\Resources\election_data.csv'
output_file_path = r'C:\Users\sarit\OneDrive\Desktop\Class_Folder\mygithub\Python_Challenge\PyPoll\Analysis\PyPoll.txt'


# Initialize the variables
total_votes = 0
candidates_votes = {}

# Read the dataset and calculate the total number of votes
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
    next(csv_reader)
    
    for row in csv_reader:
         total_votes += 1
         candidate_name = row[2]

    # Update candidate's vote count in the dictionary
         if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1
         else:
            candidates_votes[candidate_name] = 1


print('Election Results')

print('-------------------------------------')

# Calculate and print the total number of votes cast
print(f"The total number of votes cast is: {total_votes}")

print('-------------------------------------')

# Calculate and print the percentage of votes each candidate won

for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print('-------------------------------------')

# Find the winner based on the popular vote
winner = max(candidates_votes, key=candidates_votes.get)
print(f"Winner: {winner}")

print('-------------------------------------')

#Write the election results to a text file
with open(output_file_path, mode='w') as output_file:
    output_file.write('Election Results\n')
    output_file.write('-------------------------------------\n')
    output_file.write(f"The total number of votes cast is: {total_votes}\n")
    output_file.write('-------------------------------------\n')
    
    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    output_file.write('-------------------------------------\n')
    output_file.write(f"Winner: {winner}\n")
    output_file.write('-------------------------------------\n')

print('Results exported to results.txt')





























