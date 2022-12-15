from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


def parse_input():
	close_map = {}
	for x in data:
		close_map[(int(x[2].split('=')[1][:-1]), int(x[3].split('=')[1][:-1]))] = (int(x[8].split('=')[1][:-1]), int(x[9].split('=')[1]))
	return close_map


def get_all_range_coverage(range_list):
	r = []
	for begin,end in sorted(range_list):
		if r and r[-1][1] >= begin - 1:
			r[-1][1] = max(r[-1][1], end)
		else:
			r.append([begin, end])
	return r


def find_empty_space_ranges(close_map, target_row, valid_range=None):
	empty_spaces = set()
	for signal in close_map:
		distance = abs(close_map[signal][1] - signal[1]) + abs(close_map[signal][0] - signal[0])
		if signal[1] - distance <= target_row <= signal[1] + distance:
			x_coverage = distance - abs(signal[1] - target_row)
			if valid_range:
				empty_spaces.add((max(valid_range[0], signal[0] - x_coverage), min(valid_range[1], signal[0] + x_coverage)))
			else:
				empty_spaces.add((signal[0] - x_coverage, signal[0] + x_coverage))
	return empty_spaces


def part_one():
	return sum(x[1] - x[0] for x in get_all_range_coverage(find_empty_space_ranges(parse_input(), 2000000)))


def part_two():
	close_map = parse_input()
	for row in range(0, 4000000):
		rs = get_all_range_coverage(find_empty_space_ranges(close_map, row, valid_range=(0, 4000000)))
		if len(rs) > 1:
			return 4000000 * (rs[0][1] + 1) + row
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 5108096 -- took 0 ms
	run_with_timer(part_two)  # 10553942650264 -- took 69755 ms
