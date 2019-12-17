from aoc_utils import run_with_timer
import hashlib

data = open('input.txt').readline().strip()


def part_one():
	return find_hash(5)


def part_two():
	return find_hash(6)


def find_hash(num_zeroes):
	i = 0
	while True:
		i += 1
		h = hashlib.md5((data + str(i)).encode('UTF-8')).hexdigest()
		if h[0:num_zeroes] == str('0' * num_zeroes):
			return i


if __name__ == '__main__':
	run_with_timer(part_one)  # 282749
	run_with_timer(part_two)  # 9962624
