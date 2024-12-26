# Please write a function named all_the_longest, which takes a list of strings 
# as its argument. The function should return a new list containing the longest 
# string in the original list. If more than one are equally long, the function 
# should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.

# my_list = ["first", "second", "fourth", "eleventh"]

# result = all_the_longest(my_list)
# print(result) # ['eleventh']
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = all_the_longest(my_list)
# print(result) # ['dorothy', 'richard']
# Write your solution here
def all_the_longest(my_list:list)->list:
    lenght_list=[]
    max_number=0
    longest_list=[]
    for word in my_list:
        lenght_list.append(len(word))
    max_number = max(lenght_list)
    for word in my_list:
        if len(word) == max_number:
            longest_list.append(word)
    return longest_list



if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)