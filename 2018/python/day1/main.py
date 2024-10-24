import itertools
from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	return sum(map(int, d))


def part_two(d):
	used_frequencies = {0}
	frequency = 0
	for num in itertools.cycle(map(int, d)):
		frequency += num
		if frequency in used_frequencies:
			return frequency
		used_frequencies.add(frequency)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
