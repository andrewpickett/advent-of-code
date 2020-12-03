from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]


def part_one():
	return sum(y.count('\\"') + y.count('\\\\') + ((y.count('\\x') - y.count('\\\\x') + y.count('\\\\\\x'))*3) + 2 for y in (x[1:-1] for x in data))


def part_two():
	return sum(x.count('"') + x.count('\\') + 2 for x in data)


if __name__ == '__main__':
	run_with_timer(part_one)  # 1350 -- took 0 ms
	run_with_timer(part_two)  # 2085 -- took 0 ms
