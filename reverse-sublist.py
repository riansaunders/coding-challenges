class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverseBetween(head, left: int, right: int):
    prev = None
    cur = head
    while left > 1:
        prev =cur
        cur = cur.next
        left, right = left - 1, right - 1
        
    tail, con = cur, prev
    while right:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        right -= 1
    
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    
    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverseBetween(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()