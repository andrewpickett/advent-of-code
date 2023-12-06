from utils.timers import run_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	maps = {"seeds": [int(x) for x in lines[0].split()[1:]], "mappings": []}

	curr_map = None
	for line in lines[2:]:
		if line != "":
			if not line[0].isdigit():
				if curr_map:
					maps["mappings"].append(curr_map)
				curr_map = []
			else:
				curr_map.append(tuple([int(x) for x in line.split()]))
	maps["mappings"].append(curr_map)
	maps["mappings"] = list(map(lambda mapping: sorted(mapping, key=lambda x: x[1]), maps["mappings"]))
	return maps


def collapse(intervals):
	if len(intervals) <= 1:
		return intervals

	if len(intervals) == 2:
		if do_overlap(*intervals):
			return [(intervals[0][0], max(intervals[0][1], intervals[1][1]))]
		else:
			return intervals
	mid = len(intervals) // 2
	return collapse(intervals[:mid]) + collapse(intervals[mid:])


def do_overlap(l, r):
	if l[0] <= r[0]:
		return l[1] >= r[0]
	else:
		return l[0] <= r[1]


def process(intervals, mappings):
	new_intervals = set()

	for interval in intervals:
		int_size = interval[1] - interval[0] + 1
		relevant_mappings = [i for i in mappings if do_overlap(interval, (i[1], i[1] + i[2] - 1))]

		if not relevant_mappings:
			new_intervals.add(interval)
			continue

		not_mapped_start, not_mapped_end = interval[0], relevant_mappings[0][1] - 1
		for d_start, s_start, int_len in relevant_mappings:
			source_end = s_start + int_len - 1
			not_mapped_end = s_start - 1
			if not_mapped_end > not_mapped_start and not_mapped_start <= interval[1]:
				new_intervals.add((not_mapped_start, min(interval[1], not_mapped_end)))

			mapped_interval_length = min(int_len, interval[1]-s_start + 1, source_end - interval[0] + 1, int_size)
			mapped_interval_start = d_start + max(interval[0], s_start) - s_start
			new_intervals.add((mapped_interval_start, mapped_interval_start + mapped_interval_length - 1))
			not_mapped_start = source_end + 1

		if not_mapped_start <= interval[1]:
			new_intervals.add((not_mapped_start, interval[1]))
	return list(new_intervals)


def part_one(d):
	seed_locations = {}
	for seed in d["seeds"]:
		curr_val = seed
		for mapping in d["mappings"]:
			for ranges in mapping:
				if ranges[1] < curr_val < ranges[1] + ranges[2]:
					curr_val += ranges[0] - ranges[1]
					break
		seed_locations[seed] = curr_val
	return min(seed_locations.values())


def part_two(d):
	tmp = []
	for i in range(0, len(d["seeds"]), 2):
		tmp.append((d["seeds"][i], d["seeds"][i] + d["seeds"][i+1]))
	d["seeds"] = sorted(tmp)

	for mapping in d["mappings"]:
		intervals = sorted(process(d["seeds"], mapping))
		current_length = len(intervals)
		new_length = 0

		while current_length != new_length:
			current_length = new_length
			intervals = collapse(intervals)
			new_length = len(intervals)
		d["seeds"] = intervals
	return sorted(d["seeds"])[0][0]


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
