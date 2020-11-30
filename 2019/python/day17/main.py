from aoc_utils import run_with_timer
from intcode_new import IntcodeOpMachine

data = [int(x) for x in open('input.txt').readline().split(',')]


def part_one():
	machine = IntcodeOpMachine(list(data), input_vals=[1])
	machine.run_until_halt()
	lines = ''.join((chr(i) for i in machine.output)).strip().split('\n')

	intersection_points = set()
	for i, line in enumerate(lines):
		if 0 < i < len(lines) - 2:
			for j, char in enumerate(line):
				if 0 < j < len(line) - 1:
					if char == '#':
						if lines[i][j+1] == '#' and lines[i][j-1] == '#' and lines[i+1][j] == '#' and lines[i-1][j] == '#':
							intersection_points.add((i, j,))

	return sum(x*y for x, y in intersection_points)


def mov_func_main():
	return [ord(x) for x in 'A,B,A,B,C,C,B,A,C,A\n']


def mov_func_a():
	return [ord(x) for x in 'L,10,R,8,R,6,R,10\n']


def mov_func_b():
	return [ord(x) for x in 'L,12,R,8,L,12\n']


def mov_func_c():
	return [ord(x) for x in 'L,10,R,8,R,8\n']


def part_two():
	continuous_feed = 'n'
	inputs = []
	inputs.extend(mov_func_main())
	inputs.extend(mov_func_a())
	inputs.extend(mov_func_b())
	inputs.extend(mov_func_c())
	inputs.extend([ord(continuous_feed), ord('\n')])

	instructions = list(data)
	instructions[0] = 2
	machine = IntcodeOpMachine(instructions, input_vals=inputs)
	machine.run_until_halt()
	return machine.output[-1]


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #
