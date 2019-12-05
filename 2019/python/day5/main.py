data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	calculate_output(list(data), 1)


def part_two():
	calculate_output(list(data), 5)


def calculate_output(d, input_val):
	i = 0
	while i < len(d):
		op = d[i]
		first_param_mode = 0
		second_param_mode = 0
		if op == 99:
			return d[0]
		elif op > 99:
			str_op = str(op).zfill(5)
			op = int(str_op[3]) * 10 + int(str_op[4])
			first_param_mode = int(str_op[2])
			second_param_mode = int(str_op[1])
		i += perform_operation(d, i, op, first_param_mode, second_param_mode, input_val)


def perform_operation(d, i, op, first_param_mode, second_param_mode, input_val):
	first_param_idx = d[i+1] if first_param_mode == 0 else i+1
	second_param_idx = d[i+2] if second_param_mode == 0 else i+2

	if op == 1:
		return op_addition(d, first_param_idx, second_param_idx, d[i+3])
	elif op == 2:
		return op_multiplication(d, first_param_idx, second_param_idx, d[i+3])
	elif op == 3:
		return op_input(d, d[i+1], input_val)
	elif op == 4:
		return op_output(d, first_param_idx)
	elif op == 5:
		return op_jump_if_true(d, i, first_param_idx, second_param_idx)
	elif op == 6:
		return op_jump_if_false(d, i, first_param_idx, second_param_idx)
	elif op == 7:
		return op_less_than(d, first_param_idx, second_param_idx, d[i+3])
	elif op == 8:
		return op_equals(d, first_param_idx, second_param_idx, d[i+3])


def op_addition(d, in1_idx, in2_idx, out_idx):
	d[out_idx] = d[in1_idx] + d[in2_idx]
	return 4


def op_multiplication(d, in1_idx, in2_idx, out_idx):
	d[out_idx] = d[in1_idx] * d[in2_idx]
	return 4


def op_input(d, idx, val):
	d[idx] = val
	return 2


def op_output(d, idx):
	print(d[idx])
	return 2


def op_jump_if_true(d, idx, test_idx, jump_idx):
	return d[jump_idx] - idx if d[test_idx] != 0 else 3


def op_jump_if_false(d, idx, test_idx, jump_idx):
	return d[jump_idx] - idx if d[test_idx] == 0 else 3


def op_less_than(d, test1_idx, test2_idx, out_idx):
	d[out_idx] = 1 if d[test1_idx] < d[test2_idx] else 0
	return 4


def op_equals(d, test1_idx, test2_idx, out_idx):
	d[out_idx] = 1 if d[test1_idx] == d[test2_idx] else 0
	return 4


if __name__ == '__main__':
	part_one()  # 13787043
	part_two()  # 3892695
