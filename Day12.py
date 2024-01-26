#Write a program to reverse a given string.

def reverse_str(str):
    #slice the input string from start to end with step value -1
    return str[::-1]

#test cases
# print(reverse_str("HelloWorld!")) #it should return !dlroWolleH
# print(reverse_str("H e l l o")) #it should return o l l e H
