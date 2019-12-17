from aoc_utils import run_with_timer

data = [tuple(map(int, x.split('x'))) for x in open('input.txt').readlines()]


def part_one():
	return sum(2*i[0]*i[1] + 2*i[0]*i[2] + 2*i[1]*i[2] + min(i[0]*i[1], i[0]*i[2], i[1]*i[2]) for i in data)


def part_two():
	return sum(2*min(i[0]+i[1], i[0]+i[2], i[1]+i[2]) + (i[0]*i[1]*i[2]) for i in data)


if __name__ == '__main__':
	run_with_timer(part_one)  # 1588178
	run_with_timer(part_two)  # 3783758
