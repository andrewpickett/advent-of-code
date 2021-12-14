import math

from aoc_utils import run_with_timer

data = [line.strip() for line in open("input.txt").readlines()]


def map_input():
	mapping = {}
	for line in data[2:]:
		parts = line.split(" -> ")
		mapping[parts[0]] = parts[1]

	letter_combos = {}
	for i in range(len(data[0]) - 1):
		key = data[0][i:i+2]
		if key not in letter_combos:
			letter_combos[key] = 0
		letter_combos[key] += 1
	return mapping, letter_combos


def perform_step(mapping, letter_combos):
	new_letter_combos = {}
	for x in letter_combos:
		if x in mapping:
			key1 = x[0] + mapping[x]
			key2 = mapping[x] + x[1]
			if key1 not in new_letter_combos:
				new_letter_combos[key1] = 0
			new_letter_combos[key1] += letter_combos[x]

			if key2 not in new_letter_combos:
				new_letter_combos[key2] = 0
			new_letter_combos[key2] += letter_combos[x]
		else:
			new_letter_combos[x] = letter_combos[x]
	return new_letter_combos


def count_letters(combs):
	letter_counts = {}
	for x in combs:
		for y in x:
			if y not in letter_counts:
				letter_counts[y] = 0
			letter_counts[y] += combs[x]
	for x in letter_counts:
		letter_counts[x] = math.ceil(letter_counts[x] / 2)
	return letter_counts


def run_steps_and_get_counts(steps):
	mapping, letter_combos = map_input()
	for _ in range(steps):
		letter_combos = perform_step(mapping, letter_combos)
	letter_counts = count_letters(letter_combos)
	return max(letter_counts.values()) - min(letter_counts.values())


def part_one():
	return run_steps_and_get_counts(10)


def part_two():
	return run_steps_and_get_counts(40)


if __name__ == '__main__':
	run_with_timer(part_one)  # 2975 -- took 1 ms
	run_with_timer(part_two)  # 3015383850689 -- took 3 ms
