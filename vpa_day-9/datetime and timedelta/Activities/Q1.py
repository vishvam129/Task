# Write a program to:
# Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
# Parse a date string (e.g., "2025-01-01") into a datetime object.

from datetime import datetime

def activity1():
    print(datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))
    print("Parsed datetime object:", datetime.strptime("2025-01-01", '%Y-%m-%d') )

activity1()

# Create a program that:
# Accepts two dates from the user and calculates the number of days between them.
# Adds 7 days to the current date and displays the result

from datetime import datetime, timedelta

def activity2():
    date1 = datetime.strptime(input("Enter date d/m/y :- "),'%d/%m/%Y')
    date2 = datetime.strptime(input("Enter date d/m/y :- "),'%d/%m/%Y')
    print(f"The remainning day is {date1-date2}")
    print(datetime.today().date() + timedelta(days=7))
activity2()

# Use timedelta to:
# Schedule a recurring task every 5 minutes for the next hour.
# Calculate the age of a person based on their birthdate.

from datetime import datetime, timedelta
def activity3():
    start_time = datetime.now()
    current_time = start_time
    while current_time < start_time + timedelta(hours=1):
        current_time += timedelta(minutes=5)
        print("After 5 minutes :- ",current_time)
    
    birthday_date = input("Enter your birthday date in d-m-yyyy formate ")
    birthday = datetime.strptime(birthday_date,'%d-%m-%Y')
    today_date = datetime.now()
    age = today_date.year - birthday.year - ((today_date.month,today_date.month) < (birthday.day,birthday.day))
    print("Your age is ",age)
    
activity3()

# Write a program to:
# Generate a list of dates for the next 7 days.
# Find all Mondays in the current month.

from datetime import datetime,timedelta

def activity4():
    days = []
    today_date = datetime.now()
    for i in range(1,8):
        next_date = today_date + timedelta(days=i)
        days.append(next_date.strftime('%Y-%m-%d'))
    print(days)
    
    start_date = datetime(2025, 1 ,1)
    end_date = start_date + timedelta(days=30)
    mondays = []
    while start_date < end_date :
        if start_date.weekday() == 0:
            mondays.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)
    print(mondays)
activity4()
        