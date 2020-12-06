from aoc_utils import run_with_timer

data = open("input.txt").read().strip().split('\n\n')

ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def part_one():
	return sum(len(set(y for y in x.replace('\n', ''))) for x in data)


def part_two():
	return sum(sum(1 for i in [x.count(letter) for letter in ALPHA] if i == len(x.split('\n'))) for x in data)


if __name__ == '__main__':
	run_with_timer(part_one)  # 6583 -- took 1 ms
	run_with_timer(part_two)  # 3290 -- took 4 ms
