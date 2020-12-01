from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def part_one():
	for i, first in enumerate(data):
		for second in data[i+1:]:
			if first + second == 2020:
				return first * second


def part_two():
	for i, first in enumerate(data):
		for j, second in enumerate(data[i:]):
			for third in data[j:]:
				if first + second + third == 2020:
					return first * second * third


if __name__ == '__main__':
	run_with_timer(part_one)  # 197451 -- took 1 ms
	run_with_timer(part_two)  # 138233720 -- took 312 ms
