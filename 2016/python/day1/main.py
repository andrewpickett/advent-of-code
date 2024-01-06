from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [(x[0], int(x[1:])) for x in open(filename).readline().split(", ")]


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_points_between(start, end):
	pts = {end}.union({(i, start[1]) for i in range(start[0], end[0], -1 if start[0] > end[0] else 1)})
	return pts.union({(start[0], i) for i in range(start[1], end[1], -1 if start[1] > end[1] else 1)})


def part_one(d):
	curr_or = 0
	curr_pos = (0, 0)

	for x in d:
		curr_or = ((curr_or + 1) if x[0] == 'R' else (curr_or - 1)) % 4
		curr_pos = (curr_pos[0] + (DIRS[curr_or][0] * x[1]), curr_pos[1] + (DIRS[curr_or][1] * x[1]))
	return abs(curr_pos[0]) + abs(curr_pos[1])


def part_two(d):
	curr_or = 0
	curr_pos = (0, 0)
	visited = [curr_pos]

	for x in d:
		curr_or = ((curr_or + 1) if x[0] == 'R' else (curr_or - 1)) % 4
		next_pos = (curr_pos[0] + (DIRS[curr_or][0] * x[1]), curr_pos[1] + (DIRS[curr_or][1] * x[1]))
		line = get_points_between(curr_pos, next_pos)
		for y in line:
			if y in visited and y != curr_pos:
				return abs(y[0]) + abs(y[1])
			visited.append(y)
		curr_pos = next_pos
	return None


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
