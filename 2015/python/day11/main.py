from utils.timers import run_with_timer, get_data_with_timer

alpha = [x for x in 'abcdefghijklmnopqrstuvwxyz']


def get_data(filename):
	return open(filename).readline().strip()


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


def part_one(d):
	return get_next_pass(d)


def part_two(d):
	return get_next_pass(d)


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	p1 = run_with_timer(part_one, data)
	run_with_timer(part_two, p1)
