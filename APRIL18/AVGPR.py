for _ in xrange(input()):
	n = input()
	even = []
	odd = []
	s = {}#set()

	for i in map(int, raw_input().strip().split()):
		if i % 2 == 1:
			odd.append(i)
		else:
			even.append(i)
		# s.add(i)
		if i in s:
			s[i] += 1
		else:
			s[i] = 1
	ans = 0
	keys = s.keys()
	for k, v in s.iteritems():
		if v > 1:
			ans = ans + (v-1)**v
	l = len(s)

	for i in xrange(l):
		for j in xrange(i+1, l):
			if (keys[i] + keys[j])/2 in s:
				ans += 1
	# for i in xrange(len(odd)):
	# 	for j in xrange(i+1, len(odd)):
	# 		if (odd[i] + odd[j])/2 in s:
	# 			ans += 1
	print ans
