# Write a program to:
# Count the frequency of characters in a string using Counter.
# Find the top 3 most common elements in a list.

from collections import Counter

def activity1():
    user_input = input("Enter The String u Want find frequency :- ")
    freq_char = Counter(user_input)
    print(f"The freq of char is {freq_char}")
    
    numbers = [1,2,3,4,5,5,6,7,8,2,3,4,5,2,3,2,2,2,2,2,2,3,3,4,5,6,7]
    ctr = Counter(numbers)
    print(f"The most common 3 element is {ctr.most_common(3)}")
activity1()

# Create a program that:
# Uses defaultdict to group words by their lengths from a list of strings.
# Handles cases where a word length does not exist.

from collections import defaultdict

def activity2():
    words = input("Enter The list of Strings :- ").strip().split()
    words_dict = defaultdict(list)
    for word in words:
        words_dict[len(word)].append(word)
    print(words_dict)    
           
activity2()

# Write a program to:
# Use deque to implement a queue with the ability to add and remove elements from both ends.
# Rotate the deque and display the results.

from collections import deque

def activity3():
    numbers = [1,2,3,4,5,6,7,8,9]
    user_deque = deque(numbers)
    print(f"The current deque is {user_deque}")
    add_right = int(input("Enter the number u want to add from right :- "))
    user_deque.append(add_right)
    print(f"The updated deque is {user_deque}")
    add_left = int(input("Enter the number u want to add from left :- "))
    user_deque.appendleft(add_left)
    print(f"The updated deque is {user_deque}")
    print(f"The removed element from right is {user_deque.pop()}")
    print(f"The updated deque is {user_deque}")
    print(f"The removed element from left is {user_deque.popleft()}")
    print(f"The updated deque is {user_deque}")
    print(len(user_deque))
    user_deque.rotate(4)
    print(f"The rotated deque is {list(user_deque)}")

activity3()

# Use namedtuple to:
# Create a Point class and calculate the distance between two points.
# Store student records (name, age, grade) and print their details.

from collections import namedtuple

def activity4():
    point = namedtuple("Point",['a','b'])
    p = point(4,5)
    p1 = point(9,8)
    print(f"({p1.a-p.a},{p1.b-p.b})")
    
    students = namedtuple('Students',["name","age","grade"])
    students1 = students("ABC",25,"A")
    print(f"The name of the Student is {students1.name}")
    print(f"The age of the Student is {students1.age}")
    print(f"The grade of the Student is {students1.grade}")

activity4()