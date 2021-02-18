from aoc_utils import run_with_timer

data = [x for x in open('input.txt').readline()]


def part_one():
	return data.count('(') - data.count(')')


def part_two():
	floor = 0
	for i, direction in enumerate(data):
		floor += 1 if direction == '(' else -1
		if floor < 0:
			return i + 1


if __name__ == '__main__':
	run_with_timer(part_one)  # 138 -- took 0 ms
	run_with_timer(part_two)  # 1771 -- took 0 ms
