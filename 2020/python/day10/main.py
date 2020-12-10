from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def get_adapter_list():
	adapters = [0] + data.copy() + [(max(data) + 3)]
	adapters.sort()
	return adapters


def trib(n):
	return [1, 1, 2][n] if n <= 2 else trib(n-1) + trib(n-2) + trib(n-3)


def count_ways(diff_list):
	curr_len = 0
	total = 1
	for i in diff_list:
		if i == 1:
			curr_len += 1
		else:
			total *= trib(curr_len)
			curr_len = 0
	return total * trib(curr_len)


def part_one():
	adapters = get_adapter_list()
	diff_list = [adapters[i+1] - adapters[i] for i in range(len(adapters) - 1)]
	return diff_list.count(1) * diff_list.count(3)


def part_two():
	adapters = get_adapter_list()
	diff_list = [adapters[i+1] - adapters[i] for i in range(len(adapters) - 1)]
	return count_ways(diff_list)


if __name__ == '__main__':
	run_with_timer(part_one)  # 1625 -- took 0 ms
	run_with_timer(part_two)  # 3100448333024 -- took 0 ms
