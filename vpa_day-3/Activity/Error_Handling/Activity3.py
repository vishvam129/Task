# Implement error handling in a function that takes user input,
# converts it to an integer, and divides a number by it.

def error_handle():
    user_input=input("Enter the number 1 :- ")
    user_input1=input("Enter the number 2 :-")
    try:
        num1=int(user_input)
        num2=int(user_input1)
        ans=num1//num2
    except TypeError:
        print(TypeError)
    except ZeroDivisionError:
        print(ZeroDivisionError)
    else:
        print("The Answer is :- ",ans)
    finally:
        print("this is finally part ")
        
error_handle()
        