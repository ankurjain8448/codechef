for _ in xrange(int(raw_input().strip())):
	n = input()
	arr = map(int,raw_input().strip().split())
	arr.sort()
	b = arr[n:]
	median = b[(n+1)/2 - 1]
	temp = n
	for i in xrange(0, n , 2):
		arr[i] , arr[temp] = arr[temp], arr[i]
		temp += 2
	for i in xrange(2*n):
		arr[i] = str(arr[i])
	print median
	print " ".join(arr)  