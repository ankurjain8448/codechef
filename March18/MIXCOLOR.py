for _ in range(input()):
	print input() - len({ i for i in raw_input().strip().split() })
