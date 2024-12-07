from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.utils import DIRS, turn_right


def get_data(filename):
	grid = Grid(file=filename)
	grid.set_neighbors_for_all()
	start = [x for x in grid.get_points() if x.get_value() == "^"][0]
	start.set_value(".")
	return {"grid": grid, "start": start, "path": {}}


def part_one(d):
	d["path"] = set([x[:2] for x in run(d["start"])[0]])
	return len(d["path"])


def part_two(d):
	loop_count = 0
	for x in [d["grid"].get_point(coords=y[:2]) for y in d["path"] if y != d["start"].get_coord()]:
		x.set_value("#")
		loop_count += 1 if run(d["start"])[1] else 0
		x.set_value(".")
	return loop_count


def run(start):
	cur_pos = start
	curr_dir = DIRS["^"]
	visited = {(cur_pos.get_row(), cur_pos.get_col(), curr_dir[0], curr_dir[1])}
	while True:
		next_pos = cur_pos.get_neighbor(curr_dir)
		if not next_pos:
			return visited, False
		else:
			n = (next_pos.get_row(), next_pos.get_col(), curr_dir[0], curr_dir[1])
			if n in visited:
				return None, True
			elif next_pos.get_value() != ".":
				curr_dir = turn_right(curr_dir)
			else:
				visited.add(n)
				cur_pos = next_pos


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
