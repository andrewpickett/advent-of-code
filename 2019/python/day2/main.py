data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	return calculate_output(create_data_list(12, 2))


def part_two():
	for noun in range(99):
		for verb in range(99):
			if calculate_output(create_data_list(noun, verb)) == 19690720:
				return noun * 100 + verb


def create_data_list(noun, verb):
	op_data = list(data)
	op_data[1] = noun
	op_data[2] = verb
	return op_data


def calculate_output(d):
	for i in range(0, len(d), 4):
		op, in1, in2, out = d[i], d[i+1], d[i+2], d[i+3]
		if op == 99:
			return d[0]
		d[out] = d[in1] + d[in2] if op == 1 else d[in1] * d[in2]


if __name__ == '__main__':
	print(part_one())  # 3716293
	print(part_two())  # 6429
