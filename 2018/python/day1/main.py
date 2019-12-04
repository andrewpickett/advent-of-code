import itertools
data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	return sum(map(int, data))


def part_two():
	used_frequencies = {0}
	frequency = 0
	for num in itertools.cycle(map(int, data)):
		frequency += num
		if frequency in used_frequencies:
			return frequency
		used_frequencies.add(frequency)


if __name__ == '__main__':
	print(part_one())
	print(part_two())
