for cas in xrange(input()):
	n = input()
	population_per_city = map(int, raw_input().strip().split())
	sorted_population = sorted(population_per_city)
	population_to_city_map = {}
	matrix = []
	for city, population in enumerate(population_per_city):
		population_to_city_map[str(population)] = city + 1
		matrix.append([population])
	for i in xrange(n-1):
		u, v = map(int, raw_input().strip().split())
		u -= 1
		v -= 1
		matrix[u].append(population_per_city[v])
		matrix[v].append(population_per_city[u])
	for i in xrange(n):
		d = {i for i in matrix[i]}
		for i in xrange(n):
			val = sorted_population[n-1-i]
			if val not in d:
				print population_to_city_map[str(val)]
				break
		else:
			print 0