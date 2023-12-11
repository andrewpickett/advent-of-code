from utils.timers import run_with_timer
from utils.grid import Grid


def get_data(filename):
	vals = []
	ex_rows = []
	for i, line in enumerate([x.strip() for x in open(filename).readlines()]):
		vals.append(list(line))
		if line.replace(".", "") == "":
			ex_rows.append(i)

	ex_cols = []
	for i, x in enumerate(list(zip(*vals[::-1]))):
		if ''.join(x).replace(".", "") == "":
			ex_cols.append(i)
	g = Grid(values=vals)
	d = {"grid": g, "ex_rows": ex_rows, "ex_cols": ex_cols}
	return d


def calc_dists(d, exps):
	pts = [x for x in d["grid"].get_points() if x.value == "#"]
	s = 0
	for i in range(len(pts)-1):
		for j in range(i+1, len(pts)):
			max_row = max(pts[j].get_row(), pts[i].get_row())
			min_row = min(pts[j].get_row(), pts[i].get_row())
			max_col = max(pts[j].get_col(), pts[i].get_col())
			min_col = min(pts[j].get_col(), pts[i].get_col())

			num_row_expansions = sum(1 if min_row < x < max_row else 0 for x in d["ex_rows"])
			num_col_expansions = sum(1 if min_col < x < max_col else 0 for x in d["ex_cols"])

			s += ((abs(pts[j].get_row() - pts[i].get_row()) + (exps - 1) * num_row_expansions) + (abs(pts[j].get_col() - pts[i].get_col()) + (exps - 1) * num_col_expansions))
	return s


def part_one(d):
	return calc_dists(d, 2)


def part_two(d):
	return calc_dists(d, 1000000)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
