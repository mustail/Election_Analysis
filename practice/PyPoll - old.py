#mustafa
# In this project, our final Python script will need to be able to deliver the following information when the script is run: 

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# the pseudocode:
# 1. open the data fie
# 2. write down the names of all candidates
# 3. add a  vote count for each candidate
# 4. get the total votes for each candidate
# 5. get the total votes cast

import csv
import os
#print(dir(int))

#import datetime
#import random


# assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'
# using the os.path.join method:
file_to_load = os.path.join("Resources", "election_results.csv")


# read file using the open and close methods:
#election_data = open(file_to_load, 'r')
#print(election_data)
#election_data.close()

# alternative way to open and read file:
with open(file_to_load) as election_data:
    # perform analysis # no need to close when using with
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    # print each row in the csv file
    for row in file_reader:
        print(row)




# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the open() function with the "w" mode we will write data to the file
#open(file_to_save, "w")

# open the file as a text file.
# outfile = open(file_to_save,"w")
# write some data to the file
# outfile.write("Hello world.")
#close the file
# outfile.close()

# using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # write some data to the file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")


