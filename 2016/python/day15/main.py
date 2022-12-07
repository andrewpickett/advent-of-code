from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_discs(optional_discs=[]):
	discs = []
	for x in data:
		parts = x.split(" ")
		discs.append({
			"disc": int(parts[1][1:]),
			"positions": int(parts[3]),
			"start": int(parts[11][:-1])
		})
	if optional_discs:
		for i, x in enumerate(optional_discs):
			discs.append({
				"disc": len(discs) + i + 1,
				"positions": x["positions"],
				"start": x["start"]
			})
	return discs


def find_ideal_time(discs):
	times = {}
	i = 1
	while True:
		for y in discs:
			ideal_time = i * y["positions"] - y["start"] - y["disc"]
			if ideal_time not in times:
				times[ideal_time] = 0
			times[ideal_time] += 1
			if times[ideal_time] == len(discs):
				return ideal_time
		i += 1


def part_one():
	return find_ideal_time(get_discs())


def part_two():
	return find_ideal_time(get_discs([{"positions": 11, "start": 0}]))


if __name__ == '__main__':
	run_with_timer(part_one)  # 16824 -- took 26 ms
	run_with_timer(part_two)  # 3543984 -- took 5829 ms
