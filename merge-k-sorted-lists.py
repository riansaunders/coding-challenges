class ListNode:
    def __init__(self) -> None:
        pass

def mergeLists(lists):
    if not lists or len(lists) == 0:
        return None



    def mergeTwo(l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
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

        # We do it this way because have singly linked lists.
        return dummy.next
 

    while len(lists) > 0:

        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            mergedLists.append(mergeTwo(l1, l2))
        lists = mergedLists    

    return lists[0]