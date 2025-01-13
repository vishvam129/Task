# Use regular expressions to:
# Identify and extract hashtags from a social media post.
# Validate passwords (e.g., length >= 8, at least one uppercase letter,
# one digit, and one special character).

import re
text = input("Enter text with #included :- ")
print(re.findall(r'#\w+',text))

password = input("Enter password for check :- ")
print("Password valid " if re.findall(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',password) else "password is not valid")
