# Create a Student class with attributes name, grade, and marks for three subjects.
# Add a method to calculate the total and average marks.
# Add a class method to track the total number of students.
# Create a subclass Scholar that adds an attribute scholarship_amount and a method to display it.

class Student:
    total_students=0
    def __init__(self,name,grade,marks):
        self.name=name
        self.grade=grade
        self.marks=marks
        self.sub1=marks[0]
        self.sub2=marks[1]
        self.sub3=marks[2]
        Student.total_students+=1
        
    def calculate(self):
        total_marks=self.sub1+self.sub2+self.sub3
        average_marks=total_marks/len(self.marks)
        print("The total marks of the student is :- ",total_marks)
        print("the average marks of the student is :- ",average_marks)
        
    @classmethod
    def no_of_students(cls):
        print("Total student in the class is :- ",Student.total_students)
        
class Scholar(Student):
    def __init__(self, name, grade,marks,scholarship_amount):
        super().__init__(name, grade, marks)
        self.scholarship_amount=scholarship_amount
    
    def display(self):
        print("Name :- ",self.name)
        print("Grade :- ",self.grade)
        print("marks of sub1  :- ",self.sub1)
        print("marks of sub2  :- ",self.sub2)
        print("marks of sub3  :- ",self.sub3)
        
S1=Student('abc',95,[90,93,97])
S2=Scholar('xyz',97,[97,97,97],45000)

S1.calculate()
S2.calculate()
Student.no_of_students()
        
        
        
        