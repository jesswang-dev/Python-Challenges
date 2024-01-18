#Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
#i: string o: tuple that includes two int
#use ASCII character code to tell if letter is uppercase or lowercase

def upper_and_lower(string):
    #declare two vars upper and lower
    upper = 0
    lower = 0
    #iterate through the string and evaluate if each char's ascii code is either in range 65-90 (upper) or 97-122 (lower) both ends inclusive
    for char in string:
        char_code = ord(char)
        if char_code >= 65 and char_code <= 90:
            upper += 1
        if char_code >= 97 and char_code <= 122:
            lower += 1
            
    return (upper, lower)

#test cases
print(upper_and_lower("AaBbCc123")) #it should return (3,3)
print(upper_and_lower("AaBBCc efgGh")) #it should return (5,6)
print(upper_and_lower("Jessica Wang")) #it should return (2,9)

