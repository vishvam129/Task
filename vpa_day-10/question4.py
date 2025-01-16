# Write a Python program that removes and prints every third
# number from a list of numbers until the list is empty.

sample_list = [1,2,3,4,5,6,7,8,9]
position = 2
while sample_list:
    if len(sample_list) > 0:
        if position >= len(sample_list):
            position = position % len(sample_list)
        print(sample_list.pop(position))
        position += 2
print(sample_list)