# Write a program to:
# Calculate the number of weekends between two given dates.
# Display the weekday name for a user-provided date.

from datetime import datetime, timedelta

def assignment1(start_date,end_date):
    start = datetime.strptime(start_date,'%d-%m-%Y')
    end = datetime.strptime(end_date,'%d-%m-%Y')
    weekand = 0
    current = start
    while current < end:
        if current.weekday() in [5,6]:
            weekand += 1
        current += timedelta(days=1)
    print(weekand)
    
    date_str = input("Enter date in d-m-yyyy :- ")
    date = datetime.strptime(date_str,'%d-%m-%Y')
    print(date.strftime('%A'))
    

assignment1('1-3-2025','31-3-2025')

# Create a program that:
# Schedules reminders for a list of tasks with specific deadlines.
# Checks which tasks are overdue based on the current date and time.

from datetime import datetime

class Task:
    def __init__(self,name,deadline):
        self.name = name
        self.deadline = deadline
        
def schedule_task(name,deadline):
        task = Task(name,deadline)
        tasks.append(task)
        
def check_overdue_tasks():
        now = datetime.now()
        overdue_tasks = [task for task in tasks if task.deadline < now]
        if overdue_tasks:
            print("Overdue Tasks:")
            for task in overdue_tasks:
                print(f"{task.name} (Duedate: {task.deadline})")
        else:
            print("No overdue tasks.")

        
tasks = []
while True:
    print("""
          1: Add Task 
          2: Check Overdue 
          3: Exit""")
    choice = int(input("Enter your choice :- "))
    if (choice == 1):
        name = input("Enter the Task :- ")
        deadline_str = input("Enter deadline of your task (d:m:yyyy) :- ")
        deadline = datetime.strptime(deadline_str, '%d-%m-%Y')
        schedule_task(name,deadline)
    if (choice == 2):
        check_overdue_tasks()
    if (choice == 3):
        break