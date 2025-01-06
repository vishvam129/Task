# Write a function to check the visibility of a variable defined inside a loop

def Test():
    a=0
    for i in range(21):
        b=0
        b+=i
        a+=i
    print('This is defined in the loop thats why it prints only last element :-',b)
    print('this is defind outside of the loop that why it prints the sum of the loop :- ',a)

Test()