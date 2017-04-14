for cas in xrange(input()):
	count = 0
	n = input()
	for i in xrange(n):
		mat = map(int, raw_input().strip().split())
		count = count + sum(mat)
	k = 0
	temp = n 
	count -= temp
	while count > 0 :
		temp -= 1
		count -= temp*2
		k += 1
	print k	