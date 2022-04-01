def removeKthNodeFromEnd(head, k):
	
	cur, p2 = head, head

	prev = None
	rSteps = k

	count = 0
	length = 0
	
	while cur:
		
		while rSteps and p2:
			length = length + 1
			p2 = p2.next
			rSteps = rSteps - 1
			
		if not rSteps and p2:
			rSteps = k 
			
		if not p2 and length and length - k == count:
			if prev:
				prev.next= cur.next if cur else None
			elif cur and cur.next:
				head.value = head.next.value
				head.next = head.next.next
			break
			
		
		prev = cur
		cur = cur.next
		count = count + 1