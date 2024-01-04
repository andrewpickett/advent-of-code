from utils.timers import run_with_timer, get_data_with_timer

DIRS = {
	'^': (0, 1),
	'>': (1, 0),
	'<': (-1, 0),
	'v': (0, -1)
}


def get_data(filename):
	return open(filename).readline().strip()


def run_santas(d, santa_pos):
	mover = 0
	visited_pos = {santa_pos[mover]}
	for direction in d:
		santa_pos[mover] = move(direction, santa_pos[mover])
		visited_pos.add(santa_pos[mover])
		mover = (mover + 1) % len(santa_pos)
	return len(visited_pos)


def part_one(d):
	return run_santas(d, [(0, 0)])


def part_two(d):
	return run_santas(d, [(0, 0), (0, 0)])


def move(direction, pos):
	return pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1]


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
