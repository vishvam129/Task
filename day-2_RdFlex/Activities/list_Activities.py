# Write programs using list methods:
# Add/remove elements dynamically.
# Find the second largest number in a list.
# Combine two lists and remove duplicates.


List = list()

while True:
    print("""
          Enter 0 : Add Element :-
          Enter 1 : Remove Element:- 
          Enter 2 : Exit 
          """)
    value = int(input("Enter your Choice :- "))
    
    if (value == 0):
        add_Elements = int(input("Enter the element you want to enter :- "))
        List.append(add_Elements)
        
    elif(value == 1):
        remove_Elements = int(input("Enter the element you want to remove :- "))
        List.remove(remove_Elements)
    
    elif(value == 2):
        break
    
print("List is :- ",List)


# Find the second largest number in a list.

sorted_List = sorted(List,reverse=True)
print("Sorted List is :- ",sorted_List)
print("Second Largest Number is :- ",sorted_List[1])


# Combine two lists and remove duplicates.

List1 = list()

while True:
    print("""
          For Second List for combine
          Enter 0 : Add Element :-
          Enter 1 : Exit :- 
          """)
    value = int(input("Enter your Choice :- "))
    
    if (value == 0):
        add_Elements = int(input("Enter the element you want to enter :- "))
        List1.append(add_Elements)
        
    elif(value == 1):
        break
print("First List :- ",List)
print("Secoond List:- ",List1)

List2 = List + List1

List3 = list()

for i in List2:
    if i not in List3:
        List3.append(i)
print("List without duplicates :- ",List3)

