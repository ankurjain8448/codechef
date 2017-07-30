for _ in xrange(input()):
	n = input()
	arr = map(int, raw_input().strip().split())
 
	negative = [i for i in arr if i < 0]
	negative.sort(reverse=True)
	negative_sum = sum(negative)
	negative_count = len(negative)
	
	positive = sum(arr) - negative_sum
	positive_count = n - negative_count
 
	ans = positive*positive_count + negative_sum
	temp = 0
	while temp < negative_count:
		positive = positive + negative[temp]
		negative_sum -= negative[temp]
		positive_count += 1
		ansss = positive*positive_count + negative_sum
		if ansss > ans:
			ans = ansss
		else:
			break
		temp += 1
	print ans
