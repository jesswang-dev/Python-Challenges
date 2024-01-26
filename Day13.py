#Write a program to shuffle the elements of a list randomly.
import random

def shuffle (list):
    random.shuffle(list)
    return list

# print(shuffle([1,2,3,4,5]))
# print(shuffle(["a", "b", "c", "d"]))