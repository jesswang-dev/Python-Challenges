#Write a program to count the occurrences of a specific character in a string.
#i: string and character o: int

def count_times (str, char):
    #formatting the input str and char into lower cases
    str_lower = str.lower()
    char_lower = char.lower()
    return str_lower.count(char_lower)

#test cases
print(count_times("abc etdfec", "e")) #should return 2
print(count_times("ABCabcA", "A")) #should return 3