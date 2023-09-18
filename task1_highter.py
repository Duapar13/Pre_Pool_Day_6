import string

def funA(s, n):
    lowercase_count = sum(1 for char in s if char.islower())
    return lowercase_count >= n

def funB(s, n):
    uppercase_count = sum(1 for char in s if char.isupper())
    return uppercase_count >= n

def funC(s, n):
    return len(s) >= n

def funD(s, n):
    special_chars = set(string.punctuation)
    special_count = sum(1 for char in s if char in special_chars)
    return special_count >= n



def funE(s, n):
    digit_count = sum(1 for char in s if char.isdigit())
    return digit_count >= n

s = "Bonjour@FR13_"


print(funA(s, 2)) 
print(funB(s, 2))  
print(funC(s, 8))  
print(funD(s, 2))  
print(funE(s, 3))  