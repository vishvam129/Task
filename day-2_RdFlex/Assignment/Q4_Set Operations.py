# Write a program that:
# Accepts two lists of numbers.
# Converts them to sets and finds their union, intersection, and difference.

user_input1 = input("Enter the number Ex: 1 2 3 4 5 :- ").strip().split()
List1 = []
for i in user_input1:
    List1.append(int(i))
    
user_input2 = input("Enter the number Ex: 1 2 3 4 5 :- ").strip().split()
List2 = []
for i in user_input2:
    List2.append(int(i))

Set1 = set(List1)
Set2 = set(List2)

print("The Union of Set1 and Set2 is :- ",Set1.union(Set2))
print("The intersection of Set1 and Set2 is :- ",Set1.intersection(Set2))
print("The difference of Set1 and Set2 is :- ",Set1.difference(Set2))