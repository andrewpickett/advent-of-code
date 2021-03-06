from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def part_one():
	return next(first*second for i, first in enumerate(data) for second in data[i+1:] if first + second == 2020)


def part_two():
	return next(first*second*third for i, first in enumerate(data) for j, second in enumerate(data[i+1:]) for third in data[j+1:] if first + second + third == 2020)


if __name__ == '__main__':
	run_with_timer(part_one)  # 197451 -- took 0 ms
	run_with_timer(part_two)  # 138233720 -- took 94 ms
