# Convert a list of strings to uppercase using list comprehensions.

user_input = input("Enter a String you Like :- ").strip().split()
user_List = [i.upper() for i in user_input]
print(f"The Final List is {user_List}")