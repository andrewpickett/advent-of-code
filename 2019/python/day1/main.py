from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def part_one():
	return sum(calc_spec_fuel(i) for i in data)


def part_two():
	return sum(calc_total_fuel(i) for i in data)


def calc_spec_fuel(val):
	return (val // 3) - 2


def calc_total_fuel(start):
	n = calc_spec_fuel(start)
	return 0 if n <= 0 else n + calc_total_fuel(n)


if __name__ == '__main__':
	run_with_timer(part_one)  # 3382284
	run_with_timer(part_two)  # 5070541
