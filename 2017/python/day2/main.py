import copy
from utils.timers import run_with_timer


def get_data(filename):
	return [[int(y) for y in x.split()] for x in open(filename).readlines()]


def part_one(d):
	return sum(max(x) - min(x) for x in d)


def part_two(d):
	return sum(sum(max(x[y], x[z]) // min(x[y], x[z]) for y in range(len(x)) for z in range(y+1, len(x)) if max(x[y], x[z]) % min(x[y], x[z]) == 0) for x in d)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, copy.deepcopy(data))
	run_with_timer(part_two, copy.deepcopy(data))
