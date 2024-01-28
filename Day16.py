#Write a function that counts the frequency of each word in a sentence.
#i: string o: dictionary
def count_words(string):
    #split the string by space and iterate through the item, and add the item to the dict with the key as item and value as freq
    word_list = string.split()
    output = {}
    for word in word_list:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    
    return output


# print(count_words("Apple Mango Orange Mango Guava Guava Mango"))
# print(count_words("Train Bus Bus Train Taxi Aeroplane Taxi Bus"))