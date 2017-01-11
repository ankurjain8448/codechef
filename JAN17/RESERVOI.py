for cas in xrange(input()):
	n, m = map(int, raw_input().strip().split())
	arr = []
	flag = True
	for r in xrange(n):
		row = []
		for i in raw_input().strip():
			row.append(i)
		arr.append(row)

	rows = n
	columns = m
	
	for r in xrange(rows-1,-1,-1):
		for c in xrange(columns):
			if arr[r][c] == 'B':
				if r+1 < rows and arr[r+1][c] != 'B':
					flag = False
					break
			elif arr[r][c] == 'A':
				if (r-1 > -1 and arr[r-1][c] != 'A') or  (c-1 > -1 and arr[r][c-1] == 'W') or (c+1< columns and arr[r][c+1] == 'W'):
					flag = False
					break
			elif arr[r][c] == 'W':
				if c == 0 or c == columns -1 or r == rows-1 or (r-1 > -1 and arr[r-1][c] == 'B') or (r+1< rows and arr[r+1][c] == 'A') or (c-1 > -1 and arr[r][c-1] == 'A') or (c+1< columns and arr[r][c+1] == 'A'):
					flag = False
					break
		if not flag:
			break
	print 'yes' if flag else 'no'
	