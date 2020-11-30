from intcode_new import IntcodeOpMachine

data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	machine = IntcodeOpMachine(list(data), input_vals=[1])
	machine.run_until_halt()
	return machine.output[-1]


def part_two():
	machine = IntcodeOpMachine(list(data), input_vals=[2])
	machine.run_until_halt()
	return machine.output[-1]


if __name__ == '__main__':
	print(part_one())  # 3460311188
	print(part_two())  # 42202
