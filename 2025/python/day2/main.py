from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return open(filename).readline().strip().split(",")


def part_one(d):
	s = set()
	for x in d:
		get_invalid_of_len(x, 2, s)
	return sum(s)


def part_two(d):
	s = set()
	for x in d:
		for i in range(len(x.split("-")[1]), 1, -1):
			get_invalid_of_len(x, i, s)
	return sum(s)


def get_invalid_of_len(r, l, s):
	parts = r.split("-")
	if len(parts[0]) % l != 0:
		parts[0] = "1" + ("0" * len(parts[0]))
	if len(parts[1]) % l != 0:
		parts[1] = "9" * (len(parts[1]) - 1)
	if int(parts[1]) >= int(parts[0]):
		new_range = range(int(parts[0]), int(parts[1]) + 1)
		half_range = range(int(parts[0][0:len(parts[0]) // l]), int(parts[1][0:len(parts[1]) // l]) + 1)
		for i in half_range:
			new_num = int(str(i) * l)
			if new_num in new_range and new_num not in s:
				s.add(new_num)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
