def f(head):

    cur = head
    prev = None
    
    while cur:

        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return head

def f(prev, cur):
    if cur == None:
        return prev

    tmp = cur.next
    cur.next = prev

    return f(cur, tmp) 