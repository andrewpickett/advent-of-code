from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid


def get_data(filename):
	d = [x.strip() for x in open(filename).readlines()[2:]]
	pts = []
	last_row = 0
	pt_row = []
	for x in d:
		line = [y.strip() for y in x.split() if y.strip() != '']
		parts = line[0].split("-")
		row = int(parts[1][1:])
		if last_row != row:
			pts.append(pt_row)
			pt_row = []
			last_row = row
		pt_row.append({"pos": (int(parts[2][1:]), row), "size": int(line[1][:-1]), "used": int(line[2][:-1]), "avail": int(line[3][:-1]), "usepercent": int(line[4][:-1])})
	pts.append(pt_row)
	g = Grid(values=pts)
	g.set_neighbors_for_all()
	return g


def get_viable_pairs(d):
	return [(x, y) for x in d.get_points() for y in d.get_points() if 0 < x.get_value()["used"] < y.get_value()["avail"] and x != y]


def part_one(d):
	return len(get_viable_pairs(d))


def part_two(d):
	viable_pairs = get_viable_pairs(d)
	print(viable_pairs)
	access_node = d.get_point(0, 0).value
	target = d.get_point(0, d.get_width()-1).value
	print(access_node, target)
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
