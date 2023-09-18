# Write a recursive function that tests if a string is a palindrome, such as “kayak”, “never odd or even”
# or “Was it a car or a cat I saw?”.

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()

    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print(is_palindrome("kayak")) 
print(is_palindrome("never odd or even"))  
print(is_palindrome("Was it a car or a cat I saw?"))  
print(is_palindrome("hello"))