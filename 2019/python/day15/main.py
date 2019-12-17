import random
from intcode import IntcodeOpMachine

data = [int(x) for x in open("input.txt").readline().split(',')]

DIRS = {
	'1': {'code': 1, 'opposite': 2, 'x': 0, 'y': -1},
	'2': {'code': 2, 'opposite': 1, 'x': 0, 'y': 1},
	'3': {'code': 3, 'opposite': 4, 'x': -1, 'y': 0},
	'4': {'code': 4, 'opposite': 3, 'x': 1, 'y': 0}
}


def determine_next_direction(ship_map, curr_pos, last_dir, last_output):
	d = DIRS[str(last_dir)]
	if ship_map[curr_pos[1] + d['y']][curr_pos[0] + d['x']] == ' ':
		return d['code']
	d = DIRS[str(((last_dir + 1) % 4) + 1)]
	if ship_map[curr_pos[1] + d['y']][curr_pos[0] + d['x']] == ' ':
		return d['code']

	valid_moves = [1, 2, 3, 4]
	if last_output == 0:
		valid_moves.remove(last_dir)

	return valid_moves[random.randint(0, len(valid_moves) - 1)]


def get_next_position(curr_pos, in_val):
	return curr_pos[0] + DIRS[str(in_val)]['x'], curr_pos[1] + DIRS[str(in_val)]['y'],


def part_one():
	ship_map = [[' ' for i in range(3000)] for i in range(3000)]
	curr_pos = (len(ship_map) // 2, len(ship_map[0]) // 2,)
	ship_map[curr_pos[1]][curr_pos[0]] = 'D'
	# draw_map(ship_map)

	machine = IntcodeOpMachine(list(data), in_val=1)
	exit_code = 0
	last_dir = 1
	last_output = 1
	while exit_code != 99:
		machine.in_val = determine_next_direction(ship_map, curr_pos, last_dir, last_output)
		last_dir = machine.in_val
		next_pos = get_next_position(curr_pos, machine.in_val)
		exit_code = machine.run(request_input=True)
		if exit_code == 3:
			continue
		elif exit_code == 4:
			resp = machine.output[-1]
			last_output = resp
			if resp == 0:
				ship_map[next_pos[1]][next_pos[0]] = '#'
				continue
			elif resp == 1:
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
