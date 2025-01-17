# assert <condition>
# assert <condition>,<error message>

def avg1(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg1(mark2))

mark1 = []
print("Average of mark1:",avg1(mark1))