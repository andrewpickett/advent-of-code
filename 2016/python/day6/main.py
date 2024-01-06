from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def get_letter_counts(d):
	col_counts = []
	for i in range(len(d[0])):
		col_counts.append({})
	for x in d:
		for i, y in enumerate(x):
			if y not in col_counts[i].keys():
				col_counts[i][y] = 0
			col_counts[i][y] += 1
	return col_counts


def part_one(d):
	ret_val = ""
	col_counts = get_letter_counts(d)
	for i in col_counts:
		ret_val += max(i, key=i.get)
	return ret_val


def part_two(d):
	ret_val = ""
	col_counts = get_letter_counts(d)
	for i in col_counts:
		ret_val += min(i, key=i.get)
	return ret_val


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
