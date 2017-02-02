for _ in xrange(input()):
	n, x = map(int, raw_input().strip().split())
	q = n/x
	if q*x == n :
		print x
	else:
		print n - (q*x)