from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ret_val = {"initial": lines[0].split()[-1], "rules": {}, "generations": 20}
	for line in lines[2:]:
		parts = line.split(" => ")
		ret_val["rules"][parts[0]] = parts[1]
	return ret_val


def part_one(d):
	current = {i: char for i, char in enumerate(d["initial"]) if char == "#"}
	for i in range(d["generations"]):
		current = run_generation(d, current)
	return sum(current)


def part_two(d):
	current = {i: char for i, char in enumerate(d["initial"]) if char == "#"}
	last_sum = 0
	last_diff = 0
	d["generations"] = 50000000000
	i = 0
	while last_diff != last_sum - sum(current.keys()):
		last_diff = last_sum - sum(current.keys())
		last_sum = sum(current.keys())
		current = run_generation(d, current)
		i += 1
	return (d["generations"] - i) * abs(last_diff) + last_sum


def run_generation(d, current):
	min_i, max_i = min(current) - 2, max(current) + 2
	next_state = {}
	for x in range(min_i, max_i + 1):
		pattern = ""
		for i in range(x-2, x+3):
			if i in current:
				pattern += current[i]
			else:
				pattern += "."
		next_state[x] = d["rules"][pattern] if pattern in d["rules"] else "."
	return {i: next_state[i] for i in next_state if next_state[i] == "#"}


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
