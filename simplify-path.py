def simplify(path):
    stack = []
    cur = ""
    for c in path + "/":
        if c == "/":
            if cur == ".." and stack:
                stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            elif cur == ".":
                pass
            cur = ""
        else:
            cur += c 

    return "/" + "/".join(stack)

print(simplify("/a/./b/../../c/"))
print(simplify("./dots/./"))
print(simplify("./home/"))
print(simplify(".../home/"))
print(simplify("/../home/"))
print(simplify("/..../"))
print(simplify("/home//foo/"))