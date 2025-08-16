cnt = 0
def digit_count(s: str) -> int:
    global cnt
    if not s:
        return 0
    
    if s[0].isdigit():
        cnt += 1
    print(cnt)
    return digit_count(s[1:])
        
print(digit_count("svs2141dfb3"))

