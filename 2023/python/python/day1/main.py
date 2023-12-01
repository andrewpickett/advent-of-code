from utils.timers import run_with_timer
import re


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	s = 0
	for x in d:
		nums = re.sub('[a-z]', '', x)
		s += int(nums[0])*10 + int(nums[-1])
	return s


def part_two(d):
	numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	s = 0
	for x in d:
		nums = []
		for i in range(len(x)):
			if x[i].isdigit():
				nums.append(int(x[i]))
			else:
				for n in numbers:
					if x[i:].startswith(n):
						nums.append(numbers.index(n))
						break
		s += nums[0]*10 + nums[-1]
	return s


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())
