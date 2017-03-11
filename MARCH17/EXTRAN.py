for _ in xrange(input()):
	n = input()
	sq = map(int, raw_input().strip().split())
	MIN = min(sq)
	if MIN + 1 not in sq:
		print MIN
		continue
	MAX = max(sq)
	if MAX - 1 not in sq:
		print MAX
		continue
	s = set()
	for each in sq:
		if each not in s:
			s.add(each)
		else:
			print each
			break