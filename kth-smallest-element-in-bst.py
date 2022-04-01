def kthsmall(head, k):
    stack = []
    n = 0
    cur = head

    while cur or stack:
        # Left
        while cur:
            stack.append(cur)
            cur = cur.left
        
        # Me
        n += 1
        if n == k:
            return cur.val
        # Right
        cur = cur.right