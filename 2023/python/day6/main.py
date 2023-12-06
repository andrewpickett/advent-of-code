from utils.timers import run_with_timer
from math import sqrt, pow, floor, ceil, prod


def get_data(filename):
	lines = [x.strip().split(":") for x in open(filename).readlines()]
	return [[int(x.strip()) for x in lines[0][1].strip().split()], [int(x.strip()) for x in lines[1][1].strip().split()]]


def win_count(t, d):
	top = (t + sqrt(pow(t, 2) - 4*d)) / 2
	bottom = (t - sqrt(pow(t, 2) - 4*d)) / 2
	top = floor(top-1 if top == floor(top) else top)
	bottom = ceil(bottom+1 if bottom == ceil(bottom) else bottom)
	return (top-bottom)+1


def part_one(d):
	return prod(win_count(d[0][i], d[1][i]) for i in range(len(d[0])))


def part_two(d):
	return win_count(int(''.join([str(x) for x in d[0]])), int(''.join([str(x) for x in d[1]])))


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
