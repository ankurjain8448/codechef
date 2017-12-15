n ,h = map(int, raw_input().strip().split())
stack = map(int, raw_input().strip().split())
op = map(int, raw_input().strip().split())
head_index = 0
is_holding_box = False

# 1 : Move left
# 2 : Move right
# 3 : Pick up box
# 4 : Drop box
# 0 : Quit

for each_op in op:
	if each_op == 0:
		break
	elif each_op == 1:
		if head_index > 0:
			head_index -= 1
	elif each_op == 2:
		if head_index < n-1:
			head_index += 1
	elif each_op == 3:
		if not is_holding_box:
			if stack[head_index]:
				stack[head_index] -= 1
				is_holding_box = True
	else:
		# each_op == 4
		if is_holding_box :
			if stack[head_index] < h:
				stack[head_index] += 1
				is_holding_box = False
print " ".join(map(str, stack))

