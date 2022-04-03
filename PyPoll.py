# The data we need to retrieve.
import csv
import os
dir(csv)
#file_variable = open(filename, mode)
file_to_load = os.path.join('Resources/election_results.csv')
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    #print(election_data)

#Import the datetime class from the datatime module
import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)


#1. The total number of votes cast

#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

#Read the file object with the reader function
file_reader = csv.reader(election_data)
  # Print each row in the CSV file.
for row in file_reader:
        print(row)

# Close the file
#outfile.close()

#Close the file
#election_data.close()