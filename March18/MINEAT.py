import sys
def check(arr, speed, hours):
	for i in arr:
		q = i / speed
		q = q + 1 if q * speed < i else q
		hours -= q
		if hours < 0:
			return False
	return True

def get_optimum_speed(arr, hours):
	start = 1
	end = max(arr)
	ans = sys.maxint
	while start <= end:
		mid = (start + end) / 2
		possible = check(arr, mid, hours)
		if possible:
			ans = min(ans, mid)
			end = mid - 1
		else:
			start = mid + 1
	return ans

for _ in xrange(input()):
	n, h = map(int, raw_input().strip().split())
	arr = map(int, raw_input().strip().split())
	print get_optimum_speed(arr, h)
