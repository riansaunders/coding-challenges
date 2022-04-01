def mcw(paragraph, banned):
        paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        count = {}
        
        most_common = ""
        most_common_count = 0 
        for word in paragraph.split(" "):
            nw = word 
            if not nw or (banned and nw in banned):
                continue
                
            count[nw] = 1 + count.get(nw, 0)    
            
            if count[nw] > most_common_count:
                most_common_count = count[nw]
                most_common = nw
        
        return most_common

print(mcw("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mcw("a.", []))
print(mcw("a, a, a, a, b,b,b,c, c", ["a"]))