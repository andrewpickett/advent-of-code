from aoc_utils import run_with_timer

data = [(x.strip()[0:1], int(x.strip()[1:])) for x in open("input.txt").readlines()]


def rotate_dir(point, dir, rotation):
	rotations = rotation // 90
	for i in range(rotations):
		if dir == 'R':
			point = (-1 * point[1], point[0])
		elif dir == 'L':
			point = (point[1], -1 * point[0])
	return point


def part_one():
	curr_dir = (1, 0)
	curr_pos = (0, 0)
	for x in data:
		if x[0] == 'F':
			curr_pos = (curr_pos[0]+(curr_dir[0]*x[1]), curr_pos[1]+(curr_dir[1]*x[1]))
		elif x[0] in ['R', 'L']:
			curr_dir = rotate_dir(curr_dir, x[0], x[1])
		elif x[0] == 'N':
			curr_pos = (curr_pos[0], curr_pos[1]-x[1])
		elif x[0] == 'S':
			curr_pos = (curr_pos[0], curr_pos[1]+x[1])
		elif x[0] == 'E':
			curr_pos = (curr_pos[0]+x[1], curr_pos[1])
		elif x[0] == 'W':
			curr_pos = (curr_pos[0]-x[1], curr_pos[1])
	return abs(curr_pos[0]) + abs(curr_pos[1])


def part_two():
	curr_dir = (10, -1)
	curr_pos = (0, 0)
	for x in data:
		if x[0] == 'F':
			curr_pos = (curr_pos[0]+(curr_dir[0]*x[1]), curr_pos[1]+(curr_dir[1]*x[1]))
		elif x[0] in ['R', 'L']:
			curr_dir = rotate_dir(curr_dir, x[0], x[1])
		elif x[0] == 'N':
			curr_dir = (curr_dir[0], curr_dir[1]-x[1])
		elif x[0] == 'S':
			curr_dir = (curr_dir[0], curr_dir[1]+x[1])
		elif x[0] == 'E':
			curr_dir = (curr_dir[0]+x[1], curr_dir[1])
		elif x[0] == 'W':
			curr_dir = (curr_dir[0]-x[1], curr_dir[1])
	return abs(curr_pos[0]) + abs(curr_pos[1])


if __name__ == '__main__':
	run_with_timer(part_one)  # 1838 -- took 0 ms
	run_with_timer(part_two)  # 89936 -- took 0 ms
