# Write a package for basic string utilities like reversing strings, counting vowels, 
# and checking palindromes.

def reversed_string(s):
    return f"The reverse String of {s} is {s[::-1]}"

def count_vowels(s):
    vowel="aeiou"
    count=0
    for i in s.lower():
        if i in vowel:
            count += 1
    return f"The count of vowel in string {s} is {count}"

def is_palindromes(s):
    if (s == s[::-1]):
        return f"The String {s} is palindrome. "
    else:
        return f"The String {s} is not a palindrome. "