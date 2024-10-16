from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import DIRS, turn_right, turn_left, turn_around


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	infect_coords = {}
	center = len(lines) // 2
	for i, x in enumerate(lines):
		for j, y in enumerate(x):
			if y == '#':
				infect_coords[(i - center, j - center)] = "#"
	return infect_coords


def part_one(d, bursts=10000):
	curr_dir = DIRS["U"]
	curr_pos = (0, 0)
	infects = 0
	for i in range(bursts):
		if curr_pos in d:
			curr_dir = turn_right(curr_dir)
			del d[curr_pos]
		else:
			curr_dir = turn_left(curr_dir)
			d[curr_pos] = "#"
			infects += 1
		curr_pos = tuple(map(sum, zip(curr_pos, curr_dir)))
	return infects


def part_two(d, bursts=10000000):
	curr_dir = DIRS["U"]
	curr_pos = (0, 0)
	infects = 0
	for i in range(bursts):
		if curr_pos in d:
			if d[curr_pos] == "W":
				d[curr_pos] = "#"
				infects += 1
			elif d[curr_pos] == "F":
				curr_dir = turn_around(curr_dir)
				del d[curr_pos]
			elif d[curr_pos] == "#":
				curr_dir = turn_right(curr_dir)
				d[curr_pos] = "F"
		else:
			curr_dir = turn_left(curr_dir)
			d[curr_pos] = "W"
		curr_pos = tuple(map(sum, zip(curr_pos, curr_dir)))
	return infects


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()
