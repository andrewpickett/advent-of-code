from utils.timers import run_with_timer, get_data_with_timer
from itertools import combinations
from operator import itemgetter
from functools import reduce


def get_data(filename):
	return [int(x.strip()) for x in open(filename).readlines()]


def find_answer(d, compartments=3):
	weight = sum(d) // compartments
	for n in range(1, len(d)-compartments):
		ans = []
		for comb in combinations(d, n):
			if sum(comb) == weight:
				prod = reduce(lambda x, y: x * y, comb)
				ans.append((prod, comb))
		if len(ans) > 0:
			for (prod, comb) in sorted(ans, key=itemgetter(0)):
				rest = tuple(set(d) - set(comb))
				if compartments == 3:
					other_groups = find_other_two_groups(rest, weight)
					if other_groups:
						return prod
				elif compartments == 4:
					other_groups = find_other_three_groups(rest, weight)
					if other_groups:
						return prod


def find_other_two_groups(rest, weight):
	for n in range(1, len(rest)):
		for comb in combinations(rest, n):
			if sum(comb) == weight:
				return comb
	return False


def find_other_three_groups(rest, weight):
	for n in range(1, len(rest)):
		for comb in combinations(rest, n):
			if sum(comb) == weight:
				new_rest = tuple(set(rest) - set(comb))
				other_groups = find_other_two_groups(new_rest, weight)
				if other_groups:
					return comb
	return False


def part_one(d):
	return find_answer(d, 3)


def part_two(d):
	return find_answer(d, 4)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
