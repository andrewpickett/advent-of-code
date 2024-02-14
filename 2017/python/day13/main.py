from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = {}
	for x in open(filename).readlines():
		parts = x.strip().split(": ")
		ret_val[int(parts[0])] = int(parts[1])
	return ret_val


def get_severity(d, delay):
	severity = 0
	for x in d:
		if (x+delay) >= d[x] and (x+delay) % ((d[x]-1)*2) == 0:
			severity += (x * d[x])
	return severity


def part_one(d):
	return get_severity(d, 0)


def part_two(d):
	i = 0
	severity = 1
	while severity > 0:
		i += 1
		if i % ((d[0]-1) * 2) == 0:
			continue
		severity = get_severity(d, i)
	return i


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
