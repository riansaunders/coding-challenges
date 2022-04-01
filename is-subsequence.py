def iss(s, t):
    j = 0
    i = 0
    while j < len(t):
        if s[i] == t[j]:
            i = i + 1
        j = j + 1
    
    return i == len(s)

print(iss("abc", "ahbgdc"))
print(iss("aec", "abcde"))
print(iss("ace", "abcde"))
print(iss("ace", "ace"))
print(iss("axc", "ahbgdc"))
    