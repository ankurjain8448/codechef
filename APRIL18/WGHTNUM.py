mod = 10**9 + 7
for _ in xrange(input()):
	n, w = map(int, raw_input().strip().split())
	weight = [9,8,7,6,5,4,3,2,1]
	w = w % 9
	if n == 2:
		print weight[w]
	else:
		t = (10**(n-2))%mod
		print (2*(t*weight[w])) % mod
