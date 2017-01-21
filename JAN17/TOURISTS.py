n, e = map(int, raw_input().strip().split())
direct = {}
reverse= {}
flag = True
output = []
sequence = []*e
if n > e:
	for i in xrange(e):
		a = raw_input()
	a = None
	flag = False
else:
	for i in xrange(e):
		a, b = raw_input().strip().split()
		sequence.append(a)
		if a in direct:
			direct[a].append(b)
		else:
			direct[a] = [b]

		if b in reverse:
			reverse[b].append(a)
		else:
			reverse[b] = [a]
	print direct
	print reverse
	for i in xrange(1,n+1):
		city = str(i)
		if city not in direct:
			if city not in reverse:
				flag = False
				break
			cities = reverse[city]
			for each_city in cities:
				if len(direct[each_city]) > 1:
					direct[each_city].remove(city)
					direct[city] = [each_city]
					break
			else:
				flag = False
				break
	# print "======"
	# print direct
	# print "======"
	# create proper output
	# for _ in create_output:
	# 	pass

			
if flag:
	print "YES"
	for k,v in direct.iteritems():
		for each_v in v:
			print "%s %s" % (k, each_v)
	# for i in sequence:
	# 	print "%s %s" % (i, direct[i])
else:
	print "NO"