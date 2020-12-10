from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]
trib_nums = [1, 1, 2]


def get_adapter_list():
	curr_joltage = 0
	used_adapters = [0]
	while len(used_adapters) < len(data) + 1:
		curr_joltage += 1
		if curr_joltage in data:
			used_adapters.append(curr_joltage)
	used_adapters.append(used_adapters[-1] + 3)
	return used_adapters


def trib(n):
	if len(trib_nums)-1 >= n:
		return trib_nums[n]
	else:
		next_val = trib(n-1) + trib(n-2) + trib(n-3)
		trib_nums.append(next_val)
		return next_val


def part_one():
	adapters = get_adapter_list()
	diff_list = [adapters[i+1] - adapters[i] for i in range(len(adapters) - 1)]
	return diff_list.count(1) * diff_list.count(3)


def count_ways(diff_str):
	repeats = [0] * len(diff_str)
	curr_len = 0
	for i in diff_str:
		if i == '1':
			curr_len += 1
		else:
			if curr_len > 1:
				repeats[curr_len] += 1
			curr_len = 0
	if curr_len > 1:
		repeats[curr_len] += 1

	total = 1
	max_idx = max(i for i, x in enumerate(repeats) if x > 0) + 1
	for i in range(2, max_idx):
		if repeats[i] > 0:
			next_base = trib(i)
			total *= next_base**repeats[i]
	return total


def part_two():
	adapters = get_adapter_list()
	diff_list = [adapters[i+1] - adapters[i] for i in range(len(adapters) - 1)]
	return count_ways(''.join([str(i) for i in diff_list]))


if __name__ == '__main__':
	run_with_timer(part_one)  # 1625 -- took 0 ms
	run_with_timer(part_two)  # 3100448333024 -- took 0 ms
