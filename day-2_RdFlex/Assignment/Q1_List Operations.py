# Write a program that:
# Accepts a list of integers.
# Returns a new list with duplicates removed, sorted in ascending order.

print("Enter a list of Integer Ex: 1 2 3 4 5")

user_input = input().strip().split()
user_list = []
for i in user_input:
    user_list.append(int(i))
    
def remove_duplicates(user_list):
    new_list = list()
    for i in user_list:
        if i in new_list:
            break
        else:
            new_list.append(i)
        sorted_list = sorted(new_list)
    return sorted_list

print("The sorted List is :- ",remove_duplicates(user_list))