# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.

sample_string = 'hellohowareuwhyareuhihowareyou'
sample_dict = {}

for i in sample_string:
    if i in sample_dict:
        sample_dict[i] += 1
    else:
        sample_dict[i] = 1
    
print(sample_dict)