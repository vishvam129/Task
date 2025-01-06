# Add a class variable total_books to count the number of books created.

class Book:
    total_books = 0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books += 1
    
    def display(self):
        print(f"title : {self.title}")
        print(f"author : {self.author}")
        
student=Book("Alice's Adventures in Wonderland","Lewis Carroll")
student1=Book("The Adventures of Tom Sawyer","Mark Twain")

student.display()
student1.display()

print("Total no of books is :- ",Book.total_books)