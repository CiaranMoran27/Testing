
# This program that asks the user to input any positive integer and 
# outputs the successive values of the following calculation
# Author: Ciaran Moran

number = int(input("Please enter a positive whole number: "))

number_list = [number]


if number < 0:
    print("This program will only accept positive whole numbers")
    number = int(input("Please enter a positive whole number: "))
else:
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        number_list.append(number)
        
            
print(number_list)



#At each step calculate the next value by taking the current value and, if it is even, 
#divide it by two, but if it is odd, multiply it by three and add one.