# String Reversal with Conditions:

# Reverses the order of words in a sentence

String=input('Enter String :- ')
word=String.split()
result=''
if len(word)>3:
    for i in word:
        result=i+" "+result
    print("",result)
else:
    print(String)