from locale import currency


class ListNode:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

def f(head, val):
    dummy = ListNode(next=head)
    prev, cur = dummy, head
    while cur:

        nxt = cur.next
        if cur.val == val:
            prev.next = nxt
        else:
            prev = cur
        cur = cur.next

    return dummy.next