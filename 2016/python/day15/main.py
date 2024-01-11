from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	d = [x.strip() for x in open(filename).readlines()]
	discs = []
	for x in d:
		parts = x.split(" ")
		discs.append({"id": int(parts[1][1:]), "pos": int(parts[3]), "s": int(parts[11][:-1])})
	return discs


def find_ideal_time(discs):
	times = {}
	i = 1
	while True:
		for y in discs:
			ideal_time = i * y["pos"] - y["s"] - y["id"]
			if ideal_time not in times:
				times[ideal_time] = 0
			times[ideal_time] += 1
			if times[ideal_time] == len(discs):
				return ideal_time
		i += 1


def part_one(d):
	return find_ideal_time(d)


def part_two(d):
	d.append({"id": len(d) + 1, "pos": 11, "s": 0})
	return find_ideal_time(d)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
