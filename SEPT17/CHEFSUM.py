def get_min_index(arr, n):
	total_sum = sum(arr)
	prefix_sum = arr[0]
	suffix_sum = total_sum
	ans = prefix_sum + suffix_sum
	index = 1
	for i in xrange(1, n):
		prefix_sum += arr[i]
		suffix_sum -= arr[i-1]
		new_sum = prefix_sum + suffix_sum
		if new_sum < ans:
			ans = new_sum
			index = i + 1
	return index

for _ in xrange(input()):
	n = input()
	print get_min_index(map(int, raw_input().strip().split()), n)
