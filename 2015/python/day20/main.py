import math

from aoc_utils import run_with_timer

data = int(open('input.txt').readline())


def print_factors(x):
	factors = [i for i in range(1, x+1) if x%i == 0]


def part_one():
	x = int(math.sqrt(data * 2)) * 50
	cur_max = 0
	while True:
		sums = sum([i for i in range(2, x, 2) if x % i == 0]) + 1 + x
		if sums > cur_max:
			print("New MAX:", x, sums*10)
			cur_max = sums
		if sums > data/10:
			return x
		x += 1


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #
