from utils.timers import run_with_timer


def get_data(filename):
	return open(filename).readline().strip()


def part_one(d):
	return d.count('(') - d.count(')')


def part_two(d):
	floor = 0
	for i, direction in enumerate(d):
		floor += 1 if direction == '(' else -1
		if floor < 0:
			return i + 1


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
