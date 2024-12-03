from utils.timers import run_with_timer, get_data_with_timer
import re
import math


def get_data(filename):
	return [w for z in [y.split("mul") for y in [x.strip() for x in open(filename).readlines()]] for w in z]


def part_one(d):
	return sum(mult_if_present(True, x) for x in d)


def part_two(d):
	s = 0
	do = True
	for x in d:
		s += mult_if_present(do, x)
		if "do()" in x:
			do = True
		elif "don't()" in x:
			do = False
	return s


def mult_if_present(do, x):
	if do and re.match("\(\d+,\d+\)", x):
		return math.prod(list(map(int, x[1:x.find(")")].split(","))))
	return 0


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

