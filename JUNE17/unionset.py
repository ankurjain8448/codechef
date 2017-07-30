def check_union(a, b):
	for i in a:
		if i not in b:
			return False
	return True
 
for _ in xrange(input()):
	n, k = map(int, raw_input().strip().split())
	ans = 0
	lis = []
	full_set_count = 0
	lis_missing_number = []
 
	super_set = set(range(1,k+1))
 
	for i in xrange(n):
		temp = map(int, raw_input().strip().split())
		if temp[0] == k:
			ans = ans + n - full_set_count - 1
			full_set_count += 1
		else:
			lis.append(set(temp[1:]))
			lis_missing_number.append(super_set-lis[-1])
			# for i in temp[1:]:
			# 	lis_k[i]+= 1
 
	# now run O(n^2) for sets
	# l = len(lis)
	# for i in xrange(l):
	# 	for j in xrange(i, l):
	# 		if len(lis[i] | lis[j]) == k :
	# 			ans += 1
 
	for index, each_set in enumerate(lis):
		missing_element_set = lis_missing_number[index]
		l = len(missing_element_set)
		for next_set in lis[index:]:
			if len(next_set) >= l:
				if check_union(missing_element_set, next_set):
					ans += 1
	print ans