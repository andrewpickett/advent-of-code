from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid

def get_data(filename):
	g = Grid(file=filename)
	g.set_neighbors_for_all(include_diagonals=True)
	return g


def part_one(d):
	return len(get_forklift_accessible(d))


def part_two(d):
	count = 0
	while True:
		removals = get_forklift_accessible(d)
		if len(removals) == 0:
			break
		count += len(removals)
		for x in removals:
			x.set_value(".")
	return count


def get_forklift_accessible(d):
	return set([p for p in [x for x in d.get_points() if x.get_value() == "@"] if len([x for x in p.get_neighbors() if x.get_value() == "@"]) < 4])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
