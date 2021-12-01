from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def part_one():
	return sum(1 for i in range(1, len(data)) if data[i] > data[i-1])


def part_two():
	return sum(1 for i in range(3, len(data)) if data[i] + data[i-1] + data[i-2] > data[i-1] + data[i-2] + data[i-3])


if __name__ == '__main__':
	run_with_timer(part_one)  # 1766 -- took 0 ms
	run_with_timer(part_two)  # 1797 -- took 0 ms
