def s(word):
    def bt(i, prev):
        if i >= len(word):
            return True

        for j in range(i, len(word)):
            num = int(word[i:j + 1])
            if num + 1 == prev and bt(j + 1, num):
                return True
                
        return False


    for i in range(len(word) - 1):
        val = int(word[:i + 1]) 
        if bt(i + 1, val):
            return True

    return False
    
print(s("009089"))