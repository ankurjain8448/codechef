mod = 10**9 + 7
 
def get_sum(P, Q, R, sum_p, sum_r, yi):
	xi = len(P) - 1
	zi = len(R) - 1
	while xi > -1:
		if Q[yi] >= P[xi]:
			break
		xi -= 1
		sum_p = (sum_p - P.pop() + mod)%mod
	sum_p = sum_p % mod
	
	while zi > -1:
		if Q[yi] >= R[zi]:
			break
		zi -= 1
		sum_r = (sum_r - R.pop() + mod)%mod
	sum_r = sum_r % mod
	return sum_p, sum_r
 
def calculate(sum_p, sum_r, P, R, y):
	return ( ( (sum_p + ( y*( len(P) )%mod ) ) %mod ) * ( (sum_r + (y*len(R) )%mod) %mod ) ) %mod
 
for _ in xrange(input()):
	p, q, r = map(int, raw_input().strip().split())
	P = map(int, raw_input().strip().split())
	Q = map(int, raw_input().strip().split())
	R = map(int, raw_input().strip().split())
 
	P.sort()
	Q.sort()
	R.sort()
 
	sum_p = 0
	for i in P:
		sum_p = (sum_p + i)%mod
 
	sum_r = 0
	for i in R:
		sum_r = (sum_r + i)%mod
 
 
	yi = q - 1
	ans = 0
 
	while yi > -1:
		sum_p, sum_r = get_sum(P, Q, R, sum_p, sum_r, yi)
		if len(P) and len(R):
			ans  += calculate(sum_p, sum_r, P, R, Q[yi])
			ans = ans%mod
		else:
			break
		yi -= 1
	print ans