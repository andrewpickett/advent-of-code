from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid

def get_data(f):
	g = Grid(file=f)
	g.set_neighbors_for_all(include_diagonals=True)
	return g


def part_one(d):
	return len(get_forklift_accessible([x for x in d.get_points() if x.get_value() == "@"]))


def part_two(d):
	count = 0
	all_points = [x for x in d.get_points() if x.get_value() == "@"]
	iters = 1
	while True:
		removals = get_forklift_accessible(all_points)
		if len(removals) == 0:
			break
		count += len(removals)
		for x in removals:
			all_points.remove(x)
			x.set_value(".")
		iters += 1
	return count


def get_forklift_accessible(rolls):
	return set([p for p in rolls if len([x for x in p.get_neighbors() if x.get_value() == "@"]) < 4])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
