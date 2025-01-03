# Generate a list of squares of all even numbers from 1 to 20 using a list comprehension.
# Create a nested list comprehension to generate a multiplication table (1 to 10).



# Generate a list of squares of all even numbers from 1 to 20 using a list comprehension.

List1=[x*x for x in range(1,21) if x%2==0 ]
print("The List of square is :- ",List1)

# Create a nested list comprehension to generate a multiplication table (1 to 10).

List2=[[num*x for x in range(1,11)] for num in range(1,11)]
print("Multiplication table :- ")
for i in List2:
    print(i)