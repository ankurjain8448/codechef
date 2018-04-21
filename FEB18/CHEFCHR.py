for _ in xrange(input()):
	s = raw_input()
	compare = sorted('chef')
	count = 0
	l = len(s)
	for i in xrange(l-3):
		val = s[i:i+4]
		if sorted(val) == compare:
			count += 1
	if count:
		print "lovely ", count
	else:
		print "normal"
