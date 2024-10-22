from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return sorted([x.strip() for x in open(filename).readlines()])


def part_one(d):
	chart = create_chart(d)
	totals = {}
	highest_total = 0
	highest_guard = 0
	for key in chart:
		if key not in totals:
			totals[key] = 0
		totals[key] += sum(chart[key])
		if totals[key] > highest_total:
			highest_total = totals[key]
			highest_guard = key
	return int(highest_guard) * chart[highest_guard].index(max(chart[highest_guard]))


def part_two(d):
	chart = create_chart(d)
	highest_total = 0
	highest_guard = 0
	for key in chart:
		if highest_total < max(chart[key]):
			highest_total = max(chart[key])
			highest_guard = key
	return int(highest_guard) * chart[highest_guard].index(max(chart[highest_guard]))


def create_chart(d):
	chart = {}
	min_start = 0
	key = None
	for line in d:
		if 'begins shift' in line:
			key = line.split()[3][1:]
			if key not in chart:
				chart[key] = [0] * 60
		elif 'falls asleep' in line:
			min_start = int(line.split()[1].split(':')[1][:-1])
		elif 'wakes up' in line:
			min_end = int(line.split()[1].split(':')[1][:-1])
			if min_end < min_start:
				min_end = 59
			for i in range(min_start, min_end):
				chart[key][i] += 1
	return chart


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
