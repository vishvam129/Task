# Convert a list to a tuple and vice versa.
# Create a tuple of numbers and find the sum, max, and min.
# Use tuple unpacking to swap values of two variables.


# Convert a list to a tuple and vice versa.

def convertion():
    List = [2,3,4,5,'Hello','Hi','Why','Bye',6,7,8,9]
    print("Default String is :- ",List)
    
    converted_Tuple = tuple(List)
    print("List to tuple is :- ",converted_Tuple)
    
    converted_List = list(converted_Tuple)
    print("Tuple to list is :- ",converted_List)
    
convertion()


# Create a tuple of numbers and find the sum, max, and min.

def operation_on_tuple():
    sample_tuple = (1,2,4,6,7,8,4,5,65,43,23,45,76,89)
    print("sum of the tupe is :-",sum(sample_tuple))
    print("max of the tuple is :- ",max(sample_tuple))
    print("min of the tuple is :- ",min(sample_tuple))
    
operation_on_tuple()

# Use tuple unpacking to swap values of two variables.

def swap_values():
    sample_tuple = (10,20,30,40,23,34)
    print("The Original Tuple is :- ",sample_tuple)
    (num1,num2,*num) = sample_tuple
    print("First num is :- ",num1)
    print("Second num is :- ",num2)
    print("Other num is :- ",num)
    
    print("After Swap ")
    
    swap_tuple = (num2,num1,*num)
    print("First num is :- ",num2)
    print("Second num is :- ",num1)
    print("Other num is :- ",num)
    
    print("After swapping the tuple is :- ",swap_tuple)

swap_values()