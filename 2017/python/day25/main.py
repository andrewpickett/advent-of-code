from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	data = {"steps": int(lines[1].split()[-2]), "states": {}, "start": lines[0].split()[-1][:-1]}
	for x in range(0, len(lines[3:]), 10):
		data["states"][lines[3:][x][-2]] = {
			"0": {
				"w": int(lines[3:][x+2].split()[-1][:-1]),
				"m": 1 if lines[3:][x+3].find("right") > 0 else -1,
				"s": lines[3:][x+4].split()[-1][:-1]
			},
			"1": {
				"w": int(lines[3:][x+6].split()[-1][:-1]),
				"m": 1 if lines[3:][x+7].find("right") > 0 else -1,
				"s": lines[3:][x+8].split()[-1][:-1]
			}
		}
	return data


def part_one(d):
	curr_pos = 0
	vals = {}
	curr_state = d["states"][d["start"]]
	for x in range(d["steps"]):
		str_pos = str(curr_pos)
		state_val = "0" if str_pos not in vals or vals[str_pos] == 0 else "1"
		if str_pos not in vals:
			vals[str_pos] = "0"
		vals[str_pos] = curr_state[state_val]["w"]
		curr_pos += curr_state[state_val]["m"]
		curr_state = d["states"][curr_state[state_val]["s"]]
	return sum(1 for x in vals if vals[x] == 1)


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
