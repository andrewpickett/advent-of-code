from aoc_utils import run_with_timer, Grid

data = int(open("input.txt").readline())


def build_office(cols, rows):
	g = Grid(rows, cols, default_value=".")
	for x in g.get_points():
		x.value = "." if bin(x.col*x.col + 3*x.col + 2*x.col*x.row + x.row + x.row*x.row + data).count("1") % 2 == 0 else "#"
	g.set_neighbors_for_all()
	return g


def find_shortest_path_bfs(src, dest):
	src.set_visited(True)
	dist_queue = [(src, 0)]
	while len(dist_queue) > 0:
		p = dist_queue.pop(0)
		if p[0] == dest:
			return p[1]
		else:
			for x in p[0].get_neighbors():
				if not x.is_visited() and x.get_value() == ".":
					x.set_visited(True)
					dist_queue.append((x, p[1] + 1))
	return False


def part_one():
	g = build_office(50, 50)
	return find_shortest_path_bfs(g.get_point(1, 1), g.get_point(39, 31))


def part_two():
	g = build_office(60, 60)
	src = g.get_point(1, 1)
	src.set_visited(True)
	dist_queue = [(src, 0)]
	visited_count = 0
	while len(dist_queue) > 0:
		p = dist_queue.pop(0)
		visited_count += 1
		for x in p[0].get_neighbors():
			if not x.is_visited() and x.get_value() == "." and p[1] < 50:
				x.set_visited(True)
				dist_queue.append((x, p[1] + 1))
	return visited_count


if __name__ == '__main__':
	run_with_timer(part_one)  # 82 -- took 29 ms
	run_with_timer(part_two)  # 138 -- took 39 ms
