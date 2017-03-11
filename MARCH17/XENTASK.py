for _ in xrange(input()):
	n = input()
	a,b = 0,0
	for index, value in enumerate(raw_input().strip().split()):
		value = int(value)
		if index%2 == 0:
			a += value
		else:
			b += value
	c,d = 0,0
	for index, value in enumerate(raw_input().strip().split()):
		value = int(value)
		if index%2 == 0:
			c += value
		else:
			d += value
	print min(a+d, b+c)