from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Point


def get_data(filename):
	return int(open(filename).readline().strip())


def part_one(d):
	if d == 1:
		return 0
	curr_ring = 0
	while pow(2*curr_ring + 1, 2) <= d:
		curr_ring += 1
	curr_val = pow(2*curr_ring + 1, 2)
	dists = list(reversed([x for x in range(curr_ring*2 - 1, curr_ring - 1, -1)] + [x for x in range(curr_ring+1, curr_ring*2+1)])) * 4
	for x in range(len(dists)):
		if curr_val - x == d:
			return dists[x]


def part_two(d):
	neighbor_mapping = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
	dir_mapping = [(0, -1), (1, 0), (0, 1), (-1, 0)]
	curr_dir = 0
	p = Point(0, 0, 1)
	points = {(0, 0): p}
	while True:
		next_dir = dir_mapping[(curr_dir + 1) % len(dir_mapping)]
		if (p.row + next_dir[0], p.col + next_dir[1]) in points:
			next_dir = dir_mapping[curr_dir]
		else:
			curr_dir = (curr_dir + 1) % len(dir_mapping)

		p = Point(p.row + next_dir[0], p.col + next_dir[1])
		p.set_value(sum(points[(p.row + neighbor[0], p.col + neighbor[1])].value for neighbor in neighbor_mapping if (p.row + neighbor[0], p.col + neighbor[1]) in points))
		points[(p.row, p.col)] = p
		if p.value > d:
			return p.value


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
