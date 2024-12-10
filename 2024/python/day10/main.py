from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import tuple_add, DIR_COORDS, read_input_as_2d_int_array
from collections import deque


def get_data(filename):
	return read_input_as_2d_int_array(filename, 1)


def part_one(d):
	return sum(simple_bfs(d, y, x, True) for y in range(len(d)) for x in range(len(d[y])) if d[y][x] == 0)


def part_two(d):
	return sum(simple_bfs(d, y, x, False) for y in range(len(d)) for x in range(len(d[y])) if d[y][x] == 0)


def simple_bfs(d, y, x, p1):
	c = 0
	q = deque([(y, x, d[y][x])])
	visited = set()
	while q:
		curr = q.popleft()
		if curr[2] == 9:
			c += 1 if not p1 or p1 and curr not in visited else 0
			visited.add(curr)
		q.extend([(z[0], z[1], d[z[0]][z[1]]) for z in tuple_add(DIR_COORDS, (curr[0], curr[1])) if d[z[0]][z[1]] - curr[2] == 1])
	return c


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main("input.txt")
