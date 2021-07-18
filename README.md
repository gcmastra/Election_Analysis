# Unit 3 PyPoll Challenge Exercise
## Student : Christopher Mastrangelo

## Overview of Project: 
The purpose was to complete an election audit for the election commission and certify the election results of an election held in Colorado. Using a data file of votes cast, compute the election results, totals per candidate, totals per county, and percentages to determine the winner with the highest percentage of votes.

Screen capture showing the winning candidate. their total votes, and percentage of total votes cast.

![image](https://user-images.githubusercontent.com/86205000/126035577-f8d39999-adbc-4833-9f25-df82beb7d543.png)

Almost 370,000 votes were cast in this election with the majority of votes cast in Denver county (306,055).

> The winning candidate is Diana DeGette who received 272,892 votes which represents 73.8 percent of the total votes cast.



## Technical Details

This challenge utilized Python code and methods- such as for loops- to scroll through all records and calculate sums/totals per candidate and per county, as well as writing the output to a text file.  When sending text output to a file using I/O, the "with" statement takes care of both opening and closing the file for output (see below). 

FIles used in this activity.  The CSV file is stored in the resources folder and the output text file is stored in the analysis folder. 

![image](https://user-images.githubusercontent.com/86205000/126035524-c1fefc8b-b293-4e58-b251-a5ca29e001c0.png)


Here is a screen capture of the output to the text file "election_analysys.txt" in the "analysis" folder.

![image](https://user-images.githubusercontent.com/86205000/126035719-aaaa8df5-5adf-4e82-b74d-2af7f7974ec9.png)


Here is a screen capture of some of the code. 

![image](https://user-images.githubusercontent.com/86205000/126035817-a683e25e-f526-42d0-82a8-4ebb8c05b9dc.png)

As mentioned earlier in this document, one technical challenge that I encountered was understanding when to open the output file in order to write to it multiple times from different places in the code.  Line 84 "with . . . " must be placed before the start of output to the file and all the other sections of code which also write to the output file must be indented below it in order for the file to remain open.  The "with" command takes care of opening and closing the file, so it you outdent before completing all the output the file is considered closed by the program. 



# Data Analysis details

![image](https://user-images.githubusercontent.com/86205000/126035664-17792314-7fbe-45d7-89a6-39e68ed29c1e.png)

The data file contains a second column representing ballot ID which is a unique seven digit identifier.  Even though the Ballot ID is not displayed in the election outcome, this was important during the data cleanup and analysis phase to insure each vote was counted exactly once and there were no duplicate ballots. 


