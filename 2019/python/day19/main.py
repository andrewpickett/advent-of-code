from aoc_utils import run_with_timer
from intcode_new import IntcodeOpMachine

data = [int(x) for x in open('input.txt').readline().strip().split(',')]


def part_one():
	w = 50
	h = 50
	disp = [['.'] * w for i in range(h)]
	total_count = 0
	for y in range(h):
		for x in range(w):
			machine = IntcodeOpMachine(list(data), input_vals=[x, y])
			machine.run_until_halt()
			if machine.output[-1] == 1:
				disp[y][x] = '#'
				total_count += 1

	for row in disp:
		print(''.join(row))
	return total_count


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #
