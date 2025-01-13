# Write a program to:
# Use Counter to analyze the frequency of words in a text file.
# Identify the top 5 most common words.

from collections import Counter

def assignment1():
    with open('file.txt','r') as file:
        text = file.read().strip().split()
        ctr = Counter(text)
        print(ctr)
        print(ctr.most_common(5))
        
assignment1()

# Create a program that:
# Uses OrderedDict to maintain the order of tasks in a to-do list.
# Allows adding, removing, and displaying tasks in the order they were added.

from collections import OrderedDict

class Todo:
    def __init__(self):
        self.Task = OrderedDict()
    
    def add_task(self,task):
        if task not in self.Task:
            self.Task[task] = None
            print(f"{task} is Added")
        else:
            print(f"{task} is already exists")
            
    def remove_task(self,task):
        if task in self.Task:
            del self.Task[task]
            print(f"{task} is deleted")
        else:
            print(f"{task} is does not exist")
    
    def display_task(self):
        if not self.Task:
            print("There is no task")
        else:
            print("TOList:- ")
            for task in self.Task.keys():
                print(task)

person = Todo()
while True:
    print("""
          Enter 1 to add task 
          Enter 2 to remove task
          Enter 3 to display task
          Enter 4 to exit.""")
    choice = int(input("Enter your choice :- "))
    
    if(choice == 1):
        task = input("Enter The task u want to add :- ")
        person.add_task(task)
    
    if(choice == 2):
        person.display_task()
        task = input("Enter The task u want to remove :- ")
        person.remove_task(task)
        
    if(choice == 3):
        person.display_task()
    
    if(choice == 4):
        break