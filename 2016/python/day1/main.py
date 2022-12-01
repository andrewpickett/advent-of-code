from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readline().split(",")]

orients = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_points_between(start, end):
	pts = {end}
	if start[0] != end[0]:
		s = end[0] if start[0] > end[0] else start[0]
		e = start[0] if start[0] > end[0] else end[0]
		for i in range(s, e):
			pts.add((i, start[1]))
	else:
		s = end[1] if start[1] > end[1] else start[1]
		e = start[1] if start[1] > end[1] else end[1]
		for i in range(s, e):
			pts.add((start[0], i))
	return pts


def part_one():
	curr_or = 0
	curr_pos = (0, 0)

	for x in data:
		curr_or = ((curr_or + 1) if x[0] == 'R' else (curr_or - 1)) % 4
		curr_pos = (curr_pos[0] + (orients[curr_or][0] * int(x[1:])), curr_pos[1] + (orients[curr_or][1] * int(x[1:])))
	return abs(curr_pos[0]) + abs(curr_pos[1])


def part_two():
	visited = list((0, 0))
	curr_or = 0
	curr_pos = (0, 0)

	for x in data:
		curr_or = ((curr_or + 1) if x[0] == 'R' else (curr_or - 1)) % 4
		next_pos = (curr_pos[0] + (orients[curr_or][0] * int(x[1:])), curr_pos[1] + (orients[curr_or][1] * int(x[1:])))
		line = get_points_between(curr_pos, next_pos)
		for y in line:
			if y in visited and y != curr_pos:
				return abs(y[0]) + abs(y[1])
			visited.append(y)
		curr_pos = next_pos
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 239 -- took 0 ms
	run_with_timer(part_two)  # 141 -- took 6 ms
