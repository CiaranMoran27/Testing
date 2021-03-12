# collatz.py
# The program asks the user for a positive integer and outputs successive values 
# based on if the input number is odd or even. The progam ends if 1 is entered.
# Author: Ciaran Moran

numberList = []

number = input("Enter a number: ")


while True:
    try:
        numberInt = int(number)  # try convert number variable to int 

        if numberInt < 0:        # checks the number is positive
            numberInt = int(input("Enter a Enter a positive number: "))
            continue                 # jump back to start of while loop
        else:
            break                    # exit loop 

    except ValueError:                          # if error raised between try and except statement:
        number = input("Enter an integer: ")    
        continue                                # jump back to start of while loop


while numberInt!=1:               # exits while loop when value is not 1
    if numberInt % 2 == 0:             # check if number is even
        numberInt = numberInt // 2         # re-defines numberInt variable as itself divide by 2
    else:
        numberInt = (numberInt * 3) + 1    # if odd re-defines numberInt variable  as (itself x 3) +1
    numberList.append(numberInt)       
print(numberList)


        
# References: 
# 1. Real Python, 2021, The try and except Block: Handling Exceptions, viewed 19 Feb 2021,*<https://realpython.com/python-exceptions/>*.
# 2. Cunningham, P, 2014, Check if input is positive integer, viewed 19 Feb 2021, <https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer>.
# 3. Programiz, 2021, What is the use of break and continue in Python?, viewed 19 Feb 2021,<https://www.programiz.com/python-programming/break-continue>.  
