# weekday.py
# This program that outputs whether or not today is a weekday.
# Author: Ciaran Moran

import datetime

# dictionary with index 0:6 for Monday:Sunday as keys and weekday / weekend as values
weekIndex = {
0 : "Weekday",
1 : "Weekday",
2 : "Weekday",
3 : "Weekday",
4 : "Weekday",
5 : "Weekend",
6 : "Weekend"
    }

todaysDate = datetime.date.today()    # checks what day it is
dayIndex = todaysDate.weekday()       # converts the day to index 0:6 for Monday:Sunday

for key, value in weekIndex.items():  # iterate over key value pairs of weekIndex dictionary
    if key == dayIndex:                 # check if key = todays day index
        if value == "Weekend":              # check of the correspinding value is Weekend
            print("It is the {}, yay!".format(value))
        else:
            print("Yes, unfortunately today is a {}.".format(value)) 


# References: 

# 1. Docs.python.org, 2021, Datetime — Basic date and time types — Python 3.9.2 Documentation, viewed 20 Feb 2021, <https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday>.
# 2. Sweigart, A, 2015, Automate the boring stuff with Python, Dictionaries and structuring data, No Starch press, San Francisco, pp 120.