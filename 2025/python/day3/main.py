from utils.timers import run_with_timer, get_data_with_timer


def get_data(f):
	return [[int(y) for y in x.strip()] for x in f.readlines()]


def part_one(d):
	return sum(find_next_val(x, 2) for x in d)


def part_two(d):
	return sum(find_next_val(x, 12) for x in d)


def find_next_val(nums, depth):
	if depth == 1:
		return max(nums)
	next_val = max(nums[:1-depth])
	return 10**(depth-1) * next_val + find_next_val(nums[nums.index(next_val)+1:], depth-1)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
