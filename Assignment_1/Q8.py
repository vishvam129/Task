# Extract Substrings:

# Accepts a string and two characters, start and end.

String=input("Enter A String :- ")

start=input("Enter A start word :- ")

end=input("Enter A end word :- ")


start_index=String.find(start)
end_index=String.find(end)

print(String[start_index+1:end_index])

