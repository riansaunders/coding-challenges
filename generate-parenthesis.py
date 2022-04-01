def gen(n):
    res = []
    paren = []
    def dfs(open, close):
  
        if open == close == n:
            res.append("".join(paren))
            return

        if open < n:
            paren.append("(")
            dfs(open + 1, close)
            paren.pop()

        if close < open:
            paren.append(")")
            dfs(open, close + 1)
            paren.pop()
            
    dfs(0,0)
    return res

print(gen(3))