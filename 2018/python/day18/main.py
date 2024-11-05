from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from copy import copy


def get_data(filename):
	grid = Grid(file=filename)
	grid.set_neighbors_for_all(True)
	return grid


def part_one(d):
	next_grid = copy(d)
	for i in range(10):
		next_grid = run_generation(next_grid)
	final_state = next_grid.output().replace("\n", "")
	return final_state.count("#") * final_state.count("|")


def part_two(d):
	next_grid = copy(d)
	previous_states = [next_grid.output().replace("\n", "")]
	i = previ = 0
	while True:
		next_grid = run_generation(next_grid)
		next_state = next_grid.output().replace("\n", "")
		if next_state in previous_states:
			previ = previous_states.index(next_state)
			break
		previous_states.append(next_state)
		i += 1
	previ -= 1
	final_state = previous_states[previ + ((1000000000 - previ) % (i - previ))]
	return final_state.count("#") * final_state.count("|")


def run_generation(orig):
	next_grid = copy(orig)
	for x in orig.get_points():
		new_point = next_grid.get_point(coords=x.get_coord())
		trees = sum(1 for y in x.get_neighbors() if y.get_value() == "|")
		lumberyards = sum(1 for y in x.get_neighbors() if y.get_value() == "#")
		if x.get_value() == ".":
			new_point.set_value("|" if trees >= 3 else ".")
		elif x.get_value() == "|":
			new_point.set_value("#" if lumberyards >= 3 else "|")
		elif x.get_value() == "#":
			new_point.set_value("." if lumberyards < 1 or trees < 1 else "#")
	return next_grid


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
