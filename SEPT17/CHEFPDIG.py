for _ in xrange(input()):
	d = {}
	for i in raw_input().strip():
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	ans = []
	
	if '6' in d:
		d['6'] -= 1
		for i in xrange(5, 10):
			if str(i) in d and d[str(i)] > 0:
				c = chr(60+i)
				ans.append(c)
		d['6'] += 1

	for i in xrange(7, 9):
		t = str(i)
		if t in d:
			d[t] -= 1
			for k , v in d.iteritems():
				if v > 0 :
					c = chr(i*10+int(k))
					ans.append(c)
			d[t] += 1
	if '9' in d and '0' in d:
		ans.append('Z')
	ans.sort()
	if not ans:
		ans.append('\n')
	print "".join(ans)
