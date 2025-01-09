# Creates a custom exception InvalidAgeError and raises it if a user
# enters an age less than 0 or greater than 100.

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be in the range of 0 to 100"):
        self.age=age
        super().__init__(message)
        
try:
    age = int(input("Enter your age or random number :- "))
    if (age < 0 or age > 100):
        raise InvalidAgeError(age)
except Exception as e:
    print(e)