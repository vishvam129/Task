# Extract even numbers from a list and their squares in a dictionary using comprehensions.

result = {num :num*num for num in range(21) if num%2 == 0}
print("The Final Rsult is ",result)