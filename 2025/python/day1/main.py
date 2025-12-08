from utils.timers import run_with_timer, get_data_with_timer


def get_data(f):
	return {"d": [(x[0], int(x[1:])) for x in f.readlines()], "s": 50}


def part_one(d):
	return run_steps(d["s"], d["d"], True)


def part_two(d):
	return run_steps(d["s"], d["d"], False)


def run_steps(start_pos, steps, p1):
	pos_count = {"c": 0, "p": start_pos}
	for x in steps:
		next_pos = pos_count["p"] - (x[1] % 100) if x[0] == "L" else pos_count["p"] + (x[1] % 100)
		if p1:
			next_pos %= 100
			pos_count["c"] += 1 if next_pos == 0 else 0
		else:
			pos_count["c"] += 1 if not next_pos in range(1, 100) and pos_count["p"] != 0 else 0
			next_pos %= 100
			if x[1] >= 100:
				pos_count["c"] += x[1] // 100
		pos_count["p"] = next_pos
	return pos_count["c"]


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
