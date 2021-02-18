#This program takes in a string the user and outputs every second letter in reverse order 
# Author: Ciaran Moran

sentence = input("Please enter a sentence: ")

#reverseString variable doesnt specify a start:finish index of string, therefor full string used as the "slice"
#A Reverse Step of -2 is employed to iterate backwards over every second character and store in variable

reverse_string = sentence[::-2]
print(reverse_string)