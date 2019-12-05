data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	calculate_output(list(data), 1)


def part_two():
	calculate_output(list(data), 5)


def calculate_output(d, input_val):
	i = 0
	while i < len(d):
		op = d[i]
		str_op = str(op).zfill(5)
		first_param_idx = d[i+1] if (i+1 < len(d)) and (0 if op <= 99 else int(str_op[2])) == 0 else i+1
		second_param_idx = d[i+2] if (i+2 < len(d)) and (0 if op <= 99 else int(str_op[1])) == 0 else i+2
		if op == 99:
			return d[0]
		elif op > 99:
			op = int(str_op[3]) * 10 + int(str_op[4])
		i += perform_operation(d, i, op, first_param_idx, second_param_idx, input_val)


def perform_operation(d, i, op, first_param_idx, second_param_idx, input_val):
	if op == 1:
		d[d[i+3]] = d[first_param_idx] + d[second_param_idx]
		return 4
	elif op == 2:
		d[d[i+3]] = d[first_param_idx] * d[second_param_idx]
		return 4
	elif op == 3:
		d[d[i+1]] = input_val
		return 2
	elif op == 4:
		print(d[first_param_idx])
		return 2
	elif op == 5:
		return d[second_param_idx] - i if d[first_param_idx] != 0 else 3
	elif op == 6:
		return d[second_param_idx] - i if d[first_param_idx] == 0 else 3
	elif op == 7:
		d[d[i+3]] = 1 if d[first_param_idx] < d[second_param_idx] else 0
		return 4
	elif op == 8:
		d[d[i+3]] = 1 if d[first_param_idx] == d[second_param_idx] else 0
		return 4


if __name__ == '__main__':
	part_one()  # 13787043
	part_two()  # 3892695
