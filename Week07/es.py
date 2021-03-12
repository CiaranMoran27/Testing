# es.py
# This program reads in a text file from an arguement on the command line. 
# It outputs the number of "e" characters in the file.
# Author: Ciaran Moran

import os
import sys

filename = sys.argv[1]                             # accept the 2nd arguement from the command line

def readFile(filename):
    with open(filename,'r') as f:                     # open file in read only mode, use of alias means no need to close file
        data = f.read()                                  # call the read function on the alias
        return data
        


def eCharacterCount(data):
    eCount = data.count("e")                       # use of .count method to count occurances of a character in a file               
    ECount = data.count("E")
    eTotal = eCount + ECount

    print("There are {} lowercase 'e' characters in this text file".format(eCount))
    print("There are {} uppercase 'E' characters in this text file".format(ECount))    
    print("There are {} total 'e' characters in this text file (case independant)".format(eTotal))

    
data = readFile(filename)
eCharacterCount(data)



# main reference list is in pands-problem-sheet reposotory README file
#Refernces used: 
# 1.Docs.python.org, 2021, 7.2. Reading and Writing Files — Python 3.9.2 Documentation, viewed 05 March 2021, https://docs.python.org/3/tutorial/inputoutput.html
# 3.GeeksforGeeks, 2019, How to use sys.argv in Python, viewed 12 March 2021, https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
# 3.GeeksforGeeks, 2019, With statement in Python, viewed 05 March 2021, https://www.geeksforgeeks.org/with-statement-in-python.
# 4.Gutenberg.org, 2000, Moby Dick, viewed 05 March 2021, https://www.gutenberg.org/files/2701/old/moby10b.txt
# 5.Zíka, H, 2018, Counting specific characters in a file (Python), viewed 12 Mar 2021, https://stackoverflow.com/questions/48885930/counting-specific-characters-in-a-file-python.


