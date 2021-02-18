
# Weekly Tasks 2021
# Programming and Scripting



## Introduction
This README file gives a more in-depth explanation of the code used to complete the weekly tasks for the 2021  
Programming and Scripting GMIT module as part of the Higher Diploma in Science in Computing.



## Task 1: (Bmi.py):
*Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in   
centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.* 



### Code:
'
height = float(input("What is your height in centimetres?:"))  
weight = float(input("What is your weight kilograms?:"))  
Metres_Sq = (height/100)**2  
bmi = round(weight / Metres_Sq,2)  
print("BMI is {} kg/m²".format(bmi))  
'


### Code breakdown:
- User is asked for their height(cm) and weight(Kg).
- Height is convered from cm to m² and stored in *Metres_Sq* variable.
- Weight(Kg) is divided by height(m²), rounded to two decimal places and passed to *bmi* variable.
- The bmi result is passed into the {} placeholder via string formatting (.format) and printed.




### References:
1.	Active, 2021, What is BMI and How to Calculate It, viewed 31 Jan 2021, *<https://www.active.com/fitness/  articles/what-is-bmi-and-how-to-calculate-it>*.
2.	GeeksforGeeks, 2021, round () function in Python, viewed 31 Jan 2021, *<https://www.geeksforgeeks.org/round  -function-python>*.
3.	Real Python, 2021, A guide to the newer Python string format techniques, viewed 31 Jan 2021, *<https://real  python.com/python-formatted-output>*.
4.	Sweigart, A, 2015, Automate the boring stuff with Python, No Starch press, San Francisco, pp 15.
