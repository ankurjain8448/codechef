for _ in xrange(input()):
	n = input()
	ans = 0.0
	for i in xrange(n):
		p,q,d = map(float, raw_input().strip().split())
		l = ((p*d*d)/10000.0)*q
		ans += l
	print ans