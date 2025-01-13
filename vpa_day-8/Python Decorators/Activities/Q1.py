# Write a program to:
# Create a decorator to log the execution time of a function.
# Create a decorator that checks user authentication before executing a function.

import time

def log_execution_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@log_execution_time
def example_function():
    time.sleep(2)  
    return "Function complete"

result = example_function()
print(result)


def check_authentication(func):
    def wrapper():
        user_authenticated = False  # Placeholder for authentication logic
        if not user_authenticated:
            print("User is not authenticated!")
            return
        return func()
    return wrapper

@check_authentication
def example_function():
    return "authentication completed"

result = example_function()
print(result)
