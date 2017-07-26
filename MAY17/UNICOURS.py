for _ in xrange(int(raw_input().strip())):
	n = input()
	arr = map(int,raw_input().strip().split())
	m = 0
	for i in arr:
		m = max(m, i)
	print n - m 