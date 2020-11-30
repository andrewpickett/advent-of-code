import random
from intcode_new import IntcodeOpMachine

data = [int(x) for x in open("input.txt").readline().split(',')]

DIR_ORDER = [1, 3, 2, 4]
DIRS = {
	'1': {'code': 1, 'opposite': 2, 'x': 0, 'y': -1},
	'2': {'code': 2, 'opposite': 1, 'x': 0, 'y': 1},
	'3': {'code': 3, 'opposite': 4, 'x': -1, 'y': 0},
	'4': {'code': 4, 'opposite': 3, 'x': 1, 'y': 0}
}


def determine_next_direction(grid, curr_pos):
	if grid[curr_pos[1]][curr_pos[0] + 1] == ' ':
		return 4
	if grid[curr_pos[1]][curr_pos[0] - 1] == ' ':
		return 3
	if grid[curr_pos[1] + 1][curr_pos[0]] == ' ':
		return 2
	if grid[curr_pos[1] - 1][curr_pos[0]] == ' ':
		return 1
	return random.randint(1, 4)


def get_next_position(curr_pos, in_val):
	return curr_pos[0] + DIRS[str(in_val)]['x'], curr_pos[1] + DIRS[str(in_val)]['y'],


def part_one():
	ship_map = [[' ' for i in range(50)] for i in range(50)]
	curr_pos = (len(ship_map) // 2, len(ship_map[0]) // 2,)
	ship_map[curr_pos[1]][curr_pos[0]] = 'D'
	# wall_positions = set()
	# visited_positions = set()
	draw_map(ship_map)

	machine = IntcodeOpMachine(list(data), input_vals=[1])
	exit_code = 0
	# hit_wall_count = 0
	while exit_code != 99:
		exit_code = machine.run(dynamic_input=True)
		if exit_code == 3:
			machine.add_input(determine_next_direction(ship_map, curr_pos))
		elif exit_code == 4:
			next_pos = get_next_position(curr_pos, machine.input_vals[-1])
			resp = machine.output[-1]
			if resp == 0:
				# wall_positions.add(next_pos)
				# if ship_map[next_pos[1]][next_pos[0]] == ' ':
				ship_map[next_pos[1]][next_pos[0]] = '#'
					# hit_wall_count += 1
			elif resp == 1:
				ship_map[next_pos[1]][next_pos[0]] = 'D'
				ship_map[curr_pos[1]][curr_pos[0]] = '.'
				curr_pos = next_pos + tuple()
				# visited_positions.add(curr_pos)
				# hit_wall_count = 0
			elif resp == 2:
				print("MADE IT {}".format(next_pos))
				# break
		draw_map(ship_map)
	draw_map(ship_map)
	return


def draw_map(ship_map):
	print(''.join('-' * len(ship_map)))
	for row in ship_map:
		print(''.join(row))
	print(''.join('-' * len(ship_map)))
	print()


def get_initial_position(grid):
	for i, row in enumerate(grid):
		if 'O' in row:
			return i, row.index('O')

def part_two():
	full_map = """######
#..###
#.#..#
#.O.##
######"""
	# full_map = """ #########################################
 # #...#.......#...#...#.........#...#.....#
 # #.###.#.###.#.#.#.#.#####.###.#.#.###.#.#
 # #.....#...#.#.#...#.#.....#.....#.....#.#
 # #.#######.#.#.#####.#.#.#########.#####.#
 # #.....#...#...#...#...#.#...#...#.#...#.#
 # #####.#.#######.###.#####.#.#.#.###.#.###
 # #...#.#.#...........#.....#...#.....#...#
 # #.#.###.#.###########.#################.#
 # #.#.....#.#.............#.....#.....#...#
 # #.#######.#.###########.###.###.###.#.###
 # #...#...#.#...#...#...#.....#...#...#...#
 # #.#.#.###.###.###.#.#.#####.#.###.#####.#
 # #.#.#.......#...#.#.#.#.....#.#...#.....#
 # #.#.###########.#.#.#.#######.#.###.###.#
 # #.#...#...#...#.#.#.#.#.....#.#.#.....#.#
 # #####.#.#.#.#.#.#.#.#.#.###.#.#.#.###.#.#
 # #...#...#...#.....#.#...#.#...#.#.#...#.#
 # #.#.###############.#####.#####.###.#####
 # #.#.............#...#...#.....#...#.#...#
 # #.#####.#######.#.#.###.#.###.###.#.#.#.#
 # #.#.....#.....#...#.#.#.#.#.#.#...#...#.#
 # #.#######.###.#####.#.#.#.#.#.#.#######.#
 # #.#.........#...#...#.#.....#.#.........#
 # #.#.###########.#.###.#######.#########.#
 # #...#...#.....#.#...#.......#.#...#.....#
 # #######.#.###.#.###.#######.#.#.#.#.#####
 # #.......#...#...#.....#.....#.#.#.#...#.#
 # #.###.#.###.#####.#####.#####.#.#.###.#.#
 # #.#...#...#.#.....#.....#...#...#.....#.#
 # #.#.#####.#.#######.#####.###.#########.#
 # #.#.#.....#.........#.........#.........#
 # #O#.#################.#########.#######.#
 # #.#.#...#...#.......#.....#.....#.....#.#
 # ###.#.#.#.#.#.#####.#####.#.###.###.#.#.#
 # #...#.#.#.#...#...#...#...#...#...#.#.#.#
 # #.###.#.#.#####.#.###.#.#########.#.#.#.#
 # #.....#.#.......#.#...#...........#.#...#
 # #.#####.#########.#.###############.#####
 # #.....#...........#.....................#
 # ######################################### """
	lines = full_map.split('\n')
	grid = [] * len(lines)
	for line in lines:
		grid.append([x for x in line.strip() if line.strip() != ''])
	print(grid)

	orig_count = get_unoxygenated_count(grid)

	initial_start = get_initial_position(grid)
	last_freed = [initial_start]
	count = 0
	while get_unoxygenated_count(grid) > 0:
		tmp = []
		for x in last_freed:
			if grid[x[0] + 1][x[1]] == '.':
				grid[x[0] + 1][x[1]] = 'O'
				tmp.append((x[0] + 1, x[1],))
			if grid[x[0] - 1][x[1]] == '.':
				grid[x[0] - 1][x[1]] = 'O'
				tmp.append((x[0] - 1, x[1],))
			if grid[x[0]][x[1] + 1] == '.':
				grid[x[0]][x[1] + 1] = 'O'
				tmp.append((x[0], x[1] + 1,))
			if grid[x[0]][x[1] - 1] == '.':
				grid[x[0]][x[1] - 1] = 'O'
				tmp.append((x[0], x[1] - 1,))
		draw_map(grid)
		count += 1
		last_freed = list(tmp)
	return count


def get_unoxygenated_count(grid):
	orig_count = 0
	for lines in grid:
		orig_count += lines.count('.')
	return orig_count


if __name__ == '__main__':
	print(part_one())  #
	# print(part_two())  #
