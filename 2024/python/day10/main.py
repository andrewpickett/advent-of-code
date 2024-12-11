from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import neighbors
from utils.input import read_input_as_2d_int_grid
from collections import deque


def get_data(filename):
	return read_input_as_2d_int_grid(filename, 1)


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
		q.extend(neighbors(d, curr, condition=lambda a, b, n: d[n[0]][n[1]] - b[2] == 1))
	return c


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
