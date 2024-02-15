from utils.timers import run_with_timer, get_data_with_timer
from utils.hash import knot_hash, single_knot_hash


def get_data(filename):
	orig_input = open(filename).readline().strip()
	return {"knot": [x for x in range(256)], "input": [int(x) for x in orig_input.split(",")], "s": orig_input}


def part_one(d):
	nums, _, _ = single_knot_hash(d["input"], knot=d["knot"].copy())
	return nums[0] * nums[1]


def part_two(d):
	return knot_hash(d["s"], d["knot"].copy(), 64)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
