s = lambda n : (n*(n+1))/2 
for _ in xrange(input()):
	u,v = map(int, raw_input().strip().split())
	if u == v == 0 :
		ss = 0
	else:
		ss = s(u+v) + u + 1
	print ss