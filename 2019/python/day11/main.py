from intcode import IntcodeOpMachine

data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	grid = [['.' for i in range(100)] for i in range(100)]
	counter, grid = run_robot(IntcodeOpMachine(list(data)), grid)
	return counter


def part_two():
	grid = [['.' for i in range(100)] for i in range(100)]
	grid[0][0] = 'W'
	counter, grid = run_robot(IntcodeOpMachine(list(data)), grid)

	out_str = ''
	for row in grid:
		row_str = ''.join(row).replace('B', '.').replace('.', ' ')
		out_str += row_str + '\n' if row_str.strip() != '' else ''
	return out_str


def run_robot(machine, grid, curr_pos=(0, 0,)):
	exit_code = 0
	direction = 0
	counter = 0
	while exit_code != 99:
		machine.in_val = 1 if grid[curr_pos[0]][curr_pos[1]] == 'W' else 0
		machine.run()
		out_val1 = machine.output[-1]
		exit_code = machine.run()
		out_val2 = machine.output[-1]

		counter += 1 if grid[curr_pos[0]][curr_pos[1]] == '.'else 0
		grid[curr_pos[0]][curr_pos[1]] = 'B' if out_val1 == 0 else 'W'

		direction = (direction - 1 if out_val2 == 0 else direction + 1) % 4
		if direction % 2 == 0:
			curr_pos = (curr_pos[0] + 1 if direction == 2 else curr_pos[0] - 1, curr_pos[1],)
		else:
			curr_pos = (curr_pos[0], curr_pos[1] + 1 if direction == 1 else curr_pos[1] - 1,)
	return counter, grid


if __name__ == '__main__':
	print(part_one())  # 2088
	print(part_two())  # URCAFLCP
