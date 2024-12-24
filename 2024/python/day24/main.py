from collections import defaultdict

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	directions = False

	dirs = []
	start = defaultdict(int)
	for line in lines:
		if line == "":
			directions = True
		else:
			if directions:
				parts = line.split(" -> ")
				dirs.append(parts)
			else:
				parts = line.split(": ")
				start[parts[0]] += int(parts[1])
	return {"s": start, "d": dirs, "o": lambda x,y: x + y}


def part_one(d):
	return get_int_val(run_all_outputs(d["d"].copy(), d["s"].copy()), "z")


def get_int_val(vals, wire):
	return int(get_bin_val(vals, wire), 2)


def get_bin_val(vals, wire):
	s = ""
	for v in {k: str(vals[k]) for k in list(reversed(sorted(vals.keys()))) if k.startswith(wire)}.values():
		s += v
	return s


def run_all_outputs(directions, vals):
	i = 0
	while len(directions) > 0:
		x = directions[i]
		parts = x[0].split()
		if parts[0] in vals and parts[2] in vals:
			if parts[1] == "AND":
				vals[x[1]] = 1 if vals[parts[0]] & vals[parts[2]] else 0
			elif parts[1] == "OR":
				vals[x[1]] = 1 if vals[parts[0]] | vals[parts[2]] else 0
			elif parts[1] == "XOR":
				vals[x[1]] = 1 if vals[parts[0]] ^ vals[parts[2]] else 0
			directions.remove(x)
		else:
			i += 1
		if len(directions) > 0:
			i %= len(directions)
	return vals


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
