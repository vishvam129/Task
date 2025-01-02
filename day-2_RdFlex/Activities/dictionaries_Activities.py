# Write programs to:
# Create a dictionary where keys are numbers from 1 to 5 and values are their cubes.
# Merge two dictionaries.
# Count occurrences of each word in a string and store the results in a dictionary.

# Create a dictionary where keys are numbers from 1 to 5 and values are their cubes.

d=dict()
for i in range(1,6):
    d[i] = i**3
print("First dictionary is :- ",d)



# Merge two dictionaries.

d1 = dict()
for i in range(6,11):
    d1[i] = i**3
print("Second dictionary is :- ",d1)

merged_dictionary=dict()

for i in d:
    value = d[i]
    merged_dictionary[i] = value

for i in d1:
    value = d1[i]
    merged_dictionary[i] = value
    
print("Mearged_dictionary is :- ",merged_dictionary)


# Count occurrences of each word in a string and store the results in a dictionary.

# this is without counting the space  

# String='hello how are u are u fine and why are u'

# d=dict()

# for i in String.split():
#     for j in i:
#         if j in d:
#             d[j]+=1
#         else:
#             d[j]=1
        
# print(d)


# This is with counting the space

String='hello how are u are u fine and why are u'

d=dict()

for i in String:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
print("countig char in String :- ",d)



        