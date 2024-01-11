from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.algorithms import bfs


def get_data(filename):
	i = int(open(filename).readline())
	g = Grid(60, 60, default_value=".")
	for x in g.get_points():
		x.value = "." if bin(x.col*x.col + 3*x.col + 2*x.col*x.row + x.row + x.row*x.row + i).count("1") % 2 == 0 else "#"
	g.set_neighbors_for_all()
	return {"g": g, "t": (39, 31)}


def part_one(d):
	return bfs(d["g"].get_point(1, 1), d["g"].get_point(d["t"][0], d["t"][1]), lambda x: [y for y in x[0].get_neighbors() if y.value == "."])[1]


def part_two(d):
	src = d["g"].get_point(1, 1)
	visited = {src}
	dist_queue = [(src, 0)]
	while len(dist_queue) > 0:
		p = dist_queue.pop(0)
		visited.add(p[0])
		for x in p[0].get_neighbors():
			if x not in visited and x.get_value() == "." and p[1] < 50:
				dist_queue.append((x, p[1] + 1))
	return len(visited)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
