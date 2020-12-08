import math
from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]
ingredients = []
ing_counts = []


def get_ingredient_counts(n):
	vals = []
	for i in range(100**(n-1) + 1):
		vals.append([])
		tot = 0
		divisor = i
		for j in reversed(range(n-1)):
			next_num = divisor // (100**j if j > 0 else 1)
			if next_num > 0:
				divisor = divisor % (100**j if j > 0 else divisor)
			tot += next_num
			vals[-1].append(next_num)

		if 100 - tot < 0:
			vals.pop()
		else:
			vals[-1].append(100 - tot)
	return vals


def calculate_total(ing_counts):
	mults = [[ing_counts[i] * j for j in ingredients[i][:-1]] for i in range(len(ing_counts))]
	return math.prod([sum(x) if sum(x) > 0 else 0 for x in zip(*mults)])


def calculate_calories(ing_counts):
	return sum(x for x in [ing_counts[i] * j for i in range(len(ing_counts)) for j in ingredients[i][-1:]])


def part_one():
	return max(calculate_total(i) for i in ing_counts)


def part_two():
	return max(calculate_total(i) for i in ing_counts if calculate_calories(i) == 500)


if __name__ == '__main__':
	ingredients = [[int(p[2][:-1]), int(p[4][:-1]), int(p[6][:-1]), int(p[8][:-1]), int(p[10])] for p in (x.split() for x in data)]
	ing_counts = get_ingredient_counts(len(ingredients))
	run_with_timer(part_one)  # 222870 -- took 1103 ms
	run_with_timer(part_two)  # 117936 -- took 446 ms
