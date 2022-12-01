from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_letter_counts():
	col_counts = []
	for i in range(len(data[0])):
		col_counts.append({})
	for x in data:
		for i, y in enumerate(x):
			if y not in col_counts[i].keys():
				col_counts[i][y] = 0
			col_counts[i][y] += 1
	return col_counts


def part_one():
	ret_val = ""
	col_counts = get_letter_counts()
	for i in col_counts:
		ret_val += max(i, key=i.get)
	return ret_val


def part_two():
	ret_val = ""
	col_counts = get_letter_counts()
	for i in col_counts:
		ret_val += min(i, key=i.get)
	return ret_val


if __name__ == '__main__':
	run_with_timer(part_one)  # usccerug -- took 0 ms
	run_with_timer(part_two)  # cnvvtafc -- took 1 ms
