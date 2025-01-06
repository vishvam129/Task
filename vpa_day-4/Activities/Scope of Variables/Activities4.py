# Compare how variables behave inside a loop versus outside it using different scopes.

for i in range(21):
    x=0
    x+=i
print("bcs the declaration is in the loop the value is be the last in the range ",x)

x=0
for i in range(21):
    x+=i
print("bcs the declaration is outside the loop the value will bw sum of the range ",x)
