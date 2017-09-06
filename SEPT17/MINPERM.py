def get_even(arr, n):
	mid = n/2
	counter = 1
	for i in xrange(mid): 
		arr.append(counter + 1)
		arr.append(counter)
		counter += 2

for _ in xrange(input()):
	n = input()
	arr = []
	if n%2:
		if n > 3:
			get_even(arr, n - 3)
		arr.append(n-1)
		arr.append(n)
		arr.append(n-2)
	else:
		get_even(arr, n)
	print " ".join(map(str, arr))
