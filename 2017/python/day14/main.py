from utils.timers import run_with_timer, get_data_with_timer
from utils.hash import knot_hash
from utils.grid import Grid


def get_data(filename):
	d = open(filename).readline().strip()
	grid_data = []
	for x in range(128):
		grid_data.append(list(''.join([bin(int(y, 16))[2:].zfill(4) for y in knot_hash(d + "-" + str(x))])))
	g = Grid(values=grid_data)
	g.set_neighbors_for_all()
	return g


def part_one(d):
	return sum(int(x.value) for x in d.get_points())


def get_group(start_node, visited):
	q = set()
	q.add(start_node)
	group = []
	while len(q) > 0:
		n = q.pop()
		visited.add(n)
		group.append(n)
		for y in n.get_neighbors():
			if y not in visited and y.value == "1":
				group += get_group(y, visited)
	return group


def part_two(d):
	groups = []
	visited = set()
	for x in d.get_points():
		if x not in visited and x.value == "1":
			groups.append(get_group(x, visited))
	return len(groups)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
