for cas in xrange(input()):
	c, d , l = map(int, raw_input().strip().split())
	if l%4 != 0:
		print 'no'
	else:
		add = 0
		if d*2 < c :
			add = c - d*2
		if l < (d + add)*4  or l > (c+d)*4:
			print "no"
		else:
			print "yes"
