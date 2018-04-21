for _ in xrange(input()):
	n = input()
	fig_len = map(int, raw_input().strip().split())
	glove_len = map(int, raw_input().strip().split())
	front = True
	back = True
	for i in xrange(n):
		if fig_len[i] > glove_len[i]:
			front = False
		if fig_len[i] > glove_len[n-i-1]:
			back = False
	if front and back:
		print "both"
	elif front:
		print "front"
	elif back:
		print "back"
	else:
		print "none"
