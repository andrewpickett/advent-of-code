from utils.timers import run_with_timer

DIRS = {
	'^': {'x': 0, 'y': 1},
	'>': {'x': 1, 'y': 0},
	'<': {'x': -1, 'y': 0},
	'v': {'x': 0, 'y': -1}
}


def get_data(filename):
	return [x for x in open(filename).readline().strip()]


def part_one(d):
	curr_pos = (0, 0,)
	visited_pos = {curr_pos}
	for direction in d:
		curr_pos = move(direction, curr_pos)
		visited_pos.add(curr_pos)
	return len(visited_pos)


def part_two(d):
	curr_pos = [(0, 0,), (0, 0,)]
	mover = 0
	visited_pos = {curr_pos[mover]}
	for direction in d:
		curr_pos[mover] = move(direction, curr_pos[mover])
		visited_pos.add(curr_pos[mover])
		mover = (mover + 1) % 2
	return len(visited_pos)


def move(direction, pos):
	return pos[0] + DIRS[direction]['x'], pos[1] + DIRS[direction]['y']


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
