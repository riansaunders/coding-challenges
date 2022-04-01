def f(val):
	for n in range(len(val) -1, -1, -1):
		offset = len(val) -1 - n
		val[n], val[offset] = val[offset], val[n]
	return val




# print(f("abc"))
c = "abc"
c[1] = "d"