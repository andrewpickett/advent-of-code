from utils.timers import run_with_timer, get_data_with_timer
from copy import deepcopy


def get_data(filename):
	return [list(x.strip()) for x in open(filename).readlines()]


def part_one(d):
	return len(find_index(identify_antinodes(d), "#"))


def part_two(d):
	return len(d) * len(d[0]) - len(find_index(identify_antinodes(d, True), "."))


def find_index(m, value):
	pts = []
	for i, row in enumerate(m):
		for j, element in enumerate(row):
			if element == value:
				pts.append((i, j))
	return pts


def identify_antinodes(o, loop=False):
	c = deepcopy(o)
	alphas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	for x in alphas:
		alpha_points = find_index(o, x)
		if len(alpha_points) > 1:
			for i in range(len(alpha_points)-1):
				for j in range(i + 1, len(alpha_points)):
					slope = (alpha_points[i][0] - alpha_points[j][0], alpha_points[i][1] - alpha_points[j][1])
					set_antinodes(alpha_points[i], slope, loop, True, c)
					set_antinodes(alpha_points[j], slope, loop, False, c)
	return c


def set_antinodes(j, slope, loop, pos, c):
	counter = 0
	next_pt = (j[0] + slope[0]*(1 if pos else -1), j[1] + slope[1]*(1 if pos else -1))
	while ((not loop and counter == 0) or loop) and (0 <= next_pt[0] < len(c) and 0 <= next_pt[1] < len(c[0])):
		c[next_pt[0]][next_pt[1]] = "#"
		next_pt = (next_pt[0] + slope[0]*(1 if pos else -1), next_pt[1] + slope[1]*(1 if pos else -1))
		counter += 1


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
