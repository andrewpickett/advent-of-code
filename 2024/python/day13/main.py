from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = [{}]
	for line in [x.strip() for x in open(filename).readlines()]:
		if line == "":
			ret_val.append({})
		else:
			parts = line.split()
			if parts[0] == "Button" and parts[1] == "A:":
				ret_val[-1]["a"] = [int(parts[2][2:-1]), int(parts[3][2:])]
			elif parts[0] == "Button" and parts[1] == "B:":
				ret_val[-1]["b"] = [int(parts[2][2:-1]), int(parts[3][2:])]
			else:
				ret_val[-1]["target"] = [int(parts[1][2:-1]), int(parts[2][2:])]
	return ret_val


def part_one(d):
	return sum(calc_tokens(machine) for machine in d)


def part_two(d):
	return sum(calc_tokens(machine, 10000000000000) for machine in d)


def calc_tokens(m, offset=0):
	m["target"] = [x + offset for x in m["target"]]

	denom = (m["a"][0] * m["b"][1] - m["a"][1] * m["b"][0])
	a_presses = (m["target"][0] * m["b"][1] - m["target"][1] * m["b"][0]) / denom
	b_presses = (m["target"][1] * m["a"][0] - m["target"][0] * m["a"][1]) / denom

	if a_presses == int(a_presses) and b_presses == int(b_presses):
		return 3 * int(a_presses) + int(b_presses)
	return 0


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main("input.txt")
