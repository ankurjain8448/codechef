import sys
n = input()
c = map(int, raw_input().strip().split())
t = raw_input().strip().split()

x = sys.maxint
y = sys.maxint
z = sys.maxint
for i in xrange(n):
	if t[i] == '1':
		x = min(x, c[i])
	elif t[i] == '2':
		y = min(y, c[i])
	else:
		z = min(z, c[i])
print min(z, x+y)