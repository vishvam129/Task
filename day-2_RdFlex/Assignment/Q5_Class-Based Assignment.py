# Create a Library class to manage a collection of books. Include methods to:
# Add a book.
# Remove a book.
# Display all books.

class Library:
    def __init__(self):
        self.books=[]
        
    def add_book(self,book):
        self.books.append(book)
        
    def remove_book(self,book):
        self.books.remove(book)
        
    def display(self):
        for i in self.books:
            print(i)
    
student1=Library()
student1.add_book("Harry Potter and the Goblet of Fire")
student1.add_book("A Little Life")
student1.add_book("Chronicles: Volume One")
student1.add_book("The Tipping Point")
student1.add_book("Darkmans")
student1.add_book("The Siege")
student1.add_book("Light")

student1.remove_book("A Little Life")
student1.remove_book("The Siege")

student1.display()

        