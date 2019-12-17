from aoc_utils import run_with_timer

data = [x for x in open('input.txt').readline().strip()]

DIRS = {
	'^': {'x': 0, 'y': 1},
	'>': {'x': 1, 'y': 0},
	'<': {'x': -1, 'y': 0},
	'v': {'x': 0, 'y': -1}
}


def part_one():
	curr_pos = (0, 0,)
	visited_pos = {curr_pos}
	for direction in data:
		curr_pos = move(direction, curr_pos)
		visited_pos.add(curr_pos)
	return len(visited_pos)


def part_two():
	curr_pos = [(0, 0,), (0, 0,)]
	mover = 0
	visited_pos = {curr_pos[mover]}
	for direction in data:
		curr_pos[mover] = move(direction, curr_pos[mover])
		mover = (mover + 1) % 2
		visited_pos.add(curr_pos[mover])
	return len(visited_pos)


def move(direction, pos):
	return pos[0] + DIRS[direction]['x'], pos[1] + DIRS[direction]['y']


if __name__ == '__main__':
	run_with_timer(part_one)  # 2565
	run_with_timer(part_two)  # 2639
