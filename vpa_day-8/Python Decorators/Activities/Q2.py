# Develop a program that:
# Uses a decorator to validate input arguments of a function.
# Chains multiple decorators to add both logging and validation to a function.

def validate_inputs(func):
    def wrapper(*args, **kwargs):
        if not args or args[0] <= 0:
            print("Invalid input!")
            return
        return func(*args, **kwargs)
    return wrapper

@validate_inputs
def process_data(data):
    return f"Processing data: {data}"

print(process_data(10))
print(process_data(-1))  # This will trigger "Invalid input!"
