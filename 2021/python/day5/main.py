from aoc_utils import run_with_timer

data = [x.strip().split(' -> ') for x in open("input.txt").readlines()]
size = 1000


def mark_vents(include_diagonals):
	floor_map = [[0]*size for i in range(size)]
	for vent in data:
		start = [int(x) for x in vent[0].split(',')]
		end = [int(x) for x in vent[1].split(',')]

		if start[0] == end[0]:
			for x in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
				floor_map[start[0]][x] += 1
		elif start[1] == end[1]:
			for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
				floor_map[x][start[1]] += 1
		elif include_diagonals:
			xdir = -1 if start[0] > end[0] else 1
			ydir = -1 if start[1] > end[1] else 1
			for x in range(abs(start[0] - end[0]) + 1):
				floor_map[start[0] + (xdir*x)][start[1] + (ydir*x)] += 1
	return floor_map


def part_one():
	floor_map = mark_vents(False)
	return sum(1 for x in floor_map for y in x if y > 1)


def part_two():
	floor_map = mark_vents(True)
	return sum(1 for x in floor_map for y in x if y > 1)


if __name__ == '__main__':
	run_with_timer(part_one)  # 7468 -- took 57 ms
	run_with_timer(part_two)  # 22364 -- took 76 ms
