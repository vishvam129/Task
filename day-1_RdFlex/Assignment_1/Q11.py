# Vowel and Consonant Counter:

# Counts the number of vowels and consonants in a string.

String="Hello why are you"

d={'vowels':0,"consonants":0}

vowel="aeiouAEIOU"

for i in String.split():
    for j in i:
        if j in vowel:
            d["vowels"]=d["vowels"]+1
        else:
            d["consonants"]=d["consonants"]+1
print(d)