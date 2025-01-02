# Write a function to calculate the factorial of a number.
# Create a function to find the largest element in a list without using the max() function.
# Write a lambda function to filter even numbers from a list.

# Write a function to calculate the factorial of a number.

def fact(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    print(f"The Factorial of {num} is :- {factorial}")

fact(5)

# Create a function to find the largest element in a list without using the max() function.

def max_list(List):
    maxnum = 0
    for i in List:
        if i >= maxnum:
            maxnum = i
    print("The maximum number in the list is :- ",maxnum)
    
List=[1,2,3,34,23,12,34,45,77,2,12,34,65,45]
max_list(List)



# Write a lambda function to filter even numbers from a list.

def even_num(List_lambda):
    num=filter(lambda x:x%2==0,List_lambda)
    print("filter even numbers using lambda is :- ",list(num))  

List_lambda=[2,4,6,8,12,1,3,5,7,9,23]
even_num(List_lambda)

