def calc():
	n , m = map(int, raw_input().strip().split())
	expected_min_salary = map(int, raw_input().strip().split())

	company_profile = [map(int, raw_input().strip().split()) for i in xrange(m)]
	company_data_for_comparision = [ i[1] for i in company_profile]

	who_got_offer = [ [int(j) for j in raw_input().strip()] for i in xrange(n)]
	placed_candidates = 0
	total_CTC = 0
	zero_placement_company_count = 0

	for each_candidate in xrange(n):
		expected_ctc = expected_min_salary[each_candidate] 
		max_ctc_company = -1
		for company in xrange(m):
			if who_got_offer[each_candidate][company]:
				if company_profile[company][1] and company_profile[company][0] >= expected_ctc:
					if max_ctc_company != -1:
						if company_profile[company][0] >= company_profile[max_ctc_company][0]:
							max_ctc_company = company
					else:
						max_ctc_company = company

		if max_ctc_company != -1:
			company_profile[max_ctc_company][1] -= 1
			placed_candidates += 1
			total_CTC += company_profile[max_ctc_company][0]
	print placed_candidates, total_CTC , sum(1 for i in xrange(m) if company_data_for_comparision[i] == company_profile[i][1])

for _ in xrange(input()):
	calc()
