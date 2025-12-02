from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return open(filename).readline().strip().split(",")


def part_one(d):
	s = set()
	for x in d:
		get_invalid_of_len(x.split("-").copy(), 2, s)
	return sum(s)


def part_two(d):
	s = set()
	for x in d:
		parts = x.split("-")
		for i in range(len(parts[1]), 1, -1):
			get_invalid_of_len(parts.copy(), i, s)
	return sum(s)


def get_invalid_of_len(parts, l, s):
	l0, l1 = len(parts[0]), len(parts[1])
	parts[0] = "1" + ("0" * l0) if l0 % l != 0 else parts[0]
	parts[1] = "9" * (l1 - 1) if l1 % l != 0 else parts[1]

	p0, p1 = int(parts[0]), int(parts[1])
	if p1 >= p0:
		true_range = range(p0, p1 + 1)
		part_range = range(int(parts[0][0:len(parts[0]) // l]), int(parts[1][0:len(parts[1]) // l]) + 1)
		for i in part_range:
			new_num = int(str(i) * l)
			if new_num in true_range and new_num not in s:
				s.add(new_num)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
