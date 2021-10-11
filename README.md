# election-analysis

## Project Overview 

A Board of Elections Employee tasked me with writing a python script to obtain information for an election audit, from a CSV file containing election results. I was to gather the following information:
  1. Total vote count 
  2. Complete list of candidates 
  3. Number of votes each candidate received 
  4. Percentage of votes each candidate won 
  5. Winner of the election based on popular votes 

## Resources 

Data received from: election_results.csv 
Software used: Python 3.7.6, Visual Studio Code 1.61.0

## Summary 

The results per the audit are as follows: 

- There were a total of 369,711 votes 
- Candidates included:  
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- Candidate results: 
  - Charles Casper Stockham received 23.0% of the vote-- (85,213 votes).
  - Diana DeGette received 73.8% of the vote-- (272,892 votes)
  - Raymon Anthony Doane: 3.1% of the vote-- (11,606 votes)
 
 The winner of the election is Diana DeGette, who received 73.8% of votes (11,606 votes). 

## Challenge Overview 

The election committee needs additional information from the CSV document that contains the election data. They need me to write a script that will also obtain the following information:
  - Voter turnout for each county that participated 
  - Percentage of votes contributed by each county 
  - The county with the highest voter turnout 
 
## Challenge Results 

As previously defined, there were a total of 369,711 votes in this election. Here are the county-based results: 

Counties included:   
  - Jefferson
    - Contributed to 10.5% of election votes (38,855 votes)
  - Denver 
    - Contributed to 82.8% of election votes (306,055 votes)
  - Arapahoe 
    - Contributed to 6.7% of election votes (24,801 votes)

Denver had the highest voter turnout. 

## Challenge Summary

This script can be used to gather data from a CSV document containing information for any election with similar data. Since the script is able to iterate through each row and collect data from each column, it can be used not only to gather county and candidate data, but other data as well.

For example, if columns were added to the election dataset that included voter demographics such as age and ethnicity, we would be able to determine trends for a specific candidate. Instead of making a dictionary with candidates and votes, we could make the value instead be the voter demographic to find trends between voter demographics and candidates. 

Another example would be to add a column for voting method. We could then iterate through the data to find the most popular voting method overall, or within a specific county, so we would know how to best cater to a precinct to increase voter turnout. 
