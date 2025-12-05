from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid

def get_data(filename):
	g = Grid(file=filename)
	g.set_neighbors_for_all(include_diagonals=True)
	g2 = Grid(height=g.get_height(), width=g.get_width())
	for col in range(g.get_height()):
		for row in range(g.get_width()):
			cur = g.get_point(row, col);
			g2.get_point(row, col).set_value(len([p for p in cur.get_neighbors() if p.get_value() == "@"]) if cur.get_value() == "@" else ".")
	print(g2.output())
	return g2


def part_one(d):
	return len(get_forklift_accessible([x for x in d.get_points() if x.get_value() == "@"]))


def part_two(d):
	count = 0
	all_rolls = [x for x in d.get_points() if x.get_value() != "."]
	last_len = 0
	while len(all_rolls) != last_len:
		last_len = len(all_rolls)

		for x in all_rolls:
			print(x)
			if x.get_value() < 4:
				count += 1
				x.set_value(".")
				for y in [p for p in x.get_neighbors() if p.get_value() != "."]:
					y.set_value(y.get_value() - 1)
	return count
	# count = 0
	# all_points = [x for x in d.get_points() if x.get_value() == "@"]
	# iters = 1
	# while True:
	# 	removals = get_forklift_accessible(all_points)
	# 	if len(removals) == 0:
	# 		break
	# 	count += len(removals)
	# 	for x in removals:
	# 		all_points.remove(x)
	# 		x.set_value(".")
	# 	iters += 1
	# # print("Took", iters, "iterations")
	return count


def get_forklift_accessible(rolls):
	return set([p for p in rolls if len([x for x in p.get_neighbors() if x.get_value() == "@"]) < 4])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
