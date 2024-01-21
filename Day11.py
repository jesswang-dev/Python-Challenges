#Write a program to print the multiplication table of a given number.
#i: num o: /
def multi_table (num):
    i = 1
    while i <= num:
        print(f"{i} x {num} = {i*num}")
        i+=1
        
#test cases
# multi_table(5)
# multi_table(6)