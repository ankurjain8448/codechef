mod = 10**9 + 7

for _ in xrange(input()):
	n, m  = map(int, raw_input().strip().split())
	ans = [0 for i in xrange(n)]
	ans_till_index = []
	for i in xrange(m):
		t, l, r = map(int, raw_input().strip().split())
		l -= 1; r -= 1
		if t == 1:
			ans[l] += 1
			if r+1 != n:
				ans[r+1] -= 1
		else:
			if l > 0:
				for i in xrange(n):
					ans[i] = ans[i] + ans_till_index[r][i] - ans_till_index[l-1][i]
			else:
				for i in xrange(n):
					ans[i] = ans[i] + ans_till_index[r][i]
 
		ans_till_index.append([i%mod for i in ans])

	count = 0
	for i in xrange(n):
		count = (count + ans[i]) % mod
		ans[i] = str(count)
 
	print " ".join(ans)
