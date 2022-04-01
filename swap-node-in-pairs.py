class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def swap(head):
        dummy = ListNode(next = head)
        prev, cur = dummy, head

        while cur and cur.next:

            nxtPair = cur.next.next
            second = cur.next

            # Reverse the pair
            second.next = cur
            cur.next = nxtPair 
            prev.next = second

            prev = cur
            cur = nxtPair 
        return dummy.next