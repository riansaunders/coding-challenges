class ListNode:
    def __init__(self, val):
        self.val = val

def copy(l):
    if not l:
        return None
    cur = l
    mapping = {}

    while cur:
        mapping[cur] = ListNode(cur.val) 
        cur = cur.next

    cur = l


    while cur:
        copy = mapping[cur]
        copy.next = mapping[cur.next] if cur.next in mapping else None
        copy.random = mapping[cur.random] if cur.random in mapping else None
        
        cur = cur.next

    return mapping[l]