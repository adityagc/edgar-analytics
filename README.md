# Table of Contents
1. [Approach](README.md#Approach)
2. [Data structures used](README.md#Data-structures-used)
3. [Dependencies and running instructions](README.md#Dependencies-and-running-instructions)

# Approach
1. The three files were opened and stored as python objects.
2. A loop was run till the end of file after skipping the first line.
3. During each iteration through the loop, the IP address was mapped to a list of relevant fields in the data using a dictionary.
4. If the IP address already existed in the dictionary, the latest access date, time and number of documents were updated.
5. Following this, a loop was iterated across the dictionary keys (ip addresses) to check which IP addresses have been inactive for a time greater than the threshold.
6. The IP, login date and time, last access date and time, duration of session and number of files accessed were then printed in the desired format for those IPs who's inactivity duration has crossed the threshold.
7. These IPs were then stored in a list and popped out of the dictionary.
8. When end of file is reached, all user sessions were terminated irresective of threshold and printed out to file.
9. A helper function was used to convert the date and time to total number of seconds. This handles cases when users could be online for mulitple days.

# Data structures used
1. A python dictionary was used for mapping {ip address : list of relevant fields such as date, time, number of files etc.}
2. The reason for using a dictionary was that lookup is O(1) on average and allowed fast access to elements in real time.

# Dependencies and running instructions
1. The source code is saved in a file called edgar.py in the src directory.
2. The source code is written in python 3.6
3. The source code needs to import sys. This is provided in case files are provided via command line arguments.
4. If no command line arguments are present, the file takes input from the default directory structure.
