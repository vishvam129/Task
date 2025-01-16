import math 
import random

def fun_math():
    radius = random.randint(1,9)
    print("the area of circle is :- ",(math.pi)*radius**2)

fun_math()

def fun_random():
    print("Rock Paper Scissors Game ")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissor")
    user_choice = int(input("Enter between (1,3) :- "))
    machine_choice = random.randint(1,3)
    print("Machine Choices")
    if machine_choice == 1:
        print("Rock")
    if machine_choice == 2:
        print("Paper")
    if machine_choice == 3:
        print("Scissor") 
    if user_choice == machine_choice:
        print("Yay it's a tie")
    elif user_choice == 1 and machine_choice == 3:
        print("Yay you win!")
    elif user_choice == 2 and machine_choice ==  1:
        print("Yay you win!")   
    elif user_choice == 3 and machine_choice == 2:
        print("Yay you win!")   
    else:
        print("Machine Win!")
    print("Ypu want to play again! (yes/no)")
    user_input = input("Enter Your choice :- ")
    if user_input == "yes":
        fun_random()
    else:   
        print("Thanks")
     
fun_random()