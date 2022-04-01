from typing import Counter


def sol(stickers, target):
    letter_counts = { s: Counter(s) for s in stickers }
    res = []
    unused = {}

    def dfs(index, stickerCount): 
        if index == len(target):
            res.append(stickerCount)
            return stickerCount

        def use(sticker):
            new_index = index
            while new_index < len(target) and target[new_index] in sticker and sticker[target[new_index]] > 0:
                sticker[target[new_index]] -= 1
                new_index = new_index + 1

            if new_index != index:
                return new_index
            return 0 

        for s in stickers:
            sticker = letter_counts[s].copy()
            sticker.update(unused)
            if unused:
                print(s, sticker)

            nxt = use(sticker)
            if nxt: 
                stickerCount += 1
                unused.update(sticker)
                dfs(nxt, stickerCount)  
    dfs(0, 0)

    print(res)

    if not res:
        return -1
    return min(res)
        
def sol2(stickers, target):
    stickCount = []
    for i, s in enumerate(stickers):
        stickCount.append({})
        for c in s:
            stickCount[i][c] = 1 + stickCount[i].get(c, 0)

    dp = {}

    def dfs(t, stick):
        if t in dp:
            return dp[t]  
        remainT = ""
        res = 1 if stick else 0
        for c in t:
            if c in stick and stick[c] > 0:
                stick[c] -= 1
            else:
                remainT += c

        # The big difference was he used the substring.
        
        if remainT:
            used = float("inf")

            for s in stickCount:
                if remainT[0] in s:
                   used = min(used, dfs(remainT, s.copy()))
            dp[remainT] = used
            res += used

        return res

    res = dfs(target, {})
    return res if res != float("inf") else -1

print(sol2(["with", "example", "science"], "thehat"))
print(sol2(["these", "guess", "about", "garden", "him"], "atomher"))
# print(sol(["notice", "possible"], "basicbasic"))
# print(sol(["example"], "example"))
# print(sol(["sail","just","point","over","hard","share","say","distant","proper","occur","before","whose","guess","lead","prove","pattern","six","fat","add","music","grand","show","final","hope","listen","week","picture","buy","run","though","between","serve","here","nation","forward","stick","decide","post","ear","than","he","word","would","band","many","well","gun","wish","toward","think"], "governgreat"))
