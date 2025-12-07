import math

from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import rotate_matrix


def get_data(filename):
	lines = open(filename).read().split("\n")[:-1]
	indices = [(i, x) for i, x in enumerate(lines[-1]) if not x.isspace()]
	data = []
	for line in lines[:-1]:
		row = [line[indices[i-1][0]:indices[i][0]-1] for i in range(1, len(indices))]
		row.append(line[indices[-1][0]:])
		data.append(row)
	return {"i": indices, "d": data}


def part_one(d):
	rotated = rotate_matrix(d["d"])
	return sum(get_amount_to_add_to_total(idx[1], rotated[i]) for i, idx in enumerate(d["i"]))


def part_two(d):
	total = 0
	formatted_data = rotate_matrix([[x.rjust(max([len(y) for y in row]), " ") for x in row] for row in d["d"]])
	for i, idx in enumerate(d["i"]):
		nums = []
		for j in range(len(formatted_data[i][0])):
			next_num = ""
			for word in formatted_data[i]:
				next_num += word[j] if word[j].isnumeric else ""
			nums.append(next_num[::-1])
		total += get_amount_to_add_to_total(idx[1], nums)
	return total


def get_amount_to_add_to_total(oper, nums):
	final_nums = [int(x) for x in nums if x.strip() != ""]
	return sum(final_nums) if oper == "+" else math.prod(final_nums)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
