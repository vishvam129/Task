
# Create a function to count the number of each vowel in a given string


def vowel():
    d=dict()
    word=input("Enter Sentence:- ")
    v='aeiouAEIOU'
    for i in word:
        if i in v:
            d[i]=1
    for i in word:
        if i in v:
            d[i]=d[i]+1
    print(d)

vowel()