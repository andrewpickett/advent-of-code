from utils.timers import run_with_timer, get_data_with_timer
from collections import defaultdict


def get_data(filename):
	data = [int(x) for x in open(filename).readline().strip().split()]
	return {num:data.count(num) for num in set(data)}


def part_one(d):
	return blink_a_bunch(d, 25)


def part_two(d):
	return blink_a_bunch(d, 75)


def blink_a_bunch(d, num):
	for _ in range(num):
		d = blink(d)
	return sum(x for x in d.values())


def blink(d):
	new_counts = defaultdict(int)
	for k, v in d.items():
		s = str(k)
		l = len(s)
		if k == 0:
			single_move = [1]
		elif l % 2 == 0:
			single_move = [int(s[:l//2]), int(s[l//2:])]
		else:
			single_move = [2024 * k]

		for stone in single_move:
			new_counts[stone] += v
	return new_counts


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()
