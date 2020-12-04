from aoc_utils import run_with_timer

data = [x for x in open('input.txt').readline().strip()]
alpha = [x for x in 'abcdefghijklmnopqrstuvwxyz']


def short_cut(pw, fc):
	intvals = [alpha.index(x) for x in pw]
	idx = alpha.index(fc)
	if idx in intvals:
		intvals[intvals.index(idx)] += 1
		for i in range(idx+1, len(intvals)):
			intvals[i] = 0
		return "".join([alpha[x] for x in intvals])
	return pw


def increment(pw):
	intvals = [alpha.index(x) for x in pw]
	i = -1
	while True:
		intvals[i] += 1
		if intvals[i] == len(alpha):
			intvals[i] = 0
			i -= 1
		else:
			return "".join([alpha[x] for x in intvals])


def check_pw(pw):
	intvals = [alpha.index(x) for x in pw]
	if any([x in pw for x in ['i', 'o', 'l']]):
		return False
	if sum(intvals[i+2]-intvals[i+1] == 1 and intvals[i+1]-intvals[i] == 1 for i in range(len(intvals) - 2)) == 0:
		return False
	if len(set(pw[i] for i in range(len(pw)-1) if pw[i] == pw[i+1])) < 2:
		return False
	return True


def get_next_pass(initial):
	pw = increment(initial)
	is_valid = check_pw(pw)
	while not is_valid:
		if 'i' in pw:
			pw = short_cut(pw, 'i')
		elif 'l' in pw:
			pw = short_cut(pw, 'l')
		elif 'o' in pw:
			pw = short_cut(pw, 'o')
		else:
			pw = increment(pw)

		is_valid = check_pw(pw)
	return pw


def part_one():
	return get_next_pass(data)


def part_two():
	initial = get_next_pass(data)
	return get_next_pass(initial)


if __name__ == '__main__':
	run_with_timer(part_one)  # hepxxyzz -- took 2388 ms
	run_with_timer(part_two)  # heqaabcc -- took 8270 ms
