#Write a program to check if a number is positive, negative, or zero.
#i: number o:/

def check_number (num):
    if num > 0 :
        print("The number is positive.")
    elif num < 0 :
        print("The number is negative.")
    else:
        print("The number is zero.")
        
#test cases
check_number(5) #it should print positive
check_number(1.234) #it should print positive
check_number(-30) #it should print negative
check_number(-30.01) #it should print negative
check_number(0) #it should print zero
check_number(0.000) #it should print zero