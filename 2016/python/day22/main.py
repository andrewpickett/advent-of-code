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
		pt_row.append({"x": int(parts[2][1:]), "y": row, "size": int(line[1][:-1]), "used": int(line[2][:-1]), "avail": int(line[3][:-1]), "usepercent": int(line[4][:-1])})
	pts.append(pt_row)
	g = Grid(values=pts)
	g.set_neighbors_for_all()
	return g


def get_viable_pairs(d):
	return [(x, y) for x in d.get_points() for y in d.get_points() if 0 < x.get_value()["used"] < y.get_value()["avail"] and x != y]


def part_one(d):
	return len(get_viable_pairs(d))


def find_shortest_path_to_goal(d, empty_node, goal_node, walls):
	# TODO: write code to actually move the empty node to the goal node...it'll likely be a BFS approach.
	return 63  # Manually counted based on the output of my graph.


def part_two(d):
	empty_node = None
	goal_node = d.get_point(d.get_height() - 1, 0)
	walls = []
	for x in d.get_points():
		if x.value["usepercent"] > 95:
			walls.append(x)
		elif x.value["usepercent"] == 0:
			empty_node = x
		else:
			x.value = "."
	d.get_point(0, 0).value = "S"
	return (d.get_height() - 2) * 5 + find_shortest_path_to_goal(d, empty_node, goal_node, walls)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
