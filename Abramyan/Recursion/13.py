def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palindrome(s[1:-1])

test_strings = [
    "radar",    
    "level",      
    "hello",     
    "aba",      
    "abcd",      
]

for s in test_strings:
    result = palindrome(s)
    print(f'palindrome("{s}") = {result}')

    
    
    