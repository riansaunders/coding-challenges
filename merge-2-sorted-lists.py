class ListNode:
    def __init__(self) -> None:
        pass

def f(l1 , l2):
    dummy = ListNode()
    tail = dummy 

    while l1 and l2:

        if l2.val > l1.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next
 
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next