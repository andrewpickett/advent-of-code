import random
from intcode import IntcodeOpMachine

data = [int(x) for x in open("input.txt").readline().split(',')]

DIRS = {
	'1': {'code': 1, 'opposite': 2, 'x': 0, 'y': -1},
	'2': {'code': 2, 'opposite': 1, 'x': 0, 'y': 1},
	'3': {'code': 3, 'opposite': 4, 'x': -1, 'y': 0},
	'4': {'code': 4, 'opposite': 3, 'x': 1, 'y': 0}
}


def determine_next_direction(ship_map, curr_pos, step_history):
	d = DIRS[str(step_history[-1])]
	if ship_map[curr_pos[1] + d['y']][curr_pos[0] + d['x']] == ' ':
		return d['code']
	d = DIRS[str(((step_history[-1] + 1) % 4) + 1)]
	if ship_map[curr_pos[1] + d['y']][curr_pos[0] + d['x']] == ' ':
		return d['code']

	# prev_dir = step_history.pop()
	# if prev_dir == 1:
	# 	return 2
	# if prev_dir == 2:
	# 	return 1
	# if prev_dir == 3:
	# 	return 4
	# if prev_dir == 4:
	# 	return 3
	#
	# if ship_map[curr_pos[1]][curr_pos[0] + 1] == '.':
	# 	return 4
	# if ship_map[curr_pos[1] + 1][curr_pos[0]] == '.':
	# 	return 2
	# if ship_map[curr_pos[1]][curr_pos[0] - 1] == '.':
	# 	return 3
	# if ship_map[curr_pos[1] - 1][curr_pos[0]] == '.':
	# 	return 1


def get_next_position(curr_pos, in_val):
	return curr_pos[0] + DIRS[str(in_val)]['x'], curr_pos[1] + DIRS[str(in_val)]['y'],


def part_one():
	ship_map = [[' ' for i in range(2000)] for i in range(2000)]
	curr_pos = (len(ship_map) // 2, len(ship_map[0]) // 2,)
	# curr_pos = (0, 0,)
	ship_map[curr_pos[1]][curr_pos[0]] = 'D'
	# draw_map(ship_map)
	# step_history = [1]

	machine = IntcodeOpMachine(list(data), in_val=1)
	exit_code = 0
	while exit_code != 99:
		machine.in_val = random.randint(1, 4)
		next_pos = get_next_position(curr_pos, machine.in_val)
		exit_code = machine.run(request_input=True)
		if exit_code == 3:
			continue
		elif exit_code == 4:
			resp = machine.output[-1]
			if resp == 0:
				ship_map[next_pos[1]][next_pos[0]] = '#'
				continue
			elif resp == 1:
				# if ship_map[next_pos[1]][next_pos[0]] == ' ':
				# 	step_history.append(machine.in_val)
				ship_map[next_pos[1]][next_pos[0]] = 'D'
				ship_map[curr_pos[1]][curr_pos[0]] = '.'
				curr_pos = (next_pos[0], next_pos[1],)
			elif resp == 2:
				print("MADE IT {}".format(next_pos))
				break
		# draw_map(ship_map)

	draw_map(ship_map)
	return


def draw_map(ship_map):
	print(''.join('-' * len(ship_map)))
	for row in ship_map:
		print(''.join(row))
	print(''.join('-' * len(ship_map)))
	print()


def part_two():
	return


if __name__ == '__main__':
	print(part_one())  #
	print(part_two())  #
