
<H1 align="center"> Weekly Tasks 2021 </H1>
<H1 align="center"> Programming and Scripting </H1>
<br/>

## Introduction
This README file gives a more in-depth explanation of the code used to complete the weekly tasks for the 2021<br/>Programming and Scripting GMIT module as part of the Higher Diploma in Science in Computing.  
<br/>


## Task 1: (Bmi.py):
*Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres<br/>and weight in kilograms. The output is their weight divided by their height in metres squared.* 
<br/>

### Code:
``` Python
height = float(input("What is your height in centimetres?:"))
weight = float(input("What is your weight kilograms?:"))
metres_sq = (height/100)**2
bmi = round(weight / metres_sq,2)
print("BMI is " + str(bmi) + ' kg/m²')
```

### Code breakdown:
- User is asked for their height(cm) and weight(Kg).
- Height is convered from cm to m² and stored in *metres_sq* variable.
- Weight(Kg) is divided by height(m²), rounded to two decimal places and passed to *bmi* variable.
- The bmi result is passed into a {} placeholder via string formatting and printed.

<br/>

### References:
1.	Active, 2021, What is BMI and How to Calculate It, viewed 31 Jan 2021,<br/>*<https://www.active.com/fitness/articles/what-is-bmi-and-how-to-calculate-it>*.
2.	GeeksforGeeks, 2021, round () function in Python, viewed 31 Jan 2021,<br/>*<https://www.geeksforgeeks.org/round-function-\python>*.
3.	Real Python, 2021, A guide to the newer Python string format techniques, viewed 31 Jan 2021,<br/>*<https://realpython.com/python-formatted-output>*.
4.	Sweigart, A, 2015, Automate the boring stuff with Python, No Starch press, San Francisco, pp 15.
<br/>
<br/>

## Task 2: (secondstring.py):

*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*
<br/>

### Code:
``` Python
sentence = input("Please enter a sentence: ")
reverse_string = sentence[::-2]
print(reverse_string)
```

### Code breakdown:
- User is asked to input a sentence.
- The full string is sliced by default as no index number is placed in the first two placeholders of [::-2].
- A negative stride of 2 is used and the the resulting string stored in the reverse_string variable.
- The reversed string is printed.
<br/>

### References:
1. Real Python, 2021, String slicing, viewed 31 Jan 2021,<br/>*<https://realpython.com/python-strings/#specifying-a-stride-in-a-string-slice>*.

<br/>
<br/>

## Task 3: (collatz.py):

*Write a program that asks the user to input any positive integer and outputs the successive values of the following:*<br/>
 *At each step calculate the next value by taking the current value and:*
    - *Divide by 2 if even.*
    - *Multily by 3 and add 1 if odd.*
    - *End the progam if current value is 1.*

<br/>

### Code:
``` Python
numberList = []

number = input("Enter a positive integer: ")

while True:
    try:
        numberInt = int(number)

        if numberInt < 0: 
            numberInt = int(input("Enter a Enter a positive number: "))
            continue            
        else:
            break                  

    except ValueError:                          
        number = input("Enter an integer: ")    
        continue                              

while numberInt!=1:              
    if numberInt % 2 == 0:             
        numberInt = numberInt // 2     
    else:
        numberInt = (numberInt * 3) + 1  
    numberList.append(numberInt)       
print(numberList)
```

### Code breakdown:
- User is asked for a positive integer.
- **First While loop** is designed to validate the user input in the block of code between  *try* and *except* where:
    - Tries to convert the input string to an integer, if this fails a *ValueError* is raised and the program asks the <br/> user to *"Enter an integer: "* and jumps back to the start of the while loop.
    - Assuming that point 1 above has executed sucessfully (i.e the user input can be cast as an integer) the program <br/>checks if the integer is negative, in which case  the program asks user to *"Enter a Enter a positive number: "* and jumps <br/> back to the start of the while loop.
 - **Second While loop** performs sucessive calculations on user input and resulting values until the resulting value=1. 
     - Checks if the remainder of the user input divided by 2 = 0 (i.e is it even), in which case the program re-defines <br/>the *numberInt* variable as itself divide by 2 and appends it to *numberList*.
     - Checks if the remainder of the user input divided by 2 != 0 (i.e is it odd), in which case the program re-defines <br/>the *numberInt* variable as (itself divided by 3) + 1 and appends it to *numberList*.
         - The while loop runs re-uses the newly defined *numberInt* variable until the value = 1, then the list is <br/>printed.
<br/>
<br/>

### References:
1. Cunningham, P, 2014, Check if input is positive integer, viewed 19 Feb 2021, <br/>*<https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer>*.
2. Real Python, 2021, 8.3 Handling exceptions, viewed 19 Feb 2021,*<https://docs.python.org/3/tutorial/errors.html>*.
3. Programiz, 2021, What is the use of break and continue in Python?, viewed 19 Feb 2021,<br/>*<https://www.programiz.com/python-programming/break-continue>*.  

<br/>
<br/>

## Task 4: (weekday.py):

*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*
<br/>

### Code:
``` Python
import datetime

weekIndex = {
0 : "Weekday",
1 : "Weekday",
2 : "Weekday",
3 : "Weekday",
4 : "Weekday",
5 : "Weekend",
6 : "Weekend"
    }

todaysDate = datetime.date.today()    
dayIndex = todaysDate.weekday()

for key, value in weekIndex.items():  
    if key == dayIndex:                 
        if value == "Weekend":              
            print("It is the {}, yay!".format(value))
        else:
            print("Yes, unfortunately today is a {}.".format(value)) 
```

### Code breakdown:
- The datetime module is imported
- Dictionary named weekIndex is declared:
    - Keys are set to 0-6 which represent the index of the days of the week (i.e index 0 = Monday, index 6 = Sunday).
    - Values distunguish between weekdays or weekend.
    - The *todaysDate* variable uses the *.date.today* methods of  datetime library to obtain todays date.
    - The *dayIndex* variable uses the *.weekday* method of  datetime library to convert todays date to an index number(0 - 6).
- The key, value pairs of dictionary *weekIndex* are iterated over until the key = *dayIndex* value.
    - When the above condition is met, the corresponding value of the key is checked in a boolean (to see if it reads "Weekend" or "Weekday") and one of two print statements are executed.

<br/>

### References:
1. Sweigart, A, 2015, Automate the boring stuff with Python, Dictionaries and structuring data, No Starch press,<br/> San Francisco, pp 120.
2. Docs.python.org, 2021, Datetime — Basic date and time types — Python 3.9.2 Documentation, viewed 20 Feb 2021,*<https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday>*.
