#PyPoll template for lesson 3.4.x

import datetime
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties In The Election\n")
    txt_file.write("------------------------- \n")
    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

#   # To do: perform analysis.
#   # All the GOOD STUFF happens here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# # Close the file.
election_data.close()
