# 3. Write a Python program to demonstrate inheritance without using the super() keyword.

class Parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def sum(self):
        print(self.a + self.b)

class child(Parent):
    def __init__(self, a, b):
        Parent.__init__(self,a, b)
        self.a = a
        self.b = b
    
c1 = child(2,5)
c1.sum()