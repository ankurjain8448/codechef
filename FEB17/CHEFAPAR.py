for _ in xrange(input()):
	n = input()
	arr = map(int, raw_input().strip().split())
	ans = (n - sum(arr))*1000
	zero_index = -1
	for i in xrange(n):
		if arr[i] == 0 :
			zero_index = i
			break
			
	if zero_index != -1:
		ans += (n-zero_index)*100
	
	print ans