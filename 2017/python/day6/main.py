from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [int(x.strip()) for x in open(filename).readline().split()]


def build_combs(comb):
	combs = []
	while '-'.join([str(x) for x in comb]) not in combs:
		combs.append('-'.join([str(x) for x in comb]))
		max_val = max(comb)
		max_idx = comb.index(max_val)
		q, rem = divmod(max_val, len(comb))
		comb[max_idx] = 0
		comb = [x + q for x in comb]
		for x in range(rem):
			comb[(max_idx + 1 + x) % len(comb)] += 1
	return combs, '-'.join([str(x) for x in comb])


def part_one(d):
	combs, _ = build_combs(d)
	return len(combs)


def part_two(d):
	combs, comb = build_combs(d)
	return len(combs) - combs.index(comb)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()
