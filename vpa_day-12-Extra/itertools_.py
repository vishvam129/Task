from itertools import combinations
import itertools
from itertools import product

comb = combinations([1, 2, 3, 4], 2)
print(list(comb))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))


print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['hello', 'how', 'u'], '2')))
print()

print("The cartesian product of the containers:")
print(list(product('hi', [3, 4])))
