from intcode import IntcodeOpMachine

data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	machine = IntcodeOpMachine(list(data))
	machine.run_until_halt()
	return machine.output[2::3].count(2)


def compare_vals(a, b):
	return 0 if a == b else ((a - b) // abs(a - b))


def part_two():
	grid = [[' ' for i in range(45)] for i in range(24)]
	i = 0
	score = 0
	list_data = list(data)
	list_data[0] = 2
	machine = IntcodeOpMachine(list_data)
	ball_pos = 0
	paddle_pos = 0
	exit_code = 0
	while True:
		machine.in_val = compare_vals(ball_pos, paddle_pos)
		exit_code = machine.run(request_input=True)
		if exit_code == 3:
			continue
		elif exit_code == 4:
			i = (i + 1) % 3
			if i == 0:
				if machine.output[-3] == -1 and machine.output[-2] == 0:
					score = machine.output[-1]
				else:
					tile_type = machine.output[-1]
					tile_disp = ' '
					if tile_type == 1:
						tile_disp = 'X'
					elif tile_type == 2:
						tile_disp = '-'
					elif tile_type == 3:
						tile_disp = '_'
						paddle_pos = machine.output[-3]
					elif tile_type == 4:
						tile_disp = 'o'
						ball_pos = machine.output[-3]
					grid[machine.output[-2]][machine.output[-3]] = tile_disp
				machine.output.clear()
		elif exit_code == 99:
			break
	return score


if __name__ == '__main__':
	print(part_one())  # 462
	print(part_two())  # 23981
