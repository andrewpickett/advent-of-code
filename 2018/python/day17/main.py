from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ranges = []
	ret_val = {}
	for line in lines:
		parts = line.split(", ")
		a = range(int(parts[0][2:]), int(parts[0][2:]) + 1)
		b = range(int(parts[1][2:parts[1].find("..")]), int(parts[1][parts[1].find("..")+2:]) + 1)
		ranges.append((b, a) if parts[0].startswith("x") else (a, b))

	ret_val["miny"] = min(y.start for y, _ in ranges)
	ret_val["xoff"] = min(x.start for _, x in ranges) - 1
	grid = Grid(height=max(y.stop for y, _ in ranges), width=max(x.stop for _, x in ranges)-ret_val["xoff"]+1, default_value=".")
	grid.set_neighbors_for_all()
	for y, x in ranges:
		for row in y:
			for col in x:
				grid.get_point(row, col-ret_val["xoff"]).set_value("#")
	ret_val["start"] = (0, 500-ret_val["xoff"])
	ret_val["grid"] = waterfall(grid, ret_val["start"])

	below_min = 0
	for y in range(ret_val["miny"]):
		below_row = ''.join([x.get_value() for x in ret_val["grid"].get_row(y)])
		below_min += below_row.count("|") + below_row.count("~")
	ret_val["below"] = below_min
	return ret_val


def part_one(d):
	result = d["grid"].output()
	return result.count("~") + result.count("|") - d["below"]


def part_two(d):
	return d["grid"].output().count("~")


def waterfall(grid, start):
	grid.get_point(start[0], start[1]).set_value("+")
	curr_pos = start
	fall_points = [curr_pos]
	fallen = set(curr_pos)
	while fall_points:
		curr_pos = fall_points.pop(0)
		curr_pos = fall(grid, (curr_pos[0]+1, curr_pos[1]))
		if curr_pos:
			left_overflow, right_overflow, boundaries = check_overflow(grid, curr_pos)
			while not left_overflow and not right_overflow:
				fill(boundaries, "~")
				curr_pos = (curr_pos[0]-1, curr_pos[1])
				left_overflow, right_overflow, boundaries = check_overflow(grid, curr_pos)
			fill(boundaries, "|")
			if left_overflow and boundaries[0].get_coord() not in fallen:
				fall_points.append(boundaries[0].get_coord())
				fallen.add(boundaries[0].get_coord())
			if right_overflow and boundaries[1].get_coord() not in fallen:
				fall_points.append(boundaries[1].get_coord())
				fallen.add(boundaries[1].get_coord())
	return grid


def fall(g, p):
	next_point = g.get_point(p[0], p[1])
	while next_point.get_value() == ".":
		next_point.set_value("|")
		p = (p[0] + 1, p[1])
		if p[0] >= g.get_height() or g.get_point(p[0], p[1]).get_value() == "|":
			return False
		next_point = g.get_point(p[0], p[1])
	return p[0] - 1, p[1]


def fill(boundaries, fill_char):
	curr_point = boundaries[0]
	while curr_point != boundaries[1] and curr_point.get_value() != "#":
		curr_point.set_value(fill_char)
		curr_point = curr_point.get_east_neighbor()
	curr_point.set_value(fill_char)


def check_overflow(g, p):
	boundaries = []
	lover = check_overflow_dir(g, p, boundaries, True)
	rover = check_overflow_dir(g, p, boundaries, False)
	return lover, rover, boundaries


def check_overflow_dir(g, p, boundaries, left):
	next_point = g.get_point(coords=p)
	overflow = False
	neighbor = next_point.get_west_neighbor() if left else next_point.get_east_neighbor()
	sneigh = next_point.get_south_neighbor()
	while neighbor and sneigh and sneigh.get_value() != "." and neighbor.get_value() != "#":
		next_point = neighbor
		neighbor = next_point.get_west_neighbor() if left else next_point.get_east_neighbor()
		sneigh = next_point.get_south_neighbor()
		if sneigh.get_value() == ".":
			overflow = True
		elif neighbor and neighbor.get_value() == "#":
			overflow = False
	boundaries.append(next_point)
	return overflow


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)  # 36790
	run_with_timer(part_two, data)  # 30765


if __name__ == '__main__':
	main()
