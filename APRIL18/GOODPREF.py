# def wrap_word(s):
# 	arr = s[0]
# 	index = 0
# 	count = 1
# 	for i in xrange(1, len(s)):
# 		if s[i] == s[i-1]:
# 			count += 1
# 		else:
# 			arr = arr + str(count) + s[i]
# 			count = 1
# 	arr = arr + str(count)
# 	return arr

def get_ans(s, n):
	ans = 0
	# s = s*n
	arr = [ s for i in xrange(n)]
	s = "".join(arr)
	a_count = 0
	b_count=0
	for i in s:
		if i =='a':
			a_count += 1
		else:
			b_count += 1
		if a_count > b_count:
			ans += 1
	return ans

def get_ans_wrap_word(s, n):
	arr = [ s for i in xrange(n)]
	s = "".join(arr)
	a_count = 0
	b_count=0
	for i in xrange(0, len(s), 2):
		i = s[i]
		if i =='a':
			a_count += s[i+1]
			if a_count > b_count:
				ans = ans + b_count - a_count
		else:
			b_count += s[i+1]
		if a_count > b_count:
			ans += 1
	return ans



for _ in xrange(input()):
	s, n = raw_input().strip().split()
	n = int(n)
	if ' ' in s:
		if n > 1 :
			t =  s
			t = t.split()
			ans = 0
			for i in xrange(1, len(t)-1):
				ans += get_ans(t[i], 1)
			ans = ans*n

			new_t = t[-1] + t[0]
			t_ans = get_ans(new_t, 1)
			t_ans = t_ans*n
			ans = ans + t_ans
			print ans

		else:
			t =  s
			t = t.split()
			ans = 0
			for i in xrange(len(t)):
				ans += get_ans(t[i], 1)
			print ans
	else:
		if 'b' not in s:
			print len(s)*n
		elif 'a' not in s:
			print 0
		else:
			print get_ans(s, n)
