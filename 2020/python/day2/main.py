from aoc_utils import run_with_timer

# data will be a list of each line stored as a list in this order: [min, max, letter, password]
data = [[int(y[0].split('-')[0]), int(y[0].split('-')[1]), y[1][:-1], y[2]] for y in [x.split() for x in open("input.txt").readlines()]]


def part_one():
	return sum(1 for x in data if x[0] <= x[3].count(x[2]) <= x[1])


def part_two():
	return sum(1 for x in data if (x[3][x[0]-1] == x[2]) ^ (x[3][x[1]-1] == x[2]))


if __name__ == '__main__':
	run_with_timer(part_one)  # 580 -- took 0 ms
	run_with_timer(part_two)  # 611 -- took 0 ms
