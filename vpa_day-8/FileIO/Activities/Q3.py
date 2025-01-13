# Use the csv module to:
# Create a CSV file with student names and scores.
# Read the CSV file and calculate the average score.

import csv
fields = ['Name',"Marks"]
rows = [['abc',70],['abcww',60],['abwd',20],['abws',22],['absc',74],['abcs',72],['abcd',80]]
marks = []
with open('student_marks_new.csv','w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    csvfile.seek(0)
    csvreader = csv.reader(csvfile)
    
    next(csvreader)
    
    print("The data which write in the csv file is :- ")
    for i in csvreader:
        print(i)
        marks.append(int(i[1]))
        
    print("The average marks of students is :- ",round(sum(marks)/len(marks),2))    