from aoc_utils import run_with_timer


def get_parts_from_line(line):
	return {
		"min": int(line[0].split('-')[0]),
		"max": int(line[0].split('-')[1]),
		"letter": str(line[1][:-1]),
		"password": str(line[2])
	}


data = [get_parts_from_line(y) for y in [x.split() for x in open("input.txt").readlines()]]


def part_one():
	return sum(1 for x in data if x["min"] <= x["password"].count(x["letter"]) <= x["max"])


def part_two():
	num_valid = 0
	for x in data:
		curr_count = 0
		curr_count = curr_count + 1 if x["password"][x["min"]-1] == x["letter"] else curr_count
		curr_count = curr_count + 1 if x["password"][x["max"]-1] == x["letter"] else curr_count
		num_valid = num_valid + 1 if curr_count == 1 else num_valid
	return num_valid


if __name__ == '__main__':
	run_with_timer(part_one)  # 580 -- took 0 ms
	run_with_timer(part_two)  # 611 -- took 0 ms
