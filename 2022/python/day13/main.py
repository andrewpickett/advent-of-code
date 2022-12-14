from aoc_utils import run_with_timer
from functools import cmp_to_key

data = [x.strip() for x in open("input.txt").readlines()]


def compare(left, right):
	for i in range(len(left)):
		if i >= len(right):
			return -1

		left_is_int = isinstance(left[i], int)
		right_is_int = isinstance(right[i], int)

		if left_is_int and right_is_int and left[i] != right[i]:
			return 1 if left[i] < right[i] else -1
		elif not left_is_int or not right_is_int:
			sub_compare = compare([left[i]] if left_is_int else left[i], [right[i]] if right_is_int else right[i])
			if sub_compare != 0:
				return sub_compare
	if len(right) > len(left):
		return 1
	return 0


def part_one():
	return sum((i // 3) + 1 for i in range(0, len(data), 3) if compare(eval(data[i]), eval(data[i+1])) == 1)


def part_two():
	dividers = [[[2]], [[6]]]
	new_data = [eval(x) for x in data if x != ""]
	new_data.extend(dividers)
	new_data = sorted(new_data, key=cmp_to_key(compare), reverse=True)
	return (new_data.index(dividers[0]) + 1) * (new_data.index(dividers[1]) + 1)


if __name__ == '__main__':
	run_with_timer(part_one)  # 5625 -- took 16 ms
	run_with_timer(part_two)  # 23111 -- took 20 ms
