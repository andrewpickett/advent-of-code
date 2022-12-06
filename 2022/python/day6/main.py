from aoc_utils import run_with_timer

data = open("input.txt").readline().strip()


def find_message_marker(size):
	for x in range(size, len(data)):
		if len(set(data[x-size:x])) == size:
			return x
	return 0


def part_one():
	return find_message_marker(4)


def part_two():
	return find_message_marker(14)


if __name__ == '__main__':
	run_with_timer(part_one)  # 1198 -- took 0 ms
	run_with_timer(part_two)  # 3120 -- took 3 ms
