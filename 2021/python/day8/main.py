from aoc_utils import run_with_timer
import re

data = [x.strip().split(" | ") for x in open("input.txt").readlines()]
inVals = [x[0].split(" ") for x in data]
outVals = [x[1].split(" ") for x in data]


def sorted_str(x):
	return ''.join(sorted(x))


def determine_mappings(vals):
	found_mappings = ['']*10
	found_mappings[1] = sorted_str(list(filter(lambda y: len(y) == 2, vals))[0])
	found_mappings[7] = sorted_str(list(filter(lambda y: len(y) == 3, vals))[0])
	found_mappings[4] = sorted_str(list(filter(lambda y: len(y) == 4, vals))[0])
	found_mappings[8] = sorted_str(list(filter(lambda y: len(y) == 7, vals))[0])

	for x in filter(lambda y: len(y) == 6, vals):
		if len(re.sub("[" + found_mappings[1] + "]", "", x)) != 4:
			found_mappings[6] = sorted_str(x)
		elif len(re.sub("[" + found_mappings[4] + "]", "", x)) != 2:
			found_mappings[0] = sorted_str(x)
		else:
			found_mappings[9] = sorted_str(x)

	for x in filter(lambda y: len(y) == 5, vals):
		if len(re.sub("[" + found_mappings[6] + "]", "", x)) == 0:
			found_mappings[5] = sorted_str(x)
		elif len(re.sub("[" + found_mappings[9] + "]", "", x)) == 0:
			found_mappings[3] = sorted_str(x)
		else:
			found_mappings[2] = sorted_str(x)

	return found_mappings


def determine_output_value(vals, mappings):
	return int(''.join([str(mappings.index(sorted_str(x))) for x in vals]))


def part_one():
	return sum(1 for x in outVals for y in x if len(y) in [2, 3, 4, 7])


def part_two():
	return sum(determine_output_value(outVals[i], determine_mappings(x)) for i, x in enumerate(inVals))


if __name__ == '__main__':
	run_with_timer(part_one)  # 421 -- took 0 ms
	run_with_timer(part_two)  # 986163 -- took 11 ms
