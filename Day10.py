#Write a program to remove duplicates from a list.
#i: List o: List
def remove_dup (list):
    #delcare an empty set, loop through the input list and check if the item already exits in the set
    s = set()
    output = []
    for item in list:
        if item not in s:
            s.add(item)
            output.append(item)
            
    return output
    

list1 = remove_dup(["a", "b", "b", "c", "c"])
# print(list1) # it should return ["a", "b", "c"]
list2 = remove_dup([1,2,3,4,5,1,3])
# print(list2) # it should return [1, 2, 3, 4, 5]
