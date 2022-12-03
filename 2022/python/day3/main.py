from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]

alphas = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part_one():
	return sum(alphas.find([y for y in x[0:len(x)//2] if y in x[len(x)//2:]][0]) for x in data)


def part_two():
	return sum(alphas.find([y for y in data[x] if y in data[x+1] and y in data[x+2]][0]) for x in range(0, len(data)-2, 3))


if __name__ == '__main__':
	run_with_timer(part_one)  # 7967 -- took 4 ms
	run_with_timer(part_two)  # 2716 -- took 1 ms
