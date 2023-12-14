from utils.timers import run_with_timer


def get_data(filename):
	grids = []
	lines = [x.strip() for x in open(filename).readlines()]
	curr_grid = []
	for line in lines:
		if line == "":
			grids.append(curr_grid)
			curr_grid = []
		else:
			curr_grid.append(list(line))
	grids.append(curr_grid)
	return grids


def get_reflection_count(grid, val_to_ignore=-1):
	for i, row in enumerate(grid[:-1]):
		if i+1 != val_to_ignore:
			if row == grid[i+1]:
				match_found = True
				for j in range(i+1):
					if i+1+j < len(grid) and grid[i-j] != grid[i+1+j]:
						match_found = False
						break
				if match_found:
					return i+1
	return 0


def part_one(d):
	return sum(100 * get_reflection_count(x) + get_reflection_count([list(r) for r in zip(*x[::-1])]) for x in d)


def smudge_test(grid, val_to_ignore):
	for i, row in enumerate(grid[:-1]):
		if 0 == val_to_ignore or val_to_ignore != i+1:
			v = 0
			for j, col in enumerate(row):
				grid[i][j] = "#" if grid[i][j] == "." else "."
				v = get_reflection_count(grid, val_to_ignore)
				grid[i][j] = "#" if grid[i][j] == "." else "."
				if v > 0 and (val_to_ignore == 0 or v != val_to_ignore):
					return v
	return 0


def part_two(d):
	orig_vals = {}
	for i, x in enumerate(d):
		orig_vals[i] = {"h": get_reflection_count(x), "v": get_reflection_count([list(r) for r in zip(*x[::-1])])}
	new_vals = {}
	for i, x in enumerate(d):
		new_vals[i] = {"h": smudge_test(x, orig_vals[i]["h"]), "v": smudge_test([list(r) for r in zip(*x[::-1])], orig_vals[i]["v"])}
	return sum(100*v["h"] + v["v"] for k, v in new_vals.items())


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
