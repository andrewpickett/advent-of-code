from utils.timers import run_with_timer
import hashlib


def get_data(filename):
	return open(filename).readline().strip()


def part_one(d):
	return find_hash(d, 5)


def part_two(d):
	return find_hash(d, 6)


def find_hash(d, num_zeroes):
	zs = "0" * num_zeroes
	i = 0
	while True:
		i += 1
		h = hashlib.md5((d + str(i)).encode('UTF-8')).hexdigest()
		if h.startswith(zs):
			return i


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
