# Create a class to represent a BankAccount with methods to deposit, withdraw, and check balance.
# Implement a class to represent a Rectangle with methods to calculate area and perimeter.
# Create a Student class with attributes for name, age, and grades. Add methods to calculate 
# average grade and display student details.

class BankAccount():
    def __init__(self,balance):
        self.balance=balance
        print("The original balance is :-",self.balance)
    
    def deposit(self,amount):
        self.balance+=amount
        new_balance=self.balance
        print(f"Your updated balance is {new_balance}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("The withdraw amount is more then the balance ")
            return f"The Available blance is {self.balance}"
        else:
            self.balance-=amount
            new_balance=self.balance
            print(f"Your remaining balance is {new_balance}")
            
    def check_balance(self):
        print(f"The Available blance is {self.balance}")

person1=BankAccount(50000)
    
person1.deposit(25000)
person1.withdraw(20000)
person1.check_balance()


# Implement a class to represent a Rectangle with methods to calculate area and perimeter.

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    
    def area_rectangle(self):
        area=self.width*self.length
        print("The Area of a Rectangle is :- ",area)
    
    def perimeter_rectangle(self):
        parimeter=2*(self.width+self.length)
        print("The Perimeter of a Rectangle is :- ",parimeter)

ract=Rectangle(5,7)

ract.area_rectangle()
ract.perimeter_rectangle()



# Create a Student class with attributes for name, age, and grades. Add methods to calculate 
# average grade and display student details.

class Student:
    def __init__(self,name,age,*grades):
        self.name=name
        self.age=age
        self.grades=grades
    
    def avg_grades(self):
        avg=sum(self.grades)//len(self.grades)
        print(f"The Avarage of {len(self.grades)} Subject is :- ",avg)
    
    def dispay(self):
        print("The name of the Student is :- ",self.name)
        print("The age of the Student is :- ",self.age)
        print("The grades of the Student is :- ",self.grades)
        
student_1=Student('Abc',18,90,89,78,90,98)

student_1.avg_grades()
student_1.dispay()