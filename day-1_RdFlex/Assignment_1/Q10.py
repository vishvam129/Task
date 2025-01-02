# Custom Caesar Cipher:

# Shifts each character in a string by a fixed number of positions in the alphabet (e.g., a Caesar cipher).

# Accepts both the string and the shift value as inputs.

String=input("Enter String :- ")
shift=int(input("Enter Shift :- "))
result=''
for i in String:
    if (i.isupper()):
        result += chr((ord(i)+shift-65)%26 +65)
    else:
        result+= chr((ord(i)+shift-97)%26+97)

print(result)