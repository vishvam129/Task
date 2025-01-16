# Write a Python Program to find the Sum of All values in a Dictionary

sample_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 'six'}
sum_values = 0

for value in sample_dict.values():
    if isinstance(value, int):
        sum_values += value
    elif isinstance(value, str) and value.isdigit():
        sum_values += int(value)

print(sum_values)
