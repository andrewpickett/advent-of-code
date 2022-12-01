from aoc_utils import run_with_timer

data = [[int(y.strip()) for y in x.strip().split(' ') if y.strip() != ''] for x in open("input.txt").readlines()]


def part_one():
	return sum(1 for x in data if 2 * max(x) < sum(x))


def part_two():
	possible = 0
	for i in range(0, len(data), 3):
		for j in range(0, 3):
			t = [data[i][j], data[i+1][j], data[i+2][j]]
			possible += 1 if 2 * max(t) < sum(t) else 0
	return possible


if __name__ == '__main__':
	run_with_timer(part_one)  # 982 -- took 1 ms
	run_with_timer(part_two)  # 1826 -- took 1 ms
