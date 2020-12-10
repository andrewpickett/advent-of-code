from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def get_adapter_list():
	adapters = [0] + data.copy()
	adapters.sort()
	adapters.append(adapters[-1] + 3)
	return adapters


def trib(n):
	trib_nums = [1, 1, 2]
	return trib_nums[n] if len(trib_nums)-1 >= n else trib(n-1) + trib(n-2) + trib(n-3)


def count_ways(diff_str):
	curr_len = 0
	total = 1
	for i in diff_str:
		if i == '1':
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
	return count_ways(''.join([str(i) for i in diff_list]))


if __name__ == '__main__':
	run_with_timer(part_one)  # 1625 -- took 0 ms
	run_with_timer(part_two)  # 3100448333024 -- took 0 ms
