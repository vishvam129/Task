# Creates a Product class with attributes name, price, and stock.
# Adds methods to sell a product, restock, and display details.
# Implements error handling to ensure valid input for price (must be positive) and 
# stock (must be an integer).
# Uses a lambda function to apply a discount to all product prices.
# Writes product details into a file and reads them back, sorting the products by stock quantity.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def sell(self,quantity):
        self.stock=self.stock-quantity
    
    def restock(self,quantity):
        self.stock+=quantity
        
    def display(self):
        print("Product Name :- ",self.name)
        print("Product Price :- ",self.price)
        print("Product Stock :- ",self.stock)
    
    def write_to_file(self):
        with open('Test.txt','w') as file:     
            file.write(self.name)
            file.write('\n')
            file.write(str(self.price))
            file.write('\n')
            file.write(str(self.stock))
            file.write('\n')
            
    def read_from_file(self):
        with open('Test.txt') as file:
            print(file.read())
            
product=input("Enter the products :- ")
try:
    stock=int(input("Enter stock :-"))
    price=int(input("Enter the price in integer :- "))
    assert price>0
    
except AssertionError:
    print("Enter positive price :- ")
    
except ValueError as e:
    print(e)
    print("Enter integer Stock :- ")
    
else:
    p=lambda price:price*0.9   
    p1=Product(product,int(p(price)),stock)
    p1.display()
    p1.restock(12)
    p1.sell(10)
    p1.display()
    p1.write_to_file()
    p1.read_from_file()      


        
            