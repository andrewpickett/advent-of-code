from utils.timers import run_with_timer
from heapq import heappop, heappush


def get_data(filename):
	return [[int(y) for y in x.strip()] for x in open(filename).readlines()]


dirs = {
	0: (0, 1),
	1: (1, 0),
	2: (0, -1),
	3: (-1, 0)
}


def dijkstra(d, min_dir, max_dir):
	q = [(0, 0, 0, -1)]
	visited = set()
	dists= {}
	while len(q) > 0:
		u = heappop(q)
		if u[1] == len(d)-1 and u[2] == len(d[0])-1:
			return u[0]

		if (u[1], u[2], u[3]) not in visited:
			visited.add((u[1], u[2], u[3]))
			for direction in range(len(dirs)):
				inc = 0
				if direction != u[3] and (direction+2) % len(dirs) != u[3]:
					for dist in range(1, max_dir+1):
						new_x = u[1] + dirs[direction][0]*dist
						new_y = u[2] + dirs[direction][1]*dist
						if new_x in range(len(d)) and new_y in range(len(d[0])):
							inc += d[new_x][new_y]
							if dist >= min_dir:
								nc = u[0] + inc
								if dists.get((new_x, new_y, direction), 1e100) > nc:
									dists[(new_x, new_y, direction)] = nc
									heappush(q, (nc, new_x, new_y, direction))


def part_one(d):
	return dijkstra(d, 1, 3)


def part_two(d):
	return dijkstra(d, 4, 10)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
