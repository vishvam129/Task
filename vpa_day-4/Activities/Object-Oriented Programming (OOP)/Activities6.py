# Write a Python Program to implement Method Overloading and Method Overriding.
class Test:
    def __init__(self):
        pass
    
    def sum(self):
        print("The original sum methods")
    
    def sum(self):
        print("The overloading sum methos")

class Result(Test):
    def __init__(self):
        super().__init__()
        
    def sum(self):
        print("The overriding sum method ")
        
T=Test()
T.sum()

R=Result()
R.sum()