from utils.timers import run_with_timer
import math


def get_data(filename):
	return [[[z.split() for z in y.strip().split(", ")] for y in x[x.find(":")+1:].strip().split(";")] for x in open(filename).readlines()]


def part_one(d):
	max_amounts = {"red": 12, "green": 13, "blue": 14}
	valid = [True] * len(d)
	for i, x in enumerate(d):
		for y in x:
			for z in y:
				valid[i] = valid[i] and max_amounts[z[1]] >= int(z[0])
	return sum(i+1 for i, x in enumerate(valid) if x)


def part_two(d):
	s = 0
	for x in d:
		mins = {"red": 0, "blue": 0, "green": 0}
		for y in x:
			for z in y:
				mins[z[1]] = max(mins[z[1]], int(z[0]))
		s += math.prod(mins.values())
	return s


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
