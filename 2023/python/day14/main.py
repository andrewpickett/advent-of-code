from utils.timers import run_with_timer
from copy import deepcopy


def get_data(filename):
	return [list(x.strip()) for x in open(filename).readlines()]


def run_tilts(d, dirs):
	for x in range(dirs):
		for i, row in enumerate(d):
			for j, col in enumerate(row):
				if d[i][j] == "O":
					if i > 0:
						nn = i-1
						while nn >= 0 and d[nn][j] == ".":
							nn -= 1
						d[i][j] = "."
						d[nn+1][j] = "O"
		d = [list(r) for r in zip(*d[::-1])]
	for y in range(4 - dirs):
		d = [list(r) for r in zip(*d[::-1])]
	return d


def part_one(d):
	d = run_tilts(d, 1)
	return sum(row.count("O") * (len(d) - i) for i, row in enumerate(d))


def part_two(d):
	orig_data = deepcopy(d)
	cycle_start = False
	states = []
	i = 0
	while True:
		d = run_tilts(d, 4)
		if str(d) in states:
			states.clear()
			if cycle_start:
				cycle_count = i - cycle_start
				break
			else:
				cycle_start = i
		states.append(str(d))
		i += 1
	cycle_start = (cycle_start - cycle_count)
	cycles = ((1000000000 - cycle_start) % cycle_count) + cycle_start

	for j in range(cycles):
		orig_data = run_tilts(orig_data, 4)
	return sum(row.count("O") * (len(orig_data) - i) for i, row in enumerate(orig_data))


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, deepcopy(data))
	run_with_timer(part_two, deepcopy(data))
