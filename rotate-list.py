class ListNode:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.next = nxt

def rl(root, k):
    if not root:
        return None

    dummy = ListNode()
    tail = dummy

    l = 0
    cur = root
    vend = None
    # Calculate the length of the list.
    while cur:
        l = l + 1
        vend = cur
        cur = cur.next
    
    # Calculate the target
    k %= l
    target = l - k

    if not k:
        return root

    # Iterate to the target element.
    # Sever the link to the next element
    cur = root
    p = 0
    head = None
    while cur:
        p += 1
        if p == target:
            head = cur.next
            cur.next = None
            break
        cur = cur.next 
        
    # Recreate the links
    vend.next = root
    tail.next = head

    return dummy.next