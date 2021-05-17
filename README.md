# Election_analysis
Python project to summarize election results.

## Project overview
This project aims to assist Tom, a Colorado Board of Elections employee, to audit tabulated elections results for a Colorado US Congress district.

The objectives are:
* find the total number of votes cast
* list all the candidates that received votes
* determine the number of votes each candidate received
* calculate the percentage of votes for each candidate
* identify the winner of the election

## Resources
This project is based on the tabulated data found in the CSV file "election_results.csv".
The code relies on two dependencies: *_csv_* and *_os_*.
The code was compiled using the IDE Visual Studio Code on Python version 3.8.5.

## Election audit results
This quick analysis found that a total of 369,711 votes were counted in this US Congress District.

The breakdown of the three counties in this district and their vote tallies are as follows:
1. Denver : 82.8% (306,055)
2. Jefferson : 10.5% (38,855)
3. Arapahoe : 6.7% (24,801)

Denver county had the largest number of votes.

Three candidates received votes, all of whom are listed below with their votes in order of the number of votes:
1. Diana DeGette : 73.8% (272,892)
2. Charles C. Stockham : 23% (85,213)
3. Raymon A. Doane : 3.1% (11,606)

Diana DeGette won the election, receiving 73.8% (272,892) of the total vote.

![Election audit output file](https://github.com/mustail/Election_analysis/blob/a0209a30ddc430910a2cfb96794858049302c613/Resources/election.png)

## Election audit summary
These findings were produced using a small Python code involving two dependencies mentioned above. It can be reused to analyze similar election data. Other variables (e.g. voting method) may be added to the existing three (county, ballot id, candidate) to incorporate wider questions and offer a richer analysis. To be able to do this, the CSV file needs to include more columns, and the Python code should use more variables accordingly.

Using the same code, it may be possible to analyze a similar data from earlier elections to capture the change and trends in voter turnout, elections, and political orientation.

One other possibility is to adapt the existing code to analyze voting trends according to county, to see which counties voted for which candidates.





