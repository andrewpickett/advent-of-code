from aoc_utils import run_with_timer, Grid

data = [[y for y in x.strip()] for x in open("input.txt").readlines()]

alpha = "abcdefghijklmnopqrstuvwxyzE"


def find_shortest_path_bfs(src, dest):
	src.set_visited(True)
	dist_queue = [(src, 0)]
	while len(dist_queue) > 0:
		p = dist_queue.pop(0)
		if p[0].get_value() == "v":
			pass
		if p[0] == dest:
			return p[1]
		else:
			for x in p[0].get_neighbors():
				if not x.is_visited() and alpha.find(x.get_value()) <= alpha.find(p[0].get_value()) + 1:
					x.set_visited(True)
					dist_queue.append((x, p[1] + 1))
	return False


def find_min_distance(grid, start_values, end_values):
	end = None
	starts = []
	for x in grid.get_points():
		if x.get_value() in end_values:
			end = x
		if x.get_value() in start_values:
			starts.append(x)
	dists = []
	for x in starts:
		for y in grid.get_points():
			y.set_visited(False)
		p = find_shortest_path_bfs(x, end)
		if p:
			dists.append(p)
	return min(dists)


def climb_hill(s, e):
	g = Grid(values=data)
	g.set_neighbors_for_all()
	return find_min_distance(g, s, e)


def part_one():
	return climb_hill(["S"], ["E"])


def part_two():
	return climb_hill(["S", "a"], ["E"])


if __name__ == '__main__':
	run_with_timer(part_one)  # 352 -- took 140 ms
	run_with_timer(part_two)  # 345 -- took 2588 ms
