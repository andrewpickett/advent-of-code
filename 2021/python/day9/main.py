from aoc_utils import run_with_timer, Grid

data = [list(x.strip()) for x in open("input.txt").readlines()]


def get_low_points():
	m = Grid(values=data)
	m.set_neighbors_for_all()

	low_points = []
	for row in range(m.get_height()):
		for col in range(m.get_width()):
			cur_p = m.get_point(row, col)
			cur_val = int(cur_p.get_value())
			if cur_val < 9:
				if len(list(filter(lambda e: int(e.get_value()) > cur_val, cur_p.get_neighbors()))) == len(cur_p.get_neighbors()):
					low_points.append(cur_p)
	return low_points


def get_uphill_neighbor_count(p, visited):
	valid_neighbors = list(filter(lambda e: int(e.get_value()) != 9 and e not in visited, p.get_neighbors()))
	if p not in visited:
		visited.append(p)
	if len(valid_neighbors) > 0:
		for x in valid_neighbors:
			get_uphill_neighbor_count(x, visited)
	return len(visited)


def part_one():
	return sum(int(p.get_value())+1 for p in get_low_points())


def part_two():
	top_three = sorted([get_uphill_neighbor_count(low_point, []) for low_point in get_low_points()])[-3:]
	return top_three[0] * top_three[1] * top_three[2]


if __name__ == '__main__':
	run_with_timer(part_one)  # 458 -- took 42 ms
	run_with_timer(part_two)  # 1391940 -- took 250 ms
