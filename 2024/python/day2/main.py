from utils.timers import run_with_timer, get_data_with_timer
from utils.input import read_input_as_int_arrays


def get_data(filename):
	return read_input_as_int_arrays(filename)


def part_one(d):
	return sum(1 for x in d if try_safety_check(x))


def part_two(d):
	c = 0
	for x in d:
		if try_safety_check(x):
			c += 1
		else:
			for i in range(len(x)):
				if try_safety_check(x[:i] + x[i+1:]):
					c += 1
					break
	return c


def try_safety_check(x):
	for i in range(len(x) - 1):
		sx = sorted(x)
		if (list(sx) != x and list(reversed(sx)) != x) or abs(x[i] - x[i+1]) not in [1, 2, 3]:
			return False
	return True


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
