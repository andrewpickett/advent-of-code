from itertools import permutations, cycle

data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	phases = [''.join(p) for p in permutations('01234')]
	max_input = 0
	for series in phases:
		next_input = 0
		for phase in series:
			next_input = calculate_output(list(data), int(phase), next_input)

		if next_input > max_input:
			max_input = next_input
	return max_input


def part_two():
	phases = [''.join(p) for p in permutations('56789')]
	max_input = 0
	# for series in phases:
	next_input = 0
	data_map = {}
	# for phase in cycle(series):
	for phase in cycle(['5', '6', '7', '8', '9']):
		if phase not in data_map:
			data_map[phase] = list(data)
			next_input, exit_code = calculate_output(data_map[phase], int(phase), next_input)
		else:
			next_input, exit_code = calculate_output(data_map[phase], -1, next_input)

		if next_input > max_input:
			max_input = next_input
	return max_input


def calculate_output(d, phase_setting, input_val):
	i = 0
	had_phase = False
	ret_val = d[0]
	last_op = 0
	while i < len(d):
		op = d[i]
		str_op = str(op).zfill(5)
		first_param_idx = d[i+1] if (i+1 < len(d)) and (0 if op <= 99 else int(str_op[2])) == 0 else i+1
		second_param_idx = d[i+2] if (i+2 < len(d)) and (0 if op <= 99 else int(str_op[1])) == 0 else i+2
		if op == 99:
			if last_op == 4:
				return ret_val, 4
			return ret_val, 99
		elif op > 99:
			op = int(str_op[3]) * 10 + int(str_op[4])

		in_val = phase_setting if not had_phase and phase_setting > 0 else input_val
		i += perform_operation(d, i, op, first_param_idx, second_param_idx, in_val)

		if op == 3:
			had_phase = True
		elif op == 4:
			ret_val = d[first_param_idx]
			# return d[first_param_idx], 4
		last_op = op


def perform_operation(d, i, op, first_param_idx, second_param_idx, input_val):
	if op == 1:  # Addition
		d[d[i+3]] = d[first_param_idx] + d[second_param_idx]
		return 4
	elif op == 2:  # Multiplication
		d[d[i+3]] = d[first_param_idx] * d[second_param_idx]
		return 4
	elif op == 3:  # Input
		# if not ignore_input:
		d[d[i+1]] = input_val
		return 2
	elif op == 4:  # Output
		# print(d[first_param_idx])
		return 2
	elif op == 5:  # Jump if true
		# print("d[second]={} i={} diff = {} ?? {}".format(d[second_param_idx], i, d[second_param_idx] - i, d[second_param_idx] != 0))
		return d[second_param_idx] - i if d[first_param_idx] != 0 else 3
	elif op == 6:  # Jump if false
		return d[second_param_idx] - i if d[first_param_idx] == 0 else 3
	elif op == 7:  # test if less than
		d[d[i+3]] = 1 if d[first_param_idx] < d[second_param_idx] else 0
		return 4
	elif op == 8:  # test if equals
		d[d[i+3]] = 1 if d[first_param_idx] == d[second_param_idx] else 0
		return 4
	# else:
		# print(op)


if __name__ == '__main__':
	# print("Part one: {}".format(part_one()))  # 38834
	print("Part two: {}".format(part_two()))  #
