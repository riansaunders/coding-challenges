from typing import Counter


def group(strs):
    res = {}

    for str in strs:
        chars = {}
        
        for c in str:
            chars[c] = 1 + chars.get(c, 0)
        
        key = tuple(chars)

        if not key in res:
            res[key] = []
        
        res[key].append(str)
    
    return list(res.values())

print(group(["eat", "tea", "tan", "ate", "nat", "bat"]))