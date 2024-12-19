from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	return {"avail": lines[0].split(", "), "designs": lines[2:]}


def part_one(d):
	return sum(matches(design, d["avail"], True, {}) for design in d["designs"])


def part_two(d):
	return sum(matches(design, d["avail"], False, {}) for design in d["designs"])


def matches(design, available, p1, func_cache):
	if design in func_cache:
		return func_cache[design]
	if design == '':
		return 1
	possible = 0
	for start in available:
		if design.startswith(start):
			possible = (possible or matches(design[len(start):], available, p1, func_cache)) if p1 else (possible + matches(design[len(start):], available, p1, func_cache))
	func_cache[design] = possible
	return possible


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
