# Build a program that:
# Reads a CSV file containing student names and scores (use a sample file or mock data).
# Calculates the average score and writes it back into a new file.
# Handles any file-related errors.


with open('student-dataset.csv') as file:
    file.readline()
    for i in file.readlines():
        data=i.split(",")
        print(data)
        names=data[1]
        english=float(data[9])
        maths=float(data[10])
        science=float(data[11])
        avg_grades=((english + maths + science)//3)
        with open('names_avg.txt','a') as file:
            file.write(names)
            file.write("-->")
            file.write(str(avg_grades))
            file.write('\n')
            