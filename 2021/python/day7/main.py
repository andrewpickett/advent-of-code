from aoc_utils import run_with_timer
import sys

data = [int(x) for x in open("input.txt").readline().strip().split(",")]


def calc_fuel(fun):
	return min(min([sum(fun(x, y) for y in data)]) for x in range(max(data)+1))


def part_one():
	return calc_fuel(lambda x, y: abs(y-x))


def part_two():
	return calc_fuel(lambda x, y: (abs(y-x)*(abs(y-x)+1))//2)


if __name__ == '__main__':
	run_with_timer(part_one)  # 356992 -- took 806 ms
	run_with_timer(part_two)  # 101268110 -- took 1413 ms
