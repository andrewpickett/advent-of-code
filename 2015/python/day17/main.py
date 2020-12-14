from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open('input.txt').readlines()]


def f(available, target, curr_combo, valid_combos):
	if sum(curr_combo) == target:
		valid_combos.append(curr_combo)
		return 1
	elif sum(curr_combo) > target:
		return 0
	return sum(f(available[i+1:], target, curr_combo + [x], valid_combos) for i, x in enumerate(available))


def part_one():
	containers = data.copy()
	containers.sort(reverse=True)
	return f(containers, 150, [], [])


def part_two():
	containers = data.copy()
	containers.sort(reverse=True)
	valid_combos = []
	f(containers, 150, [], valid_combos)
	return sum(1 for x in valid_combos if len(x) == min([len(x) for x in valid_combos]))


if __name__ == '__main__':
	run_with_timer(part_one)  # 654 -- took 34 ms
	run_with_timer(part_two)  # 57 -- took 68 ms
