from utils.timers import run_with_timer


def get_data(filename):
	d = [int(x.strip()) for x in open(filename).readlines()]
	d.sort(reverse=True)
	return {"target": 150, "containers": d}


def f(available, target, curr_combo, valid_combos):
	if sum(curr_combo) == target:
		valid_combos.append(curr_combo)
		return 1
	elif sum(curr_combo) > target:
		return 0
	return sum(f(available[i+1:], target, curr_combo + [x], valid_combos) for i, x in enumerate(available))


def part_one(d):
	return f(d["containers"], d["target"], [], [])


def part_two(d):
	valid_combos = []
	f(d["containers"], d["target"], [], valid_combos)
	return sum(1 for x in valid_combos if len(x) == min([len(x) for x in valid_combos]))


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
