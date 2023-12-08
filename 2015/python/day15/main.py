from utils.timers import run_with_timer
import math


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ingredients = [[int(p[2][:-1]), int(p[4][:-1]), int(p[6][:-1]), int(p[8][:-1]), int(p[10])] for p in (x.split() for x in lines)]
	ing_counts = get_ingredient_counts(len(ingredients))
	return {"ingredients": ingredients, "counts": ing_counts}


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


def calculate_total(d, i_counts):
	mults = [[i_counts[i] * j for j in d["ingredients"][i][:-1]] for i in range(len(i_counts))]
	return math.prod([sum(x) if sum(x) > 0 else 0 for x in zip(*mults)])


def calculate_calories(d, i_counts):
	return sum(x for x in [i_counts[i] * j for i in range(len(i_counts)) for j in d["ingredients"][i][-1:]])


def part_one(d):
	return max(calculate_total(d, i) for i in d["counts"])


def part_two(d):
	return max(calculate_total(d, i) for i in d["counts"] if calculate_calories(d, i) == 500)


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
