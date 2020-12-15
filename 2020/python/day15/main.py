from aoc_utils import run_with_timer

data = [int(x) for x in open("input.txt").readline().split(',')]


def get_next_num(last_num, called_nums):
	if len(called_nums[last_num]) > 1:
		return called_nums[last_num][-1] - called_nums[last_num][-2]
	else:
		return 0


def run_until_steps(n):
	called_nums = {}
	for i, x in enumerate(data):
		called_nums[str(x)] = [i]

	last_num = data[-1]
	for counter in range(len(data), n):
		last_num = get_next_num(str(last_num), called_nums)
		if not str(last_num) in called_nums.keys():
			called_nums[str(last_num)] = []
		called_nums[str(last_num)].append(counter)
	return last_num


def part_one():
	return run_until_steps(2020)


def part_two():
	return run_until_steps(30000000)


if __name__ == '__main__':
	run_with_timer(part_one)  # 206
	run_with_timer(part_two)  # 955
