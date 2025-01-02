# Write programs to:
# Find unique elements from two lists using sets.
# Check if one set is a subset of another.
# Use set comprehensions to generate squares of even numbers from 1 to 20.

# Find unique elements from two lists using sets.

List = [1,2,3,4,5,6,1,3,2,4,5,6,7,8,9,1]
List1 = [11,21,31,41,51,61,11,31,21,41,51,61,71,81,91,11]

print("First List is :- ",List)
print("First List is :- ",List1)

print("The unique elements from two list is :- ",set(List+List1))

# Check if one set is a subset of another.

Set1={1,2,3,4}
Set2={1,2,3,4,5,6,7,8,9,10}
Set3={1,2,3,5,6,7,8,9}

print("Set1 is subset of Set2 :- ",Set1.issubset(Set2))
print("Set1 is subset of Set3 :- ",Set1.issubset(Set3))


# Use set comprehensions to generate squares of even numbers from 1 to 20.

squares_set={x**2 for x in range(1,21) if x%2 == 0 }
print("squares of even numbers is :- ",squares_set)