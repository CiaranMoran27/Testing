# squareroot.py
# The program asks the user for a positive floatint-point number and outputs an approx. square root. 
# based on if the input number is odd or even. The progam ends if 1 is entered.
# Author: Ciaran Moran


def userValidation():  
    while True:
        number = input("Please enter a positive number: ")
        try:

            numberFloat = float(number)                                         # try convert number variable to float
            if numberFloat < 0:                                         
                continue                                                           # jump back to start of while loop            
            else:
                sqrt(numberFloat)                                                  # pass float into sqrt function
                break                                                              # exit loop 
                               
        except ValueError:                                                      # if error raised between try and except statement:  
            continue                                                               # jump back to start of while loop


def sqrt(numberFloat,tolerance = 0.000001):                                      # set tolerance limit to low value (will cause more loop iterations)  
    estimate = numberFloat                                                       
    diff = 9999999999                                                            # large diff variable ensures 1st iteration of  while loop will run 

    while diff > tolerance:
        newEstimate = estimate - ((estimate**2 - numberFloat) / (2*estimate))      # Newton's Method                    
        diff = newEstimate - estimate                                              # difference between two guesses
        diff = abs(diff)                                                           # return absolute difference
        estimate = newEstimate 

    print("The square root of {} is approx. {}".format(numberFloat,round(newEstimate,2)))   

userValidation() 


# References:   
# 1. Real Python, 2021, Defining Your Own Python Function,Argument Passing, viewed 27 Feb 2021,*<https://realpython.com/defining-your-own-python-function/#argument-passing>*.
# 2  Sıddık Açıl, 2018, Newton Square Root Method in Python, viewed 27 Feb 2021, https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# 3. Approximating Square Roots w/ Newton's Method,2018, added by Nerdfirst [Online]. Available at https://www.youtube.com/watch?v=tUFzOLDuvaE&t=1042s
