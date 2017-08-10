def calc():
	n , d = map(int, raw_input().strip().split())
	a = map(int, raw_input().strip().split())
	sums = sum(a)
	s = sums/n
	if s*n != sums:
		return -1
	steps = 0
	for i in xrange(n-d):
		if a[i] != s:
			diff = abs(a[i] - s)
			steps += diff
			if a[i] > s:
				a[i+d] += diff
			else:
				a[i+d] -= diff
			a[i] = s
	for i in xrange(n-d , n):
		if a[i] != s:
			return -1
	return steps
for _ in xrange(input()):
	print calc()
