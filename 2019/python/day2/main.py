from intcode import IntcodeOpMachine

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


def part_one_with_finished_machine():
	machine = IntcodeOpMachine(create_data_list(12, 2))
	machine.run_until_halt()
	return machine.instructions[0]


def part_two_with_finished_machine():
	for noun in range(99):
		for verb in range(99):
			machine = IntcodeOpMachine(create_data_list(noun, verb))
			machine.run_until_halt()
			if machine.instructions[0] == 19690720:
				return noun * 100 + verb


if __name__ == '__main__':
	print("Solution without the final machine.")
	print(part_one())  # 3716293
	print(part_two())  # 6429
	print()
	print("Solution using the final machine.")
	print(part_one_with_finished_machine())  # 3716293
	print(part_two_with_finished_machine())  # 6429
