def ksmallest(root):
    stack = [root]
    cur = root
    n = 0
    while cur or stack:

        #  Keep going left
        while cur:
            stack.append(cur)
            cur = cur.left
        # Left processing finished (In order traversal) is l-N-r
        cur = stack.pop()
        n += 1

        if n == k:
            return cur.val

        cur = cur.right



