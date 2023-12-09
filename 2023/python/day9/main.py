from utils.timers import run_with_timer


def get_data(filename):
	return [list(map(int, line)) for line in [y.split() for y in [x.strip() for x in open(filename).readlines()]]]


def extrapolate(d, backwards=False):
	s = 0
	for x in d:
		step_arrs = [x]
		diffs = [j-i for i, j in zip(x[:-1], x[1:])]
		while len([y for y in diffs if y != 0]) > 0:
			step_arrs.append(diffs)
			diffs = [j-i for i, j in zip(diffs[:-1], diffs[1:])]
		last_val = 0
		while len(step_arrs) > 0:
			n = step_arrs.pop(-1)
			if backwards:
				n = list(reversed(n))
			n.append(n[-1] + (last_val * (-1 if backwards else 1)))
			last_val = n[-1]
		s += last_val
	return s


def part_one(d):
	return extrapolate(d)


def part_two(d):
	return extrapolate(d, True)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
