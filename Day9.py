#Write a program to check if a number is even or odd.

#use input method to get the response and check the value
input = input("Please type in a number: ")
number = float(input)

if number % 2 == 0 :
    print("The number is even.")
elif number % 2 == 1 :
    print("The number is odd.")
else:
    print("Please type in an integer.")