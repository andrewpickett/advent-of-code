from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	return sum(y.count('\\"') + y.count('\\\\') + ((y.count('\\x') - y.count('\\\\x') + y.count('\\\\\\x'))*3) + 2 for y in (x[1:-1] for x in d))


def part_two(d):
	return sum(x.count('"') + x.count('\\') + 2 for x in d)


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)
