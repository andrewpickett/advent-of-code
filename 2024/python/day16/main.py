from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.utils import DIRS, DIR_COORDS, turn_around
from collections import deque, defaultdict


def get_data(filename):
	return Grid(file=filename)


def dijkstra(grid, start):
	q = deque([start])
	came_from = {}
	cost_so_far = defaultdict(tuple)
	came_from[start] = None
	cost_so_far[start[0]] = (0, DIRS[">"])

	while q:
		x = q.popleft()
		for dir in DIR_COORDS:
			next_node = grid.get_point(coords=tuple(sum(z) for z in zip(x[0].get_coord(), dir)))
			if next_node and next_node.get_value() != "#" and dir != turn_around(x[1]):
				new_cost = cost_so_far[x[0]][0] + (1 if dir == cost_so_far[x[0]][1] else 1001)
				if next_node not in cost_so_far or new_cost < cost_so_far[next_node][0]:
					cost_so_far[next_node] = (new_cost, dir)
					q.append((next_node, dir, new_cost))
					came_from[next_node] = x
	return came_from, cost_so_far


def reconstruct_path(came_from, start, end):
	current = end
	path = []
	if end not in came_from:
		return []
	while current != start and current not in path:
		path.append(current)
		current = came_from[current][0]
	path.append(start)
	path.reverse()
	return path


def part_one(d):
	start = [x for x in d.get_points() if x.get_value() == "S"][0]
	end = [x for x in d.get_points() if x.get_value() == "E"][0]
	path, cost = dijkstra(d, (start, DIRS[">"], 0), end)
	return cost[end][0]


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
