# Write a program to:
# Extract all email addresses from a large text document.
# Replace sensitive information (like phone numbers) in a text file with ****.
# import re
import re

def extract_emails(text):
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return email_pattern.findall(text)

def replace_phone_numbers(text):
    phone_pattern = re.compile(r'\d{10}')
    return phone_pattern.sub('****', text)

sample_text = """
Hello, you can reach me at example@example.com or contact@example.org.
My phone number is 9876543210.
Another email: someone.else@domain.com
"""

emails = extract_emails(sample_text)
print("Extracted Emails:")
for email in emails:
    print(email)

cleaned_text = replace_phone_numbers(sample_text)
print("\nText with Phone Numbers Replaced:")
print(cleaned_text)
