# Create a class Book with attributes title, author, and a method to display details.

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def display(self):
        print(f"title : {self.title}")
        print(f"author : {self.author}")
        
student=Book("Alice's Adventures in Wonderland","Lewis Carroll")
student1=Book("The Adventures of Tom Sawyer","Mark Twain")

student.display()
student1.display()
